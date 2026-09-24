insert into public.positions (title, department, status, user_id) values
('Frontend Developer','Tech','active','ebf57b5b-e8e4-4a63-8258-b4df2a532c50'),
('Recruiter','HR','paused','ebf57b5b-e8e4-4a63-8258-b4df2a532c50'),
('Diseñador UX','Design','active','ebf57b5b-e8e4-4a63-8258-b4df2a532c50');

select id, title, department, status, user_id from public.positions;