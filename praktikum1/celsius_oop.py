class derajat:
    def __init__(self,celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        F = self.celsius * 9/5 + 32
        return F    
    def to_kelvin(self):
        K = self.celsius + 273.15
        return K
    def to_reamur(self):
        R = self.celsius * 4/5
        return R
    
C = float(input("masukkan nilai celsius : "))

A = derajat(C)

myfahrenheit = A.to_fahrenheit()
myreamur = A.to_reamur()
mykelvin = A.to_kelvin()

print("konversi",C, "derajat celcius adalah ",myfahrenheit, "derajat fahrenheit")
print("konversi",C, "derajat celcius adalah ",mykelvin, "derajat kelvin")
print("konversi",C, "derajat celcius adalah ",myreamur, "derajat reamur")