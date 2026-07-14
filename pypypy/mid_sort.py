"""def mid_postition(arr: list, item: int):
    count = 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        count += 1
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == item:
            return mid, count
        
        elif guess > item:
            right = mid - 1

        else: 
            left = mid + 1

    return None

print (mid_postition([1,2,3,4,5,6,7,8], 3))"""


def mid_position(arr: list, item: int):
    count = 0
    left = 0
    right = len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]
        count +=1

        if guess == item:
            return mid, count
        
        elif guess > item:
            right = mid - 1

        else:
            left = mid + 1
        
    return None 

print(mid_position([1,2,3,4,5,6,7,8,9,10], 5))