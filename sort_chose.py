import random


class Sort :
    _mode_domain = {"smaller" : 0 , "bigger" : 1}

    def __init__ ( self , arg ) :
        self._arg = arg
        self._mode = 0

    def getter_arg ( self ) :
        return self._arg

    def setter_arg ( self , value ) :
        self._arg = value

    def getter_mode ( self ) :
        return self._mode

    def setter_mode ( self , value ) :
        self._mode = value

    def set_mode ( self , mode ) :
        try :
            self._mode = Sort._mode_domain [ mode ]
        except :
            print ( "Don\'t found this mode" )

    def _indexSmallest ( self ) :
        smallest = self._arg [ 0 ]
        smallest_index = 0
        for i in range ( 1 , len ( self._arg ) ) :
            if self._arg [ i ] < smallest :
                smallest = self._arg [ i ]
                smallest_index = i
        return smallest_index

    def _indexBiggest ( self ) :
        biggest = self._arg [ -1 ]
        biggest_index = -1
        for i in range ( 2 , len ( self._arg ) + 1 ) :
            if self._arg [ -i ] > biggest :
                biggest = self._arg [ -i ]
                biggest_index = -i
        return biggest_index

    def _sort_chose_smaller ( self , new_arg ) :
        for i in range ( 0 , len ( self._arg ) - 1 ) :
            smallest = self._indexSmallest ( )
            new_arg.append ( (self._arg.pop ( smallest )) )
        return new_arg

    def _sort_chose_bigger ( self , new_arg ) :
        for i in range ( 0 , len ( self._arg ) - 1 ) :
            biggest = self._indexBiggest ( )
            new_arg.append ( (self._arg.pop ( biggest )) )
        self._arg = new_arg

    def sort_chose ( self ) :
        new_arg = [ ]
        if self._mode == 0 :
            self._sort_chose_smaller ( new_arg )
        if self._mode == 1 :
            self._sort_chose_bigger ( new_arg )


random_list = [ ]
for el in range ( 0 , 10 ) :
    random_list.append ( random.randint ( 0 , 10000 ) )
print ( random_list )
random_list_obj = Sort ( random_list )
random_list_obj.set_mode ( "bigger" )
random_list_obj.sort_chose ( )
print ( random_list_obj.getter_arg ( ) )
s = [ 2 , 4 , 5 , 6 , 3 , 7 , 7.5 ]
s = filter ( lambda x : isinstance ( x , int ) , s )
print ( s )
