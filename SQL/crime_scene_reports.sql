SELECT * 
FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND year = 2023
AND street = 'Humphrey Street'
AND description LIKE '%CS50%';

SELECT * FROM interviews 
WHERE day = 28
AND month = 7
AND year = 2023
And transcript LIKE '%bakery%';

SELECT * FROM bakery_security_logs 
WHERE year = 2023
AND day = 28
AND month = 7
AND activity = 'exit'
AND hour LIKE '10'
AND minute BETWEEN 15 AND 25;

SELECT * FROM phone_calls
WHERE year = 2023
AND day = 28
AND month = 7
AND duration < 60;
(
    SELECT * FROM people 
    EXCEPT 
    SELECT * FROM bakery_security_logs
)   INTERSECT (
    SELECT * FROM people 
    EXCEPT
    SELECT * FROM bakery_security_logs
);

SELECT * from atm_transactions
WHERE year = 2023
AND day = 28
AND month = 7
AND transaction_type LIKE '%withdraw%'
AND atm_location LIKE 'leggett Street';

 
SELECT * FROM airports
WHERE city LIKE '%Fiftyville';

SELECT * FROM flights
WHERE year = 2023
AND day = 29
AND month = 7
AND origin_airport_id = 8
AND hour BETWEEN 8 AND 12;

SELECT * FROM passengers 
WHERE flight_id = 8
AND passport_number










