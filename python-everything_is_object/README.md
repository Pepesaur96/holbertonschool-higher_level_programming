GENERAL TOPICS:

## What is an object

In Python, an object is a fundamental concept. An object is a self-contained unit that contains both data (attributes) and behavior (methods). Everything in Python is an object, and objects are instances of classes. Objects are created based on a class blueprint, and each instance of an object can have unique data values while sharing the behavior defined by the class.

## What is the difference between a class and an object or instance

- A class is a blueprint or template for creating objects.
- An object (or instance) is a concrete realization of a class. Objects are created from a class and have specific data values associated with them.

## What is the difference between immutable object and mutable object

- An immutable object is an object whose state cannot be modified after it is created. Immutable objects include numbers (int, float), strings, and tuples.
- A mutable object is an object whose state can be modified after it is created. Mutable objects include lists, dictionaries, and sets.

## What is a reference

In Python, a reference is a value that points to an object in memory. When you create a variable and assign it a value, you're creating a reference to the object in memory, not directly working with the object itself.

## What is an assignment

Assignment in Python is the process of creating a reference (variable) and binding it to an object. It associates a variable with a specific value (object) in memory.

## What is an alias

An alias is a situation where two or more variables (references) point to the same object in memory. When you modify the object through one reference, the changes are visible through all aliases.

## How to know if two variables are identical

You can use the is operator to check if two variables refer to the same object:

    x is y  # Returns True if x and y are identical (refer to the same object)

## How to know if two variables are linked to the same object

You can use the id() function to get the memory address of an object and compare the memory addresses to check if two variables reference the same object:

    id(x) == id(y)  # Returns True if x and y reference the same object

## How to display the variable identifier (which is the memory address in the CPython implementation)

You can use the id() function to obtain the memory address of an object:

    print(id(x)) # Prints the memory address of the object referenced by x

## What is mutable and immutable

- Mutable objects can be modified after creation, and changes are reflected in the same object.
- Immutable objects cannot be modified after creation; any operation that appears to modify them actually creates a new object.

## What are the built-in mutable types

Some built-in mutable types in Python include lists, dictionaries, and sets.

## What are the built-in immutable types

Some built-in immutable types in Python include numbers (int, float), strings, tuples, and frozensets.

## How does Python pass variables to functions

In Python, variables are passed to functions by reference. When you pass a variable to a function, you're passing the reference (memory address) to the object that the variable is bound to. This means that changes made to the object inside the function are reflected outside the function as well, but reassigning the variable inside the function does not affect the original variable outside the function.

    def modify_list(my_list):
        my_list.append(4)  # Modifies the original list

    my_list = [1, 2, 3]
    modify_list(my_list)
    print(my_list)  # Output: [1, 2, 3, 4]

However, if you reassign the variable inside the function, it creates a new local reference, and the original variable outside the function is not affected:

    def reassign_variable(x):
        x = 42  # Creates a new local reference to 42

    my_var = 7
    reassign_variable(my_var)
    print(my_var)  # Output: 7
