def main():
#meerdere read mogelijkheden: runnen vr mogeijkheden
    #1e manier: Open file for input: alles inlezen en printen
    inputFile = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(inputFile.read()) # Read all in the file, alles ingelezen en alles geprint
    inputFile.close() # Close the input file

    #2e manier: Open file for input: aantal karakters
    inputFile = open("Presidents.txt", "r")
    print("\n(2) Using read(number): ")
    s1 = inputFile.read(5)
    print(s1)
    s2 = inputFile.read(15) # Read 15 characters to s2
    print(repr(s2))  #repr functie toont letterlijk wat is ingelezen
    inputFile.close() # Close the input file

    # Open file for input: readline: CSV bestand inlezen: elke lijn komt overeen met een aankoop: zo lijn per lijn inlezen
    inputFile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = inputFile.readline() # Read a line
    line2 = inputFile.readline()
    line3 = inputFile.readline()
    line4 = inputFile.readline()
    print(repr(line1))  #repr vr \n, leest ook nieuwe lijn mee
    print(repr(line2))
    print(repr(line3))  #meest gebruikt
    print(repr(line4))
    inputFile.close() # Close the input file

    # Open file for input : alles inlezen, plaatst het in een lijst ook handig vr alle records v csv bestand in te lezen
    inputFile = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ")
    print(inputFile.readlines())
    inputFile.close() # Close the input file

main() # Call the main function
