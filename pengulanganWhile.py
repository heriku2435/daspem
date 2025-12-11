#pengulangan while
#tampilkan kata hello dunia sebanyak 100 kali

print("---Pengulangan While---")
hit = 0
while(hit <= 100):
    if(hit % 3 == 0 and hit % 5 == 0):
        print("Fizz Bazz")
    elif(hit % 3 == 0):
        print("Fizz")
    elif(hit % 5 == 0):
        print("Bazz")
    else:
        print(hit)
    hit += 1

print("---Akhir Pengulangan While---")

#buat pengulangan 0 - 100
#jika bilangan habis dibagi 3 maka ganti angkanya menjadi fizz
#jika bilangan habis dibagi 5 maka ganti angka menjadi bazz
#jika bilangan habis dibagi 3 dan 5 ganti angka menjadi fizz bazz
    