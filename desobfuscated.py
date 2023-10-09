import wave
from Crypto.Cipher import AES
import struct
import hashlib

def deobfuscate_audio(input_file, output_file, password):
    key = hashlib.sha256(password.encode()).digest()
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    with wave.open(input_file, 'rb') as obfuscated_wave:
        obfuscated_audio = obfuscated_wave.readframes(-1)
        sample_width = obfuscated_wave.getsampwidth()
        num_channels = obfuscated_wave.getnchannels()
        framerate = obfuscated_wave.getframerate()
    
    padded_audio = cipher.decrypt(obfuscated_audio)
    
    TARGET_FRAMERATE = 44100  
    
    if framerate != TARGET_FRAMERATE:
        import scipy.signal
        resampled_audio = scipy.signal.resample(padded_audio, int(len(padded_audio) * TARGET_FRAMERATE / framerate))
        padded_audio = struct.pack('<' + ('h' * len(resampled_audio)), *resampled_audio)
    
    with wave.open(output_file, 'wb') as f:
        f.setnchannels(num_channels)
        f.setsampwidth(sample_width)
        f.setframerate(framerate)
        f.writeframes(padded_audio.rstrip(b"\0"))

password = input("Password : ")

deobfuscate_audio("obfuscated.wav", "deobfuscated.wav", password)
