import tkinter as tk
import datetime as dt
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from peminjaman import Peminjaman
from tkcalendar import DateEntry

class FormPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("930x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Nomor Bukti:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tgl Pinjam:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kode Anggota:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kode Buku 1:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kode Buku 2:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tgl Harus Kembali:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tgl Dikembalikan:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Status Pinjam:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomorBukti = Entry(mainFrame) 
        self.txtNomorBukti.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNomorBukti.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txttgl_pinjam = DateEntry(mainFrame) 
        self.txttgl_pinjam.grid(row=1, column=1, padx=5, pady=5)
        self.txtkode_anggota = Entry(mainFrame) 
        self.txtkode_anggota.grid(row=2, column=1, padx=5, pady=5)
        self.txtkode_buku1 = Entry(mainFrame) 
        self.txtkode_buku1.grid(row=3, column=1, padx=5, pady=5)
        self.txtkode_buku2 = Entry(mainFrame) 
        self.txtkode_buku2.grid(row=4, column=1, padx=5, pady=5)
        self.txttgl_hrskembali = DateEntry(mainFrame) 
        self.txttgl_hrskembali.grid(row=5, column=1, padx=5, pady=5) 
        self.txtTgl_Dikembalikan = DateEntry(mainFrame) 
        self.txtTgl_Dikembalikan.grid(row=6, column=1, pady=5) 
        self.txtStatus_Pinjam = Entry(mainFrame) 
        self.txtStatus_Pinjam.grid(row=7, column=1, padx=5, pady=5) 

        # Radio Button
        self.txtStatus_Pinjam = StringVar()
        self.S = Radiobutton(mainFrame, text='Sudah Dikembalikan', value='S', variable=self.txtStatus_Pinjam)
        self.S.grid(row=7, column=1, padx=5, pady=5, sticky=W)
        self.S.select() # set pilihan yg pertama
        self.B = Radiobutton(mainFrame, text='Belum Dikembalikan', value='B', variable=self.txtStatus_Pinjam)
        self.B.grid(row=7, column=2, padx=5, pady=5, sticky=W)
        
    
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = (0,1,2,3,4,5,6,7,8)

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading(0, text='ID')
        self.tree.column(0, width="30")
        self.tree.heading(1, text='Nomor Bukti')
        self.tree.column(1, width="100")
        self.tree.heading(2, text='Tanggal Pinjam')
        self.tree.column(2, width="100")
        self.tree.heading(3, text='Kode Anggota')
        self.tree.column(3, width="100")
        self.tree.heading(4, text='Kode Buku 1')
        self.tree.column(4, width="100")
        self.tree.heading(5, text='Kode Buku 2')
        self.tree.column(5, width="100")
        self.tree.heading(6, text='Tanggal Harus Kembali')
        self.tree.column(6, width="140")
        self.tree.heading(7, text='Tanggal Dikembalikan')
        self.tree.column(7, width="130")
        self.tree.heading(8, text='Status Pinjam')
        self.tree.column(8, width="120")
        # set tree position
        self.tree.place(x=0, y=300)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNomorBukti.delete(0,END)
        self.txtNomorBukti.insert(END,"")
        self.txttgl_pinjam.delete(0,END)
        self.txttgl_pinjam.insert(END,"")
        self.txtkode_anggota.delete(0,END)   
        self.txtkode_anggota.insert(END,"")
        self.txtkode_buku1.delete(0,END)   
        self.txtkode_buku1.insert(END,"")
        self.txtkode_buku2.delete(0,END) 
        self.txtkode_buku2.insert(END,"")
        self.txttgl_hrskembali.delete(0,END)
        self.txttgl_hrskembali.insert(END,"")   
        self.txtTgl_Dikembalikan.delete(0,END)
        self.txtTgl_Dikembalikan.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.S.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        perpustakaan = Peminjaman()
        result = perpustakaan.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        per=[]
        for row_data in result:
            per.append(row_data)

        for per in per:
            self.tree.insert('',END, values=per)
    
    def onCari(self, event=None):
        nomorbukti = self.txtNomorBukti.get()
        perpustakaan = Peminjaman()
        res = perpustakaan.getByNomorBukti(nomorbukti)
        rec = perpustakaan.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txttgl_pinjam.focus()
        return res
        
    def TampilkanData(self, event=None):
        nomorbukti = self.txtNomorBukti.get()
        perpustakaan = Peminjaman()
        res = perpustakaan.getByNomorBukti(nomorbukti)
        self.txttgl_pinjam.delete(0,END)
        self.txttgl_pinjam.insert(END,perpustakaan.tgl_pinjam)
        self.txtkode_anggota.delete(0,END)
        self.txtkode_anggota.insert(END,perpustakaan.kode_anggota)
        self.txtkode_buku1.delete(0,END)
        self.txtkode_buku1.insert(END, perpustakaan.kode_buku1)
        self.txtkode_buku2.delete(0,END)
        self.txtkode_buku2.insert(END,perpustakaan.kode_buku2)
        self.txttgl_hrskembali.delete(0,END)
        self.txttgl_hrskembali.insert(END,perpustakaan.tgl_hrskembali)
        self.txtTgl_Dikembalikan.delete(0,END)
        self.txtTgl_Dikembalikan.insert(END,perpustakaan.tgl_dikembalikan)
        statuspinjam = perpustakaan.status_pinjam
        if(statuspinjam=="B"):
            self.B.select()
        else:
            self.S.select()
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nomorbukti = self.txtNomorBukti.get()
        tgl_pinjam = self.txttgl_pinjam.get()
        kode_anggota = self.txtkode_anggota.get()
        kode_buku1 = self.txtkode_buku1.get()
        kode_buku2 = self.txtkode_buku2.get()
        tgl_hrskembali = self.txttgl_hrskembali.get()
        tgl_dikembalikan = self.txtTgl_Dikembalikan.get()
        status_pinjam = self.txtStatus_Pinjam.get()
        
        perpustakaan = Peminjaman()
        perpustakaan.nomorbukti = nomorbukti
        perpustakaan.tgl_pinjam = tgl_pinjam
        perpustakaan.kode_anggota = kode_anggota
        perpustakaan.kode_buku1 = kode_buku1
        perpustakaan.kode_buku2 = kode_buku2
        perpustakaan.tgl_hrskembali = tgl_hrskembali
        perpustakaan.tgl_dikembalikan = tgl_dikembalikan
        perpustakaan.status_pinjam = status_pinjam

        if(self.ditemukan==True):
            res = perpustakaan.updateByNomorBukti(nomorbukti)
            ket = 'Diperbarui'
        else:
            res = perpustakaan.simpan()
            ket = 'Disimpan'
            
        rec = perpustakaan.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nomorbukti = self.txtNomorBukti.get()
        perpustakaan = Peminjaman()
        perpustakaan.nomorbukti = nomorbukti
        if(self.ditemukan==True):
            res = perpustakaan.deleteByNomorBukti(nomorbukti)
            rec = perpustakaan.affected
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
    aplikasi = FormPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop() 
