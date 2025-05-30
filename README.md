# pwnCheck

Python script to check [haveibeenpwned.com](https://haveibeenpwned.com) for any known password leaks.  
This script uses the **k-anonymity model** for privacy, as it only sends the first 5 characters of the SHA-1 hash to the API.
