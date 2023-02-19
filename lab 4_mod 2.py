class Painting:
    def __init__(self, picture: str, author: str, address: str):
        """
        Класс содержит базовую информацию о картине.
        :param picture: Описание изображенного, информация об авторе.
        :param author: Автор (художник или фотограф).
        :param address: Адрес выставки.
        """
        self.picture = picture
        self.author = author
        self.address = address


        if not isinstance(picture, str):
            raise TypeError("Изображение должно быть типа str")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть типа str")
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть типа str")


    def __str__(self):
        return f"{self.__class__.__name__} Картина {self.picture}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(picture={self.picture!r}, author={self.author!r}," \
               f" address={self.address!r})"

    @property
    def picture(self) -> str:
        """
        Возвращает состояние атрибута picture
        :return: изображение на картине.
        """
        return self.picture

    @picture.setter
    def picture(self, value):
        """
        Изменяет состояние атрибута picture
        :param value: новое значение атрибута picture
        """
        self.picture = value

    @property
    def author(self) -> str:
        """
        Возвращает состояние атрибута author
        :return: автора открытки.
        """
        return self.author

    @author.setter
    def author(self, value):
        """
        Изменяет состояние атрибута author
        :param value: новое значение атрибута author
        """
        self.author = value

    @property
    def address(self) -> str:
        """
        Возвращает состояние атрибута address
        :return: адрес выставки.
        """
        return self.address

    @address.setter
    def address(self, value):
        """
        Изменяет состояние атрибута address
        :param value: новое значение атрибута address
        """
        self.address = value


    def change_address(self, adr: str):
        """
        Функция меняет адрес выставки.
        :param adr: Новый адрес выставки.
        """
        if not isinstance(adr, str):
            raise TypeError("Адрес на открытке должен быть типа str")
        self.address = adr



class ArchitecturePaint(Painting):
    def __init__(self, picture: str, author: str, archit_address: str, address: str):
        """
        Этот класс содержит информацию об изображенном о
        :param picture:
        :param author:
        :param archit_address: название изображенного здания и его адрес.
        :param address:
        """
        super(ArchitecturePaint, self).__init__(picture=picture, author=author, address=address)
        self.archit_address = archit_address

        if not isinstance(archit_address, str):
            raise TypeError("Адрес и название изображенного здания должны быть типа str")

    def __str__(self):
        return f"{self.__class__.__name__} Картина {self.picture}. Автор {self.author}. Адрес и название здания {self.archit_address}."

    def __repr__(self):
        return f"{self.__class__.__name__}(picture={self.picture!r}, author={self.author!r}," \
               f" address={self.address!r}, archit_address={self.archit_address})"

    @property
    def archit_address(self) -> str:
        """
        Возвращает состояние атрибута archit_address
        :return: Адрес и название здания
        """
        return self.archit_address

    @archit_address.setter
    def archit_address(self, value):
        """
        Изменяет состояние атрибута archit_address
        :param value: новое значение атрибута archit_address
        """
        self._archit_address = value

    def change_archit_address(self, adr: str):
        """
        Функция меняет описание изображенного здания и его адресс.
        :param adr: Новое описание.
        :return:
        """
        if not isinstance(adr, str):
            raise TypeError("Адрес и название здания должены быть типа str")


