def main():
    print("Двузначные простые числа:")
    for i in range(10, 100):
        if prime_number_calculation(i):
            print(i, end=" ")

def prime_number_calculation(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()