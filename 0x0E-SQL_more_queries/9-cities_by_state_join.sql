-- script lists all cities contained in db hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE cities.state_id = states.id
