---
name: LN Markets
description: Plataforma de negociação do Bitcoin no Lightning Network
---

![cover](assets/cover.webp)



O LN Markets é a primeira plataforma de negociação Bitcoin verdadeiramente nativa do Lightning, permitindo-lhe negociar derivados Bitcoin alavancados diretamente a partir do seu wallet Lightning, sem KYC, liquidações instantâneas e custódia mínima. Lançado em 2020, elimina os atritos das trocas tradicionais: sem verificação de identidade, sem depósitos bloqueados, sem esperar por confirmações de blockchain. O seu wallet Lightning torna-se a sua conta de negociação.



## O que é o LN Markets?



O LN Markets oferece **Futuros** (contratos perpétuos com alavancagem até 100×) e **Opções** (Call/Put com risco limitado ao prémio pago). A plataforma funciona como uma camada de agregação de liquidez que consolida múltiplos locais de negociação para uma execução óptima de zero derrapagem. Os seus fundos ficam bloqueados apenas durante a duração exacta das suas posições activas, e não durante dias ou semanas, como acontece com uma conta de custódia tradicional.



### Produtos comerciais disponíveis



**Futuros (contratos perpétuos)



Os contratos perpétuos são futuros sem data de expiração, permitindo-lhe especular sobre a tendência de preços do Bitcoin com alavancagem. O LN Markets oferece dois modos de gestão de margens:



**Modo isolado**: Cada posição tem a sua própria margem dedicada. Apenas os fundos afectados a esta posição específica estão em risco. Se a posição atingir o preço de liquidação, **apenas esta posição é liquidada**, as suas outras posições e o saldo restante não são afectados. Ideal para limitar estritamente o risco por transação.



**Modo cruzado (margem cruzada)** : A margem é partilhada entre todas as suas posições abertas. O saldo total da sua conta serve de garantia para todas as suas posições. Se uma posição correr mal, o sistema utiliza todo o seu saldo disponível para evitar a liquidação. **Risco**: se o seu saldo total se esgotar, todas as suas posições podem ser liquidadas simultaneamente. Recomendado apenas para operadores experientes que procuram maximizar a eficiência do capital.



**Gestão de posições** :





- Posição longa**: aposta na subida do BTC/USD. Se o preço subir, ganha; se descer, perde. **Exemplo**: Bitcoin a $100.000, abre uma posição longa com 10.000 sats e uma alavancagem de 10×. Se o Bitcoin subir para $105.000 (+5%), a sua posição ganha 50% (5% × 10), ou seja, ~5.000 sats de lucro. Se o Bitcoin cair para $95.000 (-5%), perde 50%, ou seja, uma perda de ~5.000 sats.





- Posição curta**: aposta na descida do BTC/USD. Se o preço descer, ganha; se subir, perde. **Exemplo**: Bitcoin a $100.000, abre uma posição curta com 10.000 sats e uma alavancagem de 10×. Se o Bitcoin cair para $95.000 (-5%), ganha 50%, ou seja, ~5.000 sats. Se o Bitcoin subir para $105.000 (+5%), perde 50%.



A alavancagem (até 100×) amplifica proporcionalmente os ganhos e as perdas. Um mecanismo de **funding rate** (encargos periódicos de 8 em 8 horas) equilibra as posições longas e curtas. Pode gerir até 100 posições de futuros em simultâneo.



**Opções**



Uma opção é como um ** bilhete de lotaria com data de validade**. Paga-se um prémio para apostar na direção do preço do Bitcoin. **Grande vantagem**: nunca se pode perder mais do que o prémio pago, não há liquidação possível.





- Opção de compra (aposta de alta)**: Aposta-se que o Bitcoin subirá acima do preço de exercício antes do vencimento. Ganha se o preço subir, perde apenas o prémio se o preço descer.





- Opção de venda (aposta de baixa)**: Aposta que o Bitcoin vai descer abaixo do preço de exercício. Ganha se o preço descer, perde apenas o prémio se o preço subir.





