import os
import base64
import requests

BASE_URL = "https://api.vachana.ai"

LANGUAGES = {
    "hi": "hi-IN", "en": "en-IN",
    "bn": "bn-IN", "ta": "ta-IN",
    "te": "te-IN", "kn": "kn-IN",
    "ml": "ml-IN", "mr": "mr-IN",
    "pa": "pa-IN", "gu": "gu-IN",
}

class GnaniAsr:
    def __init__(self, timeout=60):
        self.timeout = timeout

    def infer(self, wav_bytes, language):
        key = os.environ.get("GNANI_API_KEY")
        if not key:
            raise RuntimeError("GNANI_API_KEY not configured")

        response = requests.post(
            BASE_URL + "/stt/v3",
            headers={"X-API-Key-ID": key},
            files={
                "audio_file": (
                    "recording.wav", wav_bytes, "audio/wav"
                )
            },
            data={
                "model": "prisma-v3.0",
                "language_code": LANGUAGES.get(
                    language, "indic-auto"
                ),
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        result = response.json()
        if not result.get("success", False):
            raise RuntimeError("Gnani STT unsuccessful")
        return {"text": result.get("transcript", "")}


class GnaniTts:
    def __init__(self, timeout=60):
        self.timeout = timeout

    def infer(self, text, language):
        key = os.environ.get("GNANI_API_KEY")
        if not key:
            raise RuntimeError("GNANI_API_KEY not configured")

        response = requests.post(
            BASE_URL + "/api/v1/tts/inference",
            headers={"X-API-Key-ID": key},
            json={
                "text": text,
                "model": "timbre-v3.0",
                "voice": "Shivani",
                "language": LANGUAGES.get(
                    language, "auto"
                ),
                "audio_config": {
                    "encoding": "linear_pcm",
                    "container": "wav",
                    "num_channels": 1,
                    "sample_rate": 16000,
                    "sample_width": 2,
                },
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        if not response.content.startswith(b"RIFF") or len(response.content) <= 44:
            raise RuntimeError(
                f"Gnani TTS returned empty or invalid WAV ({len(response.content)} bytes)"
            )
        return {
            "audio_base64": base64.b64encode(
                response.content
            ).decode("ascii")
        }
