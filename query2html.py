import sqlite3
import sys

if __name__ == '__main__':
    db_path = sys.argv[1] if len(sys.argv) == 2 else 'db.sqlite'
    db = sqlite3.connect(db_path)
    query = sys.stdin.read()
    print('<html><body><table border=3>')
    for cell in db.execute(query):
        print(f'<tr><td>{cell}</td></tr>')
    print('</table></body></html>')

