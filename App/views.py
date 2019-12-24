from flask import Blueprint, request

blue = Blueprint('blue', __name__)

def init_blue(app):
	app.register_blueprint(blue)


@blue.route('/')
def index():
	return "Index"

@blue.route('/sendrequest/', methods=["GET","POST","DELETE","PUT","PATCH"])
def send_request():
	print(request.args)
	print(request.form)
	print(type(request.args))

	return 'send success'