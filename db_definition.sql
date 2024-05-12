CREATE DATABASE IF NOT EXISTS transporter;

CREATE TABLE IF NOT EXISTS cities (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS locations (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(100) NOT NULL,
	city_id INT NOT NULL,
	FOREIGN KEY(city_id) REFERENCES cities(id)
);

CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY NOT NULL,
	created_at datetime NOT NULL,
	updated_at datetime NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(100) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	phone VARCHAR(100),
	birthday DATE,
	img_id INT,
	FOREIGN KEY(img_id) REFERENCES images(id)
);

CREATE TABLE IF NOT EXISTS ratings (
	id INTEGER PRIMARY KEY NOT NULL,
	rated_driver_id INTEGER NOT NULL,
	rater_customer_id INTEGER NOT NULL,
	rating decimal(2, 1),
	comment VARCHAR(1000),
	FOREIGN KEY(rated_driver_id) REFERENCES drivers(id),
	FOREIGN KEY(rater_customer_id) REFERENCES customer(id)
);

CREATE TABLE IF NOT EXISTS customers (
	id INTEGER PRIMARY KEY NOT NULL,
	user_id INTEGER NOT NULL,
	company VARCHAR(100),
	FOREIGN KEY(user_id) REFERENCES users(id),
);
	

CREATE TABLE IF NOT EXISTS vehicles (
	id INTEGER PRIMARY KEY NOT NULL,
	model VARCHAR(100),
	year YEAR,
	capacity INTEGER
)

CREATE TABLE IF NOT EXISTS drivers (
	id INTEGER PRIMARY KEY NOT NULL,
	user_id INT NOT NULL,
	license_num VARCHAR(100),
	vehicle_id INT NOT NULL,
	current_location_id INT,
	status ENUM('enroute', 'inactive', 'available'),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(current_location_id) REFERENCES locations(id),
	FOREIGN KEY(vehicle_id) REFERENCES vehicles(id),
);

CREATE TABLE IF NOT EXISTS items (
	id INTEGER PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	description VARCHAR(1000),
	weight INTEGER,
	size_x  DECIMAL(4, 2),
	size_y  DECIMAL(4, 2),
	pickup_location_id INTEGER,
	delivery_location_id INTEGER,
	FOREIGN KEY(customer_id) REFERENCES customers(id),
	FOREIGN KEY(pickup_location_id) REFERENCES locations(id),
	FOREIGN KEY(delivery_location_id) REFERENCES locations(id)
)


CREATE TABLE IF NOT EXISTS items (
	id INTEGER PRIMARY KEY NOT NULL,
	/* Still wratting */
