select * from people
INNER JOIN phone_calls on people.phone_number = phone_calls.caller
INNER join bakery_security_logs on bakery_security_logs.license_plate = people.license_plate
INNER JOIN passengers on passengers.passport_number = people.passport_number
INNER join bank_accounts on bank_accounts.person_id = people.id
INNER join atm_transactions on atm_transactions.account_number = bank_accounts.account_number
inner join flights on passengers.flight_id = flights.id
inner join airports on airports.id = flights.origin_airport_id
where phone_calls.day = 28 and phone_calls.month = 7
and phone_calls.duration < 60
and bakery_security_logs.activity like '%exit%'
and bakery_security_logs.month = 7 and bakery_security_logs.day = 28
and bakery_security_logs.hour = 10 and bakery_security_logs.minute BETWEEN 15 and 25
and atm_transactions.transaction_type like '%withdraw%' and atm_transactions.day = 28
and airports.full_name like '%fiftyville%' and flights.day = 29 and flights.hour < 12














