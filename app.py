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

#### for the sorting, we will have another endpoint that can display reviews based on search criteria ####
# @app.route("/sorted", methods=["GET"])
# def show_sorted():
#     """Endpoint that renders an HTML page with reviews sorted by a search

#     Args:
#         search_criteria (str): the content from the search box

#     Returns:
#         html template or JSON : the html file or a message if an error occurs
#     """

#     try:
#         search_option = request.form.get("search_dropdown")
#         search_string = request.form['search_box']
#         coll = ReviewCollection()
        
#         if search_option.lower() == 'course':
#             sorted_reviews = coll.get_review_by_course(search_string)
#         elif search_option.lower() == 'instructor':
#             sorted_reviews = coll.get_review_by_instr(search_string)
        
#         return render_template("home.html", reviews=sorted_reviews), 200
#     except:
#         return jsonify({"Error": "Collection not found."}), 404

#Return all the reviews as JSON
@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    # Instantiate a review collection object
    collection = ReviewCollection()
    #Get all reviews
    reviews = collection.get_reviews_as_dicts()
    #Convert to JSON
    return jsonify(reviews), 200


#Change the list when an instructor is searched in the search bar(in the html)
@app.route("/api/reviews/instructor", methods=["GET"])
def get_reviews_by_instr():
    try:
        instructor = request.args.get("instructor")
        collection = ReviewCollection()
        reviews = collection.get_reviews_by_instr(instructor)
        return jsonify(reviews), 200
    except:
        return jsonify({"Error": "Collection not found."}), 404

# starting app in debug mode if ran
# debug mode auto restarts the server after every change made to the code
if __name__ == "__main__":
    app.run(debug=True)
