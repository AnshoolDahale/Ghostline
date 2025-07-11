# 👻 Ghostline

**Ghostline** is a stealth-focused DNS exfiltration framework designed for Red Team operations. Unlike traditional DNS tunneling tools like Iodine or DNScat2, Ghostline simulates realistic DNS behavior—evading modern detection systems using entropy shaping, domain rotation, TTL randomization, and optional DNS-over-HTTPS (DoH) encryption.

> 🔐 Built to leak silently. Designed to blend in. Developed to challenge Blue Teams.

---

## 🔧 Features

- ⚙️ Modular architecture for full control
- 🧬 XOR + Base64 encoded payload chunks
- 🌐 DNS and DNS-over-HTTPS (DoH) support
- 🌀 Domain rotator with CDN/typo mimicry
- 🧠 Entropy shaping to mimic real traffic
- ⏱️ Timing jitter and TTL randomization
- 📄 Passive listener (Flask) for live decoding
- 📊 Logging and analytics-ready

---

## 📦 Installation

```bash
git clone https://github.com/AnshoolDahale/Ghostline.git
cd Ghostline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
