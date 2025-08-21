from flask import Blueprint, request, jsonify
from datetime import datetime
import json

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('/api/lead', methods=['POST'])
def capture_lead():
    """Erfasst einen neuen Lead von der Landing Page"""
    data = request.json
    
    # Lead in Datei speichern (später Datenbank)
    lead_info = {
        'timestamp': datetime.now().isoformat(),
        'name': data.get('name'),
        'telefon': data.get('telefon'),
        'stadt': data.get('stadt'),
        'problem': data.get('problem'),
        'budget': data.get('budget')
    }
    
    # In Datei schreiben
    with open('leads.txt', 'a') as f:
        f.write(json.dumps(lead_info) + '\n')
    
    return jsonify({"status": "success", "message": "Lead erfasst"}), 200

@leads_bp.route('/api/test', methods=['GET'])
def test():
    """Test-Endpoint"""
    return jsonify({"status": "online", "service": "Handwerker Leads"}), 200
