class Calculator :
    def __init__(self, id1, color1, manf_date1):
        self.id=id1
        self.color=color1
        self.manf_date=manf_date1
        print('this is a constructor')
    
    def print_id(self):
        print(Calculator.company_name)
        print(self.id)

    def add(self):
        print("This is an add function")

    def mul(self):
        print("this is a function for multiflication")

    @staticmethod
    def print_company_desc():
        print("we don't use any variables")

calc1=Calculator(1,'black','01feb')
calc1=Calculator(2,'white','01feb')

calc1.add()
calc1.add()

calc1.id=12
calc1.color='black'
calc1.manf_date='01feb'
calc1.id=14

#METHODS:

calc1.print_id()


Calculator.change_company_name('NEW_CASIO')
calc1.change_company_name('NEW_CASIO10')
print(calc1.company_name)

@classmethod
def change_company_name(cls,new_name):
    cls.company_name = new_name
    print("company name changed")

#EXPLANATION OF ABOVE CODE -----------------------------------------------------------------------------
# Defining the Calculator class
class Calculator:

    # Class Attribute - shared by all instances of the class
    company_name = "CASIO"

    # Constructor - automatically called when an object is created
    def __init__(self, id1, color1, manf_date1):
        self.id = id1                     # Instance Attribute
        self.color = color1              # Instance Attribute
        self.manf_date = manf_date1      # Instance Attribute
        print('This is a constructor')   # Just a message

    # Instance Method - works with object-specific data
    def print_id(self):
        print(Calculator.company_name)   # Access class attribute using class name
        print(self.id)                   # Access instance attribute

    def add(self):
        print("This is an add function")  # Simulated addition method

    def mul(self):
        print("This is a function for multiplication")  # Simulated multiplication method

    # Static Method - doesn't use self or cls; general utility
    @staticmethod
    def print_company_desc():
        print("Static Method: We don't use any object/class variables here.")

    # Class Method - modifies class attribute
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print("Class Method: Company name changed to", cls.company_name)


# Creating an object of Calculator
calc1 = Calculator(1, 'black', '01-Feb')  # Constructor is called

# Overwriting with a new object (only this will be used)
calc1 = Calculator(2, 'white', '01-Feb')  # Constructor is called again

# Calling instance methods
calc1.add()         # Outputs add function message
calc1.mul()         # Outputs multiplication function message

# Modifying instance attributes
calc1.id = 14
calc1.color = 'black'
calc1.manf_date = '01-Feb'

# Accessing instance method that prints instance and class data
calc1.print_id()

# Calling class method from both class and object
Calculator.change_company_name('NEW_CASIO')     # Using class
calc1.change_company_name('NEW_CASIO10')        # Using object

# Printing updated class attribute
print("Company Name:", calc1.company_name)

# Calling static method
Calculator.print_company_desc()
#---------------------------------------------------------------------------------------------------------------
