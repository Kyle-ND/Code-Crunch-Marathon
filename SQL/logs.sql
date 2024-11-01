``` markdown
Crime Scene Report (Query 1): Looks for reports containing the "CS50 duck" keyword and provides details on the theft, which happened at Humphrey Street bakery at 10:15 am.
```
SELECT *
FROM crime_scene_reports csr
WHERE
    day = 28
    AND year = 2023
    AND month = 7
    AND description LIKE '%CS50 duck%';

```bash
id |year|month|day|street         |description                                                                                                                                                                                                             |
---+----+-----+---+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
295|2023|    7| 28|Humphrey Street|Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.|
```

``` markdown
Interviews (Query 2): Collects interviews mentioning the bakery from the same day. Notable witness details include:

Ruth saw the thief drive away.
Eugene recognized the thief and previously saw them at an ATM on Leggett Street.
Raymond overheard a conversation where the thief mentioned taking an early flight from Fiftyville the next day.
```
SELECT *
FROM interviews i
WHERE
    day = 28
    AND year = 2023
    AND month = 7
    AND transcript LIKE '%bakery%'

```bash
id |name   |year|month|day|transcript                                                                                                                                                                                                                                                     |
---+-------+----+-----+---+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
161|Ruth   |2023|    7| 28|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.     |
162|Eugene |2023|    7| 28|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                            |
163|Raymond|2023|    7| 28|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the o|
```

``` markdown
Bakery Security Logs (Query 3): Retrieves security records from 10:15 to 10:25 am on July 28, showing cars exiting with specific license plates. These plates might link to potential suspects or witnesses.
```
SELECT *
FROM bakery_security_logs bsl
WHERE
    day = 28
    AND year = 2023
    AND month = 7
    AND "hour" = 10
    AND "minute" BETWEEN 15 AND 25

```bash
id |year|month|day|hour|minute|activity|license_plate|
---+----+-----+---+----+------+--------+-------------+
260|2023|    7| 28|  10|    16|exit    |5P2BI95      |
261|2023|    7| 28|  10|    18|exit    |94KL13X      |
262|2023|    7| 28|  10|    18|exit    |6P58WS2      |
263|2023|    7| 28|  10|    19|exit    |4328GD8      |
264|2023|    7| 28|  10|    20|exit    |G412CB7      |
265|2023|    7| 28|  10|    21|exit    |L93JTIZ      |
266|2023|    7| 28|  10|    23|exit    |322W7JE      |
267|2023|    7| 28|  10|    23|exit    |0NTHK55      |
```

``` markdown
Airport ID (Query 4): Retrieves the airport ID for Fiftyville, used in later queries to find flight details.
```

SELECT id FROM airports a WHERE city = 'Fiftyville'

```bash id| --+ 8| ```

``` markdown
Flights from Fiftyville (Query 5): Lists flights departing from Fiftyville on July 29, with the earliest flight at 8:20 am, aligning with the thief’s plan.
```

SELECT *
FROM flights f
WHERE
    day = 29
    AND year = 2023
    AND month = 7
    AND origin_airport_id
ORDER BY hour ASC, minute ASC;

```bash 
id|origin_airport_id|destination_airport_id|year|month|day|hour|minute|
--+-----------------+----------------------+----+-----+---+----+------+
36|                8|                     4|2023|    7| 29|   8|    20|
43|                8|                     1|2023|    7| 29|   9|    30|
23|                8|                    11|2023|    7| 29|  12|    15|
53|                8|                     9|2023|    7| 29|  15|    20|
18|                8|                     6|2023|    7| 29|  16|     0|
```

``` markdown
Phone Calls (Query 6): Collects calls on July 28 under 60 seconds, possibly identifying relevant short calls, including the one overheard by Raymond.
```
SELECT *
FROM phone_calls pc
WHERE
    day = 28
    AND year = 2023
    AND month = 7
    AND duration < 60

```bash 
id |caller        |receiver      |year|month|day|duration|
---+--------------+--------------+----+-----+---+--------+
221|(130) 555-0289|(996) 555-8899|2023|    7| 28|      51|
224|(499) 555-9472|(892) 555-8872|2023|    7| 28|      36|
233|(367) 555-5533|(375) 555-8161|2023|    7| 28|      45|
251|(499) 555-9472|(717) 555-1342|2023|    7| 28|      50|
254|(286) 555-6063|(676) 555-6554|2023|    7| 28|      43|
255|(770) 555-1861|(725) 555-3243|2023|    7| 28|      49|
261|(031) 555-6622|(910) 555-3251|2023|    7| 28|      38|
279|(826) 555-1652|(066) 555-9701|2023|    7| 28|      55|
281|(338) 555-6650|(704) 555-2131|2023|    7| 28|      54|
```

``` markdown
ATM Transactions (Query 7): Finds ATM withdrawals on Leggett Street, where Eugene spotted the thief. The results include account numbers and transaction amounts.
```
SELECT *
FROM atm_transactions at2
WHERE
    day = 28
    AND year = 2023
    AND month = 7
    AND atm_location = "Leggett Street"
    AND transaction_type = 'withdraw'

