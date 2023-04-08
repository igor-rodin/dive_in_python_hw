'''Animal module'''


class Animal:
    def __init__(self, name: str = 'jon dow'):
        self._name = name

    def who_am_i(self):
        print(f"I'm {self._name}")


class Bird(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.__color = color

    @property
    def color(self):
        return self.__color

    def sing(self):
        print(f"Bird {self._name} is singing")


class Fish(Animal):
    def __init__(self, name: str, is_sea: bool = True):
        super().__init__(name)
        self.__is_sea = is_sea

    @property
    def is_sea(self):
        return self.__is_sea

    def swim(self):
        print(f"Fish {self._name} is swiming")


class Cat(Animal):
    def __init__(self, name: str, breed: str = 'mongrel'):
        super().__init__(name)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed

    def swim(self):
        print(f"Fish {self._name} is swiming")


class AnimalFactory:
    def __init__(self, animal_type: str, *args, **kwargs) -> None:
        self.__animal_type = animal_type
        self.__args = args
        self.__kwargs = kwargs
        pass

    def create(self) -> Animal | Fish | Cat | Bird:
        match self.__animal_type.lower():
            case 'cat':
                return Cat(*self.__args, **self.__kwargs)
            case 'fish':
                return Fish(*self.__args, **self.__kwargs)
            case 'bird':
                return Bird(*self.__args, **self.__kwargs)


if __name__ == '__main__':
    zoo: list[Animal] = []

    cat = AnimalFactory('Cat', 'Chip', 'Майкун').create()
    zoo.append(cat)
    print(f'breed = {cat.breed}')

    fish = AnimalFactory('Fish', 'Catfish', is_sea=False).create()
    zoo.append(fish)
    fish.swim()
    print(f'Is sea fish: {fish.is_sea}')

    bird = AnimalFactory('bird', 'Nightingale', 'red').create()
    zoo.append(bird)
    print(f'Bird color: {bird.color}')
    bird.sing()

    print(' Zoo animals '.center(40, '*'))
    for animal in zoo:
        animal.who_am_i()
