# Creational Patterns

* We use creational design patterns to systematically build objects.
* The main benefit of creational patterns is their flexibility.
* For example, different types of objects from the same class can be created at runtime using creational patterns.
* Polymorphism is often used in creational patterns.

***

### [Factory](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns/01-factory)
A Factory encapsulates object creation. It is an object specializing in creating other objects.
A Factory solves the following problems:

* When it's uncertain what type of objects will be used at runtime.
* When the application needs to decide which classes to use at runtime.

***

### [Abstract Factory](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns/02-abstract-factory)
* The Abstract Factory builds on the factory pattern.
* Abstract Factory is useful when the user expects to receive a family of multiple related objects but doesn't need to know which family it is until runtime.
* A factory returns a single object, whereas an abstract factory returns two or multiple related objects, such as a dog and dog food in our example.
* Abstract Factory creates objects while concrete factories are often singletons.

***

### [Singleton](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns/03-singleton)

Singleton is used when you want to allow only one object to be created from a class. It's an object-oriented way of providing global variables.

* In the Python community, a "borg" is a term that allows the creation of multiple instances, but they all share the same state, unlike a singleton.
* Let's say there's a need to keep a cache of information shared by multiple objects. This can be done by either keeping the information in a singleton or sharing it under a borg object.

***

### [Builder](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns/04-builder)

A Builder is a solution to an antipattern called a "telescoping constructor." An antipattern is the opposite of a best practice that we want to avoid. It occurs when a developer tries to create a complex object using an excessive number of constructors.

* The Builder design pattern tries to solve this problem by dividing the process into four roles (a divide and conquer strategy):

  - Director: In charge of actually building the product.
  - Abstract Builder: Provides all the necessary interfaces required to build the product.
  - Concrete Builder: Inherits from the abstract builder and implements the details of the interface.
  - Product: Represents the object being built.
The Builder pattern does not rely on polymorphism, unlike the factory and abstract factory.

***

### [Prototype](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns/05-prototype)

Prototype means copying or cloning objects instead of building a new object using the `__init__` method. Prototype is useful when instantiating many identical objects individually.

* Here, we first create a prototypical instance and then clone it whenever we need a replica.
* Cloning makes a carbon copy in the memory space instead of building individual objects.

***

Homepage: [Home](https://github.com/rauljrz/python-design-patterns)