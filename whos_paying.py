import random
print("welcome to my first project in githup")
print('you will me give me a list of names and i will apick aperson to pay ')
names=input("enter the name separated by commin").split(", ")
print(f"sorry {random.choice(names)} but you pay")
