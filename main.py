def exercicio1():
    for i in range(1, 11):
        print(i)

def exercicio2():
    for i in range(2, 21, 2):
        print(i)


def exercicio3():
    soma = sum(range(1, 101))
    print("A soma dos números de 1 a 100 é:", soma)

def exercicio4():
    for i in range(5, 51, 5):
        print(i)

def exercicio5():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

def exercicio6():
    num = float(input("Digite um número: "))
    if num > 0:
        print("O número é positivo.")
    elif num < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

def exercicio7():
    num = int(input("Digite um número para ver sua tabuada: "))
    print("Tabuada de", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

def exercicio8():
    numero = int(input("Digite um número: "))
    for i in range(1, numero + 1):
        print(i, end=" ")

def exercicio9():
    numero = int(input("Digite um número: "))
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    print("A soma dos números de 1 até", numero, "é:", soma)

def exercicio10():
    print("Números primos de 1 a 20:")
    for num in range(1, 21):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

def exercicio11():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    num = int(input("Digite um número para verificar se é primo: "))
    if is_prime(num):
        print(num, "é um número primo.")
    else:
        print(num, "não é um número primo.")

def exercicio12():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    num = int(input("Digite um número para calcular o fatorial: "))
    print("O fatorial de", num, "é:", factorial(num))

def exercicio13():
    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence

    n = 10
    print("Sequência de Fibonacci até o décimo termo:")
    print(fibonacci(n))

def exercicio14():
    def is_fibonacci(n):
        def is_perfect_square(x):
            s = int(x ** 0.5)
            return s * s == x

        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

    num = int(input("Digite um número para verificar se é um número de Fibonacci: "))
    if is_fibonacci(num):
        print(num, "é um número de Fibonacci.")
    else:
        print(num, "não é um número de Fibonacci.")

def exercicio15():
    num = int(input("Digite um número para calcular a soma dos seus dígitos: "))
    soma = sum(int(digit) for digit in str(num))
    print("A soma dos dígitos de", num, "é:", soma)

def exercicio16():
    num = int(input("Digite um número para imprimir os números pares e ímpares até esse número: "))
    print("Números pares até", num, ": ", end="")
    for i in range(2, num + 1, 2):
        print(i, end=" ")
    print("\nNúmeros ímpares até", num, ": ", end="")
    for i in range(1, num + 1, 2):
        print(i, end=" ")

def exercicio17():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    num = int(input("Digite um número para imprimir os números primos até esse número: "))
    print("Números primos até", num, ": ", end="")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")

def exercicio18():
    def collatz_sequence(n):
        while n != 1:
            print(n, end=' ')
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        print(1)

    num = int(input("Digite um número para imprimir a sequência de Collatz: "))
    collatz_sequence(num)

def exercicio19():
    num = int(input("Digite um número para calcular a soma dos números pares e ímpares até esse número: "))
    soma_pares = sum(i for i in range(1, num + 1) if i % 2 == 0)
    soma_impares = sum(i for i in range(1, num + 1) if i % 2 != 0)
    print(f"A soma dos números pares até {num} é {soma_pares}.")
    print(f"A soma dos números ímpares até {num} é {soma_impares}.")

def exercicio20():
    def is_perfect_number(n):
        divisors_sum = sum(i for i in range(1, n) if n % i == 0)
        return divisors_sum == n

    num = int(input("Digite um número para verificar se é um número perfeito: "))
    if is_perfect_number(num):
        print(num, "é um número perfeito.")
    else:
        print(num, "não é um número perfeito.")






def menu():
    while True:
        print("\n\n\n\n\n\n0. Sair\n1. Imprimir números de 1 a 10\n2. Imprimir números pares de 1 a 20\n3. Calcular soma de 1 a 100\n4. Imprimir múltiplos de 5 de 1 a 50\n5. Verificar se um número é par ou ímpar\n6. Verificar se um número é positivo, negativo ou zero\n7. Tabuada \n8. númeroAtéN \n9. SomaNatéN \n10. nPrimos \n11. verifPrimo \n12. fatorial \n13. Fibonacci \n14. ImprimaFibonnaci \n15. SomaDigitos \n16. ParImpar \n17. imprimirPrimosN \n18. Collatz \n19. SomaParImpN \n20. nPerfeito")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("Obrigado!")
            break
        elif opcao == 1:
            exercicio1()
        elif opcao == 2:
            exercicio2()
        elif opcao == 3:
            exercicio3()
        elif opcao == 4:
            exercicio4()
        elif opcao == 5:
            exercicio5()
        elif opcao == 6:
            exercicio6()
        elif opcao == 7:
            exercicio7()
        elif opcao == 8:
            exercicio8()
        elif opcao == 9:
            exercicio9()
        elif opcao == 10:
            exercicio10()
        elif opcao == 11:
            exercicio11()
        elif opcao == 12:
            exercicio12()
        elif opcao == 13:
            exercicio13()
        elif opcao == 14:
            exercicio14()
        elif opcao == 15:
            exercicio15()
        elif opcao == 16:
            exercicio16()
        elif opcao == 17:
            exercicio17()
        elif opcao == 18:
            exercicio18()
        elif opcao == 19:
            exercicio19()
        elif opcao == 20:
            exercicio20()

        else:
            print("Opção inválida!")

menu()
