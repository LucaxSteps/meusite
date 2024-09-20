class ExibirNoticiaView(View):
    def get(self, request, noticia_id, *args, **kwargs):
        noticia = get_object_or_404(Noticia, id=noticia_id)
        comentarios = noticia.comentarios.all()
        form = ComentarioForm()
        return render(request, 'JornalDigital/exibir_noticia.html', {'noticia': noticia, 'comentarios': comentarios, 'form': form})

    def post(self, request, noticia_id, *args, **kwargs):
        noticia = get_object_or_404(Noticia, id=noticia_id)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.autor = request.user
            comentario.save()
            return redirect('exibir_noticia', noticia_id=noticia.id)
        comentarios = noticia.comentarios.all()
        return render(request, 'JornalDigital/exibir_noticia.html', {'noticia': noticia, 'comentarios': comentarios, 'form': form})
