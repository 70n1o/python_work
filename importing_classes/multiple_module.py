"""
Excer3.
multiple modules
"""

from privileges import Privileges
from admin import Admin

admin = Admin('Antonio', 'Hacker', 'Kisumu', 23, ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()