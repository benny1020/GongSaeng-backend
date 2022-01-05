<<<<<<< refs/remotes/origin/main
import db_module
import sql_module
=======
<<<<<<< Updated upstream
import model.db_module
import model.sql_module
=======
from model import sql_module
from model import db_module
>>>>>>> Stashed changes
>>>>>>> complete

func = sql_module.sql_func()

<<<<<<< refs/remotes/origin/main
print(func.get_community_index())
=======

user_pass ="12345"
user_id = "ygm1020"
sql = """ update bd_member set m_pass = \'%s\' where m_id = \'%s\'
"""%(user_pass,user_id)

db_class.execute(sql)

print(rows)
>>>>>>> complete
