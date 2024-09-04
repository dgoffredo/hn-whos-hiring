create table JobPost(
  hn_comment_id integer primary key not null

  -- These two are a flattened foreign entity.
, hn_parent_id integer not null
, month_iso text not null -- derived

, when_unix integer not null
, heading text -- derived
, markup text
, ai_mentions integer not null -- derived
, remote_mentions integer not null -- derived
, onsite_mentions integer not null -- derived
, hybrid_mentions integer not null -- derived
, ny_mentions integer not null -- derived
, fulltime_mentions integer not null -- derived
);

create index IndexJobPostMonthIso on JobPost(month_iso);
create index IndexJobPostWhenUnix on JobPost(when_unix);
create index IndexJobPostAIMentions on JobPost(ai_mentions);
create index IndexJobPostRemoteMentions on JobPost(remote_mentions);
create index IndexJobPostOnsiteMentions on JobPost(onsite_mentions);
create index IndexJobPostHybridMentions on JobPost(hybrid_mentions);
create index IndexJobPostNYMentions on JobPost(ny_mentions);
create index IndexJobPostFulltime on JobPost(fulltime_mentions);
