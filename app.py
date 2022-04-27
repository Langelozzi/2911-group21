from flask import Flask, render_template, request, jsonify
from models.review import Review
from models.user import User
from models.review_collection import ReviewCollection



app = Flask(__name__)

#Create a flask app based on the templates in the templates folder
@app.route("/")
def homepage():
    #Render the homepage --a table of students showing name, id
    return render_template("home.html"), 200
    

#Return a JSON with all student info
@app.route("/reviews", methods=["GET"])
def get_reviews():
    #Get all reviews
    reviews = ReviewCollection.get_all()
    #Convert to JSON
    return jsonify(reviews), 200


#Adds a student to the school
#JSON must contain name, student_id, term
@app.route("/review", methods=["POST"])
def create_review():
    data = request.json
    try:
        review = Review(**data)
        ReviewCollection.add(review)
        ReviewCollection.save()
        return "Review added", 201
    except ValueError:
        return "Invalid parameters", 400


#Returns JSON with specified student info
@app.route("/review/<reviewID>", methods=["GET"])
def get_review(reviewID):
    review = ReviewCollection.get_by_id(reviewID)

    if not review:
        return "Review does not exist", 404
    else:
        return jsonify(review.to_dict()), 200


#Updates specified student with info provided
# must contain at least one of: name, student_id, name
@app.route("/review/<reviewID>", methods=["PUT"])
def update_review(reviewID):
    data = request.json
    review = ReviewCollection.get_by_id(reviewID)

    if not review:
        return "Review does not exist", 404
    else:
        try:
            review.update(**data)
            ReviewCollection.save()
            return "Review updated", 200
        except ValueError:
            return "Invalid parameters", 400


#Deletes specified student
@app.route("/review/<reviewID>", methods=["DELETE"])
def delete_review(reviewID):
    review = ReviewCollection.get_by_id(reviewID)

    if not review:
        return "Review does not exist", 404
    else:
        ReviewCollection.delete(review)
        ReviewCollection.save()
        return "Review deleted", 200


#Returns JSON with all student info
@app.route("/users", methods=["GET"])
def get_users():
    #Get all students
    users = UserCollection.get_all()
    #Convert to JSON
    return jsonify(users), 200


#Adds a student to the school
#JSON must contain name, student_id, term
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    try:
        user = User(**data)
        UserCollection.add(user)
        UserCollection.save()
        return "User added", 201
    except ValueError:
        return "Invalid parameters", 400


#Returns JSON with specified student info
@app.route("/user/<userID>", methods=["GET"])
def get_user(userID):
    user = UserCollection.get_by_id(userID)

    if not user:
        return "User does not exist", 404
    else:
        return jsonify(user.to_dict()), 200


#Updates specified student with info provided
# must contain at least one of: name, student_id, name
@app.route("/user/<userID>", methods=["PUT"])
def update_user(userID):
    data = request.json
    user = UserCollection.get_by_id(userID)

    if not user:
        return "User does not exist", 404
    else:
        try:
            user.update(**data)
            UserCollection.save()
            return "User updated", 200
        except ValueError:
            return "Invalid parameters", 400


#Deletes specified student
@app.route("/user/<userID>", methods=["DELETE"])
def delete_user(userID):

    user = UserCollection.get_by_id(userID)

    if not user:
        return "User does not exist", 404
    else:
        UserCollection.delete(user)
        UserCollection.save()
        return "User deleted", 200


if __name__ == "__main__":
    app.run(debug=True)
