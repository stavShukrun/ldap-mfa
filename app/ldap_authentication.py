from time import pthread_getcpuclockid
from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


def ldap_authentication(user_name, user_pwd):
    ldap_server = "ldap://openldap:8080"

    user = f'cn={user_name},dc=example,dc=org'

    server = Server(ldap_server, get_info=ALL)
    print("user:", user,"\nldap_server:", ldap_server,"\nserver:",server)

    try:
        connection = Connection(server,
                                user=user,
                                password=user_pwd)
        if not connection.bind():
            l_success_msg = f' ** Failed Authentication: {connection.last_error}'
            return l_success_msg
        else:
            l_success_msg = 'Success'
            return l_success_msg
            
    except Exception as e:
        return e