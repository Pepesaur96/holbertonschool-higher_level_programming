GENERAL TOPICS:

## What is OOP

- OOP is a programming paradigm that organizes data and behavior into reusable structures called "objects." Objects are instances of classes and encapsulate data (attributes) and the functions (methods) that operate on that data. OOP promotes concepts like abstraction, encapsulation, inheritance, and polymorphism.

## “first-class everything”

- This phrase reflects the idea that in some programming languages, including Python, everything, including functions and classes, is treated as an object and can be manipulated, passed as arguments, and returned as values like any other data.

## What is a class

- A class is a blueprint for creating objects. It defines the data and behavior of a type of object. Classes are created using the class keyword and an indented block, which contains class methods (functions).

## What is an object and an instance

- An object is an instance of a class.
- An instance is a specific realization or occurrence of an object based on a class.

## What is the difference between a class and an object or instance

- A class is a blueprint or template, while an object/instance is a concrete realization of that blueprint.

## What is an attribute

- An attribute is a variable that is associated with a class or an instance of a class. Attributes define the characteristics of the object.

## What are and how to use public, protected and private attributes

- Public attributes are accessible from anywhere in the code. They have no special notation.
- Protected attributes are indicated by a single leading underscore (e.g., \_variable). They are considered non-public, but it's a naming convention, not enforced access control.
- Private attributes are indicated by double leading underscores (e.g., \_\_variable). They are considered private and name-mangled to avoid conflicts.

## What is self

- 'self' is a reference to the instance of the class. It's used within methods to access instance attributes and call other methods. It is the first parameter of instance methods in Python.

## What is a method

- A method is a function defined inside a class, which is used to perform operations on attributes or to provide functionality associated with the class.

## What is the special \_\_init\_\_ method and how to use it

- The **init** method is a special method (constructor) in Python classes. It is called when an object is created from the class and is used to initialize object attributes.

## What is Data Abstraction, Data Encapsulation, and Information Hiding

- Data Abstraction: It is the concept of hiding complex implementation details and showing only the necessary features of an object.
- Data Encapsulation: It bundles the data (attributes) and methods (functions) that operate on the data into a single unit (a class).
- Information Hiding: It restricts direct access to some details of an object to prevent unintended misuse.

## What is a property

- A property is a special kind of attribute that is accessed like an attribute but is implemented using methods (getter and setter methods). Properties allow for controlled access and modification of an object's data.

## What is the difference between an attribute and a property in Python

- An attribute is a simple variable associated with an object, while a property is a special kind of attribute that is implemented using methods. Properties allow for control over how data is accessed and modified.

## What is the Pythonic way to write getters and setters in Python

- Pythonic getter and setter methods are typically defined using the @property decorator for the getter and the @<attribute>.setter decorator for the setter.

## How to dynamically create arbitrary new attributes for existing instances of a class

- You can add new attributes to an existing instance by simply assigning a value to a new attribute name.

  obj = MyClass()
  obj.new_attribute = 42 # Adding a new attribute

## How to bind attributes to object and classes

- Attributes can be bound to both class and instance objects. Class attributes are shared among all instances, while instance attributes are specific to an instance.

## What is the **dict** of a class and/or instance of a class and what does it contain

- **dict** is a dictionary that stores the attributes of a class or instance. It contains attribute names as keys and their corresponding values.

## How does Python find the attributes of an object or class

- Python looks for attributes first in the instance's **dict**, then in the class's **dict**, and finally in the parent classes' **dict**. If not found in any of these dictionaries, it raises an AttributeError.

## How to use the getattr function

- The 'getattr' function is used to access an attribute of an object or class dynamically. It takes the object or class and the attribute name as arguments.

  value = getattr(obj, 'attribute_name', default_value)

If the attribute exists, it returns its value. If not, it returns the default value or raises an AttributeError if no default is provided.
