class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def ADD_TWO_VALUES(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def STORE_NAME(self, name):
        self.environment[name] = self.stack.pop()

    def LOAD_NAME(self, name):
        self.stack.append(self.environment[name])

    def parse_argument(self, instruction, arg, to_execute):
        """parse argument to call the correct function"""
        numbers = ["LOAD_VALUE"]
        names = ["STORE_NAME", "LOAD_NAME"]

        if instruction in numbers:
            return (instruction, to_execute['numbers'][arg])
        elif instruction in names:
            return (instruction, to_execute['names'][arg])
        else:
            return (instruction, None)

    def run_code(self, to_execute):
        numbers = to_execute["numbers"]

        if len(numbers) == 2:
            for step in to_execute["instructions"]:
                (instruction, argument) = self.parse_argument(step[0], step[1], to_execute)
                if instruction == "LOAD_VALUE":
                    try:
                        self.LOAD_VALUE(argument)
                    except IndexError:
                        continue
                elif instruction == "ADD_TWO_VALUES":
                    self.ADD_TWO_VALUES()
                elif instruction == "PRINT_ANSWER":
                    self.PRINT_ANSWER()
                elif instruction == "STORE_NAME":
                    self.STORE_NAME(argument)
                elif instruction == "LOAD_NAME":
                    self.LOAD_NAME(argument)


if __name__ == '__main__':
    what_to_execute = {
        "instructions": [
            ("LOAD_VALUE", 0),
            ("STORE_NAME", 0),
            ("LOAD_VALUE", 1),
            ("STORE_NAME", 1),
            ("LOAD_NAME", 0),
            ("LOAD_NAME", 1),
            ("ADD_TWO_VALUES", None),
            ("PRINT_ANSWER", None)
        ],
        "numbers": [7, 5],
        "names": ['a', 'b']
    }

    Interpreter().run_code(what_to_execute)