class Course:
    platform_name="Learn Hub"
    total_courses=0
    discount=10

    def __init__(self,course_name, price):
        self.course_name=course_name
        self.price=price
        Course.total_courses+=1
    
    @classmethod
    def change_platform(cls,new_name):
        cls.platform_name=new_name

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount=new_discount

    @classmethod
    def show_platform_info(cls):
        print(f"Platform Name: {cls.platform_name}")
        print(f"Total Courses: {cls.total_courses}")
        print(f"Current Discount: {cls.discount}")

    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        return False
    
    @staticmethod
    def calculate_discount(price,discount):
        return price*(1-discount/100)
    
    def show_course(self):
        print(f"Course Name: {self.course_name}\nOriginal Price: {self.price}\n")
        print(f"Platform Name: {Course.platform_name}")
        print(f"Discount: {Course.discount}")
        final_price=self.calculate_discount(self.price, Course.discount)
        print(f"Final Price: {final_price}")

c1=Course("Python",5000)
c2=Course("Java",7000)

Course.show_platform_info()

Course.change_discount(25)
Course.change_platform("Code Academy")

c1.show_course()
c2.show_course()

print(Course.is_valid_price(-500))
print(Course.is_valid_price(3000))