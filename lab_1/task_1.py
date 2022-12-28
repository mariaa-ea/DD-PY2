from random import choice

import doctest


class Kettle:
    """
    Создает экземпляр чайника с характеристиками:
    имя, материал, объём, номинальная мощность, напряжение.
    Формирует их с помощью метода init_list() в список.
    Хотите узнать ваш настрой сегодня? Воспользуйтесь методом get_who_a_u_today()!

    Примеры использования:
    Как сформировать объект?
    >>> kettle = Kettle("Philips", "wood", 1.8, 1600)

    Как посмотреть атрибуты чайника?
    >>> kettle.voltage
    220
    >>> kettle.name
    'Philips'

    Как сформировать/сформируются данные чайника в виде списка?
    >>> kettle.init_list()
    ['Philips', 'wood', 1.8, 1600, 220]

    Хотите узнать, кто вы сегодня? :)
    >>> kettle.get_who_a_u_today("Nick")
    К сожалению, сегодня вы, Nick, являетесь чайником. Наберитесь терпения. Завтра повезет больше! (наверное)

    or

    Ура! Сегодня вы, Nick, не чайник! Ожидается продуктивный день!

    """
    def __init__(self, name: str, material: str, volume: int | float, rated_power: int) -> None:
        """
        Создает атрибуты объекта (чайника):

        :param name: название/модель
        :param material: материал
        :param volume: объем (в литрах)
        :param rated_power: номинальная мощность (Вт)

        А также атрибут, позволяющий наблюдать все характеристики в виде списка: self.init_list().
        """
        if not isinstance(name, str):
            raise TypeError("Параметр \"name\" должен быть типа \"str\"!")
        if not isinstance(material, str):
            raise TypeError("Параметр \"material\" должен быть типа \"str\"!")
        if not isinstance(volume, int | float) or volume < 0:
            raise ValueError("Параметр \"volume\" должен быть целым или дробным и положительным!")
        if not isinstance(rated_power, int) or rated_power < 0:
            raise ValueError("Параметр \"rated_power\" должен быть целочисленным и положительным!")
        self.name, self.material, self.volume, self.rated_power = name, material, volume, rated_power
        self.voltage = 220
        self.init_list()
        self._your_name = None

    def init_list(self) -> list[str | int | float]:
        main_characteristics = []
        main_characteristics.extend((self.name, self.material,
                                     self.volume, self.rated_power, self.voltage))
        return main_characteristics

    def get_who_a_u_today(self, your_name: str) -> None:
        self._your_name = your_name
        answer = choice(["чайник", "не чайник"])
        if answer == "чайник":
            print(f"К сожалению, сегодня вы, {self._your_name}, являетесь {answer}ом. "
                  f"Наберитесь терпения. Завтра повезет больше! (наверное)")
        else:
            print(f"Ура! Сегодня вы, {self._your_name}, {answer}! "
                  f"Ожидается продуктивный день!")


