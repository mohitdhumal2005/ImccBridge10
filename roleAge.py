role = input("Enter role: ")   # e.g. "student"
age = int(input("Enter age: "))

eligible = (role == "student") and (age < 21)

print("Eligible:", eligible)