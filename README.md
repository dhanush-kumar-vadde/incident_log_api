# HumanChain AI Safety Incident Log API

## Language and Framework
- Language: Python 3
- Framework: Flask

## Setup Instructions

1. Clone the repository or place all files into a directory.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux

4. Install Dependencies:
   pip install -r requirements.txt

5. Run The server:
   python app.py


##Database Setup

The database used is SQLite.

A file incidents.db will be created automatically in the project directory when the server is started for the first time.

API Endpoints

1. GET /incidents

   Fetch all incidents.

   Example using curl:
   curl http://127.0.0.1:5000/incidents


2. POST /incidents

   Add a new incident.

   Example using curl:
   curl -X POST http://127.0.0.1:5000/incidents -H "Content-Type:        application/json" -d "{\"title\":\"Sample Incident\",\"description\":\"Details of the incident.\",\"severity\":\"High\"}"

3. GET /incidents/

   Fetch a specific incident by ID.

   Example using curl:
   curl http://127.0.0.1:5000/incidents/1

4. DELETE /incidents/

   Delete a specific incident by ID.

   Example using curl:
   curl -X DELETE http://127.0.0.1:5000/incidents/1

Design Decisions and Challenges

1. To avoid circular imports, the database was initialized in a separate file  (database.py).

2. Flask Blueprints were used to modularize API routes (routes.py).

3. SQLite was chosen for simplicity and no external server setup.