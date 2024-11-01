SELECT * 
FROM people 
WHERE license_plate IN (
    SELECT license_plate 
    FROM bakery_security_logs 
    WHERE day = 28 
      AND month = 7 
      AND year = 2023 
      AND hour = 10 
      AND minute BETWEEN 18 AND 35
)



-- access information of poeple who's number plates appear on the footage.
