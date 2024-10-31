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
AND "minute" BETWEEN 15 AND 25;

SELECT id
FROM airports a 
WHERE city = 'Fiftyville';

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
AND duration < 60;

SELECT * 
FROM atm_transactions at2
WHERE day = 28
AND year = 2023 
AND month = 7
AND atm_location = "Leggett Street" 
AND transaction_type = 'withdraw';

WITH Withdrawals AS (
    SELECT ba.account_number, ba.person_id, ba.creation_year, at2.id, at2.year, at2.month, at2.day, 
           at2.atm_location, at2.transaction_type, at2.amount
    FROM bank_accounts ba
    JOIN atm_transactions at2 ON ba.account_number = at2.account_number
    WHERE at2.day = 28
    AND at2.year = 2023 
    AND at2.month = 7
    AND at2.atm_location = 'Leggett Street' 
    AND at2.transaction_type = 'withdraw'
)

SELECT w.*, p.name, p.phone_number, p.passport_number, p.license_plate
FROM Withdrawals w
JOIN people p ON w.person_id = p.id;



