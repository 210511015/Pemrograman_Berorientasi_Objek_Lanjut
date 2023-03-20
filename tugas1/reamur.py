class reamur:
    def __init__(self, Re):
        self.Re = Re

    def to_kelvin(self):
        K = (self.Re / 0.8) + 273.15
        return K

    def to_celsius(self):
        C = self.Re * 0.8
        return C

    def to_fahrenheit(self):
        F = (self.Re * 2.25) + 32
        return F

R = int(input("masukkan nilai reamur: "))
A = reamur(R)   
mycelsius = A.to_celsius()
myfahrenheit = A.to_fahrenheit()
mykelvin = A.to_kelvin()

print("konversi",R, "derajat reamur adalah ",mycelsius, "derajat celsius")
print("konversi",R, "derajat reamur adalah ",myfahrenheit, "derajat fahrenheit")
print("konversi",R, "derajat reamur adalah ",mykelvin, "derajat kelvin")