- Straddle (aposta na volatilidade)**: Compra uma Call E uma Put em simultâneo. Ganha se o Bitcoin fizer um grande movimento em qualquer direção, perde ambos os prémios se o preço permanecer estável.



Limite: 50 posições simultâneas. Ideal para começar a negociar com alavancagem sem receio de liquidação.



**sats ↔ sUSD**: Converta instantaneamente os seus satoshis em dólares sintéticos (sUSD) para se proteger da volatilidade, ou vice-versa para recuperar a exposição ao Bitcoin.



## Acesso à plataforma e criação de conta



### Ir para LN Markets



Aceda a [lnmarkets.com] (https://lnmarkets.com) e clique em "Open App" (Abrir aplicação).



![Page d'accueil LN Markets](assets/fr/01.webp)



### Criar a sua conta



O ecrã de boas-vindas oferece vários métodos de ligação:



![Méthodes de connexion](assets/fr/02.webp)



**Opções disponíveis** :


1. **Registo com um Lightning wallet** (recomendado) : LNURL-auth com Phoenix, Breez, Zeus ou BlueWallet


2. **Registar com o e-mail**: conta clássica (limita a experiência Lightning)


3. **Alby** ou **Ledger**: extensões do browser



### Ligação via Lightning (LNURL-auth)



Clique em "Registar com um Lightning wallet". Digitalize o código QR com o seu wallet Lightning :



![QR code LNURL-auth](assets/fr/03.webp)



O seu wallet assina automaticamente um pedido criptográfico e a sua conta é criada instantaneamente, sem e-mail ou palavra-passe. Segurança forte e anonimato total.



### Configuração inicial



![Configuration post-connexion](assets/fr/04.webp)



**Parâmetros disponíveis** :




- Nome de utilizador**: personalize o seu nome de utilizador
- Levantamentos automáticos**: ativar os levantamentos automáticos para o seu wallet após o fecho da negociação
- Autenticação de dois factores**: segurança melhorada com 2FA
- Documentação**: aceder aos recursos oficiais



## Visita ao Interface



A interface do LN Markets está organizada em várias secções acessíveis a partir do menu lateral:



### Painel de controlo



![Dashboard](assets/fr/06.webp)



Apresenta o seu desempenho por tipo de produto (Futuros Cruzados, Futuros Isolados, Opções) com P&L, volumes negociados e o seu Address Lightning pessoal (por exemplo, `pivi@lnmarkets.com`).



### Perfil



![Profil trader](assets/fr/07.webp)



Estatísticas pormenorizadas: número de transacções, tipo de negociante (SCALPER, etc.), duração média da posição, repartição Longa/Curta, taxa de ganhos, médias (quantidade, margem, alavancagem) e estrutura progressiva das comissões em função do volume.



### Comércio



![Historique des trades](assets/fr/08.webp)



O separador Negociações apresenta um histórico completo das suas posições, com todas as métricas importantes: data de criação, direção (Longa/Curta), tamanho da posição (quantidade), margem comprometida, preço de entrada e saída, lucros/perdas realizados (P&L) e comissões de negociação. Pode filtrar por tipo de produto (futuros/opções) e exportar os seus dados para análise externa ou contabilidade.



### Definições



![Paramètres de la plateforme](assets/fr/05.webp)



O separador Definições tem dois separadores: **Conta** e **Interface**.



*separador *Conta**:



Gestão de contas com campos editáveis :




- Nome de utilizador**: altere o seu nome de utilizador (por exemplo, "pivi") com o botão "Atualizar"
- E-mail**: adicionar/editar o seu endereço de e-mail
- Endereço de depósito de bitcoin**: o endereço de bitcoin que pode utilizar para depositar fundos on-chain.



**Três alternâncias de configuração** :




- Aparecer nas tabelas de classificação**: escolher se quer ou não aparecer nas tabelas de classificação públicas
- Utilizar endereços Taproot**: utilizar endereços Bitcoin Taproot para depósitos/retiradas on-chain
- Ativar levantamentos automáticos**: ativar levantamentos automáticos para o seu wallet Lightning após o fecho da negociação



**Migração de conta**: Secção que lhe permite migrar a sua conta Lightning para a autenticação clássica de e-mail/palavra-passe.



**Gestão Session**: botão "Limpar sessão e dados locais" para desligar e limpar os dados do browser local.



*separador *Interface**:



Personalize a experiência do utilizador com sete botões de alternância:




- Ignorar confirmação da ordem**: desativar o modal de confirmação antes da execução da transação (negociação rápida)
- Mostrar dicas de ferramentas**: mostra dicas de ferramentas quando se passa o rato sobre elementos
- Modo privado (oculta dados sensíveis)**: oculta quantidades e dados sensíveis na interface (modo de privacidade)
- Mostrar PL líquido no perfil**: mostrar o lucro/perda líquido no seu perfil público
- Utilizar ícones de unidade**: apresenta ícones para unidades monetárias (sats, $)
- Ativar as notificações sonoras**: ativar as notificações sonoras para eventos de negociação
- Ativar as notificações do ambiente de trabalho**: ativar as notificações do ambiente de trabalho do sistema operativo



### Wallet



![Wallet](assets/fr/09.webp)



Saldos em Bitcoin e em USD sintético com histórico de depósitos, levantamentos, transferências cruzadas, swaps, financiamentos e gestão de endereços on chain.



### API



![API V3](assets/fr/10.webp)



O LN Markets oferece um API REST completo (V2 e V3) para automatizar totalmente a sua negociação através de scripts ou bots. Pode criar chaves API com permissões personalizáveis (apenas leitura, negociação, levantamentos) diretamente a partir da interface. Os SDKs oficiais TypeScript e Python estão disponíveis para uma fácil integração. A documentação completa do API V3 está disponível em [api.lnmarkets.com/v3] (https://api.lnmarkets.com/v3).



## Primeiro depósito de fundos



Clique em "Depositar". Estão disponíveis três métodos:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: ler o código QR com o seu wallet Lightning


2. **Invoice**: introduzir um montante e digitalizar a fatura relâmpago


3. **On-Chain**: depósito Bitcoin on chain



## A negociação na prática



### Negociar Futuros Longos: apostar na subida



No painel de controlo, clique em "Futuros" e depois em "Isolados". Clique em **"Comprar "** para abrir uma posição longa.



![Interface Futures Long](assets/fr/12.webp)



Clique no ícone **calculadora** ao lado do botão "Comprar" para visualizar a calculadora de posições:



![Calculateur de position Long](assets/fr/13.webp)



**Exemplo concreto** :




- Quantidade**: $100 (tamanho da posição)
- Margem comercial**: 12.336 sats (margem comprometida)
- Alavancagem**: 7.73× (cada variação de 1% BTC = 7,73% sobre o seu capital)
- Preço de entrada** : $104,863.5
- Liquidação**: $92.852 (preço crítico de liquidação automática)
- Preço de saída**: $110.000 (para cálculo do lucro)
- PL** : 4,492 sats (lucro se sair a $110,000)



**Cenários** :




- Aumento de +4,9%** ($110.000) : +4.492 sats de lucro (+36,4%)
- Neutro** ($104,863) : -185 sats (apenas taxas)
- Descida de -11,5%** ($92.852): liquidação total (-100%)



Clique no botão "Comprar" para confirmar a transação. **Dois casos possíveis** :





- Se tiver liquidez suficiente** na sua conta: é apresentado diretamente um modal de confirmação (imagem abaixo). Clique em "Sim" para executar a transação instantaneamente.



![Confirmation trade Long](assets/fr/14.webp)





- Se não tiver dinheiro suficiente**: é apresentado um código QR Lightning. Digitalize-o com o seu wallet Lightning para pagar a margem necessária. A transação abre-se automaticamente após a receção do pagamento



### Negociar Futuros a descoberto: apostar no lado negativo



Clique em **"Sell "** para abrir uma posição curta (ganha se o preço descer). Abra a calculadora com o ícone da calculadora para definir a sua posição:



![Calculateur de position Short](assets/fr/15.webp)



Clique em "Vender" para confirmar. Quanto à Longa, **dois casos possíveis**:





- Se tiver dinheiro suficiente**: modo de confirmação direta, clique em "Sim"
- Se não tiver dinheiro suficiente**: é apresentado um código QR Lightning (imagem abaixo). Digitalize-o com o seu wallet Lightning para pagar a margem necessária:



![Paiement Lightning pour Short](assets/fr/16.webp)



Assim que o pagamento Lightning for recebido, a sua posição curta abre-se automaticamente. Pode então geri-la a partir da interface de negociação.



#### Encerrar uma posição



Para fechar a sua posição (longa ou curta), clique na **pequena cruz no canto inferior direito** da interface de gestão:



![Interface de clôture](assets/fr/17.webp)



É apresentada uma caixa de diálogo de confirmação para confirmar o fecho da transação:



![Confirmation clôture](assets/fr/18.webp)



O modal apresenta o seu P&L atual (lucros ou perdas). Clique em "Sim" para fechar. O saldo é instantaneamente adicionado (lucro) ou deduzido (perda) do seu Wallet através do Lightning.



### Opções de negociação Call: direito condicional de compra



As opções oferecem **risco limitado** ao prémio pago, sem possibilidade de liquidação. Uma Call dá-lhe o direito (não a obrigação) de comprar o Bitcoin ao preço de exercício antes da expiração. Ao contrário dos futuros, nunca se pode perder mais do que o prémio investido.



No painel de controlo, clique em "Opções" e, em seguida, selecione o separador "Chamada".



![Interface Options Call](assets/fr/19.webp)



Configure a sua transação com os seguintes parâmetros:




- Quantidade**: $100 (tamanho do seu contrato)
- Validade** : 2025-11-15 (data de expiração)
- Strike**: $96.000 (preço alvo)



Os outros campos são calculados automaticamente:




- Margem**: 1.045 sats (prémio a pagar, o seu investimento)
- Breakeven**: $96,923 (preço para recuperar a sua aposta)
- Delta**: 40 (sensibilidade do preço do Bitcoin)



**Como calcular o seu prémio?



O seu lucro depende do preço do Bitcoin no final do prazo. Fórmula: **(Preço BTC - Strike) × Tamanho Contract - Prémio pago**.



**Exemplos concretos** :





- Bitcoin a $96.000** (preço atual) : Valor intrínseco = $0. **Perda: -1,045 sats** (perde o prémio)





- Bitcoin a $97.000**: Valor intrínseco = (97.000 - 96.000) × 0,00105 BTC = $1,05. Convertido para sats ≈ 2,175 sats. **Lucro: 2.175 - 1.045 = +1.130 sats** (+108% de ganho)





- Bitcoin a $98.000**: valor intrínseco = $2.000 ≈ 3.224 sats. **Lucro: +2.179 sats** (+208% de ganho)





- Bitcoin a $100.000**: valor intrínseco = $4.000 ≈ 5.263 sats. **Lucro: +4.218 sats** (+403% de ganho)





- Bitcoin abaixo de $96.000**: A opção expira sem valor. **Perda limitada: -1.045 sats**, sem possibilidade de liquidação



Clicar em "Comprar compra". Aparece uma caixa de diálogo de confirmação:



![Confirmation Call option](assets/fr/20.webp)



Clique novamente em "Buy Call" para confirmar. A opção aparece em "Opções em curso". No vencimento, o LN Markets calcula automaticamente o valor intrínseco e ajusta o seu lucro/perda.



**Nota sobre as opções de venda** : O funcionamento é idêntico ao de uma Call, mas ao contrário. Com uma Put, aposta-se que o preço do Bitcoin vai **descer**. Se o Bitcoin descer abaixo do seu strike, ganha; se ficar acima, perde apenas o prémio pago. O cálculo dos ganhos segue a mesma lógica: **(Strike - preço BTC) × tamanho do Contract - Prémio pago**.



### Levantamento do fundo relâmpago



Clique em "Levantar":



![Modal de retrait](assets/fr/21.webp)



**Métodos** : LNURL, Invoice, Lightning Address, On-Chain.



**Procedimento Invoice** :


1. Gerar uma fatura Lightning a partir do seu wallet


2. Copiar a fatura (começa com `lnbc...`)


3. Colar no campo LN Markets


4. Confirmar a retirada


5. O seu wallet é creditado em 1-3 segundos



Sem comissões de levantamento no Lightning, apenas custos de encaminhamento mínimos (<0,1% na prática).



## Riscos e melhores práticas



**Principais riscos** :




- Liquidação total**: uma alavancagem elevada pode anular 100% da margem em minutos
- Serviço experimental**: fase alfa, incertezas tecnológicas
- Risco de contraparte**: a plataforma continua a ser a única contraparte



**Melhores práticas** :



1. **Gestão do capital**: adotar uma estratégia de gestão do risco adaptada ao seu perfil. Por exemplo: afetar 5% dos seus activos totais à negociação alavancada e arriscar um máximo de 1% deste capital por transação (por exemplo: 1 ativo BTC → 5M sats para negociar → 50k sats risco máximo por posição)



2. **Stop-loss sistemático**: configure stop-losses para limitar as suas perdas por transação. Com uma regra de risco de 1%, por exemplo, mesmo 10 transacções perdedoras consecutivas representam apenas 10% do seu capital de negociação



3. **Comece com pouco**: teste primeiro com alguns milhares de satss para compreender os mecanismos antes de aplicar a sua estratégia de gestão de capital



4. **Retire regularmente os seus lucros**: garanta os seus lucros no seu wallet principal, deixando apenas o capital de negociação ativo na plataforma



5. **Cuidado com a alavancagem**: evite uma alavancagem >20×, a menos que esteja plenamente consciente dos riscos de liquidação



**Custos**: sem taxas de depósito/levantamento Lightning, spread ~0,1% por transação (descendo para 0,06% dependendo do volume).



## Vantagens e limitações



**Vantagens** :




- Sem custódia (controlo total excluindo períodos de negociação)
- Sem KYC (anonimato via Lightning/Nostr)
- Liquidações instantâneas (depósitos/levantamentos em segundos)
- Execução sem derrapagem com agregação de liquidez
- API público e Nostr de apoio



**Limitações** :




- Serviço alfa (possíveis evoluções)
- Liquidez inferior à da Binance/Deribit
- Proibido a residentes nos EUA



## Conclusão



O LN Markets representa uma grande evolução do comércio do Bitcoin, integrando nativamente o Lightning Network para devolver o controlo aos utilizadores. Para bitcoiners experientes que procuram especular sem comprometer a sua soberania, é uma alternativa única às trocas centralizadas tradicionais.



A plataforma continua a evoluir com futuros lineares USDT e negociação sem custódia através de Contratos de Registo Discreto (DLC) em desenvolvimento. Ao aplicar boas práticas de gestão de risco (pequenos montantes, stop-loss, levantamentos regulares), o LN Markets torna-se uma ferramenta poderosa para explorar a alavancagem do Bitcoin de forma responsável.



Comece com pouco, teste com alguns milhares de satss e explore gradualmente esta nova fronteira do Lightning Network. Feliz comércio soberano ⚡️!



## Recursos





- [Sítio Web oficial do LN Markets](https://lnmarkets.com)
- [Documentação](https://docs.lnmarkets.com)