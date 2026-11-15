
### Giving India a Voice in AI

**An Indian-language, voice-first AI companion powered by Gnani AI's speech technology, designed for people who cannot always rely on smartphones, fluent English, digital literacy, or reliable connectivity.**

**Built for the Great Indian AI Internship Challenge 2026**

---

## What if accessing AI were as simple as speaking?

Imagine a farmer trying to understand a government notice written in an unfamiliar language.

A parent attending a school meeting but struggling to communicate with a teacher.

A traveller stranded in an unfamiliar state, unable to explain what they need.

The information exists. The technology exists.

**But can everyone actually access it?**

That's the problem Apna Saathi is built to solve.

Apna Saathi combines **Gnani AI's Indian-language speech recognition and speech synthesis** with local AI reasoning on an NVIDIA Jetson device to create a conversational assistant that listens, understands, responds, and speaks naturally.

No complicated menus. No typing required. Just a conversation.

> **Our belief:** AI should understand the way India speaks — not require India to speak the language of technology.

---

## Powered by Gnani AI

At the heart of Apna Saathi's voice experience is **Gnani AI**, an Indian AI company building speech and language technologies for Indian users.

Instead of treating Indian languages as an afterthought, Apna Saathi uses Gnani AI to make voice the primary interface.

| Technology | Role in Apna Saathi |
|---|---|
| **Gnani AI Speech-to-Text** | Converts spoken Indian-language input into text |
| **Gnani AI Text-to-Speech** | Generates spoken responses |
| **Local Qwen LLM** | Processes requests and generates contextual responses |
| **NVIDIA Jetson** | Hosts the application and on-device intelligence |
| **Multilingual processing** | Supports language-aware interactions and translation workflows |
| **Physical voice interface** | Makes interaction possible without typing or navigating a smartphone |

### Why Gnani AI?

India's linguistic diversity creates challenges that conventional English-first interfaces do not adequately address.

Real conversations involve regional accents, informal phrasing, mixed-language expressions, and different levels of fluency.

Gnani AI's focus on Indian speech makes it a natural foundation for Apna Saathi.

**Gnani AI gives Apna Saathi its voice. Local intelligence gives that voice context.**

*Implementation note: The current Gnani AI speech integration uses cloud APIs. Local reasoning can run on the Jetson, but the complete Gnani-powered voice pipeline requires connectivity to those APIs.*

---

## 🎙️ How Apna Saathi Works

```text
               PERSON SPEAKS
                     |
                     v
          Physical Voice Interface
           (Microphone + Button)
                     |
                     v
          GNANI AI SPEECH-TO-TEXT
             Spoken Language
                 to Text
                     |
                     v
           Language Processing
             & Translation
                     |
                     v
           LOCAL QWEN AI MODEL
           NVIDIA Jetson Device
                     |
                     v
          Contextual AI Response
                     |
                     v
          GNANI AI TEXT-TO-SPEECH
             Text to Voice
                     |
                     v
              SPEAKER OUTPUT
                     |
                     v
             PERSON UNDERSTANDS
```

### The interaction

1. **Listen:** The user speaks naturally into the device.
2. **Recognize:** Gnani AI converts the spoken request into text.
3. **Understand:** The application processes the request using its language workflow and local AI model.
4. **Respond:** A contextual response is generated.
5. **Speak:** Gnani AI synthesizes the response into speech.
6. **Continue:** The user can interact through the device's physical voice interface.

The goal is to make AI interaction feel less like operating software and more like asking someone for help.

---

## 🌏 Built for Real India, Not Just Ideal Conditions

### 01. The farmer who needs answers

A farmer may need help understanding crop-related information, government schemes, or an unfamiliar notice.

Instead of navigating multiple websites, the user can ask a question aloud.

**Apna Saathi aims to turn complicated information into understandable conversation.**

### 02. The parent who needs a voice

At a parent-teacher meeting, language and literacy barriers can make communication difficult.

A voice-first multilingual assistant can help bridge communication gaps between parents and teachers.

**The objective is not to replace the conversation, but to make it possible.**

### 03. The traveller who needs translation

A traveller arriving in a region where they do not speak the local language may struggle with simple requests.

Apna Saathi's multilingual workflow is designed to support communication across language barriers.

**Language should not determine whether someone can ask for help.**

### 04. The person who cannot navigate a digital interface

Not everyone is comfortable with apps, keyboards, English menus, or complicated digital workflows.

A physical, voice-first interface reduces the need to learn how to operate another application.

**Accessibility begins with designing around the user.**

*These are intended application scenarios. Specific capabilities and reliability should be demonstrated and evaluated individually.*

---

## ⚙️ Technical Architecture

Apna Saathi combines Indian speech AI, edge computing, and a physical interaction layer.

### Hardware

- NVIDIA Jetson Orin Nano platform
- USB microphone for voice input
- Speaker for spoken output
- Physical interaction controls
- Compact display/interface components

### Software

| Layer | Technology |
|---|---|
| Speech recognition | Gnani AI STT API |
| Speech synthesis | Gnani AI TTS API |
| Local language reasoning | Qwen via local inference |
| Application logic | Python |
| Audio processing | Python audio pipeline |
| Device interface | Jetson hardware integration |
| Language workflows | Multilingual processing and translation |
| Deployment | Linux-based embedded environment |

### What makes this different?

**1. Voice is the interface, not an additional feature.**

The device is designed around spoken interaction rather than expecting users to navigate a conventional application.

**2. Indian speech technology is central to the experience.**

