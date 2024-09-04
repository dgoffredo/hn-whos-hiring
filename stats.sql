select
  month_iso as "month"
, count(*) as "jobs"
, round(100.0*sum(ai_mentions > 0)/count(*), 1) as "ai%"
, round(100.0*sum(remote_mentions > 0)/count(*), 1) as "remote%"
, round(100.0*sum(onsite_mentions > 0)/count(*), 1) as "onsite%"
, round(100.0*sum(hybrid_mentions > 0)/count(*), 1) as "hybrid%"
, round(100.0*sum(ny_mentions > 0)/count(*), 1) as "ny%"
, round(100.0*sum(fulltime_mentions > 0)/count(*), 1) as "fulltime%"
from JobPost
group by month_iso
order by month_iso desc;
