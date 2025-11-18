def main():
    # Open file for output
    outputFile = open("President.txt", "w") #object openen, object beschikbaar met als naam outputfile

    # Write data to the file
    outputFile.write("George Washington\n") #stuk tekst met nieuwe lijn op einde
    outputFile.write("John Adams\n") #2e stuk tekst met op einde nieuwe lijn
    outputFile.write("Thomas Jefferson") #Write Thomas Jefferson

    outputFile.close() # Close the output file #niet vergeten sluiten!

main() # Call the main function

"als je dit runt bekom je nieuwe tkst file: president.txt"
"2 lijnen code kennen: openen en write: "
