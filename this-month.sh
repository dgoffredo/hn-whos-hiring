#!/bin/sh

this_month=$(date --iso | head -c 7)

python query2html.py "$@" <<END_QUERY
select markup
from JobPost
where ai_mentions = 0
  and fulltime_mentions > 0
  and ny_mentions > 0
  and month_iso = '$this_month'
order by hn_comment_id;
END_QUERY

