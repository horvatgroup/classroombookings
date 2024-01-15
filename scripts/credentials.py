import os

db_user = os.getenv("MARIADB_DATABASE", "crbs_user")
db_password =os.getenv("MARIADB_PASSWORD", "6vTccw7zYF")
db_host =os.getenv("crbs-mariadb", "127.0.0.1")
db_port = 3306
db_database = os.getenv("MARIADB_DATABASE", "crbs_db")
