from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Campus events data
CAMPUS_EVENTS = [
    {
        "id": 1,
        "title": "Fall Career Fair",
        "category": "academic",
        "date": "2024-12-15",
        "time": "10:00 AM",
        "location": "Stamp Student Union",
        "description": "Meet with employers from various industries",
        "tags": ["career", "networking", "jobs"]
    },
    {
        "id": 2,
        "title": "Basketball Game: UMD vs Duke",
        "category": "sports",
        "date": "2024-12-18",
        "time": "7:00 PM",
        "location": "Xfinity Center",
        "description": "Terps take on Duke in exciting Big Ten matchup",
        "tags": ["basketball", "athletics", "terps"]
    },
    {
        "id": 3,
        "title": "Final Exam Study Session",
        "category": "academic",
        "date": "2024-12-12",
        "time": "6:00 PM",
        "location": "McKeldin Library",
        "description": "Free tutoring and study resources available",
        "tags": ["finals", "studying", "tutoring"]
    },
    {
        "id": 4,
        "title": "Winter Concert Series",
        "category": "entertainment",
        "date": "2024-12-20",
        "time": "8:00 PM",
        "location": "Clarice Smith Center",
        "description": "Student orchestra performs holiday classics",
        "tags": ["music", "concert", "holiday"]
    },
    {
        "id": 5,
        "title": "Coding Workshop: Python Basics",
        "category": "workshop",
        "date": "2024-12-13",
        "time": "3:00 PM",
        "location": "Iribe Center",
        "description": "Learn Python programming fundamentals",
        "tags": ["coding", "python", "tech"]
    },
    {
        "id": 6,
        "title": "Club Fair",
        "category": "social",
        "date": "2024-12-14",
        "time": "12:00 PM",
        "location": "Stamp Student Union",
        "description": "Explore student organizations and clubs",
        "tags": ["clubs", "organizations", "social"]
    },
    {
        "id": 7,
        "title": "Guest Lecture: AI in Healthcare",
        "category": "academic",
        "date": "2024-12-16",
        "time": "2:00 PM",
        "location": "Edward St. John Learning Center",
        "description": "Industry expert discusses AI applications in medicine",
        "tags": ["AI", "healthcare", "lecture"]
    },
    {
        "id": 8,
        "title": "Finals Week Stress Relief",
        "category": "wellness",
        "date": "2024-12-17",
        "time": "1:00 PM",
        "location": "Eppley Recreation Center",
        "description": "Free yoga, meditation, and therapy dogs",
        "tags": ["wellness", "stress-relief", "finals"]
    },
    {
        "id": 9,
        "title": "Holiday Market",
        "category": "social",
        "date": "2024-12-19",
        "time": "11:00 AM",
        "location": "Campus Mall",
        "description": "Shop local vendors for holiday gifts",
        "tags": ["shopping", "holiday", "local"]
    },
    {
        "id": 10,
        "title": "Graduation Ceremony",
        "category": "academic",
        "date": "2024-12-21",
        "time": "9:00 AM",
        "location": "Xfinity Center",
        "description": "Fall 2024 commencement ceremony",
        "tags": ["graduation", "ceremony", "celebration"]
    }
]

@app.route('/')
def home():
    """API home endpoint"""
    return jsonify({
        "message": "Campus Events API",
        "endpoint": "/events"
    })

@app.route('/events')
def get_events():
    """Get all campus events"""
    return jsonify(CAMPUS_EVENTS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
