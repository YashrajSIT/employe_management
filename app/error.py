from flask import Blueprint,jsonify ## Import Blueprint and jsonify from Flask
# Create a Blueprint named 'errors' with the current module name (__name__)
errors= Blueprint('errors',__name__)
# Error handlers for specific HTTP error codes
@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error":"Resource not found"}),404
@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({"error":"Bad request"}),400
@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error":"Internal server error"}),500