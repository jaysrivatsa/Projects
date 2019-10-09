# Market Basket Analysis
Market Basket Analysis is a modelling technique based upon the theory that if you buy a certain group of items, you are more (or less) likely to buy another group of items. It is a data mining technique that discovers co-occurrence relationships among activities performed by specific individuals or groups.
The data used in this project is linked in the data section of the project.
## Glossary
### 1. Antecedent
Anything that happens before. If a rule is A -> B then A is the antecedent.
### 2.Consequent 
Anything that happens after is know as Consequent. In a rule A -> B then B is the consequent.
### 3. Support 
The first measure called the support is the number of transactions that include items in the {A} and {B} parts of the rule as a  percentage of the total number of transactions.
   
support(A and B) = number(A and B)/ total number of observations
### 4. Confidence
Confidence is the number of time B has happened given A has happend.

Confidence(A -> B) = number(B)/number(A)

### 5. Lift
Lift adds further to the confidence. If the lift is greater than 1 it means that according to the data the rules are not happening by chance.

lift(A -> B) = support(A and B)/(support(A) * support(B)) 

## Apriori Algorithim
Steps invoved in apriori algorithim are as follows:
1. Calculate support and filter based on the minimum support value.
2. Add the rules filtered based on the support value to the frequent item list.
3. Calculate lift and confidence level, minimum threshold for lift should be gives as 1.
4. Filter values based on lift and confidence.
5. Review the rules and classify them as:
   * Actionable Rule
   * Trivial Rule
   * Inexplainable Rule
