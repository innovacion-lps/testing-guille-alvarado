create table if not exists positions (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users(id) on delete cascade not null,
  title text not null,
  description text,
  country text,
  currency text,
  salary_min integer,
  salary_max integer,
  requirements jsonb default '[]',
  status text default 'active',
  created_at timestamptz default now()
);
alter table positions enable row level security;
create policy "users own positions" on positions
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);