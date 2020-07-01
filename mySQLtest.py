
def db_connect(db_name: str):
    import platform
    global DBTYPE
    if platform.system() == 'Windows':
        DBTYPE= 'sqlite'
        import sqlite3 as dbengine
        return dbengine.connect("{}.db".format(db_name))
    else:
        DBTYPE = 'mysql'
        import mysql.connector as dbengine
        return dbengine.connect(user='lairning',
                                 password='Pocosi12!',
                                 host='173.249.37.119',
                                 database=db_name)

dbcursor = db_connect('laimktagent').cursor()

if DBTYPE == 'sqlite':
    dbcursor.execute('''SELECT  
                            name
                        FROM 
                            sqlite_master 
                        WHERE 
                            type ='table' AND 
                            name NOT LIKE "sqlite_%"''')
if DBTYPE == 'mysql':
    dbcursor.execute("SHOW TABLES")

tables = dbcursor.fetchall()
print(tables)
