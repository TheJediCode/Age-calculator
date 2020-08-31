x = float(input("How many years old are you?\n"))
y = int(input("\nHow many days until your birthday?\n"))
z = 365-y
c = x*365
a = c+z

def multiply():
    print("Hours:", 24*a)
    print("Days:", a)
    print("Weeks:", a/7)
    print("Months:", a/30)
    print("Years:", a/365)
    print("You're getting old, boy.")

multiply()
