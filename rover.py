import re


class Rover:
    """
    The Rover Class handles all operations of a rover inside the Plateau
    """

    def __init__(self, maxx, maxy):
        self.x = 0
        self.y = 0
        self.maxx = maxx
        self.maxy = maxy
        self.heading = 'N'
        # Define the heading constraints; realistically this could be expanded to include NE, SW etc.
        self.headings = ['N', 'E', 'S', 'W']
        self.operations = ''

    def setstart(self, userinput):
        # Check for invalid user input
        if bool(re.match('^[0-9 NESW]+$', userinput)) is False:
            raise Exception('The rover start command contains invalid characters')
            exit(1)
        # Split the input into an array
        inputarray = userinput.split(' ')
        # Checks that 3 variables came in the input string
        if len(inputarray) != 3:
            raise Exception('Rover inputs invalid. Please start again.')
            exit(1)

        self.x = int(inputarray[0])
        self.y = int(inputarray[1])
        self.heading = inputarray[2]

    def setoperations(self, operations):
        # Check for non L, R or F characters in the input string
        if bool(re.match('^[LRF]+$', operations)) is False:
            raise Exception('The operations command contains invalid characters')
            exit(1)

        self.operations = operations

    def turn(self, direction):
        # Assume the direction is (R)ight
        delta = 1
        # If L is input, reverse the delta
        if direction == 'L':
            delta = -1
        # Get the current heading index
        headingindex = self.headings.index(self.heading)
        # Add the delta to the index
        newheading = headingindex + delta
        # If the newheading is outside the limit of coordinates, reset to 0
        if newheading >= len(self.headings):
            newheading = 0
        # If the newheading index is less than zero, reset to the index limit
        if newheading < 0:
            newheading = len(self.headings) - 1
        # Set the new heading
        self.heading = self.headings[newheading]

    # Move the rover based on the operations
    def move(self):
        # Create a dictionary with x,y movement coordinates
        rules = {
            'N': [0, 1],
            'E': [1, 0],
            'S': [0, -1],
            'W': [-1, 0]
        }
        # Get the current heading's x,y coord change rules
        coords = rules[self.heading]
        # Modify the coordinates
        newx = self.x + coords[0]
        newy = self.y + coords[1]
        # Validate that the move is within bounds, then assign the new x and y values
        if self.validatemove(newx, newy):
            self.x = newx
            self.y = newy
        else:
            raise Exception('Error: Rover out of bounds at ' + str(newx) + ' ' + str(newy))
            exit(1)

    # Validate that the move is not out of bounds
    def validatemove(self, x, y):
        # Check that the x and y are not in the negative
        if x < 0 or y < 0:
            return False
        # Check that x and y do not exceed the maximum coordinates
        if x > self.maxx or y > self.maxy:
            return False

        return True

    # Perform each operation in sequence
    def operate(self):
        # Loop through each character in the string, either turning or moving
        for action in self.operations:
            if action == 'F':
                self.move()
            else:
                self.turn(action)

    # Get the final position of the rover as a string of 'X Y H'
    def getposition(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.heading)

