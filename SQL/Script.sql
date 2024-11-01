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


SELECT 
    ba.account_number, 
    ba.person_id, 
    ba.creation_year, 
    at2.id AS transaction_id, 
    at2.year, 
    at2.month, 
    at2.day, 
    at2.atm_location, 
    at2.transaction_type, 
    at2.amount,
    p.name, 
    p.phone_number, 
    p.passport_number, 
    p.license_plate,
    pc.id AS phone_call_id,
    pc.caller, 
    pc.receiver, 
    pc.duration,
    bsl.license_plate,
    p2.flight_id,
    p2.seat
FROM 
    bank_accounts ba
INNER JOIN 
    atm_transactions at2 ON ba.account_number = at2.account_number
INNER JOIN 
    people p ON ba.person_id = p.id
INNER JOIN 
    phone_calls pc ON (pc.caller = p.phone_number OR pc.receiver = p.phone_number)
INNER JOIN
	bakery_security_logs bsl ON (bsl.license_plate = p.license_plate)
INNER JOIN
	passengers p2 ON (p2.passport_number = p.passport_number)
WHERE 
    at2.day = 28
    AND at2.year = 2023 
    AND at2.month = 7
    AND at2.atm_location = 'Leggett Street' 
    AND at2.transaction_type = 'withdraw'
    AND pc.day = 28
    AND pc.year = 2023 
    AND pc.month = 7
    AND pc.duration < 60
	AND bsl.day = 28 
	AND bsl.year = 2023 
	AND bsl.month = 7
	AND bsl.hour = 10
	AND bsl.minute BETWEEN 15 AND 25
	AND p2.flight_id = 36;

SELECT * 
FROM people p
WHERE p.phone_number LIKE '%(375) 555-8161%'

