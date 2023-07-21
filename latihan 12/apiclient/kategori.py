from db import DBConnection as mydb


class Kategori:
    
    def __init__(self):
        self.__id=None
        self.__kodekategori=None
        self.__nama_kategori=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Kategori:" +self.__kodekategori + "nama_kategori:" + self.__nama_kategori
        else:
            return self.__info
        
    @info.setter
    def info(self, value):
        self.__info = value
    
    @property
    def id(self):
        return self.__id
    
    @property
    def kodekategori(self):
        return self.__kodekategori
    
    @kodekategori.setter
    def kodekategori(self, value):
        self.__kodekategori = value
    
    @property
    def nama_kategori(self):
        return self.__nama_kategori
    
    @nama_kategori.setter
    def nama_kategori(self, value):
        self.__nama_kategori = value
    
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kodekategori, self.__nama_kategori)
        sql="INSERT INTO kategori (kodekategori, nama_kategori) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__kodekategori, self.__nama_kategori, id)
        sql="UPDATE kategori SET kodekategori = %s, nama_kategori = %s WHERE idkategori = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKodekategori(self, kodekategori):
        self.conn = mydb()
        val = (self.__nama_kategori, kodekategori)
        sql="UPDATE kategori SET nama_kategori =%s WHERE kodekategori = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE idkategori='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def deleteByKodekategori(self, kodekategori):
        self.conn = mydb()
        sql="DELETE FROM kategori WHERE kodekategori='" + str(kodekategori) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE idkategori='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodekategori = self.result[1]
        self.__nama_kategori = self.result[2]
        self.conn.disconnect
        return self.result

    def getByKodekategori(self, kodekategori):
        a=str(kodekategori)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kategori WHERE kodekategori='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodekategori = self.result[1]
            self.__nama_kategori = self.result[2]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodekategori = ''
            self.__nama_kategori = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kategori"
        self.result = self.conn.findAll(sql)
        return self.result
    
# a = Kategori()
# b = a.getAllData()
# print(b)