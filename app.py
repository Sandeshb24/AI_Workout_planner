# app.py

from flask import Flask, render_template, request
from gym_ai import get_user_data
from workout_plan import generate_workout_plan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Collect data from form
    user_data = {
        'name': request.form['name'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'height': float(request.form['height']),
        'weight': float(request.form['weight']),
        'goal': int(request.form['goal']),
        'activity_level': int(request.form['activity_level']),
        'workout_type': int(request.form['workout_type']),
        'experience_level': int(request.form['experience_level']),
        'equipment': int(request.form['equipment']),
        'time_available': int(request.form['time_available'])
    }
    
    # Generate workout plan
    workout_plan = generate_workout_plan(user_data)
    
    return render_template('result.html', workout_plan=workout_plan, name=user_data['name'])

if __name__ == "__main__":
    app.run(debug=True)
