# Create posts Table
CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	content TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
