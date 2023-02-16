from tqdm import tqdm
from itertools import product as it_product
import zipfile
import sys


# # the password list path you want to use
# wordlist = sys.argv[2]
N = 5
digits_base = list(map(''.join, it_product('0123456789', repeat=N)))

# the zip file you want to crack its password
# zip_file = sys.argv[1]
zip_file = "01-2023.zip"

# with open('wordlist', 'r') as passwords, zipfile.ZipFile(zip_file, 'r') as zf:
with zipfile.ZipFile(zip_file, 'r') as zf:
    # total_pass = passwords.readlines()
    total_pass = digits_base
    total_len = len(total_pass)
    for p in tqdm(total_pass, total=total_len):
        try:
            zf.extractall(pwd=p.strip().encode())
        except:
            continue
        else:
            print("[+] Password found:", p.strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
