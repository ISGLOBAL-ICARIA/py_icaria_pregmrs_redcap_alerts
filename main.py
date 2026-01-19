#!/usr/bin/env python3.8
"""
Python script with several functions regarding the PregMRS project such as,
preparing the alarm per participant and moment, correct IDs or find duplicates
"""

import alerts
import tokens
import redcap
from datetime import datetime

__author__ = "Andreu Bofill"
__copyright__ = "Copyright 2024, ISGlobal Maternal, Child and Reproductive Health"
__credits__ = ["Andreu Bofill"]
__license__ = "MIT"
__version__ = "0.0.1"
__date__ = "20240520"
__maintainer__ = "Andreu Bofill"
__email__ = "andreu.bofill@isglobal.org"
__status__ = "Finished"


if __name__ == '__main__':
    for project_key in tokens.PREGMRS_REDCAP_PROJECTS:
        project = redcap.Project(tokens.URL, tokens.PREGMRS_REDCAP_PROJECTS[project_key])
        """ 
        This function read the status of each participant, prepare the according
        alarm that is needed in each case and saves it directly on the 
        'fu_status' variable in REDCap
        """
        alerts.pregmrs_alert(project)

        """ This part of the script cleans study number + other IDs """
        alerts.sn_cleaning(project)
        alerts.sn_cleaning(project, field_='pmrs_nasophar_swab_id')
        alerts.sn_cleaning(project, field_='pmrs_vaginal_swab_id')
        alerts.sn_cleaning(project, field_='pmrs_breast_swab_id')
        alerts.sn_cleaning(project, field_='newborn_sample_id', event='newborn_arm_1')
        alerts.sn_cleaning(project, field_='newborn_sample_id_2', event='newborn_arm_1')

        """ To find duplicates in the PregMRS project"""
        alerts.duplicates(project)

    print("\n FINISHED:\t",datetime.today())