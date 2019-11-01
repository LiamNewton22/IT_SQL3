import sqlite3
from guizero import App, Text, TextBox, PushButton, Picture

database = 'world.db' # create variable name for database

conn = sqlite3.connect(database) # connect/open to database

app = App(title="Liam Newton", bg='Purple', width=1920, height=1080)
def Country():
    record = conn.execute('SELECT * FROM Country;')
    for row in record:
        print(row)
def Population():
    record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000 ORDER BY Population;')
    for row in record:
        print(row)
def LifeExpectancy():
        record = conn.execute('SELECT IndepYear, Population, NAME, LifeExpectancy FROM Country WHERE IndepYear > 1900 ORDER BY IndepYear;')

one_Button = PushButton(app, text='Country', command=Country)
Two_Button = PushButton(app, text='population', command=Population )
Three_Button = PushButton(app)
Four_Button = PushButton(app)

app.display()
#record = conn.execute('SELECT * FROM Country;')

record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000 ORDER BY Population;')

#conn.execute('SELECT LifeExpectancy, NAME From Country WHERE LifeExpectancy < 60 ORDER BY LifeExpectancy;')

# record = conn.execute('SELECT IndepYear, Population, NAME, LifeExpectancy FROM Country WHERE IndepYear > 1900 ORDER BY IndepYear;')
#
# for row in record:
#     print(row)
#
# conn.close()
