import time
#test starttijd en eindtijd en verschil bijhouden
# eenvoudige lus die start bij 0 en gaat nr n en tijd ertussen printen
def getTime(n):
    startTime = time.time()
    k = 0
    for i in range(n):
        k = k + 5
    endTime = time.time()
    print("Execution time for n =", n, "is",
        endTime - startTime, "seconds")

def main():
    getTime(10000)  #met 10 000 iteraties uitvoeren
    getTime(100000)
    getTime(1000000)
    getTime(10000000)
#functie oproepen maar n gaat wijzigen
main()