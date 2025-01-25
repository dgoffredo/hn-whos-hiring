from bs4 import BeautifulSoup
import datetime
import json
import re
import sqlite3
import sys
import urllib.request


def http_get_json(url):
  response = urllib.request.urlopen(url)
  return json.load(response)


def ignore_comment(comment):
  return (
       comment['type'] != 'comment'
    or comment.get('deleted')
    or sum(ch == '|' for ch in comment['text']) < 2)


def num_matches(subject, *patterns):
  pattern = '|'.join(f'(?:\\b{pattern}\\b)' for pattern in patterns)
  return len(re.findall(pattern, subject))


if __name__ == '__main__':
  db = sqlite3.connect('db.sqlite')
  since = '0001-01' if len(sys.argv) < 2 else sys.argv[1]

  user_url = 'https://hacker-news.firebaseio.com/v0/user/whoishiring.json'
  user = http_get_json(user_url)
  post_ids = list(reversed(sorted(user['submitted']))) # probably redundant
  for post_id in post_ids:
    post_url = f'https://hacker-news.firebaseio.com/v0/item/{post_id}.json'
    post = http_get_json(post_url)
    title = post['title']
    if not title.lower().startswith('Ask HN: Who is hiring?'.lower()):
      continue
    print(title)
    post_unix = post['time']
    post_datetime = datetime.datetime.fromtimestamp(post_unix)
    post_month_iso = post_datetime.isoformat()[:len('2024-10')]
    if post_month_iso < since:
      # We've gone back as far as we want.
      break
    print(post_datetime)
    comment_ids = list(sorted(post['kids'])) # probably redundant
    for comment_id in comment_ids:
      comment_url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json'
      comment = http_get_json(comment_url)
      try:
        if ignore_comment(comment):
          continue
        comment_unix = comment['time']
        comment_datetime = datetime.datetime.fromtimestamp(comment_unix)
        comment_markup = comment['text']
        comment_soup = BeautifulSoup(comment_markup, 'lxml')
        comment_heading = comment_soup.select('html body > p')[0].text
        just_text = comment_soup.text
        lower = just_text.lower()
        nohyphen = lower.replace('-', '')
        n_remote = num_matches(lower, 'remote')
        n_onsite = num_matches(nohyphen, 'onsite', 'on site', 'office', 'inoffice', 'inperson', 'in person')
        n_ai = num_matches(lower, 'ai', 'llm', 'machine learning')
        n_ny = num_matches(lower, 'ny', 'new york', 'nyc')
        n_fulltime = num_matches(nohyphen, 'fulltime', 'full time')
        n_hybrid = num_matches(lower, 'hybrid')
        print(f'  {comment_heading}')
        with db:
          db.execute("""insert or ignore into JobPost(
            hn_comment_id
          , hn_parent_id
          , month_iso
          , when_unix
          , heading
          , markup
          , ai_mentions
          , remote_mentions
          , onsite_mentions
          , hybrid_mentions
          , ny_mentions
          , fulltime_mentions)
          values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
          """, (
            comment_id
          , post_id
          , post_month_iso
          , comment_unix
          , comment_heading
          , comment_markup
          , n_ai
          , n_remote
          , n_onsite
          , n_hybrid
          , n_ny
          , n_fulltime
          ))
      except Exception as error:
        print(error, file=sys.stderr)
        print(comment, file=sys.stderr)

