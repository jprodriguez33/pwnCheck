import hashlib
import requests
import getpass


password = getpass.getpass("Please enter your password: ")

def check_password(password):
    
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check API")
    
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

count = check_password(password)

if count: 
    print(f"Password was found {count:,} times in breaches.")
else:
    print(f"Password has not been found in known breaches.")