from .model import db_module
from .model import sql_module

db_class=db_module.database()

id = jdc040
sql = """ select exists (select m_id from bd_member where m_id = %s limiit 1) as success
""" %(id)

rows=db_class.executeAll(id)
print(rows)
