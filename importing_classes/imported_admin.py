"""Excer2."""

from privileges import Admin

admin = Admin('Antonio', 'Hacker', 'Kisumu', 23, ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()

 