class Bird:
    """
    Класс описывает птиц.
    При инициализации задаются параметры: вид, порода, летает или нет.
    Класс имеет дополнительные методы по установке длины полета и выводе
    установленного значения (set/get_flight_length()).
    А также методы по установке окраса/цвета птицы и выводе установленного
    значения (set/get_bird_color()).

    Примеры использования:
    Инициализировать экземпляр птицы:
    >>> my_duck = Bird("Duck", "Пекинская", "Да")

    Вызвать интересующие вас атрибуты:
    >>> my_duck.bird, my_duck.breed
    ('Duck', 'Пекинская')

    Если ваша птица летает, то можете установить длину её полёта:
    >>> my_duck.set_flight_length(555)
    555

    Хотите вывести введенное значение?
    >>> my_duck.get_flight_length()
    555

    Для установки окраса птицы воспользуйтесь:
    >>> my_duck.set_bird_color("White")
    'White'

    Для вывода значения на экран:
    >>> my_duck.get_bird_color()
    White

    """
    def __init__(self, bird: str, breed: str, ability_to_fly: str) -> None:
        """
        Инициализирует объект птицы с параметрами:

        :param bird: вид
        :param breed: порода
        :param ability_to_fly: может ли летать?
        """
        if not isinstance(bird, str):
            raise TypeError("Параметр \"bird\" должен быть типа \"str\"!")
        if not isinstance(breed, str):
            raise TypeError("Параметр \"breed\" должен быть типа \"str\"!")
        if not isinstance(ability_to_fly, str):
            raise TypeError("Параметр \"ability_to_fly\" должен быть типа \"str\"!")
        if ability_to_fly == "Да":
            self.ability_to_fly = ability_to_fly
        elif ability_to_fly == "Нет":
            self.ability_to_fly = ability_to_fly
        else:
            raise ValueError("Введено некорректное значение параметра "
                             "\"ability_to_fly\"! Ожидаемый ввод:\"Да\" или \"Нет\".")
        self.bird = bird
        self.breed = breed
        self._init_length = None
        self._color = None

    def set_flight_length(self, length: int | float) -> int | float | None:
        if not isinstance(length, int | float) or length < 0:
            raise TypeError("Параметр \"length\" должен быть типа "
                            "\"int or float\" и положительным!")
        if self.ability_to_fly == "Да":
            self._init_length = length
            return self._init_length
        else:
            print("Птица летать не умеет!")
            return self._init_length

    def get_flight_length(self) -> None:
        print(self._init_length)

    def set_bird_color(self, color: str) -> str:
        if not isinstance(color, str):
            raise TypeError("Параметр \"color\" должен быть типа \"str\"!")
        self._color = color
        return self._color

    def get_bird_color(self) -> None:
        print(self._color)


class Student:
    """
    Класс описывает данные ученика.
    С помощью метода show_init_params() выводит их в виде словаря.
    С помощью метода get_the_level_of_education() определяет текущую ступень обучения.

    Примеры использования:
    Как инициализировать объект ученика?
    >>> student = Student("Victor", 7, 1)

    Хотите узнать, с каким именем объект был создан?
    >>> student
    Student (Victor)

    Если хотите вручную посмотреть атрибуты ученика:
    >>> student.name, student.age
    ('Victor', 7)

    Как будут представлены данные в виде словаря?
    >>> student.init_dictionary()
    {'age': 7, 'grader': 1, 'name': 'Victor'}

    Хотите вывести словарь на экран?
    >>> student.show_init_params()
    {'age': 7, 'grader': 1, 'name': 'Victor'}

    Если хотите узнать ступень обучения ученика:
    >>> student.get_the_level_of_education()
    Начальная школа.

    """
    def __init__(self, name: str, age: int, grader: int) -> None:
        """
        Инициализирует экземпляр класса школьника.
        Формирует основные данные о школьнике:

        :param name: имя
        :param age: возраст
        :param grader: класс

        А также создает словарь с этими данными.
        """
        if not name.isalpha():
            raise TypeError("Введите имя ученика буквами!")
        if not isinstance(age, int) or age < 6:
            raise ValueError("Параметр \"age\" для среднестатистического ученика не может быть меньше 6!")
        if not isinstance(grader, int) or grader < 1 or grader > 11:
            raise ValueError("Введите положительное целое значение для параметра \"grader\" от 1 до 11!")
        self.name, self.age, self.grader = name, age, grader
        self._init_dict = None
        self.init_dictionary()

    def init_dictionary(self) -> dict:
        self._init_dict = [prop for prop in dir(self)
                           if (not prop.startswith("_") and not callable(getattr(self, prop)))]
        self._init_dict = {x: getattr(self, x) for x in self._init_dict}
        return self._init_dict

    def __repr__(self) -> str:
        return F"Student ({self.name})"

    def show_init_params(self) -> None:
        print(self._init_dict)

    def get_the_level_of_education(self) -> None:
        if 1 <= self.grader <= 4:
            print("Начальная школа.")
        elif 5 <= self.grader <= 9:
            print("Средняя школа.")
        elif 10 <= self.grader <= 11:
            print("Старшая школа.")


if __name__ == "__main__":
    doctest.testmod()
