from typing import List
from user import User


with open("users.csv", "r") as csv_file:
    csv_lines = csv_file.readlines()

clear_lines = [line.replace("\n", "") for line in csv_lines]

print(clear_lines)

users_data = {"headers": clear_lines.pop(0), "data": clear_lines}

print(users_data)

users: List[User] = User.from_csv(users_data)

print(users)

print('------')
print(users[0].__str__())

new = users[0].__add__(users[1])

print(users[0].__sub__(users[1]))

print('----------')

print(users[0].to_xml())