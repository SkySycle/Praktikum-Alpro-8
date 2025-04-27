import re
from datetime import datetime

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, 
seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).
"""

tanggal_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
tanggal_list = re.findall(tanggal_pattern, teks)

today = datetime.now()

for tgl_str in tanggal_list:
    tgl_obj = datetime.strptime(tgl_str, "%Y-%m-%d")
    
    tgl_format_baru = tgl_obj.strftime("%d-%m-%Y %H:%M:%S")
    
    selisih_hari = (today - tgl_obj).days
    
    print(f"{tgl_format_baru} selisih {selisih_hari} hari")