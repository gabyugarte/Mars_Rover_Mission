# Mars_Rover_Mission
Technical challenge - Python
# Mars Rover Mission 2022

Your Task
You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface
of the planet. Develop a software that translates the commands sent from earth to instructions
that are understood by the rover.
Requirements

● You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W)
it is facing.
● The rover receives a collection of commands. (E.g.) FFRRFFFRL
● The rover can move forward (f).
● The rover can move left/right (l,r).
● Suppose we are on a really weird planet that is square. 200x200 for example :)
● Implement obstacle detection before each move to a new square. If a given
sequence of commands encounters an obstacle, the rover moves up to the last
possible point, aborts the sequence and reports the obstacle.

Take into account

● Rovers are expensive, make sure the software works as expected.
## Usage
Run the program with `python rover.py`  
  
**Example input:**  
Enter the plateau's maximum coordinates in 'X Y' format  
`> 9 9`  
Enter the Rover's start coordinates and heading in 'X Y H' format:  
`> 2 4 E`  
Enter the Rover's instructions consisting of L, R and F in a string:  
`> FFFRLFF`  
**Final Output**  
`> 7 4 E`  

## Testing
Run all unit tests from the command line with `python test.py`  
`test_1()` tests the default Rover behaviour as per the brief  
`test_2()` runs an alternate Rover path   
`test_3()` tests Rover command and out of bounds exceptions  
`test_4()` tests Mars plateau input exceptions  
`test_5()` tests Rover start input exceptions  
