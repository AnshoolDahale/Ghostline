import os
import base64
from encoder.payload_encoder import xor_data

# Set constants
XOR_KEY = "ghost"

# Define absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # goes to project root
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "sent_chunks.txt")
OUTPUT_FILE_PATH = os.path.join(BASE_DIR, "receiver", "reconstructed_output.bin")

def decode_chunk(encoded_chunk):
    # Add base64 padding
    padded = encoded_chunk + '=' * (-len(encoded_chunk) % 4)
    try:
        decoded = base64.urlsafe_b64decode(padded.encode())
        return xor_data(decoded, XOR_KEY)
    except Exception as e:
        print(f"[!] Decode error: {e}")
        return b''

def decode_chunks():
    if not os.path.exists(LOG_FILE_PATH):
        print(f"[!] Log file not found: {LOG_FILE_PATH}")
        return

    output_data = b""

    with open(LOG_FILE_PATH, "r") as f:
        for line in f:
            encoded = line.strip()
            if encoded:
                output_data += decode_chunk(encoded)

    with open(OUTPUT_FILE_PATH, "wb") as out_file:
        out_file.write(output_data)

    print(f"[✓] File reconstructed successfully to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    decode_chunks()

