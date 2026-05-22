def count_even_numbers(arr):
    count = 0

    for num in arr:
        if num % 2 == 0:
            count += 1

    return count


nums = [1, 2, 3, 4, 5, 6]
print(count_even_numbers(nums))
