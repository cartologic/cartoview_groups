# this file is excuted from cartoview.app_manager.settings using exec_file
import os

from apps import cartoview_groups

app_folder = os.path.dirname(cartoview_groups.__file__)
TEMPLATES[0]['DIRS'] = [os.path.join(app_folder, 'templates'), ] + TEMPLATES[0]['DIRS']
# INSTALLED_APPS += ('cartoview_groups',)
# TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'apps', 'cartoview_groups', 'templates'),] + TEMPLATES[0]['DIRS']