from configure.settings import app_config
import logging.config

logging.config.dictConfig(app_config['logger'])
log = logging.getLogger()  # root

if app_config.get('socket', None) and app_config['socket'].get('mode', None) != 'disabled':
    from tool.socket_management import SocketHandler
    sh = SocketHandler(app_config['socket'])
    if not app_config['socket']['server'].get('instance', None) or \
            not app_config['socket']['client'].get('instance', None):
        log.error(f'failed to instantiate socket')

log.info(f'initialization complete')
