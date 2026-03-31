from flask import Blueprint

# Create the blueprint for Module 2
attendance_bp = Blueprint('attendance_module', __name__)

# Import routes so they are registered with the blueprint
from . import routes