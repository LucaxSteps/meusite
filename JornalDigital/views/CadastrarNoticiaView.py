class CadastrarNoticiaView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'JornalDigital/cadastrar_noticia.html'

    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.autor = self.request.user
        noticia.save()
        return redirect('exibir_edicao', edicao_id=noticia.edicao.id)
