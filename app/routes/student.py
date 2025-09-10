from flask import Blueprint,jsonify, request

# create student blueprint
student_bp = Blueprint("student", __name__)

@student_bp.route("/", methods=["GET"])
def home():
    return "Welcome to the Student Management System"

# routes and controller logic
@student_bp.route("/student/add", methods=["POST"])
def add_student():
    print("add use was hit")
    return "Adding a user"

@student_bp.route("/students", methods=["GET"])
def list_students():
    print("List Students")
    users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
    return jsonify(users) 
    return "List All students"