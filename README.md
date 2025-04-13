# 🧪 Pronounceable Domain Name Checker

This Python script generates **random, pronounceable 5-letter `.com` domain names** and checks if they are available using WHOIS lookup.

## 🚀 Features

- Generates domain names using vowel-consonant patterns (like `CVCVC`, `VCVCV`, etc.)
- Checks domain availability using the `whois` library.
- Automatically retries failed WHOIS checks (up to 3 times).
- Skips taken domains and prints out available ones.
- Throttles requests with a delay to avoid rate-limiting.

## 🛠️ Requirements

- Python 3.x
- Install required Python package:

## 📦 How to Run

1. Clone this repository:
git clone https://github.com/nobisar/domain-checker.git

2. Run the script:
python domain_checker.py

> The script checks 1000 randomly generated domain names. You can change that number by modifying the loop at the bottom.

## 📝 Notes

- WHOIS lookups can be **slow** and sometimes **inconsistent** due to rate limits.
- The `time.sleep(1)` helps avoid rate-limiting errors.
- This is a basic prototype. For large-scale use, consider using APIs from registrars like GoDaddy, Namecheap, or Dynadot.
