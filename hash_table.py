voted = {}


def check ( name ) :
    if voted.get ( name ) :  # None == False
        print ( "KIK" )
    else :
        voted [ name ] = True
        print ( "OK" )


check ( "Tom" )
check ( "Tom" )
