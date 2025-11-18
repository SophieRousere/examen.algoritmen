def main():
    try: #2 getallen vragen en delen door elkaar
        number1 = int(input("Enter an integer: "))      
        number2 = int(input("Enter an integer: "))      
        result = number1 / number2
        print("Result is " + str(result))  #/0: deze lijn ni uitgevoerd

    except ZeroDivisionError: # Catch zero divisor error
        print("Division by zero!")
    except:
        print("Something wrong in the input")
    else:   #else wordt enkel uitgevoerd als geen vd excepts w uitgevoerd
        print("No exceptions")
    finally: #deze altijd uitgevoerd
        print("The finally clause is executed")

main()