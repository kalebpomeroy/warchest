from flask import jsonify
from warchest import app
from werkzeug.exceptions import HTTPException

# This is called a decorator. It uses a bit of advanced magic to make this
# method do more than what it appears. In this case, it sets the method below
# to be the errorhandler of the entire application. Specifically, this means
# that instead of the normal error page we might see on a website, we'll get
# a json version of the error. This will be very helpful for us using the API.
@app.errorhandler(HTTPException)
# The handle_exception method is passed an exception, shortcut to be e. That
# is added by the decorator above. You can see all the functionality of the
# exceptions in the documentation below.
# https://werkzeug.palletsprojects.com/en/2.1.x/exceptions/
def handle_exception(e):
    # We're interested in only two parts of the exception. The status code (such
    # as 404 or 500) and the message from the application.
    return jsonify({"message": e.description}), e.code