```bash
id |account_number|year|month|day|atm_location  |transaction_type|amount|
---+--------------+----+-----+---+--------------+----------------+------+
246|      28500762|2023|    7| 28|Leggett Street|withdraw        |    48|
264|      28296815|2023|    7| 28|Leggett Street|withdraw        |    20|
266|      76054385|2023|    7| 28|Leggett Street|withdraw        |    60|
267|      49610011|2023|    7| 28|Leggett Street|withdraw        |    50|
269|      16153065|2023|    7| 28|Leggett Street|withdraw        |    80|
288|      25506511|2023|    7| 28|Leggett Street|withdraw        |    20|
313|      81061156|2023|    7| 28|Leggett Street|withdraw        |    30|
336|      26013199|2023|    7| 28|Leggett Street|withdraw        |    35|
 ``` ``` markdown
Withdrawing Individuals' Details (Query 8): Expands on Query 7 by joining people’s details to ATM withdrawals. Individuals making transactions on Leggett Street include Bruce, Diana, and others, with their personal information.
```
WITH
    Withdrawals AS (
        SELECT ba.account_number, ba.person_id, ba.creation_year, at2.id, at2.year, at2.month, at2.day, at2.atm_location, at2.transaction_type, at2.amount
        FROM
            bank_accounts ba
            JOIN atm_transactions at2 ON ba.account_number = at2.account_number
        WHERE
            at2.day = 28
            AND at2.year = 2023
            AND at2.month = 7
            AND at2.atm_location = 'Leggett Street'
            AND at2.transaction_type = 'withdraw'
    )

SELECT w.*, p.name, p.phone_number, p.passport_number, p.license_plate
FROM Withdrawals w
    JOIN people p ON w.person_id = p.id;

```bash
account_number|person_id|creation_year|id |year|month|day|atm_location  |transaction_type|amount|name   |phone_number  |passport_number|license_plate|
--------------+---------+-------------+---+----+-----+---+--------------+----------------+------+-------+--------------+---------------+-------------+
      49610011|   686048|         2010|267|2023|    7| 28|Leggett Street|withdraw        |    50|Bruce  |(367) 555-5533|     5773159633|94KL13X      |
      26013199|   514354|         2012|336|2023|    7| 28|Leggett Street|withdraw        |    35|Diana  |(770) 555-1861|     3592750733|322W7JE      |
      16153065|   458378|         2012|269|2023|    7| 28|Leggett Street|withdraw        |    80|Brooke |(122) 555-4581|     4408372428|QX4YZN3      |
      28296815|   395717|         2014|264|2023|    7| 28|Leggett Street|withdraw        |    20|Kenny  |(826) 555-1652|     9878712108|30G67EN      |
      25506511|   396669|         2014|288|2023|    7| 28|Leggett Street|withdraw        |    20|Iman   |(829) 555-5269|     7049073643|L93JTIZ      |
      28500762|   467400|         2014|246|2023|    7| 28|Leggett Street|withdraw        |    48|Luca   |(389) 555-5198|     8496433585|4328GD8      |
      76054385|   449774|         2015|266|2023|    7| 28|Leggett Street|withdraw        |    60|Taylor |(286) 555-6063|     1988161715|1106N58      |
      81061156|   438727|         2018|313|2023|    7| 28|Leggett Street|withdraw        |    30|Benista|(338) 555-6650|     9586786673|8X428L0      |
```

``` markdown
Comprehensive Cross-Referenced Data (Query 9): This complex query attempts to correlate several pieces of evidence, including ATM transactions, phone calls, bakery security logs, and flight bookings. It links individuals withdrawing from the ATM with matching license plates in security logs and phone call activity, enhancing the connections between ATM users, security footage, and flight plans.
```
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
    INNER JOIN atm_transactions at2 ON ba.account_number = at2.account_number
    INNER JOIN people p ON ba.person_id = p.id
    INNER JOIN phone_calls pc ON (
        pc.caller = p.phone_number
        OR pc.receiver = p.phone_number
    )
    INNER JOIN bakery_security_logs bsl ON (
        bsl.license_plate = p.license_plate
    )
    INNER JOIN passengers p2 ON (
        p2.passport_number = p.passport_number
    )
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

```bash 
account_number|person_id|creation_year|transaction_id|year|month|day|atm_location  |transaction_type|amount|name |phone_number  |passport_number|license_plate|phone_call_id|caller        |receiver      |duration|license_plate|flight_id|sea
--------------+---------+-------------+--------------+----+-----+---+--------------+----------------+------+-----+--------------+---------------+-------------+-------------+--------------+--------------+--------+-------------+---------+---
      49610011|   686048|         2010|           267|2023|    7| 28|Leggett Street|withdraw        |    50|Bruce|(367) 555-5533|     5773159633|94KL13X      |          233|(367) 555-5533|(375) 555-8161|      45|94KL13X      |       36|4A 
```

``` markdown
Comprehensive Cross-Referenced Data (Query 10): This query aims to extract detailed information about individuals whose phone number includes the substring ` "(375) 555-8161" `. It focuses on identifying specific entries in the ` people ` table based on the phone number criteria.
```
SELECT *
FROM people p
WHERE
    p.phone_number LIKE '%(375) 555-8161%'

```bash 
id    |name |phone_number  |passport_number|license_plate|
------+-----+--------------+---------------+-------------+
864400|Robin|(375) 555-8161|               |4V16VO0      |
```

``` markdown
Based on the gathered evidence:


- **Thief**: Bruce
- **Accomplice**: Robin
- **City flown to**: New York
```