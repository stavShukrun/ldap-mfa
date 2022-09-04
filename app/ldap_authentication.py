from time import pthread_getcpuclockid
from ldap3 import Server, Connection, ALL

def ldap_authentication(user_name:str, user_pwd:str)->str:
    
    ldap_server = "ldap://openldap:1389"
    user = f'cn={user_name},dc=example,dc=com'
    server = Server(ldap_server, get_info=ALL)

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