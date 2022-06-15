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
        'http://datasource_1:8000/get_data',
        'http://datasource_2:8000/get_data',
        'http://datasource_3:8000/get_data',
        }

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'DATA_'

class Config:
    app = AppConfig()
    data = DataConfig()

config = Config()
