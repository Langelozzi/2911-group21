# Web app

'''File containing endpoints for our Course Rating System application'''

# Imports
from flask import Flask, render_template, request, jsonify
from models.review import Review
from models.user import User
from models.review_collection import ReviewCollection

# Creating the app object from flask
app = Flask(__name__)

#Create a flask endpoint that renders the html homepage
@app.route("/", methods=["GET"])
def homepage():
    collection = ReviewCollection()
    reviews = collection.reviews
    #Render the homepage html all the reviews in divs as plain text
    return render_template("home.html", reviews=reviews), 200

#Return all the reviews as JSON
@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    # Instantiate a review collection object
    collection = ReviewCollection()
    #Get all reviews
    reviews = collection.get_reviews_as_dicts()
    #Convert to JSON
    return jsonify(reviews), 200

# starting app in debug mode if ran
# debug mode auto restarts the server after every change made to the code
if __name__ == "__main__":
    app.run(debug=True)
