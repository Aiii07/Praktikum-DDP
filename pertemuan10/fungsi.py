#contoh pemanggilan fungsi
hasil_akhir = [
    {'nama' : 'Reza', 'nilai' :70},
    {'nama' : 'Ciut', 'nilai' :63},
    {'nama' : 'Dian', 'nilai' :80},
    {'nama' : 'Badu', 'nilai' :40}
]
siswa_lulus = [siswa['nama']for siswa in hasil_akhir if siswa['nilai']>65]
print('siswa yang lulus', siswa_lulus)

#soal 1
buah_buah = ['pepaya', 'mangga','pisang', 'durian', 'jambu']
balikan_list = []
for i in range (len(buah_buah) - 1, -1, -1):
    balikan_list.append(buah_buah[1])
    
print('buah buahan', buah_buah)

#soal 2
duplikasi_list = []
for buah in buah_buah:
    duplikasi_list.append(buah)
    duplikasi_list.append(buah)

print('duplikasi list', duplikasi_list)

#soal 3
kalimat = "Nurul Fikri"
konsonan_string = ""
for karakter in kalimat:
    if karakter.isalpha() and karakter.lower() not in 'aeiou':
        konsonan_string += karakter

print('konsonan', konsonan_string)