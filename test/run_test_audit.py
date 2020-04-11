from audit_service.test.model import *
from audit_service.model.model import *
from db_connection.mysql_ssh import ssh
# audit session
job = AuditJob(name='Test audit job')
job.start()
step = AuditStep(job=job, name='Test audit step')
step.start()
# stop audit session
data_sources = AuditTestSource.query.all()
step.update(sent_row=len(data_sources))
count = 0
for i in data_sources:
    if AuditTestDestination.query.filter(AuditTestDestination.value==i.value).first() is None:
        data_destination = AuditTestDestination(value=i.value)
        DESTINATION_DATABASE.session.add(data_destination)
        DESTINATION_DATABASE.session.commit()
        count = count + 1
step.update(received_row=count)
# audit session
step.end()
job.end()
if job.status == 'Success' and step.status == 'Success' and step.sent_row == 6 and step.received_row == 4:
    print('Test audit success!')
else: print('Test audit failed!')

# stop audit session

# clear data test
AuditTestDestination.__table__.drop(DESTINATION_DATABASE.engine)
if ssh:
    ssh.stop()
    print('Stop ssh')
SOURCE_DATABASE.engine.execute('drop table audit_test_source;')
print('Clear data test')



