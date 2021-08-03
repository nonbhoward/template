from configure.settings import config
import logging.config
logging.config.dictConfig(config['logger'])
print(f'initialization complete')