Gnani AI handles the speech recognition and synthesis stages of the current voice pipeline.

**3. AI reasoning can run on the device.**

The local Qwen model provides an on-device reasoning component rather than requiring every part of the system to be hosted remotely.

**4. Hardware makes AI more accessible.**

The interaction model does not depend on the user owning or operating a smartphone.

**5. The architecture separates speech and reasoning.**

The speech layer and local AI layer can be developed, tested, and improved independently.

---

## 🛠️ Repository Structure

```text
apna-saathi-gnani/
│
├── live_voice_server.py
│
├── python/
│   ├── .env.example
│   ├── README.md
│   └── pocketinfer/
│       ├── applications/
│       │   └── apna_saathi.py
│       │
│       ├── models/
│       │   ├── gnani.py
│       │   ├── ollama.py
│       │   └── ...
│       │
│       ├── audio.py
│       ├── service.py
│       ├── retrieval.py
│       ├── safety.py
│       └── ui/
│
├── ioexpander/
├── rootfs/
├── assets/
├── LICENSE
└── README.md
```

### Key files

- **`python/pocketinfer/models/gnani.py`** — Gnani AI speech integration
- **`python/pocketinfer/applications/apna_saathi.py`** — Main application logic
- **`python/pocketinfer/audio.py`** — Audio handling
- **`python/pocketinfer/service.py`** — Application service orchestration
- **`live_voice_server.py`** — Voice-related server component
- **`python/.env.example`** — Example environment configuration

---

## 🚀 Getting Started

### Prerequisites

- Compatible Linux/Jetson environment
- Python and project dependencies
- Gnani AI API access
- Local AI inference environment and model
- Working microphone and speaker

### 1. Clone the repository

```bash
git clone https://github.com/AMSecretAgent/GNANI.AI.git
cd GNANI.AI
```

### 2. Configure environment variables

Use the provided example configuration:

```bash
cp python/.env.example python/.env
```

Add your Gnani AI credentials locally.

```env
GNANI_API_KEY=your_gnani_api_key
```

**Never commit API credentials or private environment files to GitHub.**

### 3. Configure the device

Follow the hardware and environment instructions in the repository's existing setup documentation.

Configure the local inference model, microphone, speaker, and required dependencies for your deployment environment.

### 4. Run the application

Launch the appropriate development service or application entry point after completing the environment setup.

The exact startup procedure depends on the Jetson configuration and available peripherals.

*This repository contains the application and integration code; a fully automated fresh-device installation is not currently documented.*

---

## 🧪 What We Are Evaluating

Building an Indian-language voice assistant is only the first step.

The important question is whether it works for real users.

Our evaluation priorities include:

| Evaluation area | What matters |
|---|---|
| Speech recognition | Understanding spoken requests accurately |
| Indian-language usability | Handling natural expressions and language variation |
| Response quality | Producing relevant, understandable answers |
| End-to-end latency | Time between speaking and hearing a response |
| Hardware usability | Whether users can interact without technical training |
| Real-world accessibility | Whether the experience reduces practical barriers |

Future testing should include different speakers, accents, languages, noisy environments, and representative use cases.

We do not claim unmeasured accuracy, latency, or language coverage.

---

## 🏆 The Great Indian AI Internship Challenge

Apna Saathi is presented as a working application built around Gnani AI's speech technology.

### Real Deal Award — Real-world impact

The project addresses barriers in communication and access to information, particularly for people who may struggle with conventional digital interfaces.

### Jugaad Genius Award — Creative use of Gnani AI

Rather than building another voice chatbot in a browser, the project integrates Gnani AI into a physical, embedded AI companion.

### Main Character Award — Indian languages

The architecture is designed around Indian-language interaction. Regional-language capability should be assessed through actual recorded demonstrations.

### Mixed Vibes Award — Code-mixed speech

Code-mixed speech is an important intended use case. Eligibility for this category should be supported by a working Hinglish or other code-mixed interaction demo.

---



## 🔭 What's Next?

Our development priorities include:

- Broader regional-language testing
- Better handling of code-mixed conversations
- Improved voice response latency
- Testing in realistic noisy environments
- More robust translation workflows
- Usability studies with intended users
- Further optimization of local inference
- Better support for low-connectivity environments

The long-term goal is to make conversational AI useful in places where conventional interfaces are difficult to access.

---

## 👩‍💻 Built By

**Akansha Mishra**

B.Tech, Computer Science and Engineering (Artificial Intelligence)  
Indira Gandhi Delhi Technical University for Women (IGDTUW)

Founder, Apna Saathi initiative

Apna Saathi was previously developed as part of the **BHASHINI VYOMA Open Handheld AI Innovation Challenge** and presented at **ESTIC 2026**, representing the BHASHINI initiative at the MeitY exhibition space.

This Gnani AI integration extends that work with Indian speech recognition and synthesis technology.

**GitHub:** [AMSecretAgent](https://github.com/AMSecretAgent)

**Contact:** mishakansha.01@gmail.com

---

##  Acknowledgements

- **Gnani AI** — Indian-language speech AI technology and developer ecosystem
- **BHASHINI** — Support for multilingual and accessible AI innovation
- **NVIDIA Jetson ecosystem** — Edge computing hardware
- **Qwen and open-source contributors** — Local AI model ecosystem
- **Current AI / Pocket Infer contributors** — Original software foundation and components, subject to the repository's existing license

---


### Technology becomes meaningful when people can actually use it.

**Apna Saathi × Gnani AI — Giving India a Voice in AI.**

#GnaniAI #GreatIndianAIInternshipChallenge
