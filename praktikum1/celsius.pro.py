class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
mycelcius = int(input("masukkan nilai celsius : "))
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
myreamur = Celcius.to_reamur(mycelcius)
mykelvin = Celcius.to_kelvin(mycelcius)

print(myfahrenheit)
print(mykelvin)
print(myreamur)