

details=[value for value in input("Enter value: ").split()]
try:
    with open('sample.txt', 'a') as file:
        file.write(str(details))
except Exception as e:
    print("Error", e)