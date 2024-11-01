# CS50 Duck Game

## Problem Statement

**The CS50 Duck has been stolen!** The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:

- **Who the thief is**
- **What city the thief escaped to**
- **Who the thief’s accomplice is**

### Known Information

- The theft took place on **July 28, 2023**.
- The crime occurred on **Humphrey Street**.

## How to Solve the Mystery

The Fiftyville authorities have provided a SQLite database, `fiftyville.db`, containing records from the town around the time of the theft. You will need to query the database using **SQL SELECT queries** to find the data necessary to solve the case.

## SQL Queries and Findings

Here’s a breakdown of each query and its findings:

1. **Crime Scene Report (Query 1)**:

   - This query looks for reports containing the "CS50 duck" keyword and provides details on the theft, which happened at Humphrey Street bakery at 10:15 am.

2. **Interviews (Query 2)**:

   - Collects interviews mentioning the bakery from the same day. Notable witness details include:
     - Ruth saw the thief drive away.
     - Eugene recognized the thief and previously saw them at an ATM on Leggett Street.
     - Raymond overheard a conversation where the thief mentioned taking an early flight from Fiftyville the next day.

3. **Bakery Security Logs (Query 3)**:

   - Retrieves security records from 10:15 to 10:25 am on July 28, showing cars exiting with specific license plates. These plates might link to potential suspects or witnesses.

4. **Airport ID (Query 4)**:

   - Retrieves the airport ID for Fiftyville, used in later queries to find flight details.

5. **Flights from Fiftyville (Query 5)**:

   - Lists flights departing from Fiftyville on July 29, with the earliest flight at 8:20 am, aligning with the thief’s plan.

6. **Phone Calls (Query 6)**:

   - Collects calls on July 28 under 60 seconds, possibly identifying relevant short calls, including the one overheard by Raymond.

7. **ATM Transactions (Query 7)**:

   - Finds ATM withdrawals on Leggett Street, where Eugene spotted the thief. The results include account numbers and transaction amounts.

8. **Withdrawing Individuals' Details (Query 8)**:

   - Expands on Query 7 by joining people’s details to ATM withdrawals. Individuals making transactions on Leggett Street include Bruce, Diana, and others, with their personal information.

9. **Comprehensive Cross-Referenced Data (Query 9)**:

   - This complex query attempts to correlate several pieces of evidence, including ATM transactions, phone calls, bakery security logs, and flight bookings. It links individuals withdrawing from the ATM with matching license plates in security logs and phone call activity, enhancing the connections between ATM users, security footage, and flight plans.

10. **Thief Identification (Query 10)**:

- This query aims to extract detailed information about individuals whose phone number includes the substring `"(375) 555-8161"`. It focuses on identifying specific entries in the `people` table based on the phone number criteria.

### Conclusions

Based on the gathered evidence:

- **Thief**: Bruce
- **Accomplice**: Robin
- **City flown to**: New York

## Running the Game

1. Ensure you have Python and SQLite installed on your machine.
2. Download the `fiftyville.db` database.
3. Run the provided SQL queries against the database to uncover the mystery.
4. Analyze the results to identify the thief, the escape city, and the accomplice.

## Acknowledgments

- This project was inspired by the CS50 course at Harvard University.
- Thanks to the Fiftyville authorities for the provided database and information.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
