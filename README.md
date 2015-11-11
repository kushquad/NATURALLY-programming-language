NATURALLY
----------

Compile with
"natural <file>.nat"
Statements end with '.'
Loops, conditional, function, structure block initial line starts with ','
Lines under them start with tabs.
Not case-sensitive
<var> = [a-z][0-9 a-z _]*

Data types
----------
// Built on Python data types, each a class
int
float
char
string
list
dictionary
set
boolean
complex

// Complex data types
set
queue
priority_queue
stack

Output
------

print <var>.
print value of <var>.
print elements of <var>. [Only if var is a complex data structure]

Input
-----

//This directly writes into the variable or data type
Read into a.
Take input into a.
Read <integer> elements into a.
Read into <integer>th element of a.
//These return a value or list
Get a.
Get <integer> elements.
Get <integer>th element of a.

Class and Operator Operations
-----------------------------

Type of a.
<firstterm> <function> <secondterm> a. a.function()
<firstterm> <function> <secondterm> a's elements. a.function() //Only valid for complex data structures.
<firstterm> <function> <secondterm> <argument list>
Value of <variable>'s <attribute> a.attribute
<firstterm> = Find |
<secondterm> = of |
<argument list> = <argument> | <argument> <last arg> | <argument>, <argument list>
<last arg> = and <argument>
<argument> = <variable> | <primitive>
