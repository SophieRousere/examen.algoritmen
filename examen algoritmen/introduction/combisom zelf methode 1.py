def combisom(lijst, somgetal):
    for i in range(len(lijst)-1):
        for j in range(i+1, len(lijst)):
            som = lijst[i] + lijst[j]
            if som == somgetal:
                return True
    return False

def main():
    lijst = [-3, 7, 9, 20, 1]
    print(combisom(lijst, 17))
main()