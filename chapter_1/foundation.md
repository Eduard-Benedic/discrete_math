
# Propositional Logic

## Propositions
Propositions - building block of logic, a declarative sentence

Proposition - is either True or False

Proposition variables
eg. x + 1 = 3;
x - propositional variable | statement variable

The **Truth Value** of a proposition is true, T it the proposition is true
else false denoted F
**Propositional calculus || logic** - area of logic that deals with props.



## Compound propositions - propositions formed from existing propositions using logical operators
*Definition* - **let p be a proposition, the negation of p is denoted ¬p**


## Connectives - operators that form new proposition from existing ones
### Conjunction p ∧ q** 
*Def* - it is the equivalent of the && operator. The conjuction is true when both truth values of the p, q propositions are true.

### Disjunction - p ∨ q -  eq to *or* operator
*Def* - the disjunction p ∨ q is false when both values are false and true otherwise.
Disjunction can be of 2 types:
1. Inclusive
2. Exclusive - p ⊕ q - if both values have the same truth value the result is false.


## Conditional Statements (Implication) (another way in which propositions can be combined)
*Def* - The conditional statement p → q is the prop "if p, then q".
In p → q, **p - hypothesis** and **q - conclusion or consequence**.

## Converse, Contrapositive and Inverse
q -> p (**converse** of p->q)
¬q → ¬p  (**contrapositive**)
¬p → ¬q (**inverse**)

When two compund propositions have the same value I call them **equivalently** so that a conditional statement and its contrapositive are **equivalent**


## Biconditinals statement  p ↔ q
Is the proposition "p if and only if q"
The biconditional statement is true when p and q have the same truth values, and is false otherwiser.
Are also called **bi-implications**
T - T = T
F - F = T
T - F = F
F - T = F


So far I have 4 important logical connectives:
1. Conjunctions
2. Disjunctions - explicit and implicit
3. Conditional statements
4. Biconditional statements
 as well as negations
and Negations

## Precedence of Logical Operators
TABLE 8 
Precedence of Logical Operators.
    Operator     Precedence
    ¬            1
    ∧            2
    ∨            3
    →            4
    ↔            5


## Application of Propositional Logic

### Logical Circuits (digital circuits)




## Propositional Equivalences

### Introduction
Methods that produce propositions with the same truth value

**Tautology** - A compound proposition that is always true no matter what the truth values of the propositional variables that occur in it
tauto - same
logos - logic
p ∨ ¬p - example of tautology. No matter what the truth values are it is also true.

## Contradiction  - compound proposition that is always false
p ∧ ¬p - always false => it is a contradiction

## Contingency - a proposition that is neither Tautology or Contradiction

### Logical Equivalences
Compound propositionts that have the same truth values in all possible cases are called **logically equivalent**.
The compound propositions p and q are called logically equivalent if p ↔ q is a tautology.
The notation p ≡ q denotes that p and q are logically equivalent.

**De Morgan Laws**

CHECK PAGE 27 for the full table


## Predicates and Quantifiers.

### Predicates

"The number is greater than 10"
The number - subject
is greater than 10 - predicate
The predicate refers to a property that the subject can possess.

P(x) - propositional function P at x.
Once x is assigned P(x) becomes a statement.

### Quantifiers
When the variables in a propositional function are assigned values the resulting statement becomes a proposition with a certain value. However, there is another way to accomplish this called **quantification**

Quantification
1. Universal - ∀xP(x) (∀ - universal quantifier)

2. Existential - ∃xP (x)(∃ - existential quantifier)

### Binding Variables
When a quantifier is used on the variable x it means that this occurence of the variable is bound.
An occurence of a variable that is not bound by a quantifier or set equal to a paricular value is said to be **free**.

All the variables that occur in a **propositional function** must be bound or set equal to a particular value to turn it into a **proposition**.

