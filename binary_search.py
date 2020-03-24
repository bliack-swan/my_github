def binary_search ( list , item ) :
    low = 0
    high = len ( list ) - 1
    while low <= high :
        mid = (low + high) // 2
        guess = list [ mid ]
        if item == guess :
            return mid
        if item < guess :
            high = mid - 1
        if item > guess :
            low = mid + 1
    return None


def bad_search ( list , item ) :
    for i in range ( 0 , len ( list ) ) :
        if item == list [ i ] :
            return i
        else :
            i += 1
    return None


print ( binary_search ( [ el for el in range ( 0 , 2 ** 24 + 1 ) ] , 2 ** 23 ) )
