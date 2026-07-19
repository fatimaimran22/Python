with open("students.txt","w") as file:
    for i in range(2):
        name=input("Enter Student name: ")
        marks=input("Enter Student marks: ")
        file.write(f"{name}: {marks}\n")

with open("students.txt","r") as file:
    print(file.read())

with open("students.txt","a") as file:
    name=input("Enter Student name: ")
    marks=input("Enter Student marks: ")
    file.write(f"{name}: {marks}\n")