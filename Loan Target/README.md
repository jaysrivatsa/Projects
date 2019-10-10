# Loan Target
The main aim of this project is to idetify the customers who were previously not given loans and build a model to identify customers who are likely to repay the loan.

The data set is provided in the data section of the project.

## Understanding the data
1. ***Loan_id*** - It is a unique identification number for each customer.
***Ctegorical Columns***
1. ***is_first_loan*** - This column describes if it is the first loan the customer has ever applied for.
2. ***fully_paid*** - This column tells us if the customer has fully paid his previous debts.
3. ***currently_repaying_other_loans*** - If the customer is currently replaying any loans.
4. ***is_employed*** - Gives us the employment status of the customer.
5. ***loan_purpose*** - Tells us about why the customer is seeking loan.
6. ***loan_granted*** - If the loan has been granted or not.

***Numeric Columns***

1.***total_credit_card_limit*** - Total credit limit of the Customer.

2.***avg_percentage_credit_card_limit_used_last_year*** - Percentage of credit limit used last year

3.***saving_amount	checking_amount*** - Bank balance in the customer's savings account.

4.***age*** - Age of the customer.

5.***dependent_number*** - Number of dependents on the customer.


In this project ***Decision Tree Algoritmim*** was used to classify if the customer will repay the loan or not.
The motive of using Decision Tree is to create a training model which can use to predict class or value of target variables by learning decision rules inferred from prior data(training data).

