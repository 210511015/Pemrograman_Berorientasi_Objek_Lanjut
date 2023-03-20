class Celcius:
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    def to_kelvin(celsius):
        return celsius + 273.15
    def to_reamur(celsius):
        return celsius * 4/5
C = int(input("masukkan nilai celsius : "))
myfahrenheit = Celcius.to_fahrenheit(C)
myreamur = Celcius.to_reamur(C)
mykelvin = Celcius.to_kelvin(C)

print("konversi",C, "derajat celcius adalah ",myfahrenheit, "derajat fahrenheit")
print("konversi",C, "derajat celcius adalah ",mykelvin, "derajat kelvin")
print("konversi",C, "derajat celcius adalah ",myreamur, "derajat reamur")