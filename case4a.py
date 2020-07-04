# jumlah input bilangan prima.
try:
    input = int(input("masukkan jumlah bilangan prima: "))
except:
  #pengecualian jika user tidak input bilangan bulat
    print("Input harus bilangan bulat.")
    exit()

# inisiasi
startNumber = 1
primeList = []
#looping function
while True:
    if input <= 0:
        print("input harus lebih dari 0.")
        break
    # Periksa setiap nomor dari 1 untuk prime kecuali entri nomor prima terpenuhi
    if startNumber > 1:
        for i in range(2,startNumber):
            if (startNumber % i) == 0:
                break
        else:
          # menambahkan nilai baru pada list prima
            primeList.append(startNumber)
    #fungsi looping cetak
    if (len(primeList) == input):
        print(primeList)
        break
    else:
        startNumber = startNumber + 1
        continue