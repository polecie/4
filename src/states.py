from aiogram.fsm.state import State, StatesGroup


class ProcessEConnection(StatesGroup):
    provider = State()
    connection_type = State()
    email = State()
    check_email = State()
    password = State()
    check_password = State()
    connect_to_server = State()


class ConnectionEForm(ProcessEConnection):
    pass


class ProcessEDisconnection(StatesGroup):
    email = State()
    disconnect_confirmation = State()


class DisconnectionEForm(ProcessEDisconnection):
    pass
