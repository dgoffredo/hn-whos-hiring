select
  month_iso as "month"
, count(*) as "jobs"
, cast(round(100.0*sum(ai_mentions > 0)/count(*), 0) as integer) as "ai%"
, cast(round(100.0*sum(remote_mentions > 0)/count(*), 0) as integer) as "remote%"
, cast(round(100.0*sum(onsite_mentions > 0)/count(*), 0) as integer) as "onsite%"
, cast(round(100.0*sum(hybrid_mentions > 0)/count(*), 0) as integer) as "hybrid%"
, cast(round(100.0*sum(ny_mentions > 0)/count(*), 0) as integer) as "ny%"
, cast(round(100.0*sum(fulltime_mentions > 0)/count(*), 0) as integer) as "fulltime%"
from JobPost
group by month_iso
order by month_iso desc;
