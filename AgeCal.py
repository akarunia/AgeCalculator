# import module
from tkinter import *
from tkinter import messagebox
from datetime import date

# initializing tkinter
root = Tk()
root.geometry("410x350")
root.title("Age Calculator")

# loading gambar 
photo = PhotoImage(file="gambar.png")
myimage = Label(image=photo)
myimage.grid(row=0, column=0, columnspan=2)

# menyiapkan label umur
ageLabel = Label()

# membuat fungsi 
def calculateAge():
    today = date.today()
    nama = nameEntry.get()
    tahun = yearEntry.get()
    bulan = monthEntry.get()
    tanggal = dayEntry.get()
    try:
        if nama == "" or tahun == "" or bulan == "" or tanggal == "":
            messagebox.showinfo("Field Kosong","Harap Isi Data Yang Kosong!")
            return
        else:
            # mengubah inputan string menjadi format tanggal lahir
            birthDate = date(int(tahun), int(bulan), int(tanggal))
            if birthDate > today:
                messagebox.showinfo("Luar Biasa","Anda Belum Memiliki Umur Jika Lahir Di Masa Depan")
                return   
        # menghitung umur
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))       
        # setting isi dari label umur
        ageLabel.config(text=f"{nama}, Umur Anda Sekarang Adalah {age} Tahun")
    except ValueError:
        messagebox.showerror("Number Error","Data Tahun, Bulan, dan Tanggal Barus Berupa Angka Bulat (Integer) > 0!")
        return

# membuat label untuk menanyakan identitas
Label(text="Nama").grid(row=1, column=0)
Label(text="Tahun Lahir").grid(row=2, column=0)
Label(text="Bulan Lahir").grid(row=3, column=0)
Label(text="Tanggal Lahir").grid(row=4, column=0)

# mendeklarasikan variable (string) untuk menyimpan identitas
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# membuat widget untuk memasukkan identitas
nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

# memposisikan label
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

# membuat button untuk menghitung umur
Button(text="Hitung Umur", command=calculateAge).grid(row=5, column=0, columnspan=2, pady=20)

# menampilkan label umur
ageLabel.grid(row=7, column=0, columnspan=2)

root.mainloop()