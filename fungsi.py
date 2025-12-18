#rumus luas persegi panjang
panjang = 5
lebar = 3
luasPersegiPanjang = panjang * lebar
print(luasPersegiPanjang)

panjang1 = 4
lebar1 = 2
luasPersegiPanjang1 = panjang1 * lebar1
print(luasPersegiPanjang1)

#fungsi pada Python
print("hai... apa kabar")
def hello(nama):
    print(f"Hai {nama}... Selamat Pagi")

hello("Hariri")
hello("Haryanto")

def luasPersegiPjg(pjg, lbr):
    luas = pjg * lbr
    hasil = print(f"Luas Persegi Panjang yang memiliki ukuran {pjg} dan {lbr} adalah {luas}"  )
    #hasil = print("Luas Persegi Panjang yang memiliki ukuran ", pjg, "dan", lbr, " adalah ", luas)
    return hasil

luasPersegiPjg(3, 2)
luasPersegiPjg(15, 4)