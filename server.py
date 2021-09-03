from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/namelist')
def renderList():

    table_list = [

        {'first_name': 'Raden', 'last_name': 'Mantuano', 'full_name': ' Raden Mantuano'},
        {'first_name': 'Michael', 'last_name': 'Jordan', 'full_name': ' Michael Jordan'},
        {'first_name': 'Steph', 'last_name': 'Curry', 'full_name': ' Steph Curry'},
        
    ]

    return render_template ('index1.html', table_list = table_list)

if __name__ == "__main__":
    app.run(debug=True)
