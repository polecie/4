import typing
from functools import wraps


def get_current_state(func: typing.Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        state = kwargs.get("state")
        print(state)
        if state:
            current_state = await state.get_state()
            if current_state is not None:
                print(f"Current state: {current_state}, {func.__name__}")
                data = await state.get_data()
                print(data)
        res = await func(*args, **kwargs)
        if state:
            current_state = await state.get_state()
            data = await state.get_data()
            print(data)
            print(f"New current state: {current_state}, {func.__name__}")
        return res
    return wrapper
