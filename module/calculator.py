
from module.clear import clear

def calculator():
    while True:
        clear()
        print("=== KALKULATOR ===")
        
        try:
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        operasi = input("Pilih operasi: \n1. +\n2. -\n3. * \n4. /  \nMasukkan pilihan: ")

        if operasi == "+":
            result = angka1 + angka2
        elif operasi == "-":
            result = angka1 - angka2
        elif operasi == "*":
            result = angka1 * angka2
        elif operasi == "/":
            if angka2 == 0:
                print("Tidak dapat membagi dengan nol!")
                input("Tekan Enter untuk melanjutkan...")
                continue
            result = angka1 / angka2
        else:
            print("Operasi tidak valid.")
            input("Tekan Enter untuk melanjutkan...")
            continue

        print(f"Hasil: {result}")

        # Lanjutkan operasi dengan hasil sementara
        while True:
            lanjut = input("Apakah ingin melanjutkan operasi dengan hasil ini? [y/n]: ") 
            if lanjut == "n":
                break
            elif lanjut == "y":
                try:
                    operasi_lanjutan = input("Masukkan operasi \n + \n - \n * \n / : ")
                    angka_baru = int(input("Masukkan angka: "))
                    
                    if operasi_lanjutan == "+":
                        result += angka_baru
                    elif operasi_lanjutan == "-":
                        result -= angka_baru
                    elif operasi_lanjutan == "*":
                        result *= angka_baru
                    elif operasi_lanjutan == "/":
                        if angka_baru == 0:
                            print("Tidak dapat membagi dengan nol!")
                            continue
                        result /= angka_baru
                    else:
                        print("Operasi tidak valid.")
                        continue
                    
                    print(f"Hasil sementara: {result}")
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'.")
                continue
        
        opsi = input("Apakah ingin menghitung lagi? [y/n]: ").lower()
        if opsi == "n":
            print("Terima kasih telah menggunakan kalkulator!")
            break
