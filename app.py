# Web app

'''File containing endpoints for our Course Rating System application'''

# Imports
from functools import wraps
from pyexpat.errors import messages
from flask import Flask, render_template, request, jsonify, redirect, session
from models.all_users import AllUsers
from models.review import Review
from models.user import User
from models.review_collection import ReviewCollection
import string
import uuid
from werkzeug.security import generate_password_hash
import jwt
import datetime

# Creating the app object from flask
app = Flask(__name__)

# creating a secret key for our authorization and authentication stuff
app.config['SECRET_KEY'] = 'mobiusdesignssecretkey'

# Creates a custom decorator for authorizing with jwt
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        users = AllUsers()
        token = None

        # if the session has a key of token (which happens after you login) then set token to the users token for the session
        if session['token']:
            token = session['token']

        # if there is no token then redirect back to the login page
        if not token:
            return redirect("http://127.0.0.1:5000/login")
        
        # if there is a token the decode it to verify it and then get the user by their public id attached to the token
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], ['HS256'])
            current_user = users.get_user_by_id(data['public_id'])
        except:
            return jsonify({"Error": "Token is invalid"}), 401

        # return the current user as first argument for all functions with this decorator
        return f(current_user, *args, **kwargs)
    
    return decorated

# Function to help with the checking of a valid password for signing up
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

#Create a flask endpoint that renders the html homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    """Endpoint that shows all the reviews and allows for sorting. Anyone can view this page

    Returns:
        html template: the html homepage
    """
    
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
    """API endpoint for getting all the reviews as JSON

    Returns:
        json: list of all reviews as json objects
    """
    
    # Instantiate a review collection object
    collection = ReviewCollection()
    #Get all reviews
    reviews = collection.get_reviews_as_dicts()
    #Convert to JSON
    return jsonify(reviews), 200


# Sign up page
@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    """Endpoint for signing up/creating an account with the CRS

    Returns:
        html template: the signup page html
    """
    
    # if a post request is made to this enpoint. This happens when the form gets submitted
    if request.method == "POST":
        # extracting the values of the sign up form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repeated_pass = request.form['password-repeat']
        
        # checking the password
        msgs = check_password(password)

        if password != repeated_pass:
            # display any error messages that occur
            return render_template("sign_up.html", messages=["Passwords do not match!"])
        if len(msgs) != 0:
            # display any error messages that occur
            return render_template("sign_up.html", messages=msgs)
        
        # if the submit button is pressed then generate a hashed password and create a new user, then save them to the json file
        if request.form.get('submitbtn') == 'Sign up':
            hashed_pass = generate_password_hash(password, method='sha256')
            
            # if the email doesn't end in "@my.bcit.ca" then a valueerror is raised by the user class
            try:
                # gives the new user a unique id using uuid module
                new_user = User(id=str(uuid.uuid4()), full_name=name, email=email, password=hashed_pass)
                new_user.save()
                return render_template("sign_up.html", messages=["Account Successfully Created!", "Please Login"]), 200
            except ValueError:
                return render_template("sign_up.html", messages=["INVALID EMAIL: Email must be a myBCIT email. (E.g. jsmith@my.bcit.ca)"])
    
    # if it is a get request then just return the html page
    return render_template("sign_up.html"), 200


# Route for logging in
@app.route("/login", methods=["GET", "POST"])
def login():
    """Endpoint for logging into your account

    Returns:
        redirect: once logged in, you are redirected to the user homepage
    """
    
    users = AllUsers()
    
    # if a post request is made to this enpoint. This happens when the form gets submitted
    if request.method == "POST":
        # extracting the values of the form
        email = request.form['email']
        password = request.form['password']
        
        # if the login button is pressed then
        if request.form.get('submitbtn') == 'Log in':
            # verify that the user is in the database and credentials are correct
            user = users.identify_user(email, password)

            # if the user is correct then generate a token for them and add it to the session object
            if user:
                token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"])
                session['token'] = token

                # redirect to the user homepage
                return redirect("http://127.0.0.1:5000/userhome")

            else:
                return render_template("login.html", messages=["User not found. Email or password may be incorrect."]), 404
    
    # when get method is sent to this endpoint
    return render_template("login.html"), 200


# Route for the homepage of a logged in user, allows them to get access to the create method
@app.route("/userhome", methods=["GET", "POST"])
@token_required
def user_homepage(current_user):
    """Endpoint for the user homepage of the application. This displays options to create a new review and view account information

    Args:
        current_user (User): the user who is accessing the page

    Returns:
        html template: the html page for the user home
    """
    
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
                return render_template("home_loggedin.html", reviews=sorted_reviews), 200
            elif search_option.lower() == 'instructor':
                sorted_reviews = collection.get_review_by_instr(search_string)
                return render_template("home_loggedin.html", reviews=sorted_reviews), 200

    return render_template("home_loggedin.html", reviews=reviews), 200

#Create GET and POST flask endpoints for the create.html page
#GET endpoint will render the create.html page
#POST endpoint will call the add_review function from the ReviewCollection class
@app.route("/create", methods=["GET", "POST"])
@token_required
def create(current_user):
    if request.method == "POST":
        review_title= request.form['Title']
        course_name = request.form['Course']
        instructor = request.form['Instructor']
        rating = request.form['Rating']
        review_content = request.form['review_content']

    #if the submit button is pressed then add the review to the collection
        if request.form.get('submitbtn') == 'Save':
            collection = ReviewCollection()
            collection.add_review(current_user, review_title, course_name, instructor, review_content, int(rating))
            collection.save()
            return redirect("http://127.0.0.1:5000/userhome")

    return render_template("create.html")


# starting app in debug mode if ran
# debug mode auto restarts the server after every change made to the code
if __name__ == "__main__":
    app.run()
