class organizacion:
    def __init__(self,nombre,superheroes):
        if type(nombre)!= str:
            raise Exception("nombre de ser str")
        else:
            self.nombre=nombre
        if type(superheroes)!= list:
            raise Exception("superheroes de ser una lista")
        else:
            self.superheroes=superheroes
    def get_nombre(self):
        return self.nombre
    def get_superheroes(self):
        describcion=""
        for i in range(len(self.superheroes)):
            describcion+=f'{i} - {self.superheroes[i].__str__()}\n'
        return describcion
    def set_superheroes(self,x):
        self.superheroes.append(x)
    def no_eliminado(self):
        return self.superheroes!=[]
    def surrender(self):
        for i in self.superheroes:
            i.energia=0
        self.superheroes=[]
    def __str__(self):
        return f'La organizacion {self.nombre}, tiene los siguientes superheroes:\n{self.get_superheroes()}'