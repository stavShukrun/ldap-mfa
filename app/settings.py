from ldap3 import Server, Connection, ALL

ldsp_server = "ldap://openldap:1389"

root_dn = "dc=example,dc=com"

ldap_user_name = 'admin'
ldap_password = 'admin'

user = f'cn={ldap_user_name},{root_dn}'

server = Server(ldsp_server, get_info=ALL)

connection = Connection(server,
                        user=user,
                        password=ldap_password,
                        auto_bind=False)

# for logs
print(f" *** Response from the ldap bind is \n{connection}" )