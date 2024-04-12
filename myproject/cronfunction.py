import os
import sys
import django

# Determine the Django project directory and add it to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
django_project_directory = os.path.dirname(current_directory)
sys.path.append(django_project_directory)

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Import required modules after Django setup
from app.createPost.models import createFeedback

def delete_feedback():
    # Your deletefeedback function
    createFeedback.objects.filter(id=18).delete()

if __name__ == "__main__":
    # Call the function when the script is executed
    delete_feedback()
