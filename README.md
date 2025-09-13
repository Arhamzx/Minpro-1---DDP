Flowchart <img width="1122" height="791" alt="Screenshot 2025-09-13 135514" src="https://github.com/user-attachments/assets/e15506e7-6296-49ff-949b-ba58b6199954" />
<img width="1124" height="796" alt="Screenshot 2025-09-13 135527" src="https://github.com/user-attachments/assets/7868a5e2-efe9-48b5-b888-917aa36b5ca2" />
Start

Setelah program dijalankan, program akan menampilkan menu

input pilihan pada menu, 1-4, diluar itu maka terdeteksi tidak valid

ketika input menu 1, maka akan menampilkan jadwal piket sebelummnya, kemudian user mulai menambah jadwal., mulai dari nama, hari, kemudian tugas piket. Selanjutnya sistem akan menampilkan jadwal piket saat ini dan end.

Ketika user menginput menu 2, program akan menampilkan Jadwal Piket saat ini kemudian end.

Ketika user menginput menu 3, program akan menampilkan jadwal piket sebelum diubah, kemudian user diminta menginput index mana yang ingin diubah jadwalnya, (mulai dari 0), tergantung dari list jadwal piket sebelum di ubah. Misal pada jadwal piket sebelumnya, menampilkan 5 list, karena dhitung mulai dari 0, maka index ada 4. Jika user menginpuit diluar dari 0-4, maka akan terdeteksi tidak valid. Misal user ingin mengubah jadwal piket pada list ke 3, maka user harus menginput index 2. Setelahnya, user menginput nama, hari, dan tugas piket. Program akan menampilkan keterangan bahwa jadwal berhasil diubah, dan menampilkan jadwal piket saat ini.

Jika user menginput menu 4, program akan menampilkan jadwal piket sebelum dihapus, kemudian user menginput index mana yang ingin di hapus, sama seperti sebelumnya, jika menginput diluar dari panjang list, maka terdeteksi tidak valid kemudian end. Jadi user harus menginput index berdasar panjang list, misal user ingin menghapus index 2, maka user harus menginput index ke 2. Setelahnya, program akan menampilkan bahwa jadwal piket berdasarkan index yang diminta berhasil dihapus dan menunjukkan jadwal piket saat ini dan end

End

Menggukakan connector agar tampilan lebih rapi dan mudah untuk menghubungkan flow line, baik dalam satu page, maupun beda page.



Code
```Python
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
```


Tampilan awal (start)<img width="1920" height="1080" alt="Screenshot 2025-09-13 124858" src="https://github.com/user-attachments/assets/ea8b7dea-fc2a-471e-bcd1-599a9082c0fa" />

Menambahkan Jadwal (create)<img width="1920" height="1080" alt="Screenshot 2025-09-13 125053" src="https://github.com/user-attachments/assets/785cfc79-e25a-436a-8264-efb895aa87a9" />

Melihat Jadwal (read)<img width="1920" height="1080" alt="Screenshot 2025-09-13 125112" src="https://github.com/user-attachments/assets/335ad059-1d3d-4627-b451-80cedb62574c" />

Mengubah Jadwal (update)<img width="1920" height="1080" alt="Screenshot 2025-09-13 125159" src="https://github.com/user-attachments/assets/3d3a6a41-d4d1-4e2b-bd52-3a5bc87f9ed3" />

Jika index untuk mengubah jadwal, diluar dari panjang list <img width="1920" height="1080" alt="Screenshot 2025-09-13 125424" src="https://github.com/user-attachments/assets/6ff31b56-e9f7-4f40-b47b-c73d7e784581" />

Menghapus jadwal (berdasarkan index)<img width="1920" height="1080" alt="Screenshot 2025-09-13 125236" src="https://github.com/user-attachments/assets/8d58c0bf-31d5-4c5c-8220-627ce823bdbb" />

Jika index diluar dari panjang list<img width="1920" height="1080" alt="Screenshot 2025-09-13 125440" src="https://github.com/user-attachments/assets/87a31e5a-a35f-406a-82d4-e05fb95d766d" />



Saya menerapkan fungsi Input yang dipelajari pada pertemuan pertama, Percabangan, List, Menambah elemen(append), Remove(del) yang dipelajari pada pertemuan ke 2.


