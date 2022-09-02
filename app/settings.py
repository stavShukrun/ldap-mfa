from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError

# ldap server hostname and port
ldsp_server = "ldap://openldap:1389"

# dn
root_dn = "dc=example,dc=org"

# ldap user and password
ldap_user_name = 'admin'
ldap_password = 'admin'

# user
user = f'cn={ldap_user_name},{root_dn}'

server = Server(ldsp_server, get_info=ALL)

connection = Connection(server,
                        user=user,
                        password=ldap_password,
                        auto_bind=False)

# for logs
print(f" *** Response from the ldap bind is \n{connection}" )