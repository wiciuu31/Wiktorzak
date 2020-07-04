from abc import ABCMeta, abstractmethod # w Pythonie mechanizm klasy abstrakcyjnej nie jest wbudowany, ale umożliwia go standardowa biblioteka


class Pet():
    __metaclass__=ABCMeta # ta linia sprawia, że cała klasa jest abstrakcyjna i nie możemy stworzyć jej obiektu
    @abstractmethod # ta linia mówi, że poniższa metoda jest abstrakcyjna
    def speak(self): # ta metoda będzie występowała we wszystkich klasach pochodnych dokładnie tak samo się nazywając i przyjmując tyleż samo argumentów
        super().__init__()
        return 'no sound'
class Cat(Pet): # klasa Cat dziedziczy po Pet
    def __init__(self, name):
        self.name = name
    def speak(self): #W związku z czym musi mieć zaimplementowaną metodę abstrakcyjną o tej samej nazwie, spróbujcie zakomentować tą linię, odpalić program i przeczytać treść błędu :)
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    
    
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): # specjalna metoda nadpisująca operator '+' dla tego typu danych, więcej w referencjach na https://docs.python.org/3/reference/datamodel.html w sekcji 3.3.8.
        return self.name[0]+ ' i ' + other.name[0]
    
    
    
class Bunny(Pet):
    pass
    
    
    
class sonia(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self): #
        text('howhowsonia', random(42, width-29), random(50, height-50))
        return 'howhowsonia'
    
    def gimmePaw(self):
        image(loadImage("CAT-DOG.png"), random(30, width-110), random(30, height-50))
    def __add__(self, other): # specjalna metoda nadpisująca operator '+' dla tego typu danych, więcej w referencjach na https://docs.python.org/3/reference/datamodel.html w sekcji 3.3.8.
        return self.name[0]+ ' i ' + other.name[0]
    
def setup():
    size(400,400)
    textSize(20)
    rex = Dog('Rex') 
    benio = Dog('Benio')
    henio = sonia('Sonia')

    global list_of_pets
    list_of_pets = [rex, benio, henio] 
    print(isinstance(henio, sonia)) 
    print(rex+henio) 

def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()# dla różnych typów (Cat, Dog) klas wywołujemy to samo polecenie jedną linijką - to właśnie przejaw polimorfizmu
   
        if isinstance(pet, sonia): # te które są charakterystyczne dla danego typu obiektu, musimy ująć w warunek, bo na niewłaściwym typie wywaliłoby błąd
            pet.gimmePaw()
            
# brakuje nadpisania odejmowania
#1,25pkt
      
