# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class coffee:
    def __int__(self, name, volume, ice, sugar):
        """
        Создание и подготовка к работе объекта "coffee"
        :param name: Название напитка
        :param volume: Объем
        :param ice: Классический кофе или ice
        :param sugar: Количество порций сахара
        Пример:
        Latte_medium = coffee("Latte", 320, "Classic", 0) #инициация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name
        if not isinstance(volume, int):
            raise TypeError("Объем должен быть типа int")
        self.volume = volume
        if not isinstance(ice, str)
            raise TypeError("Параметр iсe должен быть типа str")
        self.ice = ice
        if not isinstance(sugar, int)
            raise TypeError("Параметр sugar должен быть типа int")
        if not volume > 0
            raise TypeError("Объем должен быть больше нуля")
        if not sugar >= 0
            raise TypeError("Количество порций сахара должно быть равным нулю или больше")

        def ingredients(self)
            ...
            """
            Функция, которая выдает необходимые ингредиенты
            Пример:
            >>> Latte_medium = coffee(Latte, 320, Classic, 0)
            :return: Список ингредиентов
            >>> Latte_medium.ingredient()
            """
        def caffein(self)
            ...
            """
            Функция, рассчитывающая количество кофеина в напитке
            :return: Количество мг кофеина
            >>> Latte_medium.caffeine()
            """
class player:
    def __int__(self, name, nick_name, email):
        """
        Создание и подготовка к работе объекта "player"
        :param name: ФИО игрока
        :param nick_name: Никнейм игрока
        :param email: адрес электронной почты
        Пример:
        goncharov_ia = player("Гончаров Иван Алексеевич", "novelist_111","goncharov@mail.ru") #инициация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("ФИО должно быть типа str")
        self.name = name
        if not isinstance(nick_name, str):
            raise TypeError("Никнейм должно быть типа str")
        self.nick_name = nick_name
        if not isinstance(email, str):
            raise TypeError("Адрес эл. почты должен быть типа str")
        self.email = email
    def online(self):
        ...
        """
        Функция возвращает статус игрока
        :return: Статус игрока
        Пример:
        >>> goncharov_ia = player("Гончаров Иван Алексеевич", "novelist_111","goncharov@mail.ru")
        >>> goncharov_ia.online()
        """
    def rang(self):
        ...
        """
        Функция возвращает ранг игрока
        :return: Ранг игрока
        Пример:
        >>> goncharov_ia = player("Гончаров Иван Алексеевич", "novelist_111","goncharov@mail.ru")
        >>> goncharov_ia.rang()
        """

class table_game:
    def __init__(self, game_name, player_volume):
        """
        Создание и подготовка к работе объекта "game"
        :param game_name: Название игры
        :param player_volume: Количество игроков
        Пример:
        imaginarium = table_game("Имаджинариум", "5") #инициация экземпляра класса
        """
        if not isinstance(game_name, str):
            raise TypeError("Название должно быть типа str")
        self.game_name = name
        if not isinstance(player_volume, int):
            raise TypeError("Количество игроков должно быть типа int")
        self.player_volume = player_volume
        if not player_volume > 0
            raise TypeError("Количество игроков должно быть больше нуля")
    def rules(self):
        ...
        """
        Функция возвращает правила игры
        :return: Список правил
        Пример:
        >>> imaginarium = table_game("Имаджинариум", "5")
        >>> imaginarium.rules()
        """
    def time(self):
        ...
        """
        Функция возвращает время, необходимое для игры
        :return: Предполагаемое время
        Пример:
        >>> imaginarium = table_game("Имаджинариум", "5")
        >>> imaginarium.time()
        """

def main()
    doctest.testmod()
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    main()
    pass
