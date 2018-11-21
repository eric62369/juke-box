'''
    A place for brushing up on Python
'''

user_message = input("Starting now:")
list = []

while not user_message == "STOP":
    list.append(user_message)
    user_message = input("Keep going:")

print("Now I'm done.")
print(list)
