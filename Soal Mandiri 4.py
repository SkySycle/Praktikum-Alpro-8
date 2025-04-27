import re

def kata_pendek_panjang(kalimat):
    kata_list = re.findall(r'\b\w+\b', kalimat)
    terpendek = min(kata_list, key=len)
    terpanjang = max(kata_list, key=len)
    return terpendek, terpanjang

kalimat = "semoga yang disemogakan tersemogakan"
terpendek, terpanjang = kata_pendek_panjang(kalimat)

print(f"Terpendek: {terpendek}")
print(f"Terpanjang: {terpanjang}")
