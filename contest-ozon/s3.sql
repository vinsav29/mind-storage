with last(id) as (
  select max(id)
  from contests
),
participants(id) as (
  select distinct s.user_id
  from last l
  join contests c on c.id = l.id
  join problems p on p.contest_id = c.id
  join submissions s on s.problem_id = p.id
),
data as (
  select u.id as user_id, u.name as user_name, pc.problem_count, latest.latest_successful_submitted_at
  from participants pu
  join users u on u.id = pu.id
  join lateral (
    select count(distinct s.problem_id) as problem_count
    from last l
    join problems p on p.contest_id = l.id
    join submissions s on s.problem_id = p.id and s.success
    where s.user_id = u.id
  ) as pc on true
  join lateral (
    with solved as (
      select p.id, min(s.submitted_at) as submitted_at
      from last l
      join problems p on p.contest_id = l.id
      join submissions s on s.problem_id = p.id and s.success
      where s.user_id = u.id
      group by p.id
    )
    select max(submitted_at) as latest_successful_submitted_at
    from solved
  ) latest on true
)
select rank() over(order by problem_count desc, latest_successful_submitted_at), *
from data
order by 4 desc, 5, user_id