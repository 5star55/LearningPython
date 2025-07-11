car=["Toyota", "camry", "maybach", "mercedes", "ford", "Hyundai", "Lexus"]
index=int(input("Enter 0-6 to choose your random car: "))

def returnCar(i):
    return car[i]

try:
    print(returnCar(index))
except Exception as e:
    print(e, " Choose number from range")
except:
    print("Something went wrong")