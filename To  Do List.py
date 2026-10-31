todo = []
while True:
    tugas = input("masukkan tugas:")
    if tugas == "selesai":
        break

    todo.append(tugas)

print("\nDaftar Tugas")

for i in range(len(todo)):
    print(i+1,".",todo[i])