import uvicorn
from core.settings import config


def run_api(reload: bool = True):
    app = 'core.main:app'
    app_config = config.app
    uvicorn.run(
        app=app,
        host=app_config.HOST,
        port=app_config.INTERNAL_PORT,
        reload=reload,
    )


def main():
    run_api()


if __name__ == '__main__':
    main()
