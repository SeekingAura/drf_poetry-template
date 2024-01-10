import os
import sys
import unittest

import django

# Set expected sys.path for django app
sys.path.insert(0, os.path.abspath("./project_example"))

# Set default settings for django proyect
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_example.settings.settings")

# Initialize django conf
django.setup()

# Run tests at django apps
unittest.main(module=None, argv=["", "discover", "project_example", "-v"])
