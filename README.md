# To-do List
This code creates a to-do list based on the input of the user. 

First, the computer will ask whether the user would like either to add or mark a task, 
view the to-do list, or exit the program. 

This code doesn't have a memory, meaning that, once the user exits, the list won't 
store anything for the next log.

The add_task() and view_tasks() functions do essentially as their names say, however 
mark_task() is a bit more complicated than that. It gives the user the option to go to
any of the other functions in case they're entering a task that isn't in the list. It
also allows the user to eliminate marked tasks and to mark other tasks on the list.
