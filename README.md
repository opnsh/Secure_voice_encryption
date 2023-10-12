# Secure voice encryption
![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

This Python script allows you to secure and protect your audio recordings by encrypting them with a password. With the same password, you can decrypt and restore the audio to its original form.

**Note:** This project is a work in progress, additional features and improvements will be added.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Installation](#installation)

## Overview

- `recording.py`: This script records audio using a microphone and saves it as an unencrypted WAV file. (Optional, the script works with any wav file)

- `obfuscated.py`: It takes the unencrypted WAV file and encrypts it with a user-provided password using the AES encryption algorithm.

- `desobfuscated.py`: This script allows you to decrypt the encrypted audio file using the same password, restoring it to its original, audible form.

## Usage

Follow these steps:

1. **Recording (Optional)**: Run `recording.py` to record audio from your microphone. 

   ```bash
   python recording.py
   ```

2. **Encryption**: Run `obfuscated.py` to encrypt the record.wav file with a password.

   ```bash
   python obfuscated.py
   ```

3. **Decryption**: To decrypt the audio, run `desobfuscated.py` and provide the same password you used for encryption.

   ```bash
   python desobfuscated.py
   ```

## Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/opnsh/Secure_voice_encryption.git
   ```

2. Install the required Python packages. You can use `pip` to install them:

   ```bash
   pip install pyaudio pycryptodome scipy
   ```

3. Run the scripts as described in the [Usage](#usage) section.
