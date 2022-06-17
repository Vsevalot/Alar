from pydantic import BaseSettings


class AppConfig(BaseSettings):
    HTTP_API_NAME: str = "user_service_api"
    HTTP_API_DESCRIPTION = "API to manage users"
    HTTP_API_VERSION: str = "0.1.0"

    HOST: str = '0.0.0.0'
    INTERNAL_PORT: int = 5000

    LOG_LEVEL = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'APP_'


class DataConfig(BaseSettings):
    URLS: set[str] = {
        'http://datasource_1:8000',
        'http://datasource_2:8000',
        'http://datasource_3:8000',
        }
    TIMEOUT: int = 2
    ENDPOINT: str = '/get_data'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'DATA_'


class DBConfig(BaseSettings):
    DSN: str = 'postgresql+asyncpg://postgres:postgres@db:5432/core_db'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'DB_'


class AuthConfig(BaseSettings):
    SERVICE_SECRET: str = 'service_secret'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'AUTH_'


class Config:
    app = AppConfig()
    data = DataConfig()
    db = DBConfig()
    auth = AuthConfig()

config = Config()
