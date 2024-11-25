def get_exercises(age, height, weight,):
    exercises = []

    # Age group: 0-18
    if age<15:
         print("Wait till you are 18 ")
    elif 15<= age <= 18:
        if height < 150:
            if weight <=60:
             exercises= ["Jumping Jacks", "Bodyweight Squats", "Push-ups"]
            elif 60 < weight <=80:
                exercises = ["Running(30 mins)","Rope skipping(15 mins)","muscle exercises"]
            else:
                exercises = ["Running (20 mins,3 times with 5 min break in between)","Waist twisting(100 each side)","Daily 12000 steps "]
        elif 150 <= height < 180:
            if weight <=60:
             exercises = ["Basketball", "Swimming", "Cycling"]
            elif 60 < weight <=80:
                exercises = ["Running(40 mins)","Rope skipping(20 mins)","muscle exercises"]
            else:
                exercises = ["Running (30 mins,3 times with 5 min break in between)","Waist twisting(100 each side)","Daily 12000 steps "]
        else:
            if weight <=60:
              exercises = ["Running", "Weight Lifting", "Yoga"]
            elif 60 < weight <=80:
                exercises = ["Running(30 mins)","Rope skipping(15 mins)","muscle exercises"]
            else:
                exercises = ["Running (35 mins,3 times with 5 min break in between)","Waist twisting(100 each side)","Daily 12000 steps "]

    # Age group: 19-60
    elif 19 <= age <= 60:
        if weight < 60:
            exercises = ["Yoga", "Pilates", "Light Jogging"]
        elif 60 <= weight < 80:
            exercises = ["Running", "Cycling", "Strength Training"]
        else:
            exercises = ["Walking", "Swimming", "Low-Impact Aerobics"]

    # Age group: 61 and above
    elif age > 60:
        if height < 150:
            if weight <= 60:
              exercises = ["Walking", "Chair Yoga", "Light Stretching"]
            elif 60 < weight <=80:
              exercises = ["Little little walking is enough"]
            else:
               exercises = ["WALK JUST WALK"]
            
        elif 150 <= height < 180:
            if weight <= 60:
               exercises = ["Walking", "Swimming", "Tai Chi"]
            elif 60 < weight <=80:
              exercises = ["Little bit more walking arounf 30 mins daily"]
            else:
               exercises = ["JUST WALK 45 mins daily"]
        else:
            exercises = ["Walking", "Water Aerobics", "Gentle Yoga"]
    return exercises

    
    
    

def get_workout_plan(goal, fitness_level):
    # Define a structured workout plan based on goals and fitness levels
    workout_plans = {
        "weight_loss": {
            "beginner": [
                {"exercise": "Jumping Jacks", "sets": "3 sets", "reps": "15 reps", "rest": "30 seconds rest"},
                {"exercise": "Bodyweight Squats", "sets": "3 sets", "reps": "12 reps", "rest": "30 seconds rest"},
                {"exercise": "Push-ups", "sets": "3 sets", "reps": "10 reps", "rest": "30 seconds rest"},
            ],
            "intermediate": [
                {"exercise": "Burpees", "sets": "4 sets", "reps": "10 reps", "rest": "30 seconds rest"},
                {"exercise": "Mountain Climbers", "sets": "4 sets", "reps": "15 reps", "rest": "30 seconds rest"},
                {"exercise": "Plank", "sets": "3 sets", "duration": "for 30 seconds", "rest": "30 seconds rest"},
            ],
            "advanced": [
                {"exercise": "High-Intensity Interval Training (HIIT)", "sets": "5 sets", "duration": "for 20 seconds on","rest": "10 seconds rest"},
                {"exercise": "Kettlebell Swings", "sets": "4 sets", "reps": "15 reps", "rest": "30 seconds rest"},
                {"exercise": "Box Jumps", "sets": "4 sets", "reps": "12 reps", "rest": "30 seconds rest"},
            ],
        },
        "muscle_gain": {
            "beginner": [
                {"exercise": "Dumbbell Bench Press", "sets": "3 sets", "reps": "10 reps", "rest": "60 seconds rest"},
                {"exercise": "Dumbbell Rows", "sets": "3 sets", "reps": "10 reps", "rest": "60 seconds rest"},
                {"exercise": "Leg Press", "sets": "3 sets", "reps": "10 reps", "rest": "60 seconds rest"},
            ],
            "intermediate": [
                {"exercise": "Barbell Squats", "sets": "4 sets", "reps": "8 reps", "rest": "90 seconds rest"},
                {"exercise": "Deadlifts", "sets": "4 sets", "reps": "8 reps", "rest": "90 seconds rest"},
                {"exercise": "Pull-ups", "sets": "3 sets", "reps": "8 reps", "rest": "90 seconds rest"},
            ],
            "advanced": [
                {"exercise": "Power Cleans", "sets": "5 sets", "reps": "5 reps", "rest": "2 minutes rest"},
                {"exercise": "Barbell Bench Press", "sets": "5 sets", "reps": "5 reps", "rest": "2 minutes rest"},
                {"exercise": "Squat Variations", "sets": "5 sets", "reps": "5 reps", "rest": "2 minutes rest"},
            ],
        },
        "endurance": {
            "beginner": [
                {"exercise": "Brisk Walking", "duration": "30 minutes"},
                {"exercise": "Cycling", "duration": "30 minutes"},
                {"exercise": "Swimming", "duration": "30 minutes"},
            ],
            "intermediate": [
                {"exercise": "Jogging", "duration": "45 minutes"},
                {"exercise": "Interval Running", "duration": "30 minutes"},
                {"exercise": "Rowing", "duration": "30 minutes"},
            ],
            "advanced": [
                {"exercise": "Long-Distance Running", "duration": "60 minutes"},
                {"exercise": "Trail Running", "duration": "60 minutes"},
                {"exercise": "Cycling (High Intensity)", "duration": "60 minutes"},
            ],
        },
    }
    
    return workout_plans.get(goal, {}).get(fitness_level, [])

def main():
    print("Welcome to the Exercise Planner!")
    
    try:
        age = int(input("Please enter your age: "))
        height = float(input("Please enter your height in cm: "))
        weight = float(input("Please enter your weight in kg: "))
        
        
        exercises = get_exercises(age, height, weight)
        
        print("\nBased on your age, height, and weight, you can try the following exercises:")
        for exercise in exercises:
            print(exercise) #To read the list 
        
        # Summary 
        print("\nSummary:")
        print(f"Age: {age}, Height: {height} cm, Weight: {weight} kg")

        # Ask if the user wants gym-related exercises
        gym_request = input("\nWould you like some gym-related exercises? (yes/no): ").strip().lower()
        
        if gym_request == "yes":
            goal = input("What is your fitness goal? (weight_loss, muscle_gain, endurance): ").strip().lower()
            fitness_level = input("What is your fitness level? (beginner, intermediate, advanced): ").strip().lower()
    
           # Generate workout plan
            workout_plan = get_workout_plan(goal, fitness_level)
    
            # Display the workout plan
            if workout_plan:
               print("\nYour Structured Workout Plan:")
            for exercise in workout_plan:
              if "duration" in exercise:
                print(f"- {exercise['exercise']}: {exercise['duration']}")
              else:
                print(f"- {exercise['exercise']}: {exercise['sets']},{exercise['reps']},{exercise['rest']}")
            print("\nThanks for using the Exercise Planner")
                
    except ValueError:
        print("Please enter valid numbers for age, height, and weight.")


if __name__ == "__main__":
    main()