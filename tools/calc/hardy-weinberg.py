# p² + 2pq + q² = 1
# p + q = 1

import math

def find_p(res):
    q = float(math.sqrt(res / 100))
    p = float(1 - q)
    return  f"Frequency of dominant allele: {p:.3f}\n" \
            f"Frequency of recessive allele: {q:.3f}\n" \
            f"Frequency of dominant homozygotes: {(p**2):.3f}\n" \
            f"Frequency of heterozygotes: {(2*p*q):.3f}\n" \
            f"Frequency of recessive homozygotes: {(q**2):.3f}\n" \
            f"Frequency of dominant phenotype: {((p**2)+(2*p*q)):.3f}"

def main():
    res = float(input("Frequency of recessive allele (%): "))
    print(' ')
    print(find_p(res))

if __name__ == '__main__':
    main()