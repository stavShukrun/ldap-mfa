from time import pthread_getcpuclockid
from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


def ldap_authentication(user_name, user_pwd):

    # fetch the username and password
    ldap_user_name = user_name
    ldap_user_pwd = user_pwd

    # ldap server hostname and port
    ldap_server = "ldap://openldap:1389"

    # dn
    root_dn = "dc=example,dc=org"

    # user
    user = f'cn={ldap_user_name},{root_dn}'

    server = Server(ldap_server, get_info=ALL)

    try:
        connection = Connection(server,
                                user=user,
                                password=ldap_user_pwd)
        if not connection.bind():
            l_success_msg = f' ** Failed Authentication: {connection.last_error}'
            return l_success_msg
        else:
            l_success_msg = 'Success'
            return l_success_msg
            
    except Exception as e:
        return e