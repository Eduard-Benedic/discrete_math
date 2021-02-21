# Basic Structures: Sets, Functions, Sequences and Matrices

## Sets
*Def* - A set is an unordered collection of objects, called elements or members of the set. A set is said to contain its elements.
a ∈ A - a belongs to the set A
a ∈ (diagonally crossed) - a does not belong to A

Ways to list all the members of a set
**Roster method** - V = {a,e,i,o,u}
N = {1,2,3,...,99}

**Set Builder**
O = { x | x is an odd positive integer less than 10 }
O = {x ∈ Z+ | x is odd and x < 10 }

Q+ = {x ∈ R | x = p / q , for some positive integers p and q}

N = {0, 1, 2, 3, 4, ...} - the set of **natural numbers**
Z = {..., -2, -1, 0, 1, 2, ...} - the set of **integers**
Z+ = {1, 2, 3, ...} - the set of **positive integers**
Q = { p/q | p ∈ Z, q ∈ Z, and q =(crossed) 0   } - the set of **rational numbers**
R, the set of real numbers
R+, the set of positive real numbers
C, the set of complex numbers.

### Definition 2
Two sets are equal if and only if they have the same elements.
If A & B are sets they are equal iff ∀x(x ∈ A ↔ x ∈ B). Write A = B if A and B are equal sets. 

## The Empty Set - denoted ∅ or {}
Set that has no elements
A set with 1 element is called a **singleton set**  denoted  {∅} 
Don't confuse the two

## Subsets
A,B - sets
If all elements of A are in B we say that A is a subset of set B
A ⊆ B
∀x(x ∈ A → x ∈ B)

## Power of sets
P({0, 1, 2}) = {∅,{0},{1},{2},{0, 1},{0, 2},{1, 2},{0, 1, 2}}
2 ^ n
P({∅}) = {∅,{∅}}

## Cartesian Product
The order of elements in a collection is often important. Because sets are unordered a different structure is needed to represent ordered collections. This is provided by **ordered n-tuples**.

### Cartesian product of two sets
A, B - sets
A and B, denoted A X B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B