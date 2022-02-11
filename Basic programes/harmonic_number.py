def nthHarmonic(N) :
    harmonic = 1.00
    for i in range(2, N + 1):
        harmonic += 1 / i

    return harmonic

if __name__ == "__main__":
    N = 4
    print(round(nthHarmonic(N), 5))