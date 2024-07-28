import timeit

# Реалізація жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result

# Реалізація алгоритму динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_used_coin = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_used_coin[i] = coin
    
    result = {}
    i = amount
    while i > 0:
        coin = last_used_coin[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin
    
    return result

# Порівняння ефективності алгоритмів
def compare_algorithms(amount):
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)

    print(f"Жадібний алгоритм: {greedy_time:.6f} секунд")
    print(f"Динамічне програмування: {dp_time:.6f} секунд")

# Тести
def test_algorithms():
    assert find_coins_greedy(113) == {50: 2, 10: 1, 2: 1, 1: 1}
    assert find_min_coins(113) == {1: 1, 2: 1, 10: 1, 50: 2}
    print("Всі тести пройдені!")

# Головна функція
def main():
    amount = 113

    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))
    
    print("\nПорівняння ефективності:")
    compare_algorithms(amount)
    
    print("\nЗапуск тестів:")
    test_algorithms()

if __name__ == "__main__":
    main()
