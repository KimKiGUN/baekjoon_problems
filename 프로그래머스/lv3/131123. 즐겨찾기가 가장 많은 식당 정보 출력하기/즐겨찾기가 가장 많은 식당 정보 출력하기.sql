WITH FAV AS
(SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_FAVORITES
FROM REST_INFO
GROUP BY FOOD_TYPE)

SELECT R1.FOOD_TYPE, R1.REST_ID, R1.REST_NAME, R1.FAVORITES
FROM REST_INFO R1, FAV R2
WHERE R1.FOOD_TYPE = R2.FOOD_TYPE AND R1.FAVORITES = R2.MAX_FAVORITES
GROUP BY 1
ORDER BY 1 DESC