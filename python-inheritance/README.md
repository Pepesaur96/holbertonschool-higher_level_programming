GENERAL TOPICS:

## What is a superclass, baseclass or parentclass

A superclass, base class, or parent class is a class from which other classes (subclasses) inherit properties and behaviors. It serves as a blueprint or template for the subclasses. Superclasses define common attributes and methods that are shared among subclasses.

## What is a subclass

A subclass is a class that inherits attributes and methods from a superclass or base class. It can add its own attributes and methods or override and extend the ones inherited from the superclass.

## How to list all attributes and methods of a class or instance

You can use the dir() function to list all attributes and methods of a class or instance:

    class MyClass:
        def my_method(self):
            pass

    my_instance = MyClass()

    # List attributes and methods of the class
    print(dir(MyClass))

    # List attributes and methods of the instance
    print(dir(my_instance))

## When can an instance have new attributes

An instance can have new attributes added to it at any time by simply assigning a value to a new attribute name. For example:

    my_instance.new_attribute = "new value"

## How to inherit class from another

To inherit a class from another in Python, define the subclass with the superclass inside parentheses in the class declaration. You'll also need to call the superclass's **init** method in the subclass's **init** method using super() if you want to retain the superclass's behavior.

    class Superclass:
        def __init__(self, x):
            self.x = x

    class Subclass(Superclass):
        def __init__(self, x, y):
            super().__init__(x)
            self.y = y

## How to define a class with multiple base classes

To define a class with multiple base classes, list all the base classes inside parentheses in the class declaration, separated by commas:

    class BaseClass1:
        pass

    class BaseClass2:
        pass

    class Subclass(BaseClass1, BaseClass2):
        pass

## What is the default class every class inherit from

The default class that every class in Python inherits from is called object. If a class is defined without explicitly specifying a superclass, it implicitly inherits from object.

## How to override a method or attribute inherited from the base class

To override a method or attribute inherited from a base class, define the same method or attribute in the subclass with the desired behavior. The subclass's method or attribute will be used instead of the one in the superclass.

    class Superclass:
        def my_method(self):
            print("Superclass method")

    class Subclass(Superclass):
        def my_method(self):
            print("Subclass method")

    obj = Subclass()
    obj.my_method()  # Output: "Subclass method"

## Which attributes or methods are available by heritage to subclasses

Subclasses inherit all attributes and methods (including public, protected, and private) from their superclass unless they are explicitly overridden. Subclasses can access and use the inherited attributes and methods.

## What is the purpose of inheritance

The primary purposes of inheritance are to:

- Promote code reuse and avoid redundancy.
- Establish a relationship between classes, representing an "is-a" relationship (e.g., a "Car" is-a "Vehicle").
- Enable the extension and modification of existing classes to create new classes with similar functionality.

## What are, when and how to use isinstance, issubclass, type and super built-in functions

- isinstance(obj, class_or_tuple): Checks if an object is an instance of a specified class or a tuple of classes.
- issubclass(class, classinfo): Checks if a class is a subclass of a specified class or a tuple of classes.
- type(obj): Returns the type (class) of an object.
- super(): Returns a temporary object of the superclass, which allows you to call its methods and access its attributes. It's often used in the context of method overriding.
