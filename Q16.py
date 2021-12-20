'''Write a program to calculate the total price for car wash services. A base car wash is $10. A dictionary with each additional service
and the corresponding cost has been provided. Two additional services can be selected. A '-' signifies an additional service
was not selected. Output all selected services along with the cooresponding costs and then the total price for all car wash services.
Ex. If the input is:
Tire shine
Wax
The output is:
ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15'''

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()
print("ZyCar Wash")
print("Base car wash -- $10")
if service_choice1 in services:
    print(service_choice1,"-- $",services[service_choice1])
    base_wash += services[service_choice1]
elif(service_choice1 == "----"):
    print("-------------")
if service_choice2 in services:
    print(service_choice2, "-- $",services[service_choice2])
    base_wash += services[service_choice2]
print("----")
print("Total price: $",base_wash)

#ZyCar Wash
#Base car wash -- $10
#Tire shine -- $ 2
#Wax -- $ 3 #<---fix spacing issues and it will be correct
#----
#Total price: $ 15
