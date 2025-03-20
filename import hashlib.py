import hashlib

def sha256_to_hex(message):
    
    message_bytes = message.encode('utf-8')
    
    md5_hash = hashlib.sha256(message_bytes)
    
    return md5_hash.hexdigest()

message = "welcome to sanjivani " 
hex_result = sha256_to_hex(message)
print(f"sha256 to Hexadecimal of '{message}': {hex_result}")