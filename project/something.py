'''This is the module docstring.'''
class MyClass:
    '''This is a class.'''

    def __init__(self, value):
        '''
        Initialise my instance.

        :value: some value argument
        '''
        self.value = value
    
    def get_something_else(self, whatever, this, that):
        '''
        Brief summary.

        More and more words. Make sure to leave a space below this description
        so that the colons are picked up below!

        :param whatever: This can be whatever you want it to be
        :type whatever: str
        :param this: This can be this you want it to be
        :type this: datetime
        :param that: That can be that you want it to be
        :type that: int
        :return: A pointless string containing a number
        :rtype: str
        '''
        x = 2
        y = x * 2
        print(f'Your number is: {y}!')

def random_function(something=None):
    '''
    Return the string "random".

    Here is a longer description of what the function actually does.

    :something: parameter that does something
    '''
    return 'random'
