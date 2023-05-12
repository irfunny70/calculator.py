import math 

while True:
    print("\nchoose the math operation. \n\n0  - addition\n1  - subtraction\n2  - multiplication\n3  - division\n4  - modulo\n5  - raising to a power\n6  - square root\n7  - logarithm\n8  - sine\n9  - cosine\n10 - tangent")
    choice = input("\n choose your options:")
    
 # the float is there because the input function gets the user input as strings. 
 # But we actually need numbers in order to perform math operations like addition.
 # if not it will be interpreted as concatenation
    # addition
    if choice == "0":
        val1 = float(input ("\nchoose your first value:"))
        val2 = float(input ("\nchoose your second value:"))
        
        print("the result is:", str(val1 + val2) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break

 # subtraction
    elif choice == "1":
        val1 = float(input ("\nchoose your first value:"))
        val2 = float(input ("\nchoose your second value:"))
        print("the result is:", str(val1 - val2) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
 # multiplication
    elif choice == "2":
        val1 = float(input ("\nchoose your first value:"))
        val2 = float(input ("\nchoose your second value:"))
        print("the result is:", str(val1 * val2) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
 # division 
    elif choice == "3":
        val1 = float(input ("\nchoose your first value:"))
        val2 = float(input ("\nchoose your second value:"))
        print("the result is:", str(val1 / val2) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
 # modulo
    elif choice == "4":
        val1 = float(input ("\nchoose your first value:"))
        val2 = float(input ("\nchoose your second value:"))
        print("the result is:", str(val1 % val2) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break

 # raising to the power
    elif choice == "5":
        val1 = float(input ("\nchoose your base number:"))
        val2 = float(input ("\nchoose your power number:"))
        print("the result is:", str(math.pow(val1, val2)) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
 # square root
    elif choice == "6":
        val1 = float(input ("\nchoose your value to be square rooted:"))
        print("the result is:", str(math.sqrt(val1)) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break

 # logarithm
    elif choice == "7":
        val1 = float(input ("\nchoose your first value to calculate the logarithm with base of 2:"))
        print("the result is:", str(math.log(val1, 2)) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break

 # sine
    elif choice == "8":
        val1 = float(input ("\nchoose your value (in degrees for calculating the sine):"))
        
        print("the result is:", str(math.sin(math.radians(val1))) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
 # cosine
    elif choice == "9":
        val1 = float(input ("\nchoose your value (in degrees for calculating the cosine):"))
        
        print("the result is:", str(math.cos(math.radians(val1))) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break

 # tan
    elif choice == "10":
        val1 = float(input ("\nchoose your value (in degrees for calculating the tangent):"))
        
        print("the result is:", str(math.tan(math.radians(val1))) + "\n")
    
        back = input ("\n Go Back To The main Menu? (y/n)")
        if back == "y":
            continue
        else: 
            break
    
    else:
        print("\n invalid option!\n")
        continue


 



