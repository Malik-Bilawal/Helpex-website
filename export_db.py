import sqlite3

conn = sqlite3.connect('db.sqlite3')
f = open('database_dump.sql', 'w', encoding='utf-8')
for line in conn.iterdump():
    f.write(line + '\n')
f.close()
conn.close()
print("Exported successfully!")