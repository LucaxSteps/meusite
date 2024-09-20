class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['data', 'titulo']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de Publicação'}),
        }