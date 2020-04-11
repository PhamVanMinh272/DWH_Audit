----------------------------------- Run
+ Install:
Copy 'audit_service' to your project (your root path of project).
At audit_server/setting.py change your db variable, which will contain audit tables.

+ Basic Usage:
job = AuditJob(name=<name of job>) # init job
job.start() # start job
step = AuditStep(job=job, name=<name of step>) # init step
step.start() # start step
# ETL here
step.end() # stop step
job.end() # stop job

+ Advanced Usage:
In ETL scripts, use the follow command to update audit information:
	job.update(status=<>, comment=<>, error=<>)
	step.update(sent_row=<>, received_row=<>, status=<>, comment=<>, error=<>)



------------------------------------- Test
Copy run_test_audit.py to your project root file.
At test/setting.py change your SOURCE_DATABASE and your DESTINATION_DATABASE
Then run_test_audit.py
If you see 'Test audit success!', so you have installing successfully.


--------------------------------------Limitations
- Just can connect by flask.
- Do not have many features.
