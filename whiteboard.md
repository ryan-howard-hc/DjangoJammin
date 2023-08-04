Given an array of int, find the first non repeating element and return it
no strings in the int array, or objects, or boolean values

[ 1, 2 , 3, ,4 ,5, 1]
[22,45,2455,63,23,22]
[1,1,2,2,3,3,3,4,5,5,]


First, we would want to set up an empty variable to place each int in the array that we are looping through

We would wanmt to just loop through the array, incrementing through each position in the array, and have probably an if else with a boolean to determine whether the number presented in each position has a repeating number in it,
int[0] 1,2,3,4,5,



then be able to move on to the next integer in the array.



We would also want to have an alternative in case all of the integers are repeated at least once, returning False. When the first non repeating element returns False, we would want to return that as the integer.

Or just an if else, with a
