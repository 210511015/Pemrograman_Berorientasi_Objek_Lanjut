class kelvin:
    def __init__(self, Ke):
        self.Ke = Ke

    def to_reamur(self):
        R = (self.Ke - 273) * 4/5
        return R

    def to_celsius(self):
        C = self.Ke - 273
        return C

    def to_fahrenheit(self):
        F = (self.Ke * 9/5) - 459.67
        return F

K = int(input("masukkan nilai kelvin: "))
A = kelvin(K)   
mycelsius = A.to_celsius()
myfahrenheit = A.to_fahrenheit()
myreamur = A.to_reamur()

print("konversi",K, "derajat kelvin adalah ",str(mycelsius), "derajat celsius")
print("konversi",K, "derajat kelvin adalah ",myfahrenheit, "derajat fahrenheit")
print("konversi",K, "derajat kelvin adalah ",myreamur, "derajat reamur")