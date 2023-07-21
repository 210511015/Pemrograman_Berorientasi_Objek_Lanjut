from db import DBConnection as mydb

class Peminjaman:

    def _init_(self):
        self.__idbuku=None
        self.__nomorbukti=None
        self.__tgl_pinjam=None
        self.__kode_anggota=None
        self.__kode_buku1=None
        self.__kode_buku2=None
        self.__tgl_hrskembali=None
        self.__tgl_dikembalikan=None
        self.__status_pinjam=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "nomorbukti:" + self.__nomorbukti + "\n" + "tgl_pinjam:" + self.tgl_pinjam + "\n" + "kode_anggota" + self.kode_anggota + "\n" + "kode_buku1:" + self.__kode_buku1 + "\n" + "kode_buku2" + self.__kode_buku2 + "\n" + "tgl_hrskembali" + self.__tgl_hrskembali + "\n" + "tgl_dikembalikan" + self.__tgl_dikembalikan + "\n" + "status_pinjam" + self.__status_pinjam
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def idpeminjaman(self):
        return self.__idbuku

    @property
    def nomorbukti(self):
        return self.__nomorbukti

    @nomorbukti.setter
    def nomorbukti(self, value):
        self.__nomorbukti = value

    @property
    def tgl_pinjam(self):
        return self.__tgl_pinjam

    @tgl_pinjam.setter
    def tgl_pinjam(self, value):
        self.__tgl_pinjam = value

    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value

    @property
    def kode_buku1(self):
        return self.__kode_buku1

    @kode_buku1.setter
    def kode_buku1(self, value):
        self.__kode_buku1 = value

    @property
    def kode_buku2(self):
        return self.__kode_buku2

    @kode_buku2.setter
    def kode_buku2(self, value):
        self.__kode_buku2 = value

    @property
    def tgl_hrskembali(self):
        return self.__tgl_hrskembali

    @tgl_hrskembali.setter
    def tgl_hrskembali(self, value):
        self.__tgl_hrskembali = value

    @property
    def tgl_dikembalikan(self):
        return self.__tgl_dikembalikan

    @tgl_dikembalikan.setter
    def tgl_dikembalikan(self, value):
        self.__tgl_dikembalikan = value

    @property
    def status_pinjam(self):
        return self.__status_pinjam

    @status_pinjam.setter
    def status_pinjam(self, value):
        self.__status_pinjam = value

    def simpan(self):
        self.conn = mydb()
        val = (self.nomorbukti, self.tgl_pinjam, self.kode_anggota, self.kode_buku1, self.kode_buku2, self.tgl_hrskembali, self.tgl_dikembalikan, self.status_pinjam)
        sql="INSERT INTO peminjaman (nomorbukti, tgl_pinjam, kode_anggota, kode_buku1, kode_buku2, tgl_hrskembali, tgl_dikembalikan, status_pinjam) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, idpeminjaman):
        self.conn = mydb()
        val = (self.nomorbukti, self.tgl_pinjam, self.kode_anggota, self.kode_buku1, self.kode_buku2, self.tgl_hrskembali, self.tgl_dikembalikan, self.status_pinjam, idpeminjaman)
        sql="UPDATE peminjaman SET nomorbukti = %s, tgl_pinjam = %s, kode_anggota=%s, kode_buku1=%s, kode_buku2=%s, tgl_hrskembali=%s, tgl_dikembalikan=%s, status_pinjam=%s  WHERE idpeminjaman=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBytgl_pinjam(self, tgl_pinjam):
        self.conn = mydb()
        val = (self.nomorbukti, self.tgl_pinjam, self.kode_anggota, self.kode_buku1, self.kode_buku2, self.tgl_hrskembali, self.tgl_dikembalikan, self.status_pinjam, tgl_pinjam)
        sql="UPDATE peminjaman SET nomorbukti = %s, tgl_pinjam = %s, kode_anggota=%s, kode_buku1=%s, kode_buku2=%s, tgl_hrskembali=%s, tgl_dikembalikan=%s, status_pinjam=%s  WHERE tgl_pinjam=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected         

    def updateByNomorBukti(self, nomorbukti):
        self.conn = mydb()
        val = (self.tgl_pinjam, self.kode_anggota, self.kode_buku1, self.kode_buku2, self.tgl_hrskembali, self.tgl_dikembalikan, self.status_pinjam, nomorbukti)
        sql="UPDATE peminjaman SET tgl_pinjam = %s, kode_anggota=%s, kode_buku1=%s, kode_buku2=%s, tgl_hrskembali=%s, tgl_dikembalikan=%s, status_pinjam=%s  WHERE nomorbukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected   

    def delete(self, idpeminjaman):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE idpeminjaman='" + str(idpeminjaman) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBytgl_pinjam(self, tgl_pinjam):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE tgl_pinjam='" + str(tgl_pinjam) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNomorBukti(self, nomorbukti):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE nomorbukti='" + str(nomorbukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByidbuku(self, idpeminjaman):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE idpeminjaman='" + str(idpeminjaman) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomorbukti = self.result[1]
        self.__tgl_pinjam = self.result[2]
        self.__kode_anggota = self.result[3]
        self.__kode_buku1 = self.result[4]
        self.__kode_buku2 = self.result[5]
        self.__tgl_hrskembali = self.result[6]
        self.__tgl_dikembalikan = self.result[7]
        self.__status_pinjam = self.result[8]
        self.conn.disconnect
        return self.result

    def getByNomorBukti(self, nomorbukti):
        a=str(nomorbukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE nomorbukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomorbukti = self.result[1]
            self.__tgl_pinjam = self.result[2]
            self.__kode_anggota = self.result[3]
            self.__kode_buku1 = self.result[4]
            self.__kode_buku2 = self.result[5]
            self.__tgl_hrskembali = self.result[6]
            self.__tgl_dikembalikan = self.result[7]
            self.__status_pinjam = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomorbukti = ''
            self.__tgl_pinjam = ''
            self.__kode_anggota = ''
            self.__kode_buku1 = ''
            self.__kode_buku2 = ''
            self.__tgl_hrskembali = ''
            self.__tgl_dikembalikan = ''
            self.__status_pinjam = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getBytgl_pinjam(self, tgl_pinjam):
        a=str(tgl_pinjam)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE tgl_pinjam='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomorbukti = self.result[1]
            self.__tgl_pinjam = self.result[2]
            self.__kode_anggota = self.result[3]
            self.__kode_buku1 = self.result[4]
            self.__kode_buku2 = self.result[5]
            self.__tgl_hrskembali = self.result[6]
            self.__tgl_dikembalikan = self.result[7]
            self.__status_pinjam = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomorbukti = ''
            self.__tgl_pinjam = ''
            self.__kode_anggota = ''
            self.__kode_buku1 = ''
            self.__kode_buku2 = ''
            self.__tgl_hrskembali= ''
            self.__tgl_dikembalikan = ''
            self.__status_pinjam = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman"
        self.result = self.conn.findAll(sql)
        return self.result
    
a = Peminjaman()
b = a.getAllData()
print(b)