import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from kategori import Kategori

class FormKategori:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode kategori    :').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama kategori  :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtKodekategori = Entry(mainFrame, width=20) 
        self.txtKodekategori.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKodekategori.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtNama_kategori = Entry(mainFrame, width=20) 
        self.txtNama_kategori.grid(row=1, column=1, padx=5, pady=5)
        
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idkategori','kodekategori', 'Nama_kategori')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idkategori', text='ID')
        self.tree.column('idkategori', width="30")
        self.tree.heading('kodekategori', text='Kodekategori')
        self.tree.column('kodekategori', width="90")
        self.tree.heading('Nama_kategori', text='Nama_kategori')
        self.tree.column('Nama_kategori', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKodekategori.delete(0,END)
        self.txtKodekategori.insert(END,"")
        self.txtNama_kategori.delete(0,END)
        self.txtNama_kategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data kategori
        kategori = Kategori()
        result = kategori.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodekategori = self.txtKodekategori.get()
        kategori = Kategori()
        res = kategori.getByKodekategori(kodekategori)
        rec = kategori.affected
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
        kodekategori = self.txtKodekategori.get()
        kategori = Kategori()
        res = kategori.getByKodekategori(kodekategori)
        self.txtNama_kategori.delete(0,END)
        self.txtNama_kategori.insert(END,kategori.nama_kategori)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodekategori = self.txtKodekategori.get()
        nama_kategori = self.txtNama_kategori.get()
        
        kategori = Kategori()
        kategori.kodekategori = kodekategori
        kategori.nama_kategori = nama_kategori
        if(self.ditemukan==True):
            res = kategori.updateByKodekategori(kodekategori)
            ket = 'Diperbarui'
        else:
            res = kategori.simpan()
            ket = 'Disimpan'
            
        rec = kategori.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodekategori = self.txtKodekategori.get()
        kategori = Kategori()
        kategori.kodekategori = kodekategori
        if(self.ditemukan==True):
            res = kategori.deleteByKodekategori(kodekategori)
            rec = kategori.affected
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
    aplikasi = FormKategori(root2, "Daftar Kategori")
    root2.mainloop() 
