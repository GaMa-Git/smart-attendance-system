from flask import request, jsonify
from datetime import datetime
from . import attendance_bp
from .services import AttendanceService

@attendance_bp.route('/api/attendance/mark', methods=['POST'])
def mark_attendance():
    """Endpoint for the Face Recognition Engine to hit when a face is seen."""
    data = request.json
    
    student_id = data.get('student_id')
    session_id = data.get('session_id')
    timestamp_str = data.get('timestamp')
    
    if not all([student_id, session_id, timestamp_str]):
        return jsonify({"error": "Missing required data"}), 400
        
    # Convert string timestamp to Python datetime object
    timestamp = datetime.fromisoformat(timestamp_str)
    
    # Process logic
    result = AttendanceService.process_recognition(student_id, session_id, timestamp)
    return jsonify(result), 200

@attendance_bp.route('/api/attendance/update', methods=['PUT'])
def update_manual():
    """Endpoint for Teacher UI to manually update attendance."""
    data = request.json
    success = AttendanceService.update_manual_attendance(
        data.get('student_id'), 
        data.get('session_id'), 
        data.get('status')
    )
    return jsonify({"success": success}), 200

@attendance_bp.route('/api/attendance/duty-leave', methods=['POST'])
def duty_leave():
    """Endpoint for Admin to apply Duty Leave."""
    data = request.json
    success = AttendanceService.apply_duty_leave(data.get('student_id'), data.get('session_id'))
    return jsonify({"success": success}), 200