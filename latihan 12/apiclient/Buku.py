from db import DBConnection as mydb

class Buku:

    def __init__(self):
        self.__id=None
        self.__kode_buku=None
        self.__judul=None
        self.__pengarang=None
        self.__penerbit=None
        self.__tahun=None
        self.__kode_kategori=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "kode_buku:" + self.__kode_buku + "\n" + "judul:" + self.__judul + "\n" + "pengarang" + self.__pengarang + "\n" + "penerbit:" + self.__penerbit + "\n" + "tahun" + self.__tahun + "\n" + "kode_kategori" + self.__kode_kategori
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kode_buku(self):
        return self.__kode_buku

    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value

    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value

    @property
    def tahun(self):
        return self.__tahun

    @tahun.setter
    def tahun(self, value):
        self.__tahun = value

    @property
    def kode_kategori(self):
        return self.__kode_kategori

    @pengarang.setter
    def kode_kategori(self, value):
        self.__kode_kategori = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_buku, self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kode_kategori)
        sql="INSERT INTO BUku (kode_buku, judul, pengarang, penerbit, tahun, kode_kategori) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_buku, self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kode_kategori, id)
        sql="UPDATE Buku SET kode_buku = %s, judul = %s, pengarang=%s, penerbit=%s, tahun=%s, kode_kategori=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateBykode_buku(self, kode_buku):
        self.conn = mydb()
        val = (self.__judul, self.__pengarang, self.__penerbit, self.__tahun, self.__kode_kategori, kode_buku)
        sql="UPDATE Buku SET judul = %s, pengarang=%s, penerbit=%s, tahun=%s, kode_kategori=%s WHERE kode_buku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM Buku WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteBykode_buku(self, kode_buku):
        self.conn = mydb()
        sql="DELETE FROM Buku WHERE kode_buku='" + str(kode_buku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM Buku WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_buku = self.result[1]
        self.__judul = self.result[2]
        self.__pengarang = self.result[3]
        self.__penerbit = self.result[4]
        self.__tahun = self.result[5]
        self.__kode_kategori = self.result[6]
        self.conn.disconnect
        return self.result

    def getBykode_buku(self, kode_buku):
        a=str(kode_buku)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE kode_buku='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_buku = self.result[1]
            self.__judul = self.result[2]
            self.__pengarang = self.result[3]
            self.__penerbit = self.result[4]
            self.__tahun = self.result[5]
            self.__kode_kategori = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_buku = ''
            self.__judul = ''
            self.__pengarang = ''
            self.__penerbit = ''
            self.__tahun = ''
            self.__kode_kategori = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM Buku"
        self.result = self.conn.findAll(sql)
        return self.result

# a = Buku()
# b = a.getAllData()
# print(b)