-- Create a table
CREATE TABLE project (
  id SERIAL PRIMARY KEY,
  title VARCHAR(30),
  image_path VARCHAR(50),
  summary VARCHAR(1200),
  tags TEXT[]
);

-- Insert some initial data
INSERT INTO project (title, image_path, summary, tags)
    VALUES('bogus project name', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}');
