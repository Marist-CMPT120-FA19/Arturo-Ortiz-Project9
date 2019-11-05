#Project 11
#The Sieve of Eratosthenes, finding all prime numbers up to some limit
#By Arturo Ortiz, arturo.ortiz1@marist.edu

def main(n):
    initial = []
    primenums = []
    for i in range(2,n+1):
        if i not in initial:
            primenums.append(i)
            #Adds another number to the list each loop
            for j in range(i*i,n+1,i):
                initial.append(j)
                
        #New list with all the prime numbers
    return primenums
prime = int(input("Primes less than or equal to what number (n): "))
print(main(prime))
