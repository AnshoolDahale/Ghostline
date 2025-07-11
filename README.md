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



🚀 Usage
On Victim Machine:
Exfiltrate a file:

python3 Ghostline.py
Enter the path to the target file (e.g., /home/user/passwords.txt)

On Attacker Machine:
Start Passive Logger

python3 receiver/passive_logger.py
Reconstruct Received Data

python3 -m receiver.decoder
Output will be saved to:

receiver/reconstructed_output.bin
📁 Project Structure
Ghostline/
├── encoder/              # Payload encoding & XOR logic
├── dns_sender/           # Chunk sender with DNS/DoH logic
├── receiver/             # Passive receiver & decoder
├── utils/                # Timing & entropy helpers
├── config/               # Config file (chunk size, DoH toggle, etc.)
├── logs/                 # Sent chunks stored here
├── Ghostline.py          # Main CLI entry point
🧠 Research-Based Design
Ghostline is based on insights from 9 advanced papers on DNS exfiltration and detection. Techniques used:

GAN-based domain crafting (DOLOS)

FFT & DTW for timing anomaly evasion

Entropy tuning for lexical models

DoH tunneling evasion via flow masking

Mimicry of subdomains based on CDN & human typos

⚠️ Disclaimer
Ghostline is strictly intended for educational, research, and authorized Red Team use only. Misuse of this tool can result in criminal charges. Use responsibly.

✨ Author
Made with ❤️ by Anshool Dahale

contact me for clear explanation of working , or doubts regarding the tool
🔗 ph : 8328004134
📧 anshooldahale08@gmail.com
