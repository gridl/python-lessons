class Dog():
    name=""
    # Конструктор
    # Вызывается на момент создания объекта этого типа
    def __init__ (self, newName):
        self.name = newName

# Создаем собаку
myDog = Dog ("Spot")
# Вывести имя собаки, убедиться, что оно было установлено 
# (так обычно не делают!)

print (myDog.name)
# Эта строка выдаст ошибку, потому что
# конструктору не было передано имя
herDog = Dog()
