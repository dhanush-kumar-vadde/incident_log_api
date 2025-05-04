from flask import Blueprint, request, jsonify
from database import db
from models import Incident

incident_routes = Blueprint('incident_routes', __name__)

@incident_routes.route('/incidents', methods=['GET'])
def get_all_incidents():
    incidents = Incident.query.all()
    return jsonify([i.to_dict() for i in incidents]), 200

@incident_routes.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    # Validation
    if not data or not all(key in data for key in ('title', 'description', 'severity')):
        return jsonify({'error': 'Missing required fields'}), 400
    if data['severity'] not in ['Low', 'Medium', 'High']:
        return jsonify({'error': 'Severity must be Low, Medium, or High'}), 400

    incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    db.session.add(incident)
    db.session.commit()
    return jsonify(incident.to_dict()), 201

@incident_routes.route('/incidents/<int:id>', methods=['GET'])
def get_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    return jsonify(incident.to_dict()), 200

@incident_routes.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    db.session.delete(incident)
    db.session.commit()
    return jsonify({'message': f'Incident {id} deleted successfully.'}), 200