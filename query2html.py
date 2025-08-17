import datetime
import sqlite3
import sys

if __name__ == '__main__':
    db = sqlite3.connect('db.sqlite')
    query = sys.stdin.read()
    print('<html><body><table border=3>')
    for when_unix, comment_id, parent_id, markup in db.execute(query):
        # Replace non-ASCII unicode characters with XML entity equivalents.
        markup = markup.encode('ascii', 'xmlcharrefreplace').decode('ascii')
        when_utc = datetime.datetime.utcfromtimestamp(when_unix)
        print(f'<tr><th><a href="https://news.ycombinator.com/item?id={parent_id}#{comment_id}">{when_utc:%Y-%m-%d}</a></td></tr>')
        print(f'<tr><td>{markup}</td></tr>')
    print('</table></body></html>')

