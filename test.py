from model import db_module
from model import sql_module

func = sql_module.sql_func()

print(func.get_community_name(0))
