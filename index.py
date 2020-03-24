class Town:
    _count=0
    
    def __init__(self, name):
        self._name = name
        self._count
        

    def __repr__(self):
        return f'Town({self._name})'
    
    @staticmethod
    def _count():
         _count+=1
    
town = Town('KR')
print(town)
