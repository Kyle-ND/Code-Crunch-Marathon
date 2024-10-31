```
Query 1:
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

```
Query 2:
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

``` 
Query 3:
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

``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ``` ``` Query : ``` SELECT *

```bash ```