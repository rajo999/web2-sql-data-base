from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")
db.execute("DROP TABLE;")

db.execute("CREATE TABLE User(id integer primary key autoincrement, name text, age integer);")
db.print_tables(verbose=True) #ta verbose v oklepaju je, da izpiše datile tabele

#db.execute("INSERT INTO User(name, age) VALUES ('rajo', 29);")

result = db.execute("SELECT * FROM User;")
print(result)
db.pretty_print("SELECT*FROM User;")

db.execute("""
            UPDATE User 
            SET age=22 
            WHERE id=1;
            """)

db.execute("DELETE FROM User WHERE id >2;")
result = db.execute("SELECT * FROM User;")
db.pretty_print("SELECT*FROM User;")