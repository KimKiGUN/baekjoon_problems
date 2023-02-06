SELECT APNT_NO, PT_NAME, APPOINTMENT.PT_NO, APPOINTMENT.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT JOIN PATIENT ON (APPOINTMENT.PT_NO=PATIENT.PT_NO) JOIN DOCTOR ON (APPOINTMENT.MDDR_ID = DOCTOR.DR_ID)
WHERE APNT_CNCL_YN = 'N' AND APPOINTMENT.MCDP_CD = 'CS' AND DATE(APNT_YMD) = '2022-04-13'
ORDER BY APNT_YMD