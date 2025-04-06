from flask import Flask, session, render_template_string

app = Flask(__name__)
app.secret_key = '@3233q23'  # Needed to use sessions securely

@app.route('/')
def home():
    # Check if 'visit_count' exists in session; if not, initialize it
    if 'visit_count' in session:
        session['visit_count'] += 1  # Increment visit count
    else:
        session['visit_count'] = 1  # Initialize visit count to 1

    # Display the visit count
    return render_template_string('''
        <h1>Welcome!</h1>
        <p>You have visited this page {{ session['visit_count'] }} time(s) in this session.</p>
        <p><a href="/">Refresh</a> to see the counter increase.</p>
    ''')

@app.route('/reset')
def reset():
    session.pop('visit_count', None)  # Remove 'visit_count' from the session
    return '<h1>Counter Reset!</h1><p><a href="/">Go Back</a></p>'

if __name__ == '__main__':
    app.run(debug=True)
