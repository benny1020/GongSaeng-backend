from model import db_module
from model import sql_module

db_class=db_module.Database()

ids = "jdc0407"

sql = """select count(*) from bd_member where m_id = \'%s\'
"""%(ids)

rows=db_class.executeAll(sql)
print(len(rows))
