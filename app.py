# Web app

'''File containing endpoints for our Course Rating System application'''

# Imports
from flask import Flask, render_template, request, jsonify
from models.review import Review
from models.user import User
from models.review_collection import ReviewCollection
import string
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# Creating the app object from flask
app = Flask(__name__)

#Create a flask endpoint that renders the html homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    collection = ReviewCollection()
    reviews = collection.reviews
    
    # if a post request is made to this enpoint. This happens when the form gets submitted
    if request.method == "POST":
        # extracting the values of the drop down options and the string in the search box
        search_option = request.form.get("teams")
        search_string = request.form['search']
        
        # line 27 checks if the form submit button has been clicked. sorted = input name, Submit = input value
        if request.form.get('sorted') == 'Submit':
            # determining if the chosen sort option was instructor or course number based on the value of the dropdown option
            if search_option.lower() == 'coursen':
                # sorting the reviews and returning the homepage with the sorted reviews
                sorted_reviews = collection.get_review_by_course(search_string)
                return render_template("home.html", reviews=sorted_reviews), 200
            elif search_option.lower() == 'instructor':
                sorted_reviews = collection.get_review_by_instr(search_string)
                return render_template("home.html", reviews=sorted_reviews), 200

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

def check_password(pwd: str) -> dict:
    """This function check a password for length, upper and lowercase letters and special characters

    Args:
        pwd (str): the password being checked

    Returns:
        list: a list of messages if a condition is not satisfied
    """
    
    checks = {
        "length": "Password must be 8 or more characters in length",
        "lower": "Password must contain at least one lowercase letter",
        "upper": "Password must contain at least one uppercase letter",
        "special": "Password must contain at least one special character"
    }
    
    # checking length is 8 or more
    if len(pwd) > 7:
        checks["length"] = True
    
    # checking that it contains a lowercase letter 
    for char in pwd:
        if char.islower():
            checks["lower"] = True

    # checking that is contains an uppercase letter
    for char in pwd:
        if char.isupper():
            checks["upper"] = True

    # checking that it contains a special character
    if any(char in set(string.punctuation) for char in pwd):
        checks["special"] = True

    # getting all messages that are left over
    messages = [value for value in checks.values() if value != True]

    return messages

# Return the sign up page
@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    # if a post request is made to this enpoint. This happens when the form gets submitted
    if request.method == "POST":
        # extracting the values of the drop down options and the string in the search box
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repeated_pass = request.form['password-repeat']
        msgs = check_password(password)

        if password != repeated_pass:
            # will change these so that they show on the html page instead
            return jsonify({"msg": "passwords do not match"})
        if len(msgs) != 0:
            # will change these so that they show on the html page instead
            return jsonify({"msg": f"{msgs}"})
        
        if request.form.get('submitbtn') == 'Sign up':
            print(name, email, password, repeated_pass)
            hashed_pass = generate_password_hash(password, method='sha256')
            new_user = User(id=str(uuid.uuid4()), full_name=name, email=email, password=hashed_pass)
        else:
            return jsonify({"success": "false"})
            
    
    return render_template("sign_up.html"), 200

# starting app in debug mode if ran
# debug mode auto restarts the server after every change made to the code
if __name__ == "__main__":
    app.run(debug=True)
