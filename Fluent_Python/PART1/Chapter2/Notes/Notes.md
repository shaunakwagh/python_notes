# Chapter 2 - An Array of Sequences 


A container sequence hold reference to the objects it contains, which may be of any type, while a flat sequence stores the value of it contents in it own memory space, not as distinct Python Objects.

![alt text](Figure2-1.png)




Tuples are not just Immutable lists. Tuples do double duty: they can be used as immutavle lists and also as records with no field names. This use is sometime overlooked. 

You can see Tuple used as Record.

![alt text](TupleRecord.png)




The Python interpreter and standard library make extensive use of tuples as immuta‐
ble lists, and so should you. This brings two key benefits:

Clarity:

When you see a tuple in code, you know its length will never change.

Performance:

A tuple uses less memory than a list of the same length, and it allows Python to do some optimizations.


# Comparing Tuple and List Methods

![alt text](Table2-1-1.png)
![alt text](Table2-1-2.png)



# Using * to grab excess items


a,b *rest = range(5)

this will print out 

 a, b, rest

(0,1,[2,3,4])

# Nested Upacking

You can do nested upacking as long has it has the same structure

You can see the the Nested Unpacking code.

# Slice Objects
S[a:b:c] can be used to specify a stride or step c, causing the resulting slice to skip items. The stride allso be negative, returning the items in reverse


'''python
s='bicycle'

s[::3]

'bye'

s[::-1]

'elcycib'

 s[::-2]

'eccb'


'''