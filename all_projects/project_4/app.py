from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to check if a string is a palindrome
def is_palindrome(name):
    # Remove spaces and convert to lowercase
    name = name.replace(" ", "").lower()
    return name == name[::-1]

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to check if the name is a palindrome
@app.route('/check-palindrome', methods=['POST'])
def check_palindrome():
    data = request.get_json()
    name = data.get('name', '')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    result = is_palindrome(name)
    return jsonify({"name": name, "is_palindrome": result})

if __name__ == '__main__':
    app.run(debug=True)