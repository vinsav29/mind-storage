with result as (select distinct on (user_id, problem_id, success) * from submissions s), tasks
as (select
      s.user_id,
      count(distinct p.contest_id) as c1
      from result s
      join problems p on p.id = s.problem_id
      where s.success = True
      group by s.user_id
      having count(p.id) > 0
  ), submit
as (
      select u.id, count(distinct p.contest_id) as c2 from result s
      join problems p on p.id=s.problem_id
      right join users u on u.id=s.user_id
      group by u.id
  ), groupped
as (
      select
      distinct on (u.id)
      u.id,
      u.name,
      coalesce(t.c1, 0) as solved_at_least_one_contest_count
      from tasks t
      right join users u on t.user_id=u.id
  ) select g.*, s.c2 as take_part_contest_count from groupped g right join submit s on s.id=g.id order by 3 desc, 4 desc, 1 asc;