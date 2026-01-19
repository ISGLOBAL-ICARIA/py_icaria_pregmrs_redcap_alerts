# PregMRS_redcap_alerts

Python script to set up alerts for PregMRS ICARIA field workers. This script has several functions regarding the PregMRS project.

The most important one is to read the status of each participant, prepare the appropriate alarm that is needed in each case based on the participant's status, and save it directly on the 'fu_status' variable in REDCap.
In parallel, it also finds study number or other ID errors and corrects them, and finally, it also corrects duplicates.
