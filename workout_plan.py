# workout_plan.py

def generate_workout_plan(user_data):
    # Extracting user data
    goal = user_data['goal']
    activity_level = user_data['activity_level']
    workout_type = user_data['workout_type']
    experience_level = user_data['experience_level']
    equipment = user_data['equipment']
    time_available = user_data['time_available']
    
    # Workout plan template
    workout_plan = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    
    # Simple rule-based logic to generate a workout plan
    if goal == 1:  # Weight Loss
        workout_plan = weight_loss_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    elif goal == 2:  # Muscle Gain
        workout_plan = muscle_gain_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    elif goal == 3:  # Maintenance
        workout_plan = maintenance_plan(workout_plan, workout_type, time_available, experience_level, equipment)
    
    return workout_plan


def weight_loss_plan(workout_plan, workout_type, time_available, experience_level, equipment):
    # Basic example for weight loss workout plan
    for day in workout_plan:
        if workout_type == 1:  # Cardio
            workout_plan[day] = [f"{time_available} minutes of running or cycling"]
        elif workout_type == 2:  # Strength Training
            workout_plan[day] = [f"{time_available} minutes of circuit training with {equipment_level(equipment)}"]
        elif workout_type == 3:  # Flexibility
            workout_plan[day] = [f"{time_available} minutes of yoga"]
        elif workout_type == 4:  # HIIT
            workout_plan[day] = [f"{time_available} minutes of HIIT workout"]
        elif workout_type == 5:  # Mixed
            workout_plan[day] = [f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength training"]
    
    return workout_plan


def muscle_gain_plan(workout_plan, workout_type, time_available, experience_level, equipment):
    # Basic example for muscle gain workout plan
    for day in workout_plan:
        if workout_type == 1:  # Cardio
            workout_plan[day] = [f"{time_available // 3} minutes of light cardio and {time_available * 2 // 3} minutes of strength training with {equipment_level(equipment)}"]
        elif workout_type == 2:  # Strength Training
            workout_plan[day] = [f"{time_available} minutes of heavy lifting with {equipment_level(equipment)}"]
        elif workout_type == 3:  # Flexibility
            workout_plan[day] = [f"{time_available} minutes of stretching and light resistance training"]
        elif workout_type == 4:  # HIIT
            workout_plan[day] = [f"{time_available // 2} minutes of strength HIIT and {time_available // 2} minutes of muscle-specific training"]
        elif workout_type == 5:  # Mixed
            workout_plan[day] = [f"{time_available // 2} minutes of strength training and {time_available // 2} minutes of muscle-specific training"]
    
    return workout_plan


def maintenance_plan(workout_plan, workout_type, time_available, experience_level, equipment):
    # Basic example for maintenance workout plan
    for day in workout_plan:
        if workout_type == 1:  # Cardio
            workout_plan[day] = [f"{time_available // 2} minutes of moderate cardio and {time_available // 2} minutes of strength maintenance with {equipment_level(equipment)}"]
        elif workout_type == 2:  # Strength Training
            workout_plan[day] = [f"{time_available} minutes of balanced strength and endurance training with {equipment_level(equipment)}"]
        elif workout_type == 3:  # Flexibility
            workout_plan[day] = [f"{time_available} minutes of mixed stretching and light cardio"]
        elif workout_type == 4:  # HIIT
            workout_plan[day] = [f"{time_available // 2} minutes of HIIT and {time_available // 2} minutes of endurance training"]
        elif workout_type == 5:  # Mixed
            workout_plan[day] = [f"{time_available // 2} minutes of cardio and {time_available // 2} minutes of strength maintenance"]
    
    return workout_plan

def equipment_level(equipment):
    if equipment == 1:
        return "no equipment"
    elif equipment == 2:
        return "basic equipment"
    elif equipment == 3:
        return "full gym access"


# For testing, integrate with the user data collection
if __name__ == "__main__":
    from gym_ai import get_user_data
    
    user_data = get_user_data()
    workout_plan = generate_workout_plan(user_data)
    
    print("\nGenerated Weekly Workout Plan:")
    for day, exercises in workout_plan.items():
        print(f"{day}: {', '.join(exercises)}")
