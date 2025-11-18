def main():
    n = int(input("Enter a nonnegative integer: "))
    print("Factorial of", n, "is", factorial(n))

# Return the factorial for a specified number 
def factorial(n):
    return factorialHelper(n, 1) # Call auxiliary function
  
# Auxiliary tail-recursive function for factorial 
def factorialHelper(n, result):
    if n == 0:
        return result  #stopconditie, result zit erin als parameter
    else:
        return factorialHelper(n - 1, n * result) # Recursive call
        #deze oproep bevat het eindresultaat, er moet niets meer gebeuren want resultaat zit er als argument in
#als afbouw v frames gebeurt kun je ze wegdoen want moet er nks meer mee doen
#door te werken met argument sla je resultaat op in fctie => efficientie verhogen
main() # Call the main function