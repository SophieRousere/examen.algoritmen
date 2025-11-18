def main():
    # Open file for appending data
    outputFile = open("Info.txt", "a")  #openen met optie append (a)
    outputFile.write("\nPython is interpreted\n")
    outputFile.close() # Close the input file

main() # Call the main function

#als je dit runt gaje zien dat er lijn wordt toegevoegd aan Info.txt bestand
