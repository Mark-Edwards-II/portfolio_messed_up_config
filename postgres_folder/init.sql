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
    VALUES('bogus project name', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name2', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name3', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name4', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name5', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name6', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name7', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name8', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name9', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name10', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}'),
    VALUES('bogus project name11', 'bogus', 'sdofkjawoefijwoeIFJAOWEIFJAWOEIFJopweifjoweiFJ', '{"SKDFOSJF","SDLFKJAWOEFJ"}');
