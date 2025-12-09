# Campus Events API

A simple Flask API that provides campus events data for University of Maryland.

## Setup

1. Install dependencies:
```bash
pip install flask
```

2. Run the API:
```bash
python campus_events_api.py
```

The API will start on `http://localhost:5000`

## Endpoint

**GET /events**

Returns all campus events in JSON format.

### Example Request
```bash
curl http://localhost:5000/events
```

### Example Response
```json
[
  {
    "id": 1,
    "title": "Fall Career Fair",
    "category": "academic",
    "date": "2024-12-15",
    "time": "10:00 AM",
    "location": "Stamp Student Union",
    "description": "Meet with employers from various industries",
    "tags": ["career", "networking", "jobs"]
  }
]
```

## Usage in Your App

```python
import requests

response = requests.get('http://localhost:5000/events')
events = response.json()
```

## Event Structure

Each event contains:
- `id`: Unique identifier
- `title`: Event name
- `category`: Type of event (academic, sports, social, etc.)
- `date`: Event date (YYYY-MM-DD)
- `time`: Event time
- `location`: Venue or building name
- `description`: Brief description
- `tags`: List of related keywords

## License

MIT
