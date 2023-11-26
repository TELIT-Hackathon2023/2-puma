import hashlib
import hmac
import struct
import time

def generate_totp(secret_key, time_step=30, digits=6):
    current_time = int(time.time()) // time_step
    time_bytes = struct.pack('>Q', current_time)
    
    hash_value = hmac.new(secret_key.encode('utf-8'), time_bytes, hashlib.sha1).digest()
    offset = hash_value[-1] & 0x0F
    dynamic_code = hash_value[offset:offset + 4]
    totp = struct.unpack('>I', dynamic_code)[0] & 0x7FFFFFFF
    totp %= 10 ** digits
    totp = f"{totp:0{digits}d}"

    return totp


secret_key = "GG2@telekom.sk"
totp = generate_totp(secret_key)
print(f"Generated TOTP: {totp}")
