# gym_ai.py

def get_user_data():
    print("Welcome to the Gym AI Workout Planner!")
    
    # Collecting basic information
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (M/F): ")
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    
    # Fitness goals
    print("\nSelect your fitness goal:")
    print("1. Weight Loss")
    print("2. Muscle Gain")
    print("3. Maintenance")
    goal = int(input("Enter the number corresponding to your goal: "))
    
    # Activity level
    print("\nSelect your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Light Activity (light exercise/sports 1-3 days a week)")
    print("3. Moderate Activity (moderate exercise/sports 3-5 days a week)")
    print("4. Active (intense exercise/sports 6-7 days a week)")
    print("5. Very Active (very intense exercise, physical job, or training)")
    activity_level = int(input("Enter the number corresponding to your activity level: "))
    
    # Preferred workout type
    print("\nSelect your preferred workout type:")
    print("1. Cardio")
    print("2. Strength Training")
    print("3. Flexibility")
    print("4. HIIT")
    print("5. Mixed")
    workout_type = int(input("Enter the number corresponding to your workout type: "))
    
    # Experience level
    print("\nSelect your experience level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    experience_level = int(input("Enter the number corresponding to your experience level: "))
    
    # Available equipment
    print("\nSelect the available equipment:")
    print("1. No Equipment")
    print("2. Basic Equipment (dumbbells, resistance bands)")
    print("3. Full Gym Access")
    equipment = int(input("Enter the number corresponding to your equipment: "))
    
    # Time available per day
    time_available = int(input("Enter the time available for workout each day (in minutes): "))
    
    # Return collected data as a dictionary
    user_data = {
        'name': name,
        'age': age,
        'gender': gender,
        'height': height,
        'weight': weight,
        'goal': goal,
        'activity_level': activity_level,
        'workout_type': workout_type,
        'experience_level': experience_level,
        'equipment': equipment,
        'time_available': time_available
    }
    
    return user_data

# For testing, print the collected user data
if __name__ == "__main__":
    user_data = get_user_data()
    print("\nCollected User Data:")
    for key, value in user_data.items():
        print(f"{key}: {value}")
