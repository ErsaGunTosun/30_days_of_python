from math import floor
import math
from operator import le
# Day 2


#exercise 1

name = "ersagun"
last_name = "takar"
full_name = name+ " "+ last_name 
country = "Turkey"
city = "Istanbul"
age = 20
year = 2022
is_maried = False
is_true = True
is_light_on = False

# exercise 2

username, password,mail,is_login = "Fikret","12345678FKRT","fkrt14567455125758@fkrt.com",False
print(username)
print(password)
print(mail)
print(is_login)

#exercise 3

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one -num_two
product = num_one * num_two
divison = num_one / num_two
remainder = num_one % num_two
floor_divison = num_one // num_two
exp = num_one ** num_two

print(total)
print(diff)
print(product)
print(divison)
print(remainder)
print(floor_divison)
print(exp)


#exercise 4

print("name length: ", len(name))
print("last name  length: ", len(last_name))


#exercise 5 

r = 30
pi = int(math.pi)
area_of_circle = (r**2)*pi
circum_of_circle = 2*pi*r
print(area_of_circle)
print(circum_of_circle)

#exercise 6 

user_name = input("Name: ")
user_last_name = input("Last Name: ")
user_country = input("Country: ")
user_age = input("Age: ")

#exercise 
help(str)
