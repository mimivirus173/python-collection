# p² + 2pq + q2 = 1
# p + q = 1

import math

def calculate_freqs(q2):
    q = float(math.sqrt(q2 / 100))
    p = float(1 - q)
    return  f"Frequency of dominant allele: {p:.3f}\n" \
            f"Frequency of recessive allele: {q:.3f}\n" \
            f"Frequency of dominant homozygotes: {(p**2):.3f}\n" \
            f"Frequency of heterozygotes: {(2*p*q):.3f}\n" \
            f"Frequency of recessive homozygotes: {(q**2):.3f}\n" \
            f"Frequency of dominant phenotype: {((p**2)+(2*p*q)):.3f}"

def main():
    try:
        q2 = float(input("Frequency of recessive allele (%): "))  
    except ValueError:
        print("Invalid input!")
        exit(0)
    if q2 < 0 or q2 > 100:
        print("Invalid input!")
        exit(0) 
    print(' ')
    print(calculate_freqs(q2))

if __name__ == '__main__':
    main()