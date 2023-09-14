# Python: Design Patterns

If you’re a programmer, you’re probably plenty busy, so why not save some time and avoid reinventing the wheel by reusing well-proven design solutions—software design patterns—to improve your code quality? Design patterns encourage programming efficiency and code reuse.

### What are Design Patterns

* Design patterns were created by Christopher Alexander and are well-known solutions to recurring problems in software engineering.
* These are descriptions or templates for how to solve problems that can be used in many different situations.
* These solutions are widely accepted by the software development community.
* We should use these design patterns so that we don't reinvent the wheel when there are already perfect solutions for the problems, thus saving time.
* Design patterns allow us to reuse design ideas.
* Design patterns help us lower development costs, time, and increase the quality of the software.

***

### Characterstics of Design Patterns

* Design patterns are language neutral.
* Design patterns are dynamic because new ones are always emerging.
* Design patterns are intentionally incomplete by design to promote customization.

***

### Types of Design Patterns

There are 3 types of Design patterns

* Creational
* Structural
* Behavioral

#### Creational Patterns

* We use creational design patterns to build objects systematically.
* The main benefit of creational patterns is their flexibility.
* For example differnt types of objects from the same class can be created at runtime using creational patterns.
* In creational pattern, Polymorphism is often used.

#### Structural Patterns

* We use structural patterns to eastablish relationships between software components in particular settings.
* The goal is to satisfy functional and non-functional requirements.
* Functional requirements refer to what the software does.
* Non-Functional requiremnets refer to how well it does its job (like how fast or slow).
* Structual patterns take advantage of inheritance.

#### Behavioral Patterns

* It refers to how you make your objects interact with each other.
* The focus here is on defining protocols between these objects when working together to achieve a common goal.
* Beahavorial patterns mostly use methods and their signatures.

***

### Understanding OOPs

* Design patterns involve use of OOP.
* An object represents entity in both problem and solution domain.
* In a sotfware environment, a component usually represents an entity interacting with the software.
* For example let's consider a conference registration problem.
	Here a participant is an entity in the problem domain.
	And Registration form is an entity in the solution domain.
* Classes are templates to create objects to avoid recreating them from scratch.
* Classes define objects in terms of attributes and behaviors.
* Attributes represent properties of an entity. They capture the current state of the entity.
* Methods represent the behavior of the entity.

***

### Design Pattern context

A pattern context consist of the following

* *Participants:* It refers to classes involved to form a design pattern. Each class play a different role to accomplish the goal of the design pattern.
* *Quality Attribute:* It refer to non-functional requirements such as usability, modifiability, reliability, performance and more.
* *Forces:* It refers to various factors or trade-offs.
* *Consequences:* It can be worst performance.
A descision maker should consider a design pattern after thoroughly considering its consequences.

***

### Design Pattern Language

A design pattern is kind of a new language which consists of

* *Name:* Pattern names should be meaningful & memorable.
* *Context:* It provides a scenario in which a pattern can be used.
* *Problem:* It describes the design challenge the pattern is trying to address.
* *Solution:* It specifies a pattern itself in terms of structures and behaviors.
* *Related patterns:* These list other patterns used together with the current pattern.

### Read More

[Creational Design Pattern:](https://github.com/rauljrz/python-design-patterns/tree/main/1%20-%20Creation%20Patterns)

1- *Concrete Factory:* Encapsulates object creation. That is, factory is an object specializing in creating other objects.

2- *Abstract Factory:* Is useful when its user expects to receive a family of related object at a given time but doesn't have to know which family it is until runtime.

3 - *Singleton:* Is the pattern you need When you want to allow only one object to be created from a class. It's an object-oriented way of providing global variables.

4 - *Builder:* Is a solution to an anti-pattern called telescoping constructor. Occurs when a software developer attempts to build a complex object using an excessive number of constructors.

5 - *Prototype:* Clone objects according to a prototypical instance.

[Structural Design Pattern:](https://github.com/rauljrz/python-design-patterns/tree/main/2%20-%20Structural%20Patterns)

1 - *Decorator:* Allows adding new features to an object without changing their structures.

2 - *Proxy:* Proxy is helpful when creating a very highly resource intensive object.

3 - *Adapter:* Converts interface of a class to another the client is expecting.

4 - *Composite:* Maintains a tree data structure.

5 - *Bridge:* Helps untangle a complicated class hierarchy.

[Behavioral Design Pattern](https://github.com/rauljrz/python-design-patterns/tree/main/3%20-%20Behavional%20Patterns):

1 - *Observer:* Establishes a one-to-many relationship between a subject and multiple observers.
2 - *Visitor:*
3 - *Iterator:*
4 - *Strategy:*
5 - *Chain of responsibility:*
