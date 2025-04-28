def find_combinations(numbers, target):
    result = []
    numbers.sort()

    def search(start_index, remaining_sum, current_combination):
        if remaining_sum == 0:
            result.append(current_combination[:])
            return


        previous = None
        for i in range(start_index, len(numbers)):
            current = numbers[i]


            if current > remaining_sum:
                break
            if current == previous:
                continue


            current_combination.append(current)
            search(i + 1, remaining_sum - current, current_combination)
            current_combination.pop()

            previous = current


    search(0, target, [])
    return result

numbers = [1, 3, 4, 6, 7, 1, 3, 6, 2, 5, 1]
target = int(input("Введите вашу цель: "))

print(f"Исходные числа: {numbers}")
print(f"Целевая сумма: {target}")
combinations = find_combinations(numbers, target)
print(f"Найденные комбинации: {combinations}")