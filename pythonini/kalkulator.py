while True:
    print("\n=== Kalkulator Sederhana ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Sisa Bagi (%)")
    print("6. Keluar")

    pilihan = input("\nMasukkan pilihan (1-6): ")

    if pilihan == "6":
        print("\nTerima kasih telah menggunakan kalkulator!")
        break

    if pilihan not in ["1", "2", "3", "4", "5"]:
        print("Pilihan tidak valid!")
        continue

    angka1 = float(input("\nMasukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = angka1 + angka2
    elif pilihan == "2":
        hasil = angka1 - angka2
    elif pilihan == "3":
        hasil = angka1 * angka2
    elif pilihan == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("\nError: Pembagian dengan nol tidak bisa!")
            continue
    elif pilihan == "5":
        if angka2 != 0:
            hasil = angka1 % angka2
        else:
            print("\nError: Tidak bisa menghitung sisa bagi dengan nol!")
            continue

    print("\nHasil =", hasil)

    lanjut = input("\nIngin lanjut? (y/n): ").lower()
    if lanjut != "y":
        print("\nProgram selesai. Terima kasih!")
        break
