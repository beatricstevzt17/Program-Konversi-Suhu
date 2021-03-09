#PROGRAM KONVERSI TEMPERATURE BY BEA
def menu():
    print("=====TEMPERATURE ° CONVERTER=====")
    print("[1]. Celcius (°C)")
    print("[2]. Reamur (°R)")
    print("[3]. Fahrenheit (°F)")
    print("[4]. Kelvin (K)")
    print("[0]. Exit")
    choose = int(input(">>>"))
    if choose == 0:
        exit()
    elif choose == 1:
        print("Celcius")
        suhu = float(input("Masukkan suhu = "))
        reamur      = (4/5)*suhu
        farenheit   = ((9/5)*suhu) + 32
        kelvin      = float(suhu + 273)
        print("Suhu dalam Reamur adalah = ", reamur,"°R")
        print("Suhu dalam Fahrenheit adalah = ", farenheit,"°F")
        print("Suhu dalam Kelvin adalah = ", kelvin,"K")
        print("\n")
    elif choose == 2:
        print("Reamur")
        suhu = float(input("Masukkan suhu = "))
        celcius     = (5/4)*suhu
        fahrenheit  = ((9/4)*suhu)+32
        kelvin      = ((5/4)*suhu)+273
        print("Suhu dalam Celcius = ", celcius,"°C")
        print("Suhu dalam Fahrenheit = ", fahrenheit,"°F")
        print("Suhu dalam Kelvin = ", kelvin,"K")
        print("\n")
    elif choose == 3:
        print("Fahrenheit")
        suhu = float(input("Masukkan suhu = "))
        celcius     = (5/9)*(suhu - 32)
        reamur      = (4/9)*(suhu - 32)
        kelvin      = ((5/4)*((4/9)*(suhu-32))) + 273
        print("Suhu dalam Celcius = ", celcius,"°C")
        print("Suhu dalam Reamur = ", reamur,"°R")
        print("Suhu dalam Kelvin = ", kelvin,"K")
        print("\n")
    elif choose == 4:
        print("Kelvin")
        suhu = float(input("Masukkan suhu = "))
        celcius     = suhu - 273
        reamur      = (4/5)*(suhu - 273)
        fahrenheit  = ((9/4)*((4/5)*(suhu-273))) + 32
        print("Suhu dalam Celcius adalah = ", celcius,"°C")
        print('Suhu dalam Reamur adalah = ', reamur,"°R")
        print("Suhu dalam Fahrenheit adalah = ", fahrenheit,"°F")
    else:
        print("ERROR, coba lagi...")
        menu()
if __name__ == "__main__":
    while True:
        menu()
