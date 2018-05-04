"""
Module level doc string
Employee class
"""


class Employee(object):
    """
    My Employee class
    """
    def __init__(self, e_no, e_namae):
        print "Inside constructor "
        self.eno = e_no
        self.ename = e_namae

    def get_employee(self):
        """
        My  get_employee()
        :return:
        """
        print self.eno
        print self.ename

    def get_employee2(self):
        """
        my get_employee2() function
        :return:
        """
        print self.eno
        print self.ename


print dir(Employee)
