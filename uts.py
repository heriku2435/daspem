#inputan user
bilangan = input("Masukkan bilangan : ") #string

#hitung panjang karakter dari bilangan
pjgBilangan = len(bilangan)

#buat kondisi menentukan tempat bilangan
if(pjgBilangan == 7):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan jutaan")
    print(bilangan[1] + " merupakan ratusan ribu")
    print(bilangan[2] + " merupakan puluhan ribu")
    print(bilangan[3] + " merupakan ribuan")
    print(bilangan[4] + " merupakan ratusan")
    print(bilangan[5] + " merupakan puluhan")
    print(bilangan[6] + " merupakan satuan")
elif(pjgBilangan == 6):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan ratusan ribu")
    print(bilangan[1] + " merupakan puluhan ribu")
    print(bilangan[2] + " merupakan ribuan")
    print(bilangan[3] + " merupakan ratusan")
    print(bilangan[4] + " merupakan puluhan")
    print(bilangan[5] + " merupakan satuan")
elif(pjgBilangan == 5):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan puluhan ribu")
    print(bilangan[1] + " merupakan ribuan")
    print(bilangan[2] + " merupakan ratusan")
    print(bilangan[3] + " merupakan puluhan")
    print(bilangan[4] + " merupakan satuan")
elif(pjgBilangan == 4):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan ribuan")
    print(bilangan[1] + " merupakan ratusan")
    print(bilangan[2] + " merupakan puluhan")
    print(bilangan[3] + " merupakan satuan")
elif(pjgBilangan == 3):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan ratusan")
    print(bilangan[1] + " merupakan puluhan")
    print(bilangan[2] + " merupakan satuan")
elif(pjgBilangan == 2):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan[0] + " merupakan puluhan")
    print(bilangan[1] + " merupakan satuan")
elif(pjgBilangan == 1):
    print("Anda memasukkan bilangan ", bilangan + " dimana: ")
    print(bilangan + " merupakan satuan")
else:
    print("Anda tidak memasukkan bilangan")