import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://admin:12345@localhost:5432/admin')
connection = engine.connect()
sel = connection.execute("""SELECT name, years FROM Albums
WHERE years = 2018;
""").fetchall()
print(sel)
sel2 = connection.execute("""SELECT name, years FROM Collection
WHERE years BETWEEN 2018 AND 2020;
""").fetchall()
print(sel2)
sel3 = connection.execute("""SELECT name FROM Track
WHERE duration >= 210;
""").fetchall()
print(sel3)
sel4 = connection.execute("""SELECT name FROM Track
WHERE name LIKE ('%%My %%');
""").fetchall()
print(sel4)
sel5 = connection.execute("""SELECT name FROM Track
ORDER BY duration DESC
LIMIT 1;
""").fetchall()
print(sel5)
sel6 = connection.execute("""SELECT singer FROM Singer
""").fetchall()


sel7 = connection.execute("""SELECT name, duration FROM tracks WHERE 
    duration = (SELECT MAX(duration) FROM tracks);
""").fetchall()

sel8 = connection.execute("""SELECT singer FROM Singer
WHERE singer NOT LIKE ('%% %%');
""").fetchall()


new=[]
new.append(sel6)
new_sel6 =[]
for elem_sel6 in new:
    for elem in elem_sel6:
        for sum_one in elem:
            new_sel6.append(sum_one)

i=0
for element in new_sel6:
    elem = (len(new_sel6[i].split()))
    i = i + 1
    if elem == 2:
        print(element)

with open("final_file.txt", "a") as f:
    print(sel, file=f)
    print(sel2, file=f)
    print(sel3, file=f)
    print(sel4, file=f)
    print(sel5, file=f)
    print(element, file=f)
