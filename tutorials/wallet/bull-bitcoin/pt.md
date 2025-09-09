---
name: Touro Bitcoin Wallet
description: Saiba como utilizar o Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Este guia leva-o através da instalação, configuração e utilização do Bull Bitcoin Mobile. Aprenderá a receber e a enviar fundos nas três redes: onchain, Liquid e Lightning, e a transferir o seu Bitcoin de uma rede para outra. Os anexos fornecem recursos e contactos, informações de base e breves explicações de conceitos técnicos.



## Introdução



*o *Bull Bitcoin Mobile**, desenvolvido pela **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)), é um **self-custodial** Bitcoin Wallet, o que significa que tem controlo total sobre as suas chaves privadas e, consequentemente, sobre os seus fundos, sem depender de terceiros. De código aberto e enraizado numa filosofia Cypherpunk, este Wallet combina simplicidade, confidencialidade e caraterísticas avançadas, tais como trocas entre redes e suporte PayJoin. Permite-lhe gerir os seus bitcoins em três redes: **Bitcoin onchain**, **Liquid** e **Lightning**, cada uma adaptada a utilizações específicas.



### Contexto de desenvolvimento



O Wallet responde a um desafio importante: As tarifas da rede Bitcoin não são adequadas para pequenos pagamentos ou para a abertura de pequenos canais Lightning auto-hospedados. O Wallet Bull Bitcoin Mobile oferece uma solução de auto-custódia, apoiando-se nas 3 principais redes Bitcoin:





- Rede Bitcoin (onchain)**: Ideal para armazenamento a médio e longo prazo de UTXOs e transacções de grande valor, onde as taxas são proporcionalmente insignificantes.
- Liquid Network**: Concebido para transacções rápidas (~2 minutos), mais confidenciais (montantes ocultos) e de baixo custo, perfeito para acumular pequenos montantes ou proteger a sua privacidade.
- Rede Lightning**: Optimizada para pagamentos instantâneos e de baixo custo, adequada para transacções diárias de pequeno e médio valor.



Com o Bull Bitcoin Mobile, por exemplo, pode acumular pequenos montantes nas carteiras **Liquid** ou **Lightning** e depois, quando tiver atingido um montante significativo, pode :





- Transferência para a rede onchain para armazenamento seguro a médio ou longo prazo, com maior confidencialidade com Liquid e/ou Lightning a montante, e com taxas onchain para uma única transação



### Evolução contínua



O Wallet está em constante evolução, por isso não se surpreenda se encontrar discrepâncias entre este tutorial e a sua aplicação actualizada.




- Por exemplo, a partir de 19/07/2025, os botões **"Comprar / Vender / Pagar "** estão visíveis mas a cinzento na aplicação, uma vez que estas opções, disponíveis em Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel), serão em breve integradas para uma experiência unificada. A sua utilização continuará a ser totalmente opcional. Muitos outros desenvolvimentos estão em curso ou planeados: gestão multi-Wallet, passphrase, compatibilidade com carteiras de hardware...
- No [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), pode consultar os tópicos actuais e os próximos desenvolvimentos. Como o projeto é 100% open-source e "construído em público", pode também enviar-nos as suas sugestões e quaisquer bugs que encontre.




## 1. Pré-requisitos



Antes de começar a utilizar o **Bull Bitcoin Mobile**, certifique-se de que possui os seguintes itens:





- Smartphone compatível**: Um dispositivo **iOS** (iPhone ou iPad) ou **Android**
- Ligação à Internet
- Suportes de cópia de segurança seguros**: Escreva a sua **frase de recuperação** (12 palavras) em papel ou metal e guarde-a num local seguro.
- Conhecimentos básicos**: É útil ter um conhecimento mínimo dos conceitos Bitcoin (endereços, transacções, taxas), embora este tutorial explique cada passo para principiantes.



## 2. Instalação





