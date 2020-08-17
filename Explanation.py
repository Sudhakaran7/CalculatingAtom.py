You are given a chemical formula (given as a string), return the count of each atom.
An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1,
no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), 
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Input Description:
A string S is given as input.

Output Description:
Print the count of all elements as a string for the given formula.

Sample Input:
Mg(OH)2

Sample Output:
H2MgO2

Explanation:
The given string Mg(OH)2, the atom are, H2, Mg, O2.

Sample Input:
H2O

Sample Output:
H2O

Sample Input:
K4(ON(SO3)2)2

Sample Output:
K4N2O14S4

Sample INput:
C6H12O6

Sample Output:
C6H12O6

Sample Input:
CH3OCH3

Sample Output:
C2H6O

Sample Input:
(CH3)3CH

Sample Output:
C4H10

Sample Input:
CH3(CH2)50CH3

Sample Output:
C52H106
