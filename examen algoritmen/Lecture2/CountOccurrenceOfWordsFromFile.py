def main():
    # Prompt the user to enter a file
    filename = input("Enter a filename: ").strip()  #filename vragen en openstellen
    inputFile = open(filename, "r") # Open the file om uit te lezen

    wordCounts = {} # Create an empty dictionary to count words
    for line in inputFile: #per lijn in de file #dit al es gdn vr characters
        processLine(line.lower(), wordCounts)
    inputFile.close() 
    
    pairs = list(wordCounts.items()) # Get pairs from the dictionary   

    items = [[x, y] for (y, x) in pairs] # Reverse pairs in the list, want sorteren op getallen

    items.sort() # Sort pairs in items

    for i in range(len(items) - 1, 0, -1):  #v groot nr klein
        print(items[i][1] + "\t" + str(items[i][0]))  #kleur(key)    getallen(value)
  
# Count each word in the line
def processLine(line, wordCounts): #lijn en dictionary
    line = replacePunctuations(line) # Replace punctuations with space: alle speciale tekens worden vervangen door spaties
    words = line.split() # Get words from each line: words = lijst van woorden
    for word in words: #woorden een vr een toevoegen
        if word in wordCounts:
            wordCounts[word] += 1  #als woord al in dictionary zit +1
        else:
            wordCounts[word] = 1  #zit het er nog niet in: nieuw woord toevoegen en op 1 zetten

# Replace punctuations in the line with space
def replacePunctuations(line):
    for ch in line:
        if ch in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':  #is character speciaal teken: maak er spatie van
            line = line.replace(ch, " ")

    return line

main()
