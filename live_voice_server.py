import os
import json
import base64
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

from pocketinfer.applications.apna_saathi import ApnaSaathi
from pocketinfer.models.nmt import Nmt
from pocketinfer.models.ollama import Ollama
from pocketinfer.models.gnani import GnaniAsr, GnaniTts
from pocketinfer import retrieval

assert os.getenv("GNANI_API_KEY"), "GNANI_API_KEY is not set"

app = ApnaSaathi(None, settings={"vision_enabled": False})
app.nmt = Nmt(timeout=60)
app.speech_provider = "gnani"
app.gnani_asr = GnaniAsr(timeout=60)
app.gnani_tts = GnaniTts(timeout=60)
app.ollama = Ollama(
    model_name=app.METADATA["models"]["ollama"]["model_name"]
)
app.db = retrieval.ensure_db(
    Path("/tmp/apna_saathi_gnani_test/corpus.tsv"),
    Path("/tmp/apna_saathi_gnani_test/corpus.db")
)

class VoiceHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/talk":
            self.send_error(404)
            return

        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size < 44 or size > 5_000_000:
                self.send_error(400, "Invalid audio size")
                return

            audio = self.rfile.read(size)
            print("Received laptop audio:", len(audio), "bytes", flush=True)

            result = app.answer(
                audio,
                in_lang="hi",
                out_lang="hi",
                on_stage=lambda s: print(s, flush=True)
            )

            wav = result["tts_bytes"]
            if len(wav) <= 44 or not wav.startswith(b"RIFF"):
                raise ValueError("TTS returned empty or invalid WAV")

            payload = json.dumps({
                "answer": result["answer_out"],
                "audio": base64.b64encode(wav).decode("ascii")
            }, ensure_ascii=False).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        except Exception as e:
            print("Voice processing error:", repr(e), flush=True)
            self.send_error(500, "Voice processing failed")

print("APNA SAATHI VOICE SERVER READY on localhost:8765", flush=True)
HTTPServer(("127.0.0.1", 8765), VoiceHandler).serve_forever()
