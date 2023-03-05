with res as (select distinct on (user_id, problem_id, success) * from submissions s), tasks
as (
    select p.* from res s
    join problems p on p.id = s.problem_id
    where s.success = True
    group by p.id
    having count(s.user_id) >= 2
  ) select * from tasks order by 1