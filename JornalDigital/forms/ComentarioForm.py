class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
