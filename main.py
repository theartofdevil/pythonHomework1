### Part 1
"""
number=int(input("please enter a number: "))
if(number%2==0):
    print ("{} is an even number...".format(number))
else:
    print("{} is an odd number...".format(number))
"""
### Part 2
"""" 
number = int(input("Enter the number which is you want to check if it's a prime number or not : "))
counter = 0
for i in range(2, number/2):
    if number % i == 0:
        counter += 1

if counter == 0:
    print ("the number that you ve entered is a prime number")
else:
    print ("the number that you ve entered is NOT a prime number")
"""
### Part 3
"""
def cleaned():
    first_string = "Ah5me4t"
    second_string = "M9eHm4eT"
    third_string = "Ha3K5a1n"
    combined_value = " "
    # Remove numbers and capitalize only first letter
    first_string = ''.join([i for i in first_string if not i.isdigit()]).capitalize()
    second_string = ''.join([i for i in second_string if not i.isdigit()]).capitalize()
    third_string = ''.join([i for i in third_string if not i.isdigit()]).capitalize()
    # combine the strings
    combined_value = first_string + "-" + second_string + "-" + third_string
    # Return result
    print(combined_value)


cleaned()
"""
