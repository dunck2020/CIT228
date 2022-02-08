class Privileges:
    """A class to list privileges for users"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f'\nThis user can complete the following tasks:')
        for task in self.privileges:
            print(f'\t-{task.title()}')    
