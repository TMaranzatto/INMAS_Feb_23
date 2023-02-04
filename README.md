# INMAS_Feb_23
Airplane boarding simulation

## Basic Setup:

We use a matrix to represent the seat and when passangers board the airplane, it will change the matrix entries from 0 to 1. We also want to visulize our simulation of boarding strategy.

## Functions we have:

`initial_airplane(width, depth, groups)` we create a airplane with specified structure.

`random_on_board(width, depth)` we will get an array when passagers come boarding in a random order.

`group_on_board(width, depth)` we will get an array when passagers come boarding in what order.

`seat_passagers(row, column, matrix)` return the time needed for a passager seating at row, column to find and seat. 

`visualize_simulation(model)` we will visualize the simulation of the model we use using matplot.


