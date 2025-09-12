from flask import Blueprint,jsonify,request
from app.models import Student
from app.db import db
import re


#create student bluprint
student_bp=Blueprint("student",__name__)


@student_bp.route("/",methods=["GET"])
def single_student():
    print("Single student")
    return "Single student"

#adding a student to our db
#routes and controller logic
@student_bp.route("/add/json",methods=["POST"])
def add_student_json():
    print("Add user was hit")
    data=request.get_json() 

    name=data.get("name")
    email=data.get("email")

    if not name:
        return jsonify({"error":"Name is required"}),400
    
    if not email:
        return jsonify({"error":"Email is required"}),400
    


    #dan@gmail.com
    #
    
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"



    if not re.match(email_regex,email):
        return jsonify({"error":"Invalid email address"})
    
    #Existing student
    exists=Student.query.filter_by(email=email).first()

    if exists:
        return jsonify({"error":"Email in use"}),400
    
    new_student=Student(name=name,email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "message":"Student added",
        "student":{
            "id":new_student.id,
            "name":new_student.name,
            "email":new_student.email,
            "created_at":new_student.created_at
        }
    }),201


@student_bp.route("/add/form",methods=["POST"])
def add_user_form():
    print("Add user was hit")
    return "Adding a student",200

@student_bp.route("/edit",methods=["PUT"])
def edit_student():
    print("Add user was hit")
    return "Edit a student"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print("List Students")
    return "List All students"
