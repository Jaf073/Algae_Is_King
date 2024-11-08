# Python3 program to find modular
# inverse of A under modulo M

# A naive method to find modulor
# multiplicative inverse of A
# under modulo M
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def modInverse(A, M):
    if gcd(A, M) > 1:
      
        # modulo inverse does not exist
        return -1
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1


if __name__ == "__main__":
    A = math.log(103,29)
    M = 251

    print(A)
    print(modInverse(A, M))
