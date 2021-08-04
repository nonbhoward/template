from configure.settings import config
from tool.socket_management import SocketHandler
import logging.config
logging.config.dictConfig(config['logger'])
log = logging.getLogger(__name__)
if config.get('socket', None) and config['socket'].get('mode', None):
    sh = SocketHandler(config['socket'])
    if not sh.client and not sh.server:
        log.error(f'failed to instantiate socket')
log.info(f'initialization complete')
