from gempa import gempa

gempa1 = gempa("Banten 1.2",1.2)
gempa2 = gempa("palu 6.1",6.1)
gempa3 = gempa("Cianjur 5.6",5.6)
gempa4 = gempa("Jayapura 3.3",3.3)
gempa5 = gempa("Garut 4.0",4.0)

print(gempa1.dampak())
print(gempa2.dampak())
print(gempa3.dampak())
print(gempa4.dampak())
print(gempa5.dampak())