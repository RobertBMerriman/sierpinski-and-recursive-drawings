import turtle


class Sierpinski:

    def __init__(self, distance, repetitions):

        self.command_dict = {'A': 'B+A+B', 'B': 'A-B-A'}

        self.distance = distance
        self.repetitions = repetitions
        self.commands = "A"

        self.shelly = turtle.Turtle()
        self.shelly.shape('turtle')
        self.shelly.speed(0)

    def start(self):
        for i in range(self.repetitions):

            print(self.commands)

            new_commands = ""

            for command in self.commands:
                if command == 'A' or command == 'B':
                    self.shelly.forward(self.distance)
                    new_commands += self.command_dict[command]
                elif command == '+':
                    self.shelly.left(60)
                    new_commands += command
                elif command == '-':
                    self.shelly.right(60)
                    new_commands += command

            self.commands = new_commands


if __name__ == '__main__':
    shelly = Sierpinski(distance=2, repetitions=10)
    shelly.start()

    turtle.mainloop()