- Descarregar a candidatura** :
 - [Google Play Store] (https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Descarregar a partir da loja de aplicações para dispositivos Android
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Descarregar diretamente o APK para dispositivos Android**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Descarregar através do TestFlight para dispositivos Apple
 - Verifique o nome do programador (Bull Bitcoin) para evitar aplicações fraudulentas.
 - Certifique-se de que a versão descarregada corresponde à última versão estável indicada no GitHub.
 - O Bull Bitcoin Mobile é **open-source**. Para ver o código: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Instalar a aplicação




## 3. Configuração inicial



### 3.1 Lançar a aplicação :



A aplicação utiliza uma frase de recuperação única de 12 palavras para ambas as carteiras:




 - seguro Bitcoin' Wallet**: Para transacções na rede Bitcoin (onchain)
 - pagamentos instantâneos" Wallet**: Para transacções instantâneas nas redes Liquid e Lightning



Ao abrir, é-lhe pedido que importe uma frase de recuperação existente ou que crie um novo Wallet :



![image](assets/fr/02.webp)



### 3.2 Frase de recuperação :



Se pretender reutilizar um Wallet existente, clique em "**Recuperar Wallet**" e preencha as 12 palavras da sua frase de recuperação.



Caso contrário, clique em "**Criar novo Wallet**" :




- Escreva a sua frase de recuperação com o máximo cuidado. Escreva-a em papel ou metal e guarde-a num local seguro (cofre, local offline). Esta frase é o único meio de aceder aos seus bitcoins em caso de perda do seu dispositivo ou de eliminação da aplicação.
- Também é importante notar que qualquer pessoa com esta frase pode roubar todos os seus bitcoins. Nunca as armazene digitalmente:
 - Sem captura de ecrã
 - Sem cópias de segurança na nuvem, por correio eletrónico ou por mensagens
 - Sem copiar/colar (risco de guardar na área de transferência)



**! Este ponto é crítico**. Para mais assistência :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Garantir o acesso :





- Aceda às definições e clique em **Código PIN**.
- Configurar um código **PIN** robusto para proteger o acesso à aplicação.
- Este passo é opcional, mas fortemente recomendado para evitar que alguém com acesso ao seu telemóvel tenha acesso ao seu Wallet.



![image](assets/fr/03.webp)



### 3.4 Ligação a um nó pessoal (opcional):



O BullBitcoin Wallet liga-se aos servidores Electrum por defeito: o primeiro gerido pelo Bull Bitcoin e um servidor secundário da Blockstream, ambos considerados como não guardando registos, o que reduz o risco de rastreio.



Para uma maior confidencialidade, pode ligar a aplicação ao seu próprio nó Bitcoin através de um servidor Electrum (instruções disponíveis no [GitHub da BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Receber fundos



A receção de fundos com **Bull Bitcoin Mobile** é simples e adaptada às suas necessidades, quer utilize :




  - a rede **Bitcoin (onchain)** para a conservação a longo prazo,
  - a rede **Liquid** para um Confidential Transactions mais rápido,
  - a rede **Lightning** para pagamentos instantâneos e de baixo valor.



A aplicação gera automaticamente endereços de receção Lightning ou Invoice, consoante a rede selecionada. Eis como proceder para cada rede.



### 4.1. onchain (rede Bitcoin)



No ecrã inicial, pode :




- ou selecionar o **Secure Bitcoin Wallet** e clicar em "**Receive "** :



![image](assets/fr/04.webp)





- ou clicar em "**Receber "**, e depois escolher a rede **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opção "Copiar ou digitalizar apenas Address" desactivada (predefinição)



![image](assets/fr/06.webp)





- Esta opção dá acesso a parâmetros avançados opcionais. Pode especificar :
 - Uma **montante** em BTC, Sats ou moeda fiduciária.
 - Uma **nota pessoal** a incluir na cópia do código URI / QR.
 - Ativação do **PayJoin** (ver Apêndice 3 para mais pormenores), que melhora a confidencialidade ao combinar as entradas do remetente e do destinatário.





- Exemplo de um URI gerado automaticamente** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Utilização**: Copie o URI para partilhar com o remetente ou deixe-o digitalizar o código QR.



#### 4.1.2. Opção "Copiar ou digitalizar apenas Address" activada



![image](assets/fr/07.webp)





- Com a opção **"Copiar ou digitalizar apenas Address"** activada, a aplicação gera um Bitcoin Address simples no formato SegWit (bech32).





- Exemplo:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Mesmo que introduza um montante ou uma nota, estes não serão incluídos no código QR ou na cópia do Address





- Utilização**: Copie o Address para o partilhar com o remetente ou deixe-o ler o código QR.



#### 4.1.3. Geração de um novo Address





- Porquê utilizar um novo Address para cada transação? Isto **protege a sua privacidade** ao impedir que vários pagamentos sejam associados ao mesmo Address e limita as possibilidades de rastreio no Blockchain.
 - Por defeito, o Bull Bitcoin gera automaticamente um Address.** não utilizado
 - Pode forçar a criação de um novo Address clicando em **"New Address"** na parte inferior do ecrã.
 - Todos os seus endereços estão ligados à sua frase seed: independentemente do número de endereços que utilize, a sua carteira apresentará um único saldo e pode consolidar automaticamente os fundos quando é efectuado um envio.





- Dica: Utilize sempre o novo Address** fornecido pelo Bull Bitcoin, exceto se tiver uma necessidade específica (por exemplo, um Address público para receber donativos).



### 4.2. Liquid



No ecrã inicial, pode :




- ou selecionar o **Pagamentos instantâneos Wallet** e clicar em **"Receber "** e depois em **"Liquid"** :



![image](assets/fr/08.webp)





- ou clicar em "**Receber "** e, em seguida, selecionar a rede **Liquid**:



![image](assets/fr/09.webp)



Quando estiver no ecrã **"Receber "**, copie um Liquid Address:





- Sem montante ou nota. Exemplo:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Ou especificando um **montante** (em BTC, Sats ou fiat) e/ou uma **notícia pessoal** a incluir na cópia do URI / QR Code. Exemplo:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Utilização**: Copie o Address/URI para partilhar com o remetente ou deixe-o ler o código QR.



### 4.3. Relâmpagos



No ecrã inicial, pode :




- ou selecionar o **Pagamentos instantâneos Wallet** e clicar em "**Receber "** :



![image](assets/fr/10.webp)





- ou clicar em "**Receber "**, e depois escolher a rede **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Funcionamento, limites e vantagens





- Mecanismo**: O Bull Bitcoin Wallet é um Wallet que permite efetuar e receber pagamentos via Lightning. Os fundos recebidos via Lightning são armazenados na rede **Liquid** (no Wallet Instant Payments) graças a uma troca automática via **Boltz**. Isto permite-lhe interagir com o Lightning sem ter de gerir canais de liquidez, mantendo-se em auto-custódia.





- Limites:**
 - Um montante mínimo** de 100 satoshis (a partir de 19/07/2025) quando se utiliza o generate ou o Invoice.
 - Os custos** são pagos por si, sendo deduzidos do montante enviado pelo remetente, ao contrário da receção com o Wallet Lightning native, em que apenas o remetente paga os custos de transferência para além do montante enviado. Em 19/07/2025, 47 Sats são deduzidos do montante enviado.





- Benefícios** :
 - Auto-custodial**: Os seus fundos permanecem sob o seu controlo, armazenados no Liquid Network.
 - Sem altas taxas onchain**: O armazenamento no Liquid evita depósitos onchain dispendiosos para abrir o seu canal Lightning ou adicionar liquidez. Estas operações podem ser efectuadas mais tarde, quando o montante acumulado no Liquid justificar as taxas.





- Dica:** Se o remetente tiver o Wallet Bull Bitcoin, utilize o Liquid Network diretamente para evitar taxas de troca



#### 4.3.2. generate Invoice





- Introduzir um **montante** (em BTC, Sats ou moeda fiduciária)





- Acrescentar uma **nota pessoal** que será integrada no Invoice. Se o remetente pagar o Invoice, o seu Wallet também o incluirá nos detalhes da transação.





- Validade do Invoice:** O Lightning Invoice é válido durante **12 horas**. Após este período, expira e já não pode ser pago. Deve ser gerado um novo Invoice.





- Utilização**: Copie o Invoice para o partilhar com o remetente ou deixe-o ler o código QR.




## 5. Envio de fundos



### 5.1. Princípio de base



A partir da página inicial ou das carteiras :



![image](assets/fr/12.webp)



para aceder ao ecrã de envio:



![image](assets/fr/13.webp)



*o *Bull Bitcoin Mobile** facilita o envio de dinheiro, detectando automaticamente a rede (Bitcoin, Liquid ou Lightning) com base no Address ou Invoice introduzido (copiado ou digitalizado através do código QR).



### 5.2. transmissão em cadeia (rede Bitcoin)



#### 5.2.1. Ecrã de envio



**Ação**: Introduzir ou digitalizar um Bitcoin na cadeia Address





- Se o montante não tiver sido definido, por exemplo :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Em seguida, pode escolher no ecrã de envio :
 - Montante em BTC, sat ou fiat. Montante mínimo: 546 satoshis em 22/07/2025.
 - Uma nota opcional para identificar a transação. Apenas visível para si, nos detalhes da transação.



![image](assets/fr/14.webp)





- Se o montante já tiver sido definido, por exemplo :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Será então encaminhado diretamente para o ecrã de confirmação abaixo.



#### 5.2.2 Ecrã de confirmação



Verifique todos os parâmetros, especialmente o montante, o destino Address e as taxas.


Em seguida, pode ajustar os parâmetros:



![image](assets/fr/15.webp)




- Taxas**: Pode escolher :
  - A velocidade de execução** da sua transação e as taxas associadas serão estimadas
  - As taxas**, no modo Taxas absolutas (taxas totais em satoshis) ou Taxas relativas (taxas por byte), e a velocidade da sua transação serão estimadas





- Definições avançadas** :





 - Replace-by-fee (RBF)** : Activada por defeito, esta função acelera a transação mediante o pagamento de uma taxa mais elevada (ver Apêndice 4 para mais pormenores).





 - Seleção manual do UTXO**: Se os fundos estiverem armazenados em vários endereços Wallet diferentes, é possível selecionar os endereços a partir dos quais os fundos devem ser enviados. Porquê fazer isto? Com a crescente adoção do Bitcoin, as taxas de transferência estão a aumentar. Enviar a partir de vários endereços com pequenos montantes é mais caro do que enviar a partir de um único Address, mas fazê-lo agora evita ter de o fazer mais tarde, quando as taxas serão ainda mais elevadas. A isto chama-se **consolidação do UTXO**



![image](assets/fr/16.webp)





- Envio com PayJoin**: Se a função tiver sido activada pelo destinatário que forneceu o URI, por exemplo, :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Em seguida, o Bull Bitcoin Mobile configurará o envio combinando os seus UTXOs com os UTXOs do destinatário como entrada, melhorando a confidencialidade (ver Apêndice 3 para mais pormenores).



### 5.3. Enviar para Liquid



#### 5.3.1 Ecrã de envio



A rede **Liquid** permite transacções rápidas (~2 minutos graças a um bloco por minuto), mais confidenciais (montantes mascarados) do que na rede onchain, e com taxas muito baixas. Os fundos são retirados do **Instant Payments Wallet**.



**Ação**: Introduzir ou digitalizar um Liquid Address





- Se o montante não tiver sido definido, por exemplo :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Em seguida, pode escolher no ecrã de envio :




- Montante em BTC, sat ou fiat. Sem mínimo, 1 Satoshi possível;
- Uma nota opcional para identificar a transação. Apenas visível para si, nos detalhes da transação.



![image](assets/fr/17.webp)





- Se o montante já tiver sido definido, por exemplo :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Será então encaminhado diretamente para o ecrã de confirmação abaixo.



#### 5.3.2 Ecrã de confirmação



Verificar com tempo todos os parâmetros, especialmente a quantidade e o destino do Address.



![image](assets/fr/18.webp)





- Taxas**: Proporcionais à complexidade da transação, geralmente numa base de 0,1 sat/vB, ou seja, 20-40 satoshis para uma transação simples (33 Sats em 22/07/2025).



### 5.4. Enviar para o Lightning



#### 5.4.1 Ecrã de envio



A rede **Lightning** permite pagamentos instantâneos e de baixo custo para pequenos montantes, ideal para pequenas transacções diárias.



**Ação**: Introduzir ou digitalizar um Lightning Invoice





- Se digitalizar um LN-URL Address que permite definir a quantidade


Exemplo: `orangepeel@walletofsatoshi.com`.


depois pode escolher no ecrã de envio :




 - Montante em BTC, sat ou fiat. Montante mínimo de 1000 satoshis em 23/07/2025
 - Uma nota opcional para identificar a transação. Será enviada ao destinatário.



![image](assets/fr/19.webp)





- Se digitalizar um Lightning Invoice que contenha uma quantidade definida


Exemplo:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Será então encaminhado diretamente para o ecrã de confirmação abaixo.



Nota: o montante deve ser superior a 21 Sats em 23/07/2025



#### 5.4.2 Funcionamento, limites e vantagens





- Mecanismo**: Os fundos são retirados do **Instant Payments Wallet** (Liquid) e convertidos através de um **Liquid → Lightning** swap com **Boltz**.





- Limites:**
 - Um montante mínimo** superior a um Wallet Lightning native (ver acima)
 - Despesas** mais Liquid → Troca de raios via Boltz





- Benefícios** :
 - Auto-custodial**: Os seus fundos permanecem sob o seu controlo, armazenados no Liquid Network e transferíveis através do Lightning, se necessário
 - Sem altas taxas onchain**: O armazenamento no Liquid poupou-lhe depósitos onchain dispendiosos para abrir o seu canal Lightning ou adicionar liquidez. Estas operações podem ser efectuadas mais tarde, quando o montante acumulado no Liquid justificar as taxas.





- Sugestão:** Se o destinatário tiver o Wallet Bull Bitcoin, utilize o Liquid Network diretamente para evitar custos de troca



#### 5.3.3 Ecrã de confirmação



Verificar com calma todos os parâmetros, nomeadamente o montante e o destino do Address.



![image](assets/fr/20.webp)




## 6. Ver histórico



*o *Bull Bitcoin Mobile** facilita o acompanhamento das suas transacções nas redes **Bitcoin (onchain)**, **Liquid** e **Lightning**. O histórico pode ser acedido de duas formas e apresenta informações detalhadas para cada tipo de transação. Também pode verificar as suas transacções utilizando navegadores de blocos externos.



### 6.1. Histórico de acesso





- Através do ecrã inicial** :
 - Clique em **Secure Bitcoin Wallet** para ver as transacções **onchain**, ou em **Instant Payments Wallet** para as transacções **Liquid** e **Lightning**.
 - O histórico é apresentado diretamente abaixo do total da carteira, filtrado de acordo com o tipo de Wallet selecionado.



![image](assets/fr/21.webp)





- Através da página dedicada** :
 - No ecrã inicial, clique no símbolo **histórico** (ícone do relógio ou semelhante).
 - Aceder a uma página que lista todas as transacções, com filtros por tipo de ação: **Enviar**, **Receber**, **Trocar**, **PayJoin**, **Vender**, **Comprar** (nota: Vender e Comprar estão em desenvolvimento e não estão disponíveis neste momento, 20 de julho de 2025).



![image](assets/fr/22.webp)



### 6.2. Detalhes da transação



Cada transação apresenta informações específicas consoante a rede e o tipo de ação (envio ou receção). Eis os detalhes disponíveis para uma **transação onchain** :



![image](assets/fr/23.webp)



### 6.3. Controlo via Block explorer



A lista de exploradores para as redes **Bitcoin onchain**, **Liquid** e **Lightning** encontra-se no Apêndice 4.



Para **Lightning**, as transacções não são visíveis em navegadores públicos. Verificar os detalhes (incluindo a ID de troca para Boltz) na aplicação.




## 7. Definições



A página "Definições" pode ser acedida diretamente a partir da página inicial da aplicação Bull Bitcoin e é utilizada para configurar e gerir vários aspectos da carteira e da experiência do utilizador.



![image](assets/fr/24.webp)





- Wallet Backup**: Exibe a frase de recuperação do portfólio para backup seguro. Consulte a secção 3. sobre a criação do portfólio para obter as melhores práticas de gestão e armazenamento da frase de recuperação.





- Wallet Detalhes** :
 - Pubkey**: Chave pública associada ao Wallet, utilizada para endereços de receção generate Bitcoin.
 - Caminho de derivação**: Caminho de derivação utilizado para endereços generate Wallet a partir da chave privada.





- Servidor Electrum (Nó Bitcoin)**: Configurar uma ligação a um nó Bitcoin personalizado para transacções onchain.





- Código PIN**: Ativar e/ou modificar o código de segurança para proteger o acesso à aplicação e às funções do Wallet.





- Moeda**: Escolha se pretende apresentar os montantes em BTC ou Sats e a moeda fiduciária predefinida (dólar, euro, etc.).





- Configurações de Auto Swap**: A função _Auto Swap_ permite-lhe automatizar a transferência do seu BTC do **Instant Payments Wallet (Liquid)** para o seu **Bitcoin On-Chain** Wallet, assim que o montante atingir um limite que considere suficientemente elevado para justificar a taxa de transação.





- Registos**: Registos de atividade visualizáveis, que podem ser partilhados com a assistência técnica para facilitar a resolução de problemas.





- Acesso ao Telegram para apoio** : Ligação direta ao canal oficial do Telegram para assistência ao utilizador.





- Acesso ao Github** : Ligação ao [repositório Github do Bull Bitcoin] (https://github.com/SatoshiPortal) para visualizar o código-fonte aberto ou comunicar problemas.




## APÊNDICES



### A1. Explicação do PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definição** :




- O PayJoin, ou **Pay-to-EndPoint (P2EP)**, é uma técnica de transação do Bitcoin que aumenta a confidencialidade na rede **onchain**. Combina as entradas do remetente e do destinatário numa única transação, tornando os montantes e os endereços mais difíceis de rastrear.



**Funcionamento




- Numa transação PayJoin, o remetente e o destinatário trabalham em conjunto através de um servidor PayJoin compatível para generate uma transação conjunta.
- Em vez de ser apenas o emissor a fornecer entradas (UTXO), o recetor também contribui com um dos seus próprios UTXOs. Esta situação confunde a informação visível no Blockchain: em vez de uma única entrada correspondente ao montante real, existem agora duas entradas e as saídas não reflectem diretamente o montante trocado.
- A transação final assemelha-se a uma transação Bitcoin normal (multi-input/multi-output), mas oculta o montante real enviado e as ligações entre endereços graças a uma estrutura esteganográfica.



**Para utilização no Bull Bitcoin Mobile**




- Receber** (Address Supply): O PayJoin está ativado por predefinição.
- Enviar** : O Wallet detecta automaticamente um URI PayJoin e configura a transação em conformidade, por exemplo:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Benefícios




- Confidencialidade reforçada**: O PayJoin invalida o pressuposto de que todas as entradas numa transação pertencem a uma única entidade. Com o PayJoin, as entradas provêm tanto do emissor como do recetor, quebrando este pressuposto.
- Mascaramento do montante** : O montante real trocado não aparece diretamente nos resultados. É calculado como a diferença entre o UTXO de entrada e de saída do destinatário, o que torna a análise enganadora.



**Limites




- O PayJoin exige que o remetente e o destinatário utilizem carteiras compatíveis, caso contrário é utilizada uma transação onchain normal.
- A transação é ligeiramente mais complexa (mais entradas e saídas), o que resulta em custos ligeiramente mais elevados.
- Embora concebida para se assemelhar a uma transação normal, a heurística avançada (por exemplo, resultados ambíguos, servidores PayJoin conhecidos) pode levar a suspeitar da sua utilização, embora sem certeza absoluta.



**Mais informações:**




- [Glossário] (https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Explicação do Replace-by-fee (RBF)



**Definição**: O Replace-by-fee (RBF) é uma caraterística da rede Bitcoin que permite ao remetente acelerar a confirmação de uma transação **onchain** ao concordar em pagar uma taxa mais elevada.



**Limites** :




- O RBF não está disponível para transacções Liquid ou Lightning.
- A transação inicial deve ser marcada como compatível com RBF quando é criada, o que o Bull Bitcoin Mobile faz automaticamente, a menos que seja desativado.



**Mais informações:**




- [Glossário] (https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Melhores práticas



Para utilizar o **Bull Bitcoin Mobile** de forma segura e eficiente, siga estas recomendações. Elas ajudá-lo-ão a proteger os seus fundos, a otimizar as suas transacções e a preservar a sua confidencialidade nas redes **Bitcoin (onchain)**, **Liquid** e **Lightning**.





- Proteja a sua frase de recuperação** :
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Utilizar autenticação segura** :
 - Ativar um **PIN forte** ou **autenticação biométrica** (impressão digital ou reconhecimento facial) para proteger o acesso à aplicação.
 - Nunca partilhe o seu PIN ou dados biométricos.





- Proteger a sua privacidade** :
 - generate um novo Address para cada receção onchain ou Liquid para limitar o rastreio no Blockchain.
 - Utilizar o PayJoin quando disponível para aumentar a confidencialidade relativamente ao montante enviado na cadeia
 - Para obter a máxima confidencialidade, ligue o seu Wallet ao seu próprio nó Bitcoin através de um servidor Electrum em vez de utilizar o nó público





- Escolha a rede mais adequada às suas necessidades** :
 - Onchain**: Preferido para custódia a longo prazo ou transacções de grande valor (taxas insignificantes em relação ao montante).
 - Liquid**: Utilizar para transferências rápidas e de baixo custo com confidencialidade reforçada.
 - Relâmpago**: Opte por transferências instantâneas e de baixo custo para pequenas quantias. Se forem dois utilizadores Wallet Bull Bitcoin, escolham Liquid para evitar taxas de troca Lightning <> Liquid via Boltz.





- Verificar sempre os endereços de envio** :
 - Antes de enviar fundos, verifique cuidadosamente o Address. Os fundos enviados para um Address incorreto perdem-se para sempre. Utilize copiar/colar ou a leitura de código QR, nunca copie/altere um Address à mão.





- Otimizar os custos** :
 - Para transacções onchain, escolha taxas adequadas (lentas, médias, rápidas) de acordo com a urgência e o congestionamento da rede.
 - Utilizar Liquid, ou Lightning para pequenas quantidades.
 - Ativar o Replace-by-fee (RBF) (ver apêndice 4) para os envios onchain, se prever a necessidade de acelerar a confirmação.





- Manter a aplicação actualizada




### A4. Recursos adicionais





- Ligações oficiais e apoio:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : correio eletrónico de apoio
 - [Sítio Web oficial do Bull Bitcoin](https://bullbitcoin.com/) :** Informações sobre os serviços do Bull Bitcoin, criação de conta, acesso à aplicação
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Ver o código, a evolução e o roteiro, contribuir para o desenvolvimento...
 - [Conta X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Grupo Telegram** para Wallet mobile: chat em grupo com o apoio, ver página "Definições".





- Exploradores de blocos :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Relâmpago: **[1ML (Lightning Network)](https://1ml.com/)**





- Aprendizagem e tutoriais:** **[Plan ₿ Network](https://planb.network/)** :
 - Proteger a sua frase de recuperação



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glossário](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Glossário](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Touro Bitcoin



#### Visão geral da empresa



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, é a mais antiga plataforma não depositária Exchange dedicada exclusivamente ao Bitcoin, fundada em 2013 na Embaixada Bitcoin em Montreal, Canadá. Dirigida por Francis Pouliot, um reconhecido pioneiro no ecossistema Bitcoin, a empresa posiciona-se como um ator-chave na promoção da soberania financeira e da autonomia do utilizador. A sua missão é permitir que os indivíduos recuperem o controlo do seu dinheiro, utilizando o Bitcoin como uma ferramenta de liberdade e pagamento, rejeitando simultaneamente moedas fiduciárias e criptomoedas que não o Bitcoin.



![image](assets/fr/26.webp)



[Crie a sua conta] (https://app.bullbitcoin.com/registration/orangepeel) com 0,25% de desconto nas compras e vendas de Bitcoin.



#### Valores e filosofia



A Bull Bitcoin distingue-se pelos seus princípios Commitment a Cypherpunk e pela sua ética Bitcoin:





- Foco exclusivo no Bitcoin** : A plataforma é fiel à visão de uma moeda descentralizada e resistente à censura.





- Não-custodiante** : Os utilizadores mantêm o controlo total dos seus Bitcoins, enviando fundos para as suas próprias carteiras.





- Confidencialidade**: Recolha minimizada de dados pessoais, com opções de compra sem KYC para transacções inferiores a 999 USD. Os dados são protegidos de acordo com os regulamentos (FINTRAC no Canadá, AMF em França).





- Transparência**: Sem taxas ocultas, os custos estão incluídos no spread (a diferença entre os preços de compra e venda).





- Soberania financeira**: O touro Bitcoin promove a independência dos sistemas bancários tradicionais e das instituições centralizadas.



#### Principais serviços





- Depósito em moeda fiduciária** : Os utilizadores podem financiar a sua conta Bull Bitcoin com moeda fiduciária (CAD, EUR, etc.) através de transferência bancária ou dinheiro/cartão de débito em estações de correio canadianas selecionadas.





- Compra do Bitcoin** : Os utilizadores podem adquirir o Bitcoin que é enviado diretamente para a sua carteira não depositária, garantindo um controlo total dos seus fundos.





- Compra programada de Bitcoin**: O Bull Bitcoin oferece um serviço de compra recorrente automatizada (DCA - Dollar Cost Averaging) em intervalos regulares, utilizando o seu saldo disponível, com transferência direta de Bitcoins para um Wallet controlado pelo utilizador, reduzindo o impacto da volatilidade dos preços.



Note-se que uma opção denominada "AutoBuy" permite-lhe converter os seus fiats assim que estes tocam no seu saldo Bull Bitcoin e enviar os seus Bitcoins para o seu próprio Wallet. Esta opção também pode ser combinada com uma transferência bancária recorrente programada com o seu banco para efetuar uma DCA. Esta opção automatiza a sua acumulação de Bitcoin sem ter de abrir a aplicação.






- Comprar Bitcoin a um preço fixo "Limit Order "**: Permite-lhe comprar Bitcoin a um preço previamente especificado pelo utilizador, que é automaticamente executado quando o preço do índice Bull Bitcoin atinge ou desce abaixo do limite definido.





- Venda de Bitcoin**: Os utilizadores podem vender os seus Bitcoins e receber os fundos em moeda fiduciária diretamente na sua conta bancária através de transferência bancária ou SEPA.





- Pagamentos de terceiros**: O Bull Bitcoin permite aos utilizadores enviar dinheiro fiduciário para contas bancárias a partir dos seus Bitcoins, de forma totalmente transparente para o destinatário.





- Bull Bitcoin Prime**: O Bull Bitcoin Prime é um serviço premium para clientes empresariais e de elevado património líquido, que oferece soluções personalizadas e suporte premium. Isto inclui acesso a taxas reduzidas, um gestor de conta dedicado e serviços empresariais personalizados. Este serviço destina-se a instituições, traders profissionais e clientes empresariais que procuram uma experiência aprofundada e um tratamento prioritário.





- Wallet móvel**: A Bull Bitcoin oferece um Wallet móvel de código aberto e auto-custodial, disponível em Android e iOS, que suporta transacções onchain, Liquid e Lightning Network.





- Apoio pedagógico**: Guias gratuitos e formação personalizada para ajudar os utilizadores a criar, proteger e gerir as suas carteiras Bitcoin, reforçando a autonomia financeira.



#### Conformidade e segurança





- Regulamentação**: Registado na FINTRAC (Canadá) e na AMF (França), o Bull Bitcoin está em conformidade com os requisitos KYC/AML.





- Segurança**: Utilização de carteiras seguras e recomendações de armazenamento offline. Os dados pessoais estão alojados na infraestrutura Bitcoin da Bull, que é 100% auto-hospedada e não depende de terceiros.