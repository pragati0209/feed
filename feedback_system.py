import sys

def calculate_average_rating(ratings):
    if len(ratings) == 0:
        return 0
    return sum(ratings) / len(ratings)

def feedback_status(avg_rating):
    if avg_rating >= 4.5:
        return "Excellent Feedback"
    elif avg_rating >= 3.5:
        return "Good Feedback"
    elif avg_rating >= 2.5:
        return "Average Feedback"
    else:
        return "Poor Feedback"

if __name__ == "__main__":
    script_name = sys.argv[0]

    if len(sys.argv) > 3:
        student_name = sys.argv[1]
        faculty_name = sys.argv[2]
        ratings = list(map(int, sys.argv[3:]))
        print("User provided feedback details:")
    else:
        student_name = "Sneha"
        faculty_name = "Dr. Rao"
        ratings = [4, 5, 4, 5]
        print("No input given - using default values:")

    avg_rating = calculate_average_rating(ratings)
    status = feedback_status(avg_rating)

    print("\n========== Student Feedback Report ==========")
    print("Script Name:", script_name)
    print("Student Name:", student_name)
    print("Faculty Name:", faculty_name)
    print("Ratings:", ratings)
    print("Average Rating:", avg_rating)
    print("Feedback Status:", status)