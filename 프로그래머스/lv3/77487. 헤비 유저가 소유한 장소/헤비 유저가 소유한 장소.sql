SELECT A.ID, A.NAME, A.HOST_ID
FROM PLACES A JOIN 
(SELECT HOST_ID, COUNT(HOST_ID)
FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(HOST_ID) >= 2)B USING (HOST_ID)