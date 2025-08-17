#!/bin/sh

this_month=${1:-$(date --iso | head -c 7)}

python query2html.py <<END_QUERY
select when_unix, hn_comment_id, hn_parent_id, markup
from JobPost
where ai_mentions = 0
  and fulltime_mentions > 0
  and ny_mentions > 0
  and month_iso >= '$this_month'
order by when_unix desc;
END_QUERY

