import sqlite3
import sys

if __name__ == '__main__':
    db = sqlite3.connect('db.sqlite')
    query = sys.stdin.read()
    print('<html><body><table border=3>')
    for cell, in db.execute(query):
        print(f'<tr><td>{cell}</td></tr>')
    print('</table></body></html>')

