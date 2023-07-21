from db import DBConnection as mydb

class Anggota:

    def __init__(self):
        self.__id=None
        self.__kode_anggota=None
        self.__nama=None
        self.__jk=None
        self.__alamat=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Anggota:" + self.__kode_anggota + "\n" + "Nama:" + self.__nama + "\n" + "Jk" + self.__jk + "\n" + "Alamat:" + self.__alamat
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_anggota, self.__nama, self.__jk, self.__alamat)
        sql="INSERT INTO anggota (kode_anggota, nama, jk, alamat) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_anggota, self.__nama, self.__jk, self.__alamat, id)
        sql="UPDATE anggota SET kode_anggota = %s, nama = %s, jk=%s, alamat=%s WHERE id_anggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKode(self, kode_anggota):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__alamat, kode_anggota)
        sql="UPDATE anggota SET nama = %s, jk=%s, alamat=%s WHERE kode_anggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE id_anggota='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKode(self, kode_anggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE kode_anggota='" + str(kode_anggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE id_anggota='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_anggota = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__alamat = self.result[4]
        self.conn.disconnect
        return self.result

    def getByKode(self, Kode_anggota):
        a=str(Kode_anggota)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE kode_anggota='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_anggota = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__alamat = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_anggota = ''
            self.__nama = ''
            self.__jk = ''
            self.__alamat = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM anggota"
        self.result = self.conn.findAll(sql)
        return self.result
    
# a = Anggota()
# b = a.getAllData()
# print(b)