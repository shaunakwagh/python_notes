# Chapter 1: The Python Data Model


- **Python Data Model**: A framework that defines how objects behave in Python. It consists of a set of special methods (also called “dunder” or “magic” methods) that allow objects to integrate seamlessly with Python’s built-in features like iteration, operator overloading, and attribute access.

Magic method is slang for Special Methods

"Dunder" is a shortcut for "double underscore before and after."


Special methods are meant to be called by the python interpreter, and not by you. 

The __repr__ special method is called by the repr built-in to get the string representation of the object fro inspection. Without the custom __repr__, Python's console would display Class instance <Class Example object at 0x10e100070>


__str__ is called by str() built_in and implicityl used by th epring function. It should return a string suitable for display to end users.


## A Pythonic Card Deck

This code demonstrates of implementing the two special methods, __getitem__ and __len__

![alt text](CardDeck.png)

## Vector class

This vector class implements special methods __repr__, __abs__, __add__, __mull__
 
![alt text](Vector.png)

## Special Methods
![alt text](Table1-2-1.png)
![alt text](Table1-2-2.png)
![alt text](Table1-2-3.png)

