angka_1 = float(input("Masukkan angka pertama:"))
angka_2 = float(input("Masukkan angka kedua:"))
angka_3 = float(input("Masukkan angka ketiga:"))
angka_4 = float(input("Masukkan angka keempat:"))
angka_5 = float(input("Masukkan angka kelima:"))

print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

pilihan = input("Pilih Operasi:")

if pilihan ==  "1":
    print("hasil=", angka_1 + angka_2 + angka_3 + angka_4 + angka_5)

if pilihan ==  "2":
    print("hasil=", angka_1 - angka_2 - angka_3 - angka_4 - angka_5)

if pilihan ==  "3":
    print("hasil=", angka_1 * angka_2 * angka_3 * angka_4 * angka_5)

if pilihan ==  "4":
    print("hasil=", angka_1 / angka_2 / angka_3 / angka_4 / angka_5)

if pilihan ==  "5":
    print("hasil=", angka_1 + angka_2 - angka_3 * angka_4 / angka_5)

else:
    print("pilihan tidak valid")