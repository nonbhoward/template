from configure.settings import app_config
import logging.config

logging.config.dictConfig(app_config['logger'])
log = logging.getLogger(__name__)

if app_config.get('cache', None) and app_config['cache'].get('enabled', False):
    from tool.data_management import CacheDataHandler
if app_config.get('socket', None) and app_config['socket'].get('mode', None) != 'disabled':
    from tool.socket_management import SocketHandler
    sh = SocketHandler(app_config['socket'])
    if not sh.client and not sh.server:
        log.error(f'failed to instantiate socket')

log.info(f'initialization complete')
