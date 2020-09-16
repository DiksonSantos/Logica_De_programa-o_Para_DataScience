class aluno:
    def __init__(self, matricula, nome):
        self.Matricula = matricula
        self.Nome = nome
        
    def matricular(self):
        print("Esta Matriculado")
        return "Aluno ",self.Nome 

X = aluno(199999,"Dikson")
print(X.matricular())
print(X.Nome)


X.matricular()
