import random

lower_case ="abcdefghijklmnopqrstuvwxyz"
upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="1234567890"
symbols ="!@#$%^&*"

combination = lower_case + upper_case + numbers + symbols
length_of_password = 8
password ="".join(random.sample(combination, length_of_password))
print(f"the generate a password :,{password}")

