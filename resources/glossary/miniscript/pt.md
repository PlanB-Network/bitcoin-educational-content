---
term: MINISCRITO

---
Estrutura concebida para fornecer uma estrutura para programar scripts de forma segura no Bitcoin. A linguagem nativa do Bitcoin é chamada de script. É bastante complexa de usar na prática, especialmente para aplicações sofisticadas e personalizadas. Acima de tudo, é muito difícil verificar as limitações de um script. Miniscript usa um subconjunto de scripts Bitcoin para simplificar sua criação, análise e verificação. Cada miniscript é equivalente 1 para 1 com um script nativo. É utilizada uma linguagem de política de fácil utilização, que é depois compilada em miniscript, para finalmente corresponder a um script nativo.

![](../../dictionnaire/assets/30.webp)

Assim, o Miniscript permite aos programadores criar scripts sofisticados de uma forma mais segura e fiável. As propriedades essenciais do Miniscript são as seguintes:


- Permite a análise estática do guião, incluindo as condições de despesa que permite e o seu custo em termos de recursos;
- Permite a criação de guiões que aderem ao consenso;
- Permite analisar se as diferentes trajectórias de despesa estão ou não em conformidade com as regras padrão dos nós;
- Estabelece uma norma geral, compreensível e compostável, para todo o software e hardware de carteiras.

O projeto Miniscript foi lançado em 2018 por Peter Wuille, Andrew Poelstra e Sanket Kanjalkar, através da empresa Blockstream. O Miniscript foi adicionado à carteira Bitcoin Core em modo apenas de observação em dezembro de 2022 com a versão 24.0 e, em seguida, totalmente em maio de 2023 com a versão 25.0.