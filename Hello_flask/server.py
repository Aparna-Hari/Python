from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World!' 
    return render_template('index.html',phrase="hello",times=5)

# Return the string 'Hello World!' as a response

@app.route('/hello/<name>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name,num):
    print(name,num)
    return "Hello " + name  *num

@app.route('/success')
def success():
    return "success"

# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

