import re

def cek_anagram(kata1, kata2):
    kata1 = ''.join(re.findall(r'[a-zA-Z]', kata1)).lower()
    kata2 = ''.join(re.findall(r'[a-zA-Z]', kata2)).lower()
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kata tersebut adalah anagram.")
else:
    print("Kata tersebut bukan anagram.")
