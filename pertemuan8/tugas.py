# soal no 1
# input data
nama_kendaraan = input("Nama kendaraan :")
jenis_bensin = input("Jenis bensin :")
kota_tujuan = input("Kota tujuan :")

# Data harga dan jarak tempuh\
harga_perliter = {
    "pertalite": 10000,
    "pertamax": 14000,
    "pertamax turbo": 17000
}

jarak_tempuh = {
    "pertalite": 12,
    "pertamax": 13,
    "pertamax turbo": 13.5
}

jarak_kota = {
    "jakarta": 20,
    "bekasi": 35.7,
    "depok": 5,
    "tanggerang": 99,
    "bogor": 120
}

# menghitung total pemakaian bensin dna total biaya
pemakaian_bensin = jarak_kota[kota_tujuan]/jarak_tempuh
