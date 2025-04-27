import re
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))

teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi
anwari slamet@getnada.com dimiliki oleh slamet
slumut matahari@tokopedia.com dimiliki oleh toko matahari
"""

email_pattern = r'(\S+@\S+\.\S+)'
username_pattern = r'dimiliki oleh (\S+)'

emails = re.findall(email_pattern, teks)
usernames = re.findall(username_pattern, teks)

for email, username in zip(emails, usernames):
    password = generate_password()
    print(f"{email} username: {username} , password: {password}")
