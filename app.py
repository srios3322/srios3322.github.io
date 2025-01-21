from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Yes')
def yes_page():
    return render_template('yes.html')

@app.route('/No')
def no_page():
    return render_template('no.html')

@app.route('/choose')
def choose_page():
    return render_template('choose.html')

@app.route('/submit_choice', methods=['POST'])
def submit_choice():
    selected_choice = request.form.get('choice')  # Retrieve the selected choice
    print(f"Selected choice: {selected_choice}")  # Output the choice in the console
    if selected_choice == 'Option 1' or selected_choice == 'Option 2':
        print(f"Selected choice: {selected_choice}")
        return redirect(url_for('time_page'))
    elif selected_choice == 'Option 3':
        return redirect(url_for('redo_page'))
    else:
        return "Please select a valid option."

@app.route('/time')
def time_page():
    return render_template('time.html')

@app.route('/redo')
def redo_page():
    return render_template('redo.html')

@app.route('/submit-time', methods=['POST'])
def submit_time():
    selected_time = request.form['time']
    print(f"Selected time: {selected_time}")  # Print selected time to terminal
    return redirect(url_for('yipe_page'))

@app.route('/yipe')
def yipe_page():
    return render_template('yipe.html')

# Test route
@app.route('/test')
def test():
    print("Test route triggered")
    return "Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)
