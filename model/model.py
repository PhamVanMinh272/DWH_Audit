from ..setting import DATABASE
from datetime import datetime
import uuid
db = DATABASE

class AuditJob(db.Model):
    __tablename__ = 'audit_job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    status = db.Column(db.String(10))
    comment = db.Column(db.Text)
    error = db.Column(db.Text)

    def __init__(self, name=None, time_start=datetime.now(), time_end=None, duration=None, comment=None, error=None):
        self.name = name
        self.time_start = time_start
        self.time_end = time_end
        self.duration = duration
        self.comment = comment
        self.error = error
    def start(self):
        db.session.add(self)
        db.session.commit()
    def end(self):
        self.time_end = datetime.now()
        duration = self.time_end - self.time_start
        self.duration = duration.seconds
        self.status = 'Success'
        db.session.commit()


class AuditStep(db.Model):
    __tablename__ = 'audit_step'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    sent_row = db.Column(db.Integer)
    received_row = db.Column(db.Integer)
    status = db.Column(db.String(10))
    comment = db.Column(db.Text)
    error = db.Column(db.Text)

    def __init__(self, job, name=None, time_start=datetime.now(), time_end=None, duration=None, sent_row=None,
                 received_row=None, status='Doing', comment=None, error=None):
        self.job_id = job.id
        self.name = name
        self.time_start = time_start
        self.time_end = time_end
        self.duration = duration
        self.sent_row = sent_row
        self.received_row = received_row
        self.status = status
        self.comment = comment
        self.error = error
    def start(self):
        db.session.add(self)
        db.session.commit()

    def update(self, sent_row=None, received_row=None, status=None, comment=None, error=None):
        if sent_row is not None:
            self.sent_row = sent_row
        if received_row is not None:
            self.received_row = received_row
        if status is not None:
            self.status = status
        if comment is not None:
            self.comment = comment
        if error is not None:
            self.error = error
        db.session.commit()
    def end(self):
        self.time_end = datetime.now()
        duration = self.time_end - self.time_start
        self.duration = duration.seconds
        self.status = 'Success'
        db.session.commit()

db.create_all()
if __name__ == '__main__':
    pass
