class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.words = []
        self.states = []
        print("Hi, I'm an automaton!")

    def validate(self):
        f = open(self.config_file, "r")
        line = f.readline()
        while line:
            if line.strip()[0] == "#":
                line = f.readline()
            else:
                if line.strip() != "Sigma :":
                    f.close()
                    return "The input is not valid"
                break
        line = f.readline()
        while line.strip() != "End":
            if len(line.strip().split()) != 1:
                return "The input is not valid"
            self.words += line.strip()
            line = f.readline()
        line = f.readline()
        while line:
            if line.strip()[0] == "#":
                line = f.readline()
            else:
                if line.strip() != "States :":
                    f.close()
                    return "The input is not valid"
                break
        line = f.readline()
        okS = 0
        okF = 0
        while line.strip() != "End":
            if len(line.split(',')) > 2 or len(line.split(',')) < 1:
                f.close()
                return "The input is not  valid"
            if len(line.split(',')) > 1:
                if line.split(',')[1].strip() == 'F':
                    okF += 1
                elif line.split(',')[1].strip() == 'S':
                    okS += 1
                    if okS > 1:
                        return "The input is not valid"
                else:
                    return "The input is not valid"
            self.states += [line.split(',')[0].strip()]
            line = f.readline()
        if okS > 1 or okS  == 0 or okF == 0:
            return "The input is not valid"
        line = f.readline()
        while line:
            if line.strip()[0] == "#":
                line = f.readline()
            else:
                if line.strip() != "Transitions :":
                    f.close()
                    return "The input is not valid"
                break
        line = f.readline()
        while line.strip() != "End":
            if len(line.split(',')) != 3:
                f.close()
                return "The input is not valid1"
            if line.split(',')[0].strip() not in self.states or line.split(',')[1].strip() not in self.words or line.split(',')[2].strip() not in self.states:
                f.close()
                return "The input is not valid"
            line = f.readline()
        f.close
        return "The input is valid"

    def accepts_input(self, input_str):
        """Return a Boolean
        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration

        If the input is rejected, the method raises a
        RejectionException.
        """
        pass


if __name__ == "__main__":
    a = Automaton('input.txt')
    print(a.validate())
