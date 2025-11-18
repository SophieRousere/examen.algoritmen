from random import randint 

def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w") #w van write
    for i in range(10): #range van 1 tem 10
        # random getal genereren tussen 0 en 9
        #str: random getal printen: omzetten nr string want tekstfile verwacht strings
        outputFile.write(str(randint(0, 9)) + " ")  #spatie achter
    outputFile.close() # Close the file

#write staat los vh inlezen
    # Open file for reading data
    inputFile = open("Numbers.txt", "r")
    s = inputFile.read() # Read all data to s  #inputfile volledig inlezen
    #door string, tekstbestand gaan en omzetten naar floats
    #s.split = tekst splitten: elementen uithallen tussen spaties
    numbers = [float(x) for x in s.split()] #in list plaatsen  #float: tekstelement nr kommagetal
    for number in numbers:
        print(number, end = " ")
    inputFile.close() # Close the file
    
main() # Call the main function

#split is belangrijk en omzetten naar float om er verder mee te kunnen werken als numbers
