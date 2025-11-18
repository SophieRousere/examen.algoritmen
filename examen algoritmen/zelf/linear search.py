#linear search

def LinearSearch(lijst, key):
    for i in range(len(lijst)-1):
        if lijst[i] == key:
            return i
        else:
            i += 1

    return None

def main():
    lijst = [0,1,5,7,10]
    print(LinearSearch(lijst, 5))

main()