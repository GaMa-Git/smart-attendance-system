from datetime import datetime, timedelta

class AttendanceRuleEngine:
    MIN_ATTENDANCE_THRESHOLD = 75.0
    LATE_MARGIN_MINUTES = 10

    @classmethod
    def evaluate_status(cls, session_start: datetime, capture_time: datetime) -> str:
        """
        Determines if a student is Present or Late based on the allowed margin.
        """
        margin = timedelta(minutes=cls.LATE_MARGIN_MINUTES)
        
        if capture_time <= session_start + margin:
            return "Present"
        return "Late"

    @classmethod
    def check_minimum_percentage(cls, current_percentage: float) -> bool:
        """
        Checks if the student meets the 75% institutional threshold.
        """
        return current_percentage >= cls.MIN_ATTENDANCE_THRESHOLD