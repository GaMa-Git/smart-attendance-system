from datetime import datetime
from .rule_engine import AttendanceRuleEngine

class AttendanceService:
    
    @staticmethod
    def process_recognition(student_id: str, session_id: int, timestamp: datetime) -> dict:
        """
        Called automatically by Face Recognition Engine.
        """
        # Step 1: Fetch session start time from DB (Mocked for now)
        # session = AttendanceSession.query.get(session_id)
        mock_session_start_time = datetime.now() # Replace with session.start_time later
        
        # Step 2: Apply Business Rules
        status = AttendanceRuleEngine.evaluate_status(mock_session_start_time, timestamp)
        
        # Step 3: Debouncing - Check if student is already marked today
        # existing_log = AttendanceLog.query.filter_by(student_id=student_id, session_id=session_id).first()
        # if existing_log:
        #     return {"status": "ignored", "message": "Student already marked"}

        # Step 4: Save to Database
        # new_log = AttendanceLog(student_id=student_id, session_id=session_id, timestamp=timestamp, status=status)
        # db.session.add(new_log)
        # db.session.commit()

        return {"status": "success", "recorded_status": status}

    @staticmethod
    def update_manual_attendance(student_id: str, session_id: int, status: str) -> bool:
        """
        Allows a teacher to manually override attendance.
        """
        # DB Logic to update status directly
        return True

    @staticmethod
    def apply_duty_leave(student_id: str, session_id: int) -> bool:
        """
        Marks a student as on Duty Leave (treated as Present).
        """
        # DB Logic to insert "DutyLeave" status
        return True