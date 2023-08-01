CREATE TABLE organization (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE label (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER NOT NULL REFERENCES organization(id),
  email TEXT NOT NULL, 
  password TEXT NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

CREATE TABLE project (
  id SERIAL PRIMARY KEY,
  organization_id INTEGER NOT NULL REFERENCES organization(id),
  parent_project_id INTEGER REFERENCES project(id), -- self-referential relationship for hierarchy
  name TEXT NOT NULL,
  start_date DATE,
  end_date DATE
);

CREATE TABLE customer_project (
  customer_id INTEGER NOT NULL REFERENCES customer(id),
  project_id INTEGER NOT NULL REFERENCES project(id),
  PRIMARY KEY (customer_id, project_id)  
);

CREATE TABLE customer_label (
  customer_id INTEGER NOT NULL REFERENCES customer(id),
  label_id INTEGER NOT NULL REFERENCES label(id),
  PRIMARY KEY (customer_id, label_id)
);


CREATE TABLE project_label (
  project_id INTEGER NOT NULL REFERENCES project(id),
  label_id INTEGER NOT NULL REFERENCES label(id),
  PRIMARY KEY (project_id, label_id)
);


CREATE TABLE customer_data (
  customer_id INTEGER NOT NULL REFERENCES customer(id),
  key TEXT NOT NULL,
  value TEXT,
  PRIMARY KEY (customer_id, key)
);