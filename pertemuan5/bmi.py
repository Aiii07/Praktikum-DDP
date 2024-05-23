tb = 157/100
bb = 45
bmi = bb/(tb**2)
print(bmi)

if bmi < 18.5:
    print("anda kekurangan berat badan")

elif bmi > 18.5 and bmi < 24.9:
    print("berat badan anda normal")

elif bmi > 24.9 and bmi < 29.9:
    print("anda kelebihan berat badan")

elif bmi > 29.9:
    print("anda obesitas")

else :
    print("kondisi tidak ditemukan")