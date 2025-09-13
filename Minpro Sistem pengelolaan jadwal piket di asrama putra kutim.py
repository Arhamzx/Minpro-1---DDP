jadwal_piket = [
    ("Arham", "Senin", "Bersihkan Kulkas"),
    ("Milo", "Selasa", "Sikat Wc"),
    ("Dika", "Rabu", "Pel Lantai"),
    ("Agun", "Kamis", "Cuci Alat Masak"),
    ("Ade", "Jumat", "Buang Sampah"),
]

print("Sistem Pengelolaan Jadwal Piket di Asrama Putra Kutim")
print("1. Tambah Jadwal Piket")  #Create
print("2. Lihat Jadwal Piket")   #Read
print("3. Ubah Jadwal Piket")    #Update
print("4. Hapus Jadwal Piket")   #Delete

pilihan = input("Pilih Menu (1-4): ")

#Create
if pilihan == "1":
    print("Jadwal Piket Sebelumnya: ", jadwal_piket)
    Nama = input("Masukkan Nama Penghuni: ")
    Hari = input("Masukkan Hari Piket: ")
    Tugas = input("Masukkan Tugas Piket: ")

    data_piket = (Nama, Hari, Tugas)
    jadwal_piket.append(data_piket) #untuk nambah data ke list, pake fungsi append

    print("Jadwal Piket Berhasil Ditambahkan!")
    print("Jadwal Piket Saat Ini:", jadwal_piket)

#Read
elif pilihan == "2":
    if not jadwal_piket:
        print("Jadwal Piket Masih Kosong.")
    else:
        print("Jadwal Piket Saat Ini: ", jadwal_piket)

#Update
elif pilihan == "3":
    if not jadwal_piket:
        print("Jadwal Piket Masih Kosong, Tidak Dapat Mengubah Data.")
    else:
        print("Jadwal Piket Sebelumnya: ", jadwal_piket)
        index = int(input("Masukkan Index Jadwal Piket yang Ingin Diubah (Dari 0): "))
        if index < len(jadwal_piket): #Untuk Cek index yang diinput, gaboleh lebih dari panjang list(isi list)
            nama = input("Masukkan Nama Penghuni: ")
            hari = input("Masukkan Hari Piket yang Baru: ")
            tugas = input("Masukkan Tugas Piket yang Baru: ")

            jadwal_piket[index] = (nama, hari, tugas)
            print("Jadwal Piket Berhasil Diubah!")
            print("Jadwal Piket Saat Ini: ", jadwal_piket)

        else:
            print("Index Tidak Valid.")

#Delete (menggunakan fungsi del)hehe
elif pilihan == "4":
    if not jadwal_piket:
        print("Jadwal Piket Masih Kosong, Tidak Dapat Menghapus Data.")
    else:
        print("Jadwal Piket Sebelumnya: ", jadwal_piket)
        index = int(input("Masukkan Index Jadwal Piket yang Ingin Dihapus (Dari 0): "))
        
        if index < len(jadwal_piket): #Untuk Cek index yang diinput, gaboleh lebih dari panjang list(isi list)
            del jadwal_piket[index] #Untuk hapus data berdasarkan index, pake fungsi del
            print("Jadwal Piket Berhasil Dihapus!")
            print("Jadwal Piket Saat Ini: ", jadwal_piket)
        else:
            print("Index Tidak Valid.")

else:
    print("Pilihan Tidak Valid.")
    print("Silahkan Pilih Menu (1-4) Saja.")