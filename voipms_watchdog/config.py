import os

servers = [
	('toronto.voip.ms', 5060),
	('toronto2.voip.ms', 5060),
	('toronto3.voip.ms', 5060),
	('toronto4.voip.ms', 5060),
	('toronto5.voip.ms', 5060),
	('toronto6.voip.ms', 5060),
	('toronto7.voip.ms', 5060),
	('toronto8.voip.ms', 5060),
	('toronto9.voip.ms', 5060),
	('toronto10.voip.ms', 5060)
]

database_uri = os.environ.get("DATABASE_URI","sqlite:///data.db")