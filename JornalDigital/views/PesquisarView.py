class PesquisarView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            noticias = Noticia.objects.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))
        else:
            noticias = Noticia.objects.none()
        return render(request, 'JornalDigital/pesquisar.html', {'noticias': noticias, 'query': query})
