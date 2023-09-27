package model;

/* 1.1. Model: contains the classes which correspond to the problem entities.
Those classes can either form a hierarchy or implement the same interface.
If you choose the class hierarchy you must use the method overriding
for the  method required to solve the problem.
If you choose to implement the same interface, that interface must contain
the  method required to solve the problem.

Please use an interface.
 */

public interface Vegetable {
    float getWeight();
    String toString();
}
