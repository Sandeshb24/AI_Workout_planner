# gym_workout_planner.py

from gym_ai import get_user_data
from workout_plan import generate_workout_plan

def main():
    print("Welcome to the Gym AI Workout Planner!")

    # Collect user data
    user_data = get_user_data()

    # Generate workout plan
    workout_plan = generate_workout_plan(user_data)

    # Display the workout plan
    print("\nYour Personalized Weekly Workout Plan:")
    for day, exercises in workout_plan.items():
        print(f"\n{day}:")
        for exercise in exercises:
            print(f"- {exercise}")
    
    # Optionally save the workout plan to a file
    save_option = input("\nWould you like to save your workout plan to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        save_workout_plan(user_data['name'], workout_plan)

def save_workout_plan(name, workout_plan):
    filename = f"{name}_workout_plan.txt"
    with open(filename, 'w') as file:
        file.write("Your Personalized Weekly Workout Plan:\n")
        for day, exercises in workout_plan.items():
            file.write(f"\n{day}:\n")
            for exercise in exercises:
                file.write(f"- {exercise}\n")
    print(f"\nWorkout plan saved as {filename}.")

if __name__ == "__main__":
    main()
