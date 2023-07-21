import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from Anggota import Anggota
from tkinter import *


class FormAnggota:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("582x470")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='Kode Anggota       :').grid(row=0, column=0,
                                                           sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama                     :').grid(row=1, column=0,
                                                                 sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Jenis Kelamin        :').grid(row=2, column=0,
                                                             sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Alamat                   :').grid(row=4, column=0,
                                                                 sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DAFTAR ANGGOTA    :').grid(row=5, column=0,
                                                          sticky=W, padx=5, pady=5)

        # Textbox
        self.txtkodeA = Entry(mainFrame)
        self.txtkodeA.grid(row=0, column=1, padx=5, pady=5)
        # menambahkan event Enter key
        self.txtkodeA.bind("<Return>", self.onCari)
        self.txtnama = Entry(mainFrame)
        self.txtnama.grid(row=1, column=1, padx=5, pady=5)
        self.txtalamat = Entry(mainFrame)
        self.txtalamat.grid(row=4, column=1, padx=5, pady=5)

        # Radio Button
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki',
                             value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select()  # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan',
                             value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan',
                                command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear',
                               command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus',
                               command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id_anggota', 'kode_anggota', 'nama', 'jk', 'alamat')

        self.tree = ttk.Treeview(
            mainFrame, columns=columns, show='headings', height=7)
        # define headings
        self.tree.heading('id_anggota', text='ID')
        self.tree.column('id_anggota', width="30", anchor='center')
        self.tree.heading('kode_anggota', text='Kode Anggota')
        self.tree.column('kode_anggota', width="100", anchor='center')
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200", anchor='center')
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30", anchor='center')
        self.tree.heading('alamat', text='Alamat')
        self.tree.column('alamat', width="200", anchor='center')
        # set tree position
        self.tree.place(x=0, y=240)
        self.onReload()

        # # scrool bar
        # yscrollbar = Scrollbar(mainframe, orient="vertical", command=self.tree.yview)
        # yscrollbar.pack(side=RIGHT, fill="y")

        # self.tree.configure(yscrollcomand=yscrollbar.set)

    def onClear(self, event=None):
        self.txtkodeA.delete(0, END)
        self.txtkodeA.insert(END, "")
        self.txtnama.delete(0, END)
        self.txtnama.insert(END, "")
        self.txtalamat.delete(0, END)
        self.txtalamat.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data mahasiswa
        agt = Anggota()
        result = agt.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = []
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('', END, values=student)

    def onCari(self, event=None):
        kode_anggota = self.txtkodeA.get()
        agt = Anggota()
        res = agt.getByKode(kode_anggota)
        rec = agt.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtnama.focus()
        return res

    def TampilkanData(self, event=None):
        kode_anggota = self.txtkodeA.get()
        agt = Anggota()
        res = agt.getByKode(kode_anggota)
        self.txtnama.delete(0, END)
        self.txtnama.insert(END, agt.nama)
        self.txtalamat.delete(0, END)
        self.txtalamat.insert(END, agt.alamat)
        jk = agt.jk
        if (jk == "P"):
            self.P.select()
        else:
            self.L.select()

        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kode_anggota = self.txtkodeA.get()
        nama = self.txtnama.get()
        jk = self.txtJK.get()
        alamat = self.txtalamat.get()

        agt = Anggota()
        agt.kode_anggota = kode_anggota
        agt.nama = nama
        agt.jk = jk
        agt.alamat = alamat
        if (self.ditemukan == True):
            res = agt.updateByKode(kode_anggota)
            ket = 'Diperbarui'
        else:
            res = agt.simpan()
            ket = 'Disimpan'

        rec = agt.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kode_anggota = self.txtkodeA.get()
        agt = Anggota()
        agt.kode_anggota = kode_anggota
        if (self.ditemukan == True):
            res = agt.deleteByKode(kode_anggota)
            rec = agt.affected
        else:
            messagebox.showinfo(
                "showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0

        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FormAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()
