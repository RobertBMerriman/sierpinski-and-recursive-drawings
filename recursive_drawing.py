import turtle
import random


class RecursiveDrawing:

    """
    distance:         Distance travelled for every movement
    repetions:    How many times the will pattern be repeated
    skip_to:      Used to skip directly to a certain repeation, instead of drawing all the way up
    command_dict: Dictionary of commands containing lamba functions to execute on the turtle
                  as well as the string that replaces the command character
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

        self.set_command_curve(command_dict, axiom)

        self.shelly = turtle.Turtle()
        self.shelly.shape('turtle')
        self.shelly.speed(0)

    def set_command_curve(self, command_dict={}, axiom=""):
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

        if axiom == "":
            self.commands = "A"
        else:
            self.commands = axiom

    def draw(self):
        for repetition in range(self.repetitions):
            print(self.commands)
            new_commands = ""

            for command in self.commands:
                if repetition > self.skip_to:
                    self.command_dict[command]['func'](self)
                new_commands += self.command_dict[command]['subs']

            self.commands = new_commands
            self.shelly.color(random.random(), random.random(), random.random())

        turtle.mainloop()


if __name__ == '__main__':
    drawing = RecursiveDrawing()
    drawing.draw()
