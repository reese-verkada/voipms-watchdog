from . import db

class Log(db.Model):
	log_id = db.Column(db.Integer, primary_key=True)
	module_name = db.Column(db.String(255), nullable=False)
	req_dst_host = db.Column(db.String(255), nullable=True)
	req_dst_port = db.Column(db.Integer, nullable=True)
	req_time = db.Column(db.DateTime, nullable=True)
	resp_src_ip = db.Column(db.String(25), nullable=True)
	resp_src_port = db.Column(db.Integer, nullable=True)
	resp_time = db.Column(db.DateTime, nullable=True)
	resp_message = db.Column(db.Text, nullable=True)
	exception = db.Column(db.Text, nullable=True)
