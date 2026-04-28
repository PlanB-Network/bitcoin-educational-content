---
name: Lightning Network+
description: Obtenha liquidez de entrada gratuita com aberturas de cooperativas no seu nó Lightning
---

![cover](assets/cover.webp)



## Introdução



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) é uma plataforma comunitária concebida para facilitar a cooperação entre operadores de nós Lightning Network. O seu principal objetivo é melhorar a conetividade, a liquidez e a descentralização da rede Lightning, sem a necessidade de intermediários centralizados.



Este tutorial centrar-se-á no serviço **"Swaps "**, que é a funcionalidade mais utilizada e estruturante do LN+ atualmente. Também serão apresentados os demais serviços oferecidos pela plataforma.



## Visão geral do LN



### O que é o Lightning Network Plus?



O Lightning Network Plus (LN+) é uma plataforma comunitária para operadores de nós Lightning que desejam cooperar direta e voluntariamente. O seu objetivo é facilitar a criação de canais Lightning úteis, equilibrados e sustentáveis, evitando a necessidade de soluções centralizadas ou hubs impostos.



O LN+ baseia-se num princípio fundamental: a cooperação entre pares, assente na transparência, na reciprocidade e na reputação.



### Visão geral dos serviços LN



O LN+ oferece vários serviços destinados a melhorar a topologia e a liquidez da rede Lightning, incluindo :





- Swaps**: abertura recíproca de canais entre operadores (serviço principal).
- Anéis**: aberturas de canais circulares entre vários participantes.
- Swaps baseados na confiança**: variantes que se baseiam mais na confiança e no historial dos participantes.
- Caraterísticas sociais**: perfis, comentários e sistema de reputação.



No resto deste tutorial, vamos concentrar-nos exclusivamente no serviço **Swaps**, que está no centro da utilização atual do LN+.



## Serviço "Swaps" LN+



### Definição de um swap LN+



Uma **troca** de LN+ é um acordo voluntário entre dois operadores de nós Lightning para abrir mutuamente canais Lightning de capacidade equivalente (ou pré-acordada). Ao contrário de uma abertura de canal unilateral convencional, a troca baseia-se numa **recíproca explícita**.



Na prática :





- Abre-se um canal para o nó do seu parceiro.
- O seu parceiro abre um canal para o seu nó.
- Ambas as partes estão a empatar uma quantidade semelhante de bitcoins on-chain.



### Qual é o objetivo dos swaps para os operadores de nós?



O serviço Swaps aborda várias questões fundamentais com que se deparam os operadores da Lightning:





- Conectividade melhorada**: criação de canais bidireccionais úteis logo que são abertos.
- Melhor gestão da liquidez**: cada parte tem capacidade de entrada e de saída.
- Redução do risco de canais desnecessários**: o parceiro é encorajado a manter o canal aberto.
- Maior descentralização**: ligações diretas entre operadores, sem hubs impostos.



### Para que perfis de nós são úteis as trocas?



Os swaps são particularmente úteis para :





- Novos nós que pretendam melhorar rapidamente a sua capacidade de encaminhamento.
- Operadores intermediários que procuram aumentar a densidade do seu gráfico de canais.
- Nós orientados para o encaminhamento que pretendem otimizar a sua topologia.



## Ligue o seu nó Lightning ao LN+



### Requisitos técnicos



Antes de começar, é necessário :





- Um nó Lightning em funcionamento (LND, Core Lightning ou Eclair).
- Acesso à interface de gestão do seu nó.
- Capacidade on-chain suficiente para abrir os canais.



