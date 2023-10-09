import wave
from Crypto.Cipher import AES
import hashlib

def pad(data):
    block_size = AES.block_size
    return data + (block_size - len(data) % block_size) * b"\0"

def obfuscate_audio(input_file, output_file, password):
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    
    with open(input_file, 'rb') as f:
        original_audio = f.read()
    
    padded_audio = pad(original_audio)
    obfuscated_audio = cipher.encrypt(padded_audio)
    
    with wave.open(input_file, 'rb') as original_wave:
        output_wave = wave.open(output_file, 'wb')
        output_wave.setparams(original_wave.getparams())
        output_wave.writeframes(obfuscated_audio)
        output_wave.close()
    
password = input("Password : ")

obfuscate_audio("record.wav", "obfuscated.wav", password)
