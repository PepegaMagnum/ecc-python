class binaryNum:
    def __init__(self, *args):
        if len(args) == 2:
            if type(args[1]) != 'int':
                raise Exception("degree must be an int.")

            self.m = args[1]

            if type(args[0]) == 'str':
                self.value = args[0]
            elif type(args[0]) == 'list':
                self.value = ''.join([str(x) for x in args[0]])
        else:
            raise Exception("Provide 2 arguments.")

