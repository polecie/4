from aiogram.fsm.state import State, StatesGroup


class ConnectionEForm(StatesGroup):
    provider = State()
    connection_type = State()
    post = State()
    check_post = State()
    password = State()
    check_password = State()
    connect_to_server = State()


class ShowConnectedItems(StatesGroup):
    show_choice = State()
    content = State()
    choose_item = State()  # выбрать элемент для отвязки
