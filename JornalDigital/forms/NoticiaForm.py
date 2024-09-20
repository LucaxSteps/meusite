class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['edicao', 'titulo', 'conteudo']
