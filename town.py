class Citizen:
    def __init__(self, man):
        self._man = man 
    def __repr__(self):
        return f"Citizen({self._man})"
class Town:
    _count=0
    
    def __init__(self, name , man ):
        self._name = name
        self._count
        self.man = Citizen(man) 
        

    def __repr__(self):
        return f'Town({self._name,self.man})' 
    
    @staticmethod
    def _count():
         _count+=1
    
town = Town('KR','Toha')
print(town)
