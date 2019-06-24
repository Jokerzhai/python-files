import mcutk

from mcutk.apps import appfactory

App = appfactory('iar')
app =App.get_latest()

print app.version
print app.path
print app.is_ready