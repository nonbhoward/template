from configure.settings import app_config
import logging.config

logging.config.dictConfig(app_config['logger'])
log = logging.getLogger()  # root

if app_config.get('socket', None) and app_config['socket'].get('mode', None) != 'disabled':
    from tool.socket_management import SocketHandler

log.info(f'initialization complete')
