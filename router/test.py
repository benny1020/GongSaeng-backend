from .model import db_module
from .model import sql_module

db_class=db_module.database()


user_pass ="12345"
user_id = "ygm1020"
sql = """ update bd_member set m_pass = \'%s\' where m_id = \'%s\'
"""%(user_pass,user_id)

db_class.executeAll(id)

print(rows)
