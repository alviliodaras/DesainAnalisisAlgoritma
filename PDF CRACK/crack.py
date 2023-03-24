import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("wordlist.txt")]

for password in tqdm(passwords, 'Crack PDF'):
    try:
        with pikepdf.open('tes3.pdf', password=password) as pdf:
            print(' [+] Password found :', password)
            break
    except pikepdf._core.PasswordError as e:
        pass
    except pikepdf._core.Error as e:
        print(' [-] Error:', e)
