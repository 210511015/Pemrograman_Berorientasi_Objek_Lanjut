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
    
mycelcius = float(input("masukkan nilai celsius : "))

A = derajat(mycelcius)

myfahrenheit = A.to_fahrenheit()
myreamur = A.to_reamur()
mykelvin = A.to_kelvin()

print(myfahrenheit)
print(mykelvin)
print(myreamur)