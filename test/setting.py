# Direction:
# set source db variable
# set destination db variable
from db_connection.mysql_local import db
from db_connection.mysql_ssh import db_remote

SOURCE_DATABASE = db

DESTINATION_DATABASE = db_remote