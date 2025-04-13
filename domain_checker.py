import random
import whois
import time

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def generate_domain():
    """Generate a pronounceable five-letter domain."""
    pattern = random.choice(["CVCVC", "VCVCV", "CVCCV", "VCCVC", "CCVVC"])
    domain = "".join(random.choice(vowels if ch == "V" else consonants) for ch in pattern)
    return domain + ".com"

def is_domain_available(domain):
    """Check if the domain is available using WHOIS."""
    try:
        domain_info = whois.whois(domain)
        if domain_info.status is None or not domain_info.status:
            return True
        return False
    except whois.parser.PywhoisError:
        print(f"Error checking {domain}: No match found.")
        return True 
    except Exception as e:
        print(f"Error checking {domain}: {e}")
        return True

# Checking 1000 random domains (you can change this but this is a slow process)
for _ in range(1000):  
    domain = generate_domain()
    print(f"Checking {domain}...")

    retries = 3
    success = False
    while retries > 0 and not success:
        if is_domain_available(domain):
            print(f"✅ Available: {domain}")
            success = True
        else:
            retries -= 1
            if retries > 0:
                print(f"Retrying {domain}...")
            else:
                print(f"❌ Taken: {domain}")

        time.sleep(1)  # this is to takcle rate-limiter
