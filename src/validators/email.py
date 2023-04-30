import re
from abc import ABC, abstractmethod


class BaseCheckPost(ABC):
    # TODO: поменять название класса
    """Абстрактный класс для валидации пользовательских электронных адресов."""

    @staticmethod
    @abstractmethod
    def check_format(email: str) -> bool:
        """Абстрактный метод. Проверка формата электронного адреса.

        :param email: Электронный адрес, указанный пользователем для привязки.
        :return: True, если формат `user_email` корректный, иначе False.
        """
    @staticmethod
    @abstractmethod
    def check_domain(email: str, domain: str) -> bool:
        """Абстрактный метод. Проверка наличия выбранного пользователем домена,
        записанного в состояние, в электронном адресе почты, указанным
        пользователем для привязки. Например, проверка на наличие домена.

        @gmail.com или @yandex.ru в `user_email`.

        :param email: Электронный адрес, указанный пользователем для привязки.
        :param domain: Домен, записанный в состояние.
        :return: True, если домен присутствует в `email`, иначе False.
        """


class CheckPost(BaseCheckPost):
    # TODO: поменять название класса
    """Класс для валидации пользовательских электронных адресов."""

    # TODO: добавить проверку на количество символов
    # TODO: поменять проверки
    @staticmethod
    def check_format(email: str) -> bool:
        """Проверка формата электронного адреса.

        :param email: Электронный адрес, указанный пользователем для привязки.
        :return: True, если формат `email` корректный, иначе False.
        """
        if email.count("@") == 1:
            regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
            if re.fullmatch(regex, email):
                return True
            else:
                return False
        return False

    @staticmethod
    def check_domain(email: str, domain: str) -> bool:
        """Проверка наличия выбранного пользователем домена, записанного в
        состояние, в электронном адресе почты, указанным пользователем для
        привязки. Например, проверка на наличие домена @gmail.com или.

        @yandex.ru в `user_email`.

        :param email: Электронный адрес, указанный пользователем для привязки.
        :param domain: Домен, записанный в состояние.
        :return: True, если домен присутствует в `email`, иначе False.
        """
        if email.count("@") == 1:
            email_domain = email.split("@")[1]
            domain_in_email = email_domain.split(".")[0]
            if domain == domain_in_email:
                return True
            else:
                return False
        return False
