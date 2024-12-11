

class EcommerceUserError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    
    def __repr__(self):
        return f"{self.message}"