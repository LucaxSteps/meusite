class CadastrarEdicaoView(LoginRequiredMixin, CreateView):
    model = Edicao
    form_class = EdicaoForm
    template_name = 'JornalDigital/cadastrar_edicao.html'

    def form_valid(self, form):
        form.save()
        return redirect('index')
