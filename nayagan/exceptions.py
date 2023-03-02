class ReturnException(Exception):
    def __init__(self, msg, value):
        super().__init__(msg)
        self.value = value