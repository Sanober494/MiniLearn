!pip install flask

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Course data
courses = [
    {'id': 1, 'title': 'Introduction to Python', 'duration': '5 mins'},
    {'id': 2, 'title': 'Web Development Basics', 'duration': '7 mins'},
    {'id': 3, 'title': 'Digital Marketing 101', 'duration': '6 mins'},
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        return "Course not found", 404
    return render_template('course.html', course=course)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    # Handle quiz submission logic here
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
