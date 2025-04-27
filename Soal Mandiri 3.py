import re

def hapus_spasi_berlebih(teks):
    teks = re.sub(r'\s+', ' ', teks)
    return teks.strip()

kalimat = "saya    tidak   suka    matdis     dan   statistik "
hasil = hapus_spasi_berlebih(kalimat)

print(hasil)
