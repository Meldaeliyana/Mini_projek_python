nama = input("Nama Mahasiswa:")
nilai = int(input("Masukkan Nilai:"))

if nilai >= 85:
    grade = "A"

elif nilai >= 70:
    grade = "B"

elif nilai >=55:
    grade = "C"

else:
    grade = "D"

print("Nama:", nama)
print("Grade:", grade)