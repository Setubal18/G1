from django.db import models


# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    )
    nome = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=10, null=False, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=False, verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=13)
    tell = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.nome


class FuncionarioSuporte(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    especializacao = models.CharField(max_length=20, null=False)
    funcionario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=False)

    # def __str__(self):
    #     return self.funcionario


class Funcionario(models.Model):
    dep = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False)
    funcionario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=False)

    # def __str__(self):
    #     return self.funcionario.get_objects()


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Chamada(models.Model):
    STATUS_CHOICES = (
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluido'),
        ('cancelado', 'Cancelado'),
    )

    titulo = models.CharField(max_length=50, null=False)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False)
    descricao = models.TextField()
    telefone = models.CharField(max_length=50, null=False)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False)
    data = models.DateField(null=False, verbose_name='Data da Abertura da chamada')
    status = models.CharField(max_length=20, null=False, choices=STATUS_CHOICES)

    # status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False)

    class Meta:
        verbose_name_plural = 'Chamadas'

    def __str__(self):
        return self.titulo


class Atendimento(models.Model):
    discricao = models.TextField()
    atendimento = models.ManyToManyField(FuncionarioSuporte)
    chamada = models.ManyToManyField(Chamada)

    def __str__(self):
        return self.discricao
