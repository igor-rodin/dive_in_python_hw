from serialize.csv_serializer import CsvSerializer
from serialize.json_serializer import JsonSerializer
from serialize.pickle_serializer import PickleSerializer
from animal import AnimalFactory, Animal, Bird, Cat, Fish


def test_animal():
    print(' Testing animal module '.center(70, '*'))
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


def test_serialize():
    print(' Testing serialize module '.center(70, '*'))
    file = 'file'
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 2}, {'a': 30, 'b': -8}]
    data2 = {'a': 1, 'b': 2, 'c': 8}
    data3 = (1, 3)

    csv_ser = CsvSerializer()
    csv_ser.serialize(data, file)

    json_ser = JsonSerializer()
    json_ser.serialize(data, file, preaty_print=True)

    ser_data = csv_ser.deserialize('file.csv')
    print(f'{ser_data=}')

    json_data = json_ser.deserialize('file.json')
    print(f'{json_data=}')

    pickle_ser = PickleSerializer()
    pickle_ser.serialize(data2, file)
    pickle_str = pickle_ser.serialize(data2, as_bytes=True)
    print(f'{pickle_str=}')
    pickle_data_from_file = pickle_ser.deserialize('file.pickle')
    print(f'{pickle_data_from_file=}')
    pickle_data_from_str = pickle_ser.deserialize(pickle_str, as_bytes=True)
    print(f'{pickle_data_from_str=}')


if __name__ == '__main__':
    test_animal()
    test_serialize()
