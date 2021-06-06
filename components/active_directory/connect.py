from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPBindError


class Connect:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    def connect_server(self):
        try:
            server = Server(self.server, use_ssl=True, get_info=ALL)
            conn = Connection(server, user=self.username, password=self.password)
            conn.bind()
            return conn
        except LDAPBindError as err:
            print(err)
