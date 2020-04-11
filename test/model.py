from .setting import SOURCE_DATABASE, DESTINATION_DATABASE

class AuditTestSource(SOURCE_DATABASE.Model):
    __tablename__ = 'audit_test_source'
    id = SOURCE_DATABASE.Column(SOURCE_DATABASE.Integer, primary_key=True)
    value = SOURCE_DATABASE.Column(SOURCE_DATABASE.String(50))

class AuditTestDestination(DESTINATION_DATABASE.Model):
    __tablename__ = 'audit_test_destination'
    id = DESTINATION_DATABASE.Column(DESTINATION_DATABASE.Integer, primary_key=True)
    value = DESTINATION_DATABASE.Column(DESTINATION_DATABASE.String(50))

SOURCE_DATABASE.create_all()
DESTINATION_DATABASE.create_all()

# create data for source
sources = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
for source in sources:
    src = AuditTestSource(value=source)
    SOURCE_DATABASE.session.add(src)
    SOURCE_DATABASE.session.commit()

destinations = ['a1', 'a2']
for destination in destinations:
    des = AuditTestDestination(value=destination)
    DESTINATION_DATABASE.session.add(des)
    DESTINATION_DATABASE.session.commit()