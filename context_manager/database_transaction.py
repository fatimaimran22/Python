from contextlib import contextmanager

def update_balance(a):
    if a==0:
        raise Exception
    print("Balance updated.")

class DB():
    def begin(self):
        print("Beginning Transaction.")

    def commit(self):
        print("Commiting Transaction.")

    def rollback(self):
        print("Rollback after exception.")




@contextmanager
def transaction():
    db=DB()
    try:
        db.begin()
        yield
        db.commit()
    except:
        db.rollback()


with transaction():
    #update_balance(0)
    update_balance(1)