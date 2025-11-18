def main():
    filename = input("Enter a filename: ").strip()   #strip: spaties weglaten anders gaat file nt goed geopend worden
    inputFile = open(filename, "r") # Open the file: inlezen v bestand

    counts = 26 * [0] # Create and initialize counts: dit is de lijst die je creeert: 26 plaatsen die allemaal op 0 staan
    for line in inputFile: #lijnen inlezen
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)  #oproepen per lijn, tellen
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0: #dus nul niet printen
            print(chr(ord('a') + i) + " appears " + str(counts[i]) #gwne print
              + (" time" if counts[i] == 1 else " times")) #time - times

    inputFile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): #lijn en lijst v aantal keer a etc
    for ch in line:  #in lijn per karakter kijken
        if ch.isalpha(): # Test if ch is a letter
            counts[ord(ch) - ord('a')] += 1  #lijst counts: asci waarde v character - asci waarde van a: zorgen dat a op plaats 0 staat, b op plaats 1 etc

main() # Call the main function
