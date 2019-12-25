N = int(input("Введите целое число: "))
print("Все квадраты в данном диапозоне:")
print([i**2 for i in range (1,N) if i**2 <= N])