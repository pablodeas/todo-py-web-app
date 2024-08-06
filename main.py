import sqlite3
from pyscript import document
from datetime import datetime


#con = sqlite3.connect("./tudu.db")
#cur = con.cursor()
#
#now = datetime.now()
#now_f = now.strftime("%H:%M:%S")
#
#for row in cur.execute("SELECT sqlite_version();"):
#    print(f"> SQLite3 Version:")
#    print(f"> {row[0]}")
#    print(f"> Time:")
#    print(f"> {now_f}")

def newText(inserted):
    now = datetime.now().strftime('%d/%m')

    inserted = document.getElementById('newNote').value
    newInsert = document.createElement('p')

    newInsert.innerText = now + " - " + inserted

    document.getElementById('cont').appendChild(newInsert)
    document.getElementById('newNote').value = ''
    print(newInsert)

