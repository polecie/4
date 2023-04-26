from functools import lru_cache
from pydantic import BaseSettings, Field, ValidationError

# base_dir = Path(__file__).resolve().parent.parent.parent

__all__ = ("settings",)


class BotSettings(BaseSettings):
    token: str = Field(..., env="BOT_TOKEN")
    # TODO: кейса когда администраторов несколько
    admin_id: int

    class Config:
        env_file_encoding = 'utf-8'
        env_file = ".env", ".env.dev", ".env.prod"


class Settings(BaseSettings):
    bot: BotSettings


@lru_cache()
def get_settings() -> Settings:
    try:
        return Settings(
            bot=BotSettings()
        )
    except ValidationError:
        print("No .env was found")


settings = get_settings()
# print(settings)
