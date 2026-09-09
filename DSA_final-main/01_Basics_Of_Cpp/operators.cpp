📘 Operators in C++
🔹 What is an Operator?
An operator is a symbol that performs an operation on one or more operands (values or variables).

a + b   // '+' is an operator
1️⃣ Assignment Operators
Assignment operators are used to assign or update values of variables.

🔹 List of Assignment Operators in C++
Operator	Description	Example	Equivalent
=	Assign	a = 5	a = 5
+=	Add & assign	a += 2	a = a + 2
-=	Subtract & assign	a -= 2	a = a - 2
*=	Multiply & assign	a *= 2	a = a * 2
/=	Divide & assign	a /= 2	a = a / 2
%=	Modulus & assign	a %= 2	a = a % 2
⚠️ Important Correction
**= and //= ❌ are NOT valid in C++ (they belong to Python).

Example:
int a = 7;
int b = a;

cout << b << endl;   // 7

a += 2;
cout << a << endl;   // 9
2️⃣ Arithmetic Operators
Arithmetic operators are used for mathematical calculations.

🔹 Types of Arithmetic Operators
(A) Binary Arithmetic Operators (Two Operands)
Operator	Operation
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus (Remainder)
Example:
int a = 5, b = 2;

cout << a + b << endl; // 7
cout << a - b << endl; // 3
cout << a * b << endl; // 10
cout << a / b << endl; // 2
cout << a % b << endl; // 1
📌 Notes:

/ gives quotient

% gives remainder

% works only with integers

(B) Unary Arithmetic Operators (One Operand)
Operator	Meaning
++	Increment
--	Decrement
🔹 Pre-Increment vs Post-Increment
Operator	Behavior
++a	Increment first, then use
a++	Use first, then increment
Example:
int c = 7;

cout << ++c << endl; // 8
cout << c++ << endl; // 8 (now c = 9)
cout << c-- << endl; // 9 (now c = 8)
cout << --c << endl; // 7
🔹 Tricky Interview Example
int d = 7;
int e = d++;
✔️ e = 7, d = 8

int d = 7;
int e = ++d;
✔️ e = 8, d = 8

📌 Very commonly asked

3️⃣ Relational Operators
Relational operators are used to compare two values.

They always return:

true (1)

false (0)

🔹 List of Relational Operators
Operator	Meaning
==	Equal to
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
Example:
int a = 4, b = 6;

cout << (a == b) << endl; // 0
cout << (a != b) << endl; // 1
cout << (a > b) << endl;  // 0
cout << (a < b) << endl;  // 1
cout << (a >= b) << endl; // 0
cout << (a <= b) << endl; // 1
4️⃣ Logical Operators
Logical operators are used to combine conditions.

🔹 Logical Operators List
Operator	Name
&&	Logical AND
`	
!	Logical NOT
🔹 Truth Tables
AND (&&)
A	B	Result
0	0	0
1	0	0
1	1	1
OR (||)
A	B	Result
0	0	0
1	0	1
1	1	1
NOT (!)
A	Result
1	0
0	1
Example:
cout << false && false << endl; // 0
cout << true && false << endl;  // 0
cout << true && true << endl;   // 1

cout << false || false << endl; // 0
cout << true || false << endl;  // 1
cout << true || true << endl;   // 1

cout << !true << endl;  // 0
cout << !false << endl; // 1
🔹 Logical Operators with Integers
int a = 33, b = 44;

cout << a && b << endl; // 1
cout << a || b << endl; // 1
cout << !a << endl;     // 0
cout << !b << endl;     // 0
📌 Rule:

0 → false
non-zero → true
🔹 Short-Circuit Evaluation (VERY IMPORTANT)
false && function(); // function NOT executed
true || function();  // function NOT executed
✔️ Improves performance
✔️ Prevents runtime errors
✔️ Frequently asked in interviews

🔹 Operator Precedence (Students Forget)
int x = 5 + 2 * 3;
✔️ Result = 11

📌 * has higher precedence than +

🔹 Common Student Mistakes
❌ Using = instead of ==
❌ Expecting % to work with floats
❌ Forgetting integer division
❌ Confusing ++a and a++
❌ Ignoring operator precedence

🔹 Frequently Asked Interview Questions
Q1. Difference between = and ==?
= assigns value

== compares value

Q2. Output of:
cout << 10 / 3;
✔️ 3

Q3. Can modulus work with float?
❌ No

Q4. Output:
cout << 5 && 0;
✔️ 0

Q5. What is short-circuit evaluation?
✔️ Expression stops once result is known

🔹 Final Summary
Assignment operators update values

Arithmetic operators perform math

Unary operators change a single operand

Relational operators compare values

Logical operators combine conditions

0 means false, non-zero means true

Operator precedence affects results