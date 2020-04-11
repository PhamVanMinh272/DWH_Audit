# Direction:
# import your db variable then set db = <your db variable>
from db_connection.mysql_ssh import db_remote
DATABASE = db_remote


# Direction:
# Set your information to LOCAL or SSH (do not change 'type')
# Set DATABASE = LOCAL or DATABASE = SSH

# LOCAL = {
#     'type': 'local',
#     'name': 'database_name',
#     'username': 'username',
#     'password': 'password',
#     'port': 3306,
# }

# SSH = {
#     'type': 'ssh',
#     'ssh_ip': '172.31.0.55',
#     'ssh_port': 22,
#     'ssh_username': 'big',
#     'ssh_password': 'big',
#     'remote_bind_ip': 'localhost',
#     'remote_bind_port': 3306,
#     'local_bind_ip': 'localhost',
#     'local_bind_port': 3366,
# }
#
# DATABASE = SSH