from pathlib import Path
import logging
import os
import socket
log = logging.getLogger(__name__)


class SocketMode:
    def __init__(self):
        self.CLIENT = 'client'
        self.SERVER = 'server'


SOCKET_MODE = SocketMode()


class SocketHandler:
    def __init__(self, socket_configuration):
        log.info(f'initializing {self.__class__.__name__}')
        # init
        self._configuration = socket_configuration
        self.mode = self.configuration.get('mode', None)
        self._client = None
        self._server = None
        # startup
        if not socket_configuration.get('buffer size'):
            log.error(f'no buffer size specified, class instantiation abort')
            return
        if not socket_configuration.get('separator'):
            log.error(f'no separator specified, class instantiation abort')
            return
        if self.mode == SOCKET_MODE.SERVER:
            self.server = socket_configuration[SOCKET_MODE.SERVER]
            if not self.server:
                log.error(f'error instantiating server')
            return
        if self.mode == SOCKET_MODE.CLIENT:
            self.client = socket_configuration[SOCKET_MODE.CLIENT]
            if not self.client:
                log.error(f'error instantiating client')
            return
        if self.mode == 'disabled':
            log.error(f'fatal, socket handler is disabled')
            exit()  # should never be able to reach this state
        log.error(f'bad socket mode specified')

    def receive(self):
        socket_configuration_ = self.configuration
        self.server.listen(socket_configuration_.get('backlog', 0))
        client_socket, address = self.server.accept()
        log.info(f'{address} is connected')
        received = client_socket.recv(socket_configuration_['buffer size']).decode()
        filename, filesize = received.split(socket_configuration_['separator'])
        filename, filesize = os.path.basename(filename), int(filesize)
        with open(filename, 'wb') as file_to_write:
            while True:
                bytes_read = client_socket.recv(socket_configuration_['buffer size'])
                if not bytes_read:
                    break
                file_to_write.write(bytes_read)
        client_socket.close()
        self.server.close()

    def send(self, filepath: Path):
        socket_configuration = self.configuration
        filesize = os.path.getsize(filepath)
        separator = socket_configuration['separator']
        self.client.send(f'{str(filepath)}{separator}{filesize}'.encode())
        with open(filepath, 'rb') as file_to_read:
            while True:
                bytes_read = file_to_read.read(socket_configuration['buffer size'])
                if not bytes_read:
                    break
                self.client.sendall(bytes_read)
        self.client.close()

    @property
    def configuration(self):
        return self._configuration

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server_configuration):
        if not server_configuration.get('host', None):
            log.error(f'server configuration has no host specified')
        if not server_configuration.get('port', None):
            log.error(f'server configuration has no port specified')
        host = server_configuration['host']
        port = server_configuration['port']
        server = socket.socket()
        try:
            server.bind((host, port))
            self.mode = SOCKET_MODE.SERVER
            log.info(f'socket server bound to host {host}, port {port}')
        except Exception as exc:
            log.error(f'{exc}')
            return
        self._server = server

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client_configuration):
        if not client_configuration.get('host', None):
            log.error(f'client configuration has no host specified')
        if not client_configuration.get('port', None):
            log.error(f'client configuration has no port specified')
        host = client_configuration['host']
        port = client_configuration['port']
        client = socket.socket()
        try:
            client.connect((host, port))
            self.mode = SOCKET_MODE.CLIENT
            log.info(f'socket client connected to host {host}, port {port}')
        except Exception as exc:
            log.error(f'{exc}')
            return
        self._client = client
