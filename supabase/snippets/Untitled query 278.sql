CREATE POLICY "Users can view their own tasks"
ON tasks
FOR SELECT
TO authenticated
USING (user_id = auth.uid());