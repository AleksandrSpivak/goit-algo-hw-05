def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
 
    while low < high:

        count += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid
        else:
            return (count, arr[mid])
 
    return (count, arr[high])

if __name__ == "__main__":
    arr = [2.2, 3.3, 4.4, 10.0, 40.5, 42.2, 55.55, 68.686868, 333.333333, 354.123, 751.01, 1022.02, 5001.11]
    x = float(input(f"введіть число для перевірки\n"))

    if x > max(arr):
        print(f"В масиві не існує верхньої межі для елементy {x}")
    else:
        count, result = binary_search(arr, x)
        print(f"Верхня межа елемента {x} в масиві - це {result}")
        print(f"Ітерацій зроблено: {count}")
