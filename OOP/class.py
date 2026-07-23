class CLassName:
    def __new__(cls):
        obj=super().__new__(cls)
        print("new called")
        return obj
    
    def __init__(self):
        print("init called")

    @classmethod
    def classMethod(cls):
        pass

    @staticmethod
    def staticMethod():
        pass

obj=CLassName()

