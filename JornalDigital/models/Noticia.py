class Noticia(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, related_name='noticias')
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='noticias')

    def __str__(self):
        return self.titulo
