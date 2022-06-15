from core.settings import config
from core.api import runner


app = runner.create(config=config)
