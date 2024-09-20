class Edicao(models.Model):
    data = models.DateField()
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.data}"
