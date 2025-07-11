import base64

def xor_data(data, key='ghost'):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

def encode_chunk(chunk):
    xor_result = xor_data(chunk)
    encoded = base64.urlsafe_b64encode(xor_result).decode().rstrip("=")
    return encoded

def decode_chunk(encoded_chunk, key='ghost'):
    padded = encoded_chunk + '=' * (-len(encoded_chunk) % 4)
    decoded = base64.urlsafe_b64decode(padded.encode())
    return xor_data(decoded, key)

