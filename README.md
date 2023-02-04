# INMAS_Feb_23
Airplane boarding simulation

## Basic Setup:

We use a matrix to represent the seat and when passangers board the airplane, it will change the matrix entries from 0 to 1. We also want to visulize our simulation of boarding strategy.

## Functions we have:

`initial_airplane(width, depth, groups)` we create a airplane with specified structure.

`random_on_board()` we will get an array when passagers come boarding in a random order.

`group_on_board()` we will get an array when passagers come boarding in what order.

`seat_passagers(width, depth, matrix)` return the time needed for a passager seating at width, depth to find and seat. 

`visualize_simulation()` we will visualize the simulation using matplot.


