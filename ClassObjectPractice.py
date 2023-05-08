class Insurance:
    def __init__(self, name, coverage, clients, active):
        self.name = name
        self.coverage = coverage
        self.clients = clients
        self.active = True

    def isActive(self):
        self.active = True

    def isInactive(self):
        self.active = False

    def insurance_summary(self):
        return(f'Name: {self.name}\nCoverage: {self.coverage}\nClients: {self.clients}\nActive: {self.active}')

ins1 = Insurance('Paramount', 'Ohio', ['UTMC','IU','Midwest Hospital'], True)

print(ins1.insurance_summary())