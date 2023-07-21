import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import Buku
from tkinter import *
class FormBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("710x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode :').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Judul:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Pengarang:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Penerbit:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Terbit tahun:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kode kategori:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Daftar buku di perpustakaan').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtkode_buku = Entry(mainFrame, width=30) 
        self.txtkode_buku.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkode_buku.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtJudul = Entry(mainFrame, width=30) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        
        self.txtPengarang = Entry(mainFrame, width=30) 
        self.txtPengarang.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtPenerbit = Entry(mainFrame, width=30)
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5,)
       
        self.txtTahun = Entry(mainFrame, width=30) 
        self.txtTahun.grid(row=4, column=1, padx=5, pady=5) 
        
        self.txtKode_kategori = Entry(mainFrame, width=30) 
        self.txtKode_kategori.grid(row=5, column=1, padx=5, pady=5)

        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = (0,1,2,3,4,5,6)

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading(0, text='Kode')
        self.tree.column(0, width="70")
        self.tree.heading(1, text='Judul')
        self.tree.column(1, width="200")
        self.tree.heading(2, text='Pengarang')
        self.tree.column(2, width="150")
        self.tree.heading(3, text='Penerbit')
        self.tree.column(3, width="150")
        self.tree.heading(4, text='Tahun')
        self.tree.column(4, width="45")
        self.tree.heading(5, text='Kategori')
        self.tree.column(5, width="85")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()

        # we = Scrollbar(mainFrame, orient="horizontal", command=self.tree.xview)
        # we.grid(fill=X, side=BOTTOM)

        # self.tree.configure(hscrollcommand=we.set)
        
    def onClear(self, event=None):
        self.txtkode_buku.delete(0,END)
        self.txtkode_buku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")    
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.txtKode_kategori.delete(0,END)
        self.txtKode_kategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        buku = Buku()
        result = buku.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kode_buku = self.txtkode_buku.get()
        buku = Buku()
        res = buku.getBykode_buku(kode_buku)
        rec = buku.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtPenerbit.focus()
        return res
        
    def TampilkanData(self, event=None):
        kode_buku = self.txtkode_buku.get()
        buku = Buku()
        res = buku.getBykode_buku(kode_buku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,buku.judul)
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,buku.pengarang)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,buku.penerbit)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,buku.tahun)
        self.txtKode_kategori.delete(0,END)
        self.txtKode_kategori.insert(END,buku.kode_kategori)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kode_buku = self.txtkode_buku.get()
        judul = self.txtJudul.get()
        pengarang = self.txtPengarang.get()
        penerbit = self.txtPenerbit.get()
        tahun = self.txtTahun.get()
        kode_kategori = self.txtKode_kategori.get()
        
        buku = Buku()
        buku.kode_buku = kode_buku
        buku.judul = judul
        buku.pengarang = pengarang
        buku.penerbit = penerbit
        buku.tahun= tahun
        buku.kode_kategori = kode_kategori
        if(self.ditemukan==True):
            res = buku.updateBykode_buku(kode_buku)
            ket = 'Diperbarui'
        else:
            res = buku.simpan()
            ket = 'Disimpan'
            
        rec = buku.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kode_buku = self.txtkode_buku.get()
        buku = Buku()
        buku.kode_buku = kode_buku
        if(self.ditemukan==True):
            res = buku.deleteBykode_buku(kode_buku)
            rec = buku.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FormBuku(root2, "Daftar Buku")
    root2.mainloop() 
