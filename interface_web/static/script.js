function atualizarPainel() {
    fetch('/api/updates')
        .then(response => response.json())
        .then(dados => {
            // Atualiza o radar de notícias
            const feed = document.getElementById('news-feed');
            if(feed) {
                feed.innerHTML = `<div class="news-item">${dados.social}</div>`;
            }

            // Atualiza o Financeiro
            const financeiro = document.querySelector('.market-grid');
            if(financeiro) {
                financeiro.innerHTML = `<div class="coin">${dados.financeiro}</div>`;
            }

            // Atualiza o Top 10
            const lista = document.getElementById('top-ranking');
            if(lista) {
                lista.innerHTML = dados.top_10.map(item => `<li>${item}</li>`).join('');
            }
        })
        .catch(err => console.error("Erro na recepção do radar:", err));
}

// Executa a cada 5 segundos para um efeito de "tempo real"
setInterval(atualizarPainel, 5000);

