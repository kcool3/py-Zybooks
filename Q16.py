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


service1 = input()
service2 = input()
additional = {'Air Freshner':1, 'Rain Repellent':2, 'Tire shine':2, 'Wax':3, 'Vacuum':5}
print("ZyCar Wash")
print("Base car wash -- $10")
total_price=10
if service1 in additional:
    print(service1, "--$", additional[service1])
    total_price += additional [service1]
elif(service1 == "----"):
    print("-------------")
if service2 in additional:
    print(service2, "--$", additional[service2])
    total_price += additional[service2]
elif(service2 == "----"):
    print("-------------")
print("Total price: $", + total_price)
