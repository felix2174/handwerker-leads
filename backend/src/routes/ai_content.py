from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('/api/lead', methods=['POST'])
def capture_lead():
    data = request.json
    
    # Lead speichern (erstmal nur in Datei)
    with open('leads.txt', 'a') as f:
        f.write(f"{datetime.now()}: {data}\n")
    
    # Email an Handwerker würde hier kommen
    
    return jsonify({"status": "success"}), 200
