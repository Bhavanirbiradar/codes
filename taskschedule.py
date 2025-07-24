class UserMainCode(object):
    @classmethod
    def maxExercises(cls, input1, input2, input3):
        exercises = list(zip(input2, input3))  # Pair (duration, deadline)
        exercises.sort(key=lambda x: x[1])     # Sort by deadline
        
        current_day = 0
        count = 0
        
        for duration, deadline in exercises:
            if current_day + duration <= deadline:
                current_day += duration
                count += 1
        
        return count


if __name__ == "__main__":
    # Read inputs from the user
    input1 = int(input("Enter number of exercises: "))  # e.g. 4
    input2 = list(map(int, input("Enter durations (space-separated): ").split()))  # e.g. 10 40 30 20
    input3 = list(map(int, input("Enter deadlines (space-separated): ").split()))  # e.g. 20 50 40 30

    # Call the class method and print result
    result = UserMainCode.maxExercises(input1, input2, input3)
    print("Maximum number of exercises that can be completed:", result)
