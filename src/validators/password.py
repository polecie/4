from abc import ABC, abstractmethod


class BaseCheckPassword(ABC):
    # TODO: поменять название класса
    """Абстрактный класс для валидации пароля."""

    @staticmethod
    @abstractmethod
    def check_passwords(password1: str, password2: str) -> bool:
        """Абстрактный метод для проверки паролей на совпадение.

        :param password1: Пароль 1.
        :param password2: Пароль 2.
        :return: True - если пароли совпадают, False - если не совпадают.
        """


class CheckPasswords(BaseCheckPassword):
    # TODO: поменять название класса
    """Класс для валидации пароля."""

    @staticmethod
    def check_passwords(password1: str, password2: str) -> bool:
        """Проверка паролей на совпадение.

        :param password1: Пароль 1.
        :param password2: Пароль 2.
        :return: True - если пароли совпадают, False - если не совпадают.
        """
        if password1 == password2:
            return True
        else:
            return False
