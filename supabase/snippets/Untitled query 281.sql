alter table positions add column if not exists description text;
alter table positions add column if not exists country text;
alter table positions add column if not exists currency text;
alter table positions add column if not exists salary_min integer;
alter table positions add column if not exists salary_max integer;
alter table positions add column if not exists requirements jsonb default '[]';
alter table positions add column if not exists status text default 'active';
alter table positions add column if not exists user_id uuid references auth.users(id) on delete cascade;