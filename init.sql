CREATE TABLE organization (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE label (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE user (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER NOT NULL REFERENCES organization(id),
  email TEXT NOT NULL, 
  password TEXT NOT NULL,
  first_name TEXT,
  last_name TEXT,
);

CREATE TABLE project (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER NOT NULL REFERENCES organization(id),
  parent_project_id INTEGER REFERENCES project(id), -- self-referential relationship for hierarchy
  name TEXT NOT NULL,
  start_date DATE,
  end_date DATE
);

CREATE TABLE user_project (
  user_id INTEGER NOT NULL REFERENCES user(id),
  project_id INTEGER NOT NULL REFERENCES project(id),
  PRIMARY KEY (user_id, project_id)  
);

CREATE TABLE user_label (
  user_id INTEGER NOT NULL REFERENCES user(id),
  label_id INTEGER NOT NULL REFERENCES label(id),
  PRIMARY KEY (user_id, label_id)
);

CREATE TABLE user_data (
  user_id INTEGER NOT NULL REFERENCES user(id),
  key TEXT NOT NULL,
  value TEXT,
  PRIMARY KEY (user_id, key)
);