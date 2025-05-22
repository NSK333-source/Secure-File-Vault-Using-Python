# 🔐 Secure File Vault

## Overview
**Secure File Vault** is a simple Python-based cybersecurity tool that allows users to securely encrypt and decrypt files using **AES encryption (CBC mode)**.
It protects sensitive files by converting them into unreadable formats and only decrypts them with the correct password.

---

## 🔧 Features
- AES-256 encryption with a secure password
- Encrypt any file (text, images, etc.)
- Decrypt only with the correct password
- Automatically deletes original/encrypted files after processing
- Command-line interface for simple usage

---

## 🛠 Requirements
- Python 3.x  
- [PyCryptodome](https://pypi.org/project/pycryptodome/)

Install dependencies using:
```bash
pip install pycryptodome
