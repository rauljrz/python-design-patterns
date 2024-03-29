# Behavioral Patterns

* It refers to how you make your objects interact with each other.
* The focus here is to defining protocols between these objects when working together to achieve a common goal.
* Beahavorial patterns mostly use methods and their signatures.

***

### [Observer](https://github.com/rauljrz/python-design-patterns/tree/main/3%20-%20Behavional%20Patterns/01-Observer)

The observer pattern establishes a one-to-many relationship between a subject and multiple observers.

* The problem here is that a subjec need to be monitored i.e, a observer should be notified when there is change in the subject.
* The scenerio here is to keep track of temperature of a reactor at a powerplant. Registerd observers must be notified when there is a change in the temperature
* The solution uses a abstract class called subject which has an interface that allows operations such as attach, detach and notify. We also need concrete subject classes inheriting from abstract subject class.

***

### [Visitor](https://github.com/rauljrz/python-design-patterns/tree/main/3%20-%20Behavional%20Patterns/02-Visitor)
The visitor allows adding new features to existing class hierarchy without changing it.

* The problem here is to add new operations dynamically to existing classes.
* The scenario includes a house, a hvac specialist and an electrcian who are visitors of type 1 and type 2.
* The solution includes applying new operations on verious elements of an existing class hierarchy.

***

Homepage : [home](https://github.com/rauljrz/python-design-patterns/tree/main)