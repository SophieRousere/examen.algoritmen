import os

def main():
    # Prompt the user to enter a directory or a file
    path = input("Enter a directory or a file: ").strip()   
   
    # Display the size
    try:
        print(getSize(path), "bytes")
    except:
        print("Directory or file does not exist")

def getSize(path):
    size = 0 # Store the total size of all files
    #starten met size 0 en test doen

    #2 mogelijkheden:
    #geen file: dan is het directory
    if not os.path.isfile(path):
        lst = os.listdir(path) # All files and subdirectories ophalen #geeft lijst met namen
        for subdirectory in lst: #vr al die files opnieuw fctie oproepen
            size += getSize(path + "\\" + subdirectory)   #recursieve oproep !!! zelfde functie oproepen voor subdirectories
    #het is een file: dit hieronder uitvoeren
    else: # Base case, it is a file: stopconditie
        size += os.path.getsize(path) # Accumulate file size

    return size

main() # Call the main function
