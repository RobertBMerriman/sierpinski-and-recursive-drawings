import turtle
import random


class RecursiveDrawing:

    """
    distance:     Distance travelled for every movement
    repetions:    How many times the will pattern be repeated
    skip_to:      Used to skip directly to a certain repeation, instead of drawing all the way up
    command_dict: Dictionary of commands containing lamba functions ('func') to execute on the turtle
                  as well as the string ('subs') that replaces the command character
    axiom:        The initial command character(s) used to start the sequence of commands
    """
    def __init__(self, distance=2, angle=60, repetitions=10, skip_to=0, command_dict={}, axiom=""):

        # Assign parameters to instance values
        self.distance = distance
        self.angle = angle
        self.repetitions = repetitions

        # Check `skip_to` input and assign instance value
        if repetitions < skip_to < 0:
            self.skip_to = 0
        else:
            self.skip_to = skip_to

        # Set command curve
        self.set_command_curve(command_dict, axiom)

        # Instantiate turtle
        self.shelly = turtle.Turtle()
        self.shelly.shape('turtle')
        self.shelly.speed(0)

    def set_command_curve(self, command_dict={}, axiom=""):
        # Follows: {'command': {'subs': "substitution", 'func': lambda self: self.shelly.action()}}
        # If empty, default to Sierpinski curve
        if command_dict == {}:
            self.command_dict = {
                'A': {
                    'subs': 'B+A+B',
                    'func': lambda drawing: drawing.shelly.forward(drawing.distance)
                },
                'B': {
                    'subs': 'A-B-A',
                    'func': lambda drawing: drawing.shelly.forward(drawing.distance)
                },
                '-': {
                    'subs': '-',
                    'func': lambda drawing: drawing.shelly.right(drawing.angle)
                },
                '+': {
                    'subs': '+',
                    'func': lambda drawing: drawing.shelly.left(drawing.angle)
                }
            }
        else:
            self.command_dict = command_dict

        # Axiom - beginning command(s)
        if axiom == "":
            self.commands = "A"
        else:
            self.commands = axiom

    def draw(self):
        # Every repetition
        for repetition in range(self.repetitions):
            print(self.commands)  # Print command string]

            new_commands = ""  # Builder to reconstruct the commands
            # Every character command
            for command in self.commands:
                if repetition > self.skip_to:  # Skip if repetiton
                    self.command_dict[command]['func'](self)  # Perform function
                new_commands += self.command_dict[command]['subs']  # Apply substitution to new command string

            # Replace commands and change color
            self.commands = new_commands
            self.shelly.color(random.random(), random.random(), random.random())

        turtle.mainloop()  # Keep on screen


if __name__ == '__main__':
    drawing = RecursiveDrawing()
    # Set to Sierpinski curve - replace if necessary
    drawing.set_command_curve(
        {
            'A': {
                'subs': 'B+A+B',
                'func': lambda drawing: drawing.shelly.forward(drawing.distance)
            },
            'B': {
                'subs': 'A-B-A',
                'func': lambda drawing: drawing.shelly.forward(drawing.distance)
            },
            '-': {
                'subs': '-',
                'func': lambda drawing: drawing.shelly.right(drawing.angle)
            },
            '+': {
                'subs': '+',
                'func': lambda drawing: drawing.shelly.left(drawing.angle)
            }
        },
        axiom="A"
    )

    # Start drawing
    drawing.draw()
