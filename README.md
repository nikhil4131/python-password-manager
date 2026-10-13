# Python Password Manager

A command-line password manager built with Python to practise file handling, JSON, functions, Git, and encryption.

## Features

- Add, view, search, update, and delete accounts
- Save account data in a JSON file
- Persist data between program runs
- Encrypt passwords using the Fernet library
- Reveal passwords when requested
- Hide password input using `getpass`
- Validate duplicate website entries
- Handle missing and malformed JSON files

## Requirements

- Python 3
- `cryptography` library

## Installation

Install the dependency:

```bash
python -m pip install cryptography
```

## Setup

1. Run `setup_key.py` once to generate `secret.key`.
2. Run `password_manager.py`.
3. Follow the command-line menu.

Keep `secret.key` private and back it up securely. Losing it means encrypted passwords may become unrecoverable.

## Security Limitations

This is a learning project, not a production-ready password manager. The encryption key is stored locally without a password, and account metadata is not encrypted. Do not use real credentials.

## Technologies

- Python
- JSON
- Cryptography (Fernet)
- Git
