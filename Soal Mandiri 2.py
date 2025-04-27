import re

def hitung_kata(teks, kata_cari):
    teks = teks.lower()
    kata_cari = kata_cari.lower()
    daftar_kata = re.findall(r'\b\w+\b', teks)
    return daftar_kata.count(kata_cari)

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata_dicari = "makan"
jumlah = hitung_kata(kalimat, kata_dicari)

print(f"{kata_dicari} ada {jumlah} buah")
