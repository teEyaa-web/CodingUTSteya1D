# data mahasiswa
nama = "Rina"
nilai1 = 85
nilai2 = 78
nilai3 = 92

# menghitung total nilai
total = nilai1 + nilai2 + nilai3

# menghitung rata-rata
rata_rata  = total / 3 

# menghitung presentase
presentase = (total / 300 ) * 100

# mwmenentukan kelulusan
lulus = rata_rata >= 75

# menampilan hasil
print("===============================")
print("kartu nilai sementara") 
print("===============================")
print("nama :", nama)
print("nilai 1 :", nilai1)
print("nilai 2 :", nilai2)
print("nilai 3 :", nilai3)
print("-------------------------------")
print("total :", total)
print("rata-rata :", format(rata_rata, ".2f"))
print("presentase :", str(presentase) + "%")
print("lulus :", lulus)
print("===============================")