Aceder ao sítio Web [Lightning Network](https://lightningnetwork.plus/) Plus e clicar no botão `Login` no canto superior direito da interface.



![capture](assets/fr/03.webp)



### Autenticação por assinatura de mensagem



Para se autenticar, é necessário assinar a mensagem fornecida utilizando a chave privada do seu Lightning node. Com o ThunderHub, esta operação é muito simples.



Comece por copiar a mensagem apresentada pelo LN+.



![capture](assets/fr/04.webp)



No ThunderHub, aceda ao separador `Ferramentas` e, em seguida, clique no botão `Assinar` na secção `Mensagens`.



![capture](assets/fr/05.webp)



Cole a mensagem de autenticação fornecida pelo LN+ e, em seguida, clique em `Sign`.



![capture](assets/fr/06.webp)



O ThunderHub assina então esta mensagem utilizando a chave privada do seu nó. Copie a assinatura gerada.



![capture](assets/fr/07.webp)



Cole esta assinatura no campo correspondente no site do LN+ e, em seguida, clique em "Iniciar sessão".



![capture](assets/fr/08.webp)



Está agora ligado ao LN+ com o seu Lightning node. Este processo permite ao LN+ verificar se é o legítimo proprietário do nó que reclama na sua plataforma.



![capture](assets/fr/09.webp)



Se desejar, pode personalizar o seu perfil LN+, por exemplo, acrescentando uma pequena biografia.



## Participar num swap existente



### Acesso a ofertas de troca



Para participar na sua primeira abertura de canal, vá ao menu `Swaps` no topo da interface. Aqui encontrarás todos os swaps atualmente disponíveis, de acordo com as caraterísticas do teu nó.



![capture](assets/fr/10.webp)



### Condições de elegibilidade



Para aderir a uma oferta de troca existente, basta selecionar o anúncio correspondente e registar-se. No entanto, o LN+ permite que o criador da troca defina certas **condições de elegibilidade**, tais como :





- um número mínimo de canais já abertos ;
- capacidade total mínima dos nós ;
- determinados tipos de ligação aceites.



### Nós recentes



Como resultado, especialmente nas fases iniciais de utilização, é possível que **poucas ou nenhumas ofertas estejam disponíveis** para o seu nó. Esta é uma situação comum para os novos nós ou para os que ainda não estão ligados.



No meu caso, apesar da existência de alguns canais abertos, nenhuma das ofertas preenchia os critérios exigidos.



## Criar a sua própria oferta de troca



### Quando é que deve criar a sua própria troca?



Quando não existe uma oferta disponível, criar o seu próprio swap é muitas vezes a melhor solução. Além disso, permite-lhe manter o controlo sobre os parâmetros do swap.



### Trocar a configuração



Clique em **Start Liquidity Swap**, depois configure os parâmetros da sua oferta:





- selecionar o número total de participantes (3, 4 ou 5);
- indicam a capacidade dos canais a abrir;
- definir o período de compromisso durante o qual os participantes se comprometem a não encerrar os seus canais;
- especificar eventuais restrições aplicáveis aos participantes (número mínimo de canais, capacidade total mínima, tipo de ligação aceite).



![capture](assets/fr/11.webp)



### Publicação e expectativas dos participantes



Uma vez introduzidos todos os parâmetros, clique em **Start Liquidity Swap** para publicar a sua oferta. Agora só tem de esperar que outros operadores se inscrevam.



![capture](assets/fr/12.webp)



## Finalizar uma troca



### Abertura efectiva do canal



Agora que todas as posições de troca foram tomadas, cada participante pode ver, a partir da sua interface LN+, qual o nó para o qual precisa de abrir um canal Lightning.



![capture](assets/fr/13.webp)



Do seu lado, abra o canal utilizando o Node ID fornecido pelo LN+ e respeitando a quantidade indicada. Esta operação pode ser efectuada através do ThunderHub, outro gestor de nó Lightning ou diretamente através da interface básica do seu nó.



![capture](assets/fr/14.webp)



Uma vez aberto, o canal aparece na secção de canais em espera.



![capture](assets/fr/15.webp)



### Confirmação em LN+



De seguida, volte ao LN+ para confirmar que iniciou a abertura do canal, clicando no botão `Channel Opening Started`.



![capture](assets/fr/16.webp)



### Fim da troca



Quando todos os participantes tiverem aberto os canais a que se comprometeram, a troca é considerada completa.



## Reputação e boas práticas de comunicação



### O sistema de reputação LN+



O LN+ incorpora um sistema de reputação baseado nas opiniões deixadas pelos participantes no final dos swaps. Estas opiniões são públicas e influenciam diretamente a capacidade de um operador para participar ou criar futuros swaps.



![capture](assets/fr/17.webp)



### Melhores práticas recomendadas



A fim de preservar uma boa reputação e assegurar o bom funcionamento das trocas, recomenda-se :





- respeitar os prazos de abertura dos canais ;
- comunicar rapidamente em caso de problema ou de atraso;
- utilizar a secção de comentários para trocar impressões com outros participantes;
- não encerrar um canal antes do termo do período de compromisso.




![capture](assets/fr/18.webp)



### Porque é que a reputação é fundamental para o LN+



O LN+ baseia-se num modelo de cooperação voluntária, sem grandes condicionalismos técnicos. A reputação é, por conseguinte, o principal incentivo para garantir a fiabilidade e a credibilidade dos participantes.



## Outros serviços LN



Para além dos Swaps, o LN+ oferece outros serviços destinados a melhorar a conetividade e a coordenação entre os operadores de nós Lightning. Os Rings** permitem que vários participantes criem um loop de aberturas de canais, reforçando assim a redundância dos caminhos de encaminhamento e a densidade do gráfico Lightning. Os swaps baseados na confiança** baseiam-se em princípios semelhantes aos swaps clássicos, mas oferecem maior flexibilidade aos participantes que já têm uma reputação estabelecida na plataforma.



O LN+ também integra caraterísticas sociais, tais como perfis públicos de nós, comentários de troca e um sistema de reputação. Estas ferramentas não são serviços técnicos propriamente ditos, mas desempenham um papel central no bom funcionamento da plataforma, facilitando a comunicação, a coordenação e a confiança entre os operadores.



## Conclusão



O serviço de Swaps do LN+ é uma ferramenta eficaz para melhorar a conetividade, a liquidez e a descentralização na rede Lightning. Ao promover aberturas de canais recíprocas e coordenadas, o LN+ permite que os operadores de nós reforcem a sua topologia, promovendo ao mesmo tempo uma cooperação responsável e descentralizada.