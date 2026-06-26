

def mul(l):
    ans = 1
    for k in l:
        ans *= k 
    return ans

def prime(num):
    primes = []
    temp = num
    constant = 1
    while num != mul(primes):
        constant += 1
        if temp % constant == 0 :
            primes.append(constant)
            temp = temp/constant
            constant = 1

    return primes

def simplify(num):
    deno = 10 ** (len(str(num).lstrip("1234567890"))-1)
    nume = num * deno
    prime_deno= prime(deno)
    prime_nume= prime(nume)

    common = list(set(prime_deno)&set(prime_nume))

    for k in common:
        deno =  deno / k
        nume = nume/ k
    print("  ",int(nume))
    print("  ",int(deno))

while 1:
    simplify(float(input("\nEnter the number : ")))





