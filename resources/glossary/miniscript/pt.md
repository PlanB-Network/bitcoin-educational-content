---
termo: MINISCRIPT
---

Framework projetado para fornecer uma estrutura para programar scripts de forma segura no Bitcoin. A linguagem nativa do Bitcoin é chamada de script. É bastante complexa de usar na prática, especialmente para aplicações sofisticadas e personalizadas. Acima de tudo, é muito difícil verificar as limitações de um script. O Miniscript usa um subconjunto de scripts do Bitcoin para simplificar sua criação, análise e verificação. Cada miniscript é equivalente 1 por 1 com um script nativo. Uma linguagem de política amigável ao usuário é usada, que é então compilada em miniscript, para finalmente corresponder a um script nativo.

![](../../dictionnaire/assets/30.png)

O Miniscript permite, assim, que os desenvolvedores construam scripts sofisticados de maneira mais segura e confiável. As propriedades essenciais do Miniscript são as seguintes:
* Permite a análise estática do script, incluindo as condições de gasto que permite e seu custo em termos de recursos;
* Possibilita a criação de scripts que aderem ao consenso;
* Permite a análise de se os diferentes caminhos de gasto estão em conformidade com as regras padrão dos nós;
* Estabelece um padrão geral, compreensível e componível, para todo o software e hardware de carteiras.

O projeto Miniscript foi lançado em 2018 por Peter Wuille, Andrew Poelstra e Sanket Kanjalkar, através da empresa Blockstream. O Miniscript foi adicionado à carteira Bitcoin Core em modo somente visualização em dezembro de 2022 com a versão 24.0, e então totalmente em maio de 2023 com a versão 25.0.