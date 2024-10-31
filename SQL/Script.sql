SELECT * 
FROM crime_scene_reports csr 
WHERE day = 28 
AND year = 2023 
AND month = 7 
AND description LIKE '%CS50 duck%';

SELECT * 
FROM interviews i 
WHERE day = 28 
AND year = 2023 
AND month = 7 
AND transcript LIKE '%bakery%';

SELECT * 
FROM bakery_security_logs bsl
WHERE day = 28 
AND year = 2023 
AND month = 7
AND "hour" = 10
AND "minute" BETWEEN 15 AND 25

SELECT id
FROM airports a 
WHERE city = 'Fiftyville'

SELECT * 
FROM flights f 
WHERE day = 29
AND year = 2023 
AND month = 7
AND origin_airport_id 
ORDER BY hour ASC, minute ASC;


SELECT * 
FROM phone_calls pc
WHERE day = 28
AND year = 2023 
AND month = 7
AND duration < 60

SELECT * 
FROM atm_transactions at2
WHERE day = 28
AND year = 2023 
AND month = 7
AND atm_location = "Leggett Street" 
AND transaction_type = 'withdraw'

-- Filtered List of Exits from Bakery Parking Lot
SELECT *
FROM bakery_security_logs bsl
JOIN atm_transactions at2 ON bsl.day = at2.day AND bsl.year = at2.year AND bsl.month = at2.month
WHERE bsl.activity = 'exit'
AND bsl.hour = 10
AND bsl.minute BETWEEN 15 AND 25
AND at2.atm_location = 'Leggett Street';






