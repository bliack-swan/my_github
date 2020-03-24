def the_biggest_el ( arg ) :
    if len ( arg ) <= 1 :
        return arg [ 0 ] if len ( arg ) != 0 else None
    elif len ( arg ) == 2 :
        return arg [ 0 ] if arg [ 0 ] > arg [ 1 ] else arg [ 1 ]
    else :
        max_value = the_biggest_el ( arg [ 1 : ] )
        return arg [ 0 ] if arg [ 0 ] > max_value else max_value


def qsort ( array ) :
    if len ( array ) < 2 :
        return array
    else :
        high = len ( array )
        mid = (high) // 2
        base_el = array [ mid ]
        less = [ i for i in array if i < base_el ]
        greater = [ i for i in array if i > base_el ]
        return qsort ( less ) + [ base_el ] + qsort ( greater )


a = qsort ( [ 2 , 1 , 4 , 25 , 6 , 3547 , 6444 , 345 , 732345 , 831 , 346788 , 2 ] )
print ( a )
