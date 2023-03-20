class fahrenheit:
    def __init__(self, Fa):
        self.Fa = Fa

    def to_kelvin(self):
        K = ((self.Fa -32) * 5/9) + 273.15
        return K

    def to_celsius(self):
        C = (self.Fa - 32) * 5/9
        return C

    def to_reamur(self):
        R = (self.Fa -32) * 4/9
        return R

F = int(input("masukkan nilai fahrenheit: "))
A = fahrenheit(F)
mycelsius = A.to_celsius()
myreamur = A.to_reamur()
mykelvin = A.to_kelvin()

print("konversi",F, "derajat Fahrenheit adalah ",mycelsius, "derajat celsius")
print("konversi",F, "derajat Fahrenheit adalah ",myreamur, "derajat reamur")
print("konversi",F, "derajat Fahrenheit adalah ",mykelvin, "derajat kelvin")