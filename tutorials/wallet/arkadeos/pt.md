---
name: ArkadeOS
description: Guia completo da carteira Arkade e do Protocolo Ark
---

![cover](assets/cover.webp)



A rede Bitcoin enfrenta um grande desafio: a escalabilidade. Embora a camada principal (camada 1) ofereça segurança e descentralização inigualáveis, só pode lidar com um número limitado de transacções por segundo. A Lightning Network surgiu como uma solução promissora de segunda camada (camada 2), permitindo pagamentos rápidos e de baixo custo. No entanto, o Lightning impõe as suas próprias limitações: gestão de canais, necessidade de liquidez de entrada e uma complexidade técnica que pode afastar novos utilizadores.



Este é o contexto do **Ark**, um novo protocolo de camada 2 concebido para oferecer uma experiência de utilizador simplificada sem sacrificar a soberania. *o *ArkadeOS** (ou Arkade) é a primeira grande implementação deste protocolo, oferecendo um portefólio Bitcoin de próxima geração.



Este tutorial irá guiá-lo pelo mundo da Arkade. Exploraremos como o protocolo Ark funciona, como instalar e configurar o Arkade wallet e como usá-lo para enviar e receber bitcoins instantaneamente, de forma confidencial e sem os atritos usuais do Lightning Network.



## Compreender o protocolo Arca



Antes de mergulhar na utilização da Arkade, é essencial compreender os conceitos-chave do protocolo Ark que a impulsiona. O Ark não é uma blockchain separada, mas um mecanismo de coordenação inteligente em cima do Bitcoin.



### O conceito VTXO


No coração do Ark está o **VTXO** (Virtual UTXO). Um VTXO é um UTXO ainda não publicado na cadeia de blocos Bitcoin: existe fora da cadeia principal (off-chain), mas é apoiado por transacções pré-assinadas na cadeia de blocos.



Ao contrário de um saldo numa bolsa centralizada, um VTXO pertence-lhe realmente. Tem uma prova criptográfica que lhe permite, a qualquer momento, reclamar os bitcoins reais correspondentes na cadeia de blocos, mesmo que o servidor Ark desapareça. Os VTXOs permitem-lhe transferir valor instantaneamente entre utilizadores sem esperar por confirmações de blocos.



### O papel do ASP (Ark Service Provider)


O protocolo Ark funciona num modelo cliente-servidor. O servidor é designado por **ASP** (Ark Service Provider). O ASP desempenha o papel de condutor:




- Fornece a liquidez necessária para a rede.
- Coordena as transacções entre os utilizadores.
- Organiza "rondas" de liquidação na cadeia de blocos.



É crucial notar que o ASP é **não-custodial**. Nunca detém as suas chaves privadas, nem pode roubar os seus fundos. O seu papel é puramente técnico e logístico. Se um ASP censurar as suas transacções ou cair, pode sempre recuperar os seus fundos através de um procedimento de saída unilateral.



### Rondas e privacidade


As transações na Ark são finalizadas em lotes chamados **Rounds**. Periodicamente (por exemplo, a cada poucos segundos), o ASP reúne todas as transações pendentes e as ancora no blockchain Bitcoin em uma única transação otimizada.


Este mecanismo oferece duas grandes vantagens:




- Escalabilidade**: Uma única transação on-chain pode validar milhares de pagamentos off-chain, reduzindo drasticamente os custos para os utilizadores.
- Confidencialidade**: Cada ronda funciona como um **CoinJoin**. Os fundos de todos os participantes são misturados num fundo comum antes de serem redistribuídos sob a forma de novos VTXOs. Isto quebra a ligação entre o remetente e o destinatário, tornando extremamente difícil, se não impossível, para um observador externo rastrear os pagamentos.



## Apresentação do ArkadeOS



O ArkadeOS é a aplicação concreta que torna o protocolo Ark disponível para o público em geral. Desenvolvido pela Ark Labs, é um ecossistema completo que inclui uma carteira (Wallet), um servidor (Operator) e ferramentas de desenvolvimento.



Para o utilizador final, a Arkade assume a forma de uma elegante e intuitiva aplicação Web wallet (PWA - Progressive Web App). Ela esconde a complexidade criptográfica dos VTXOs e das rondas por trás de uma interface familiar. Com a Arkade, o utilizador tem um endereço para receber, um botão para enviar e um histórico de transacções, tal como um wallet clássico, mas com o poder do imediatismo e da confidencialidade da Arkade.



## Instalação e configuração



Como a Arkade é um aplicativo da Web progressivo, ela é particularmente fácil de instalar e não envolve necessariamente as lojas de aplicativos tradicionais.



### Acesso e instalação


Pode aceder à Arkade diretamente a partir de qualquer navegador Web moderno (Chrome, Safari, Brave) no computador ou no telemóvel.





- Visite o sítio Web oficial da aplicação: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Será recebido por uma série de ecrãs introdutórios que lhe apresentarão os principais conceitos da Arkade: um novo ecossistema para a Bitcoin, a importância da autocustódia e as vantagens das transacções em lote.



![arkade onboarding](assets/fr/02.webp)





- No Android (Chrome/Brave)** : Prima o menu do navegador (três pontos) e selecione "Instalar aplicação" ou "Adicionar ao ecrã inicial".
- No iOS (Safari)**: Prima o botão de partilha (quadrado com uma seta para cima) e escolha "No ecrã inicial".



Uma vez instalada, a Arkade é iniciada como uma aplicação nativa, em ecrã completo e sem uma barra de endereços.



### Criação de portefólio


No primeiro lançamento, ser-lhe-á pedido que configure a sua carteira.





- Clique em **"Create New Wallet"**.



![create wallet](assets/fr/03.webp)





- A wallet é criada instantaneamente. Ao contrário das carteiras Bitcoin tradicionais, a **Arkade não usa uma frase de recuperação de 12 ou 24 palavras**. Em vez disso, a Arkade gera automaticamente uma **chave privada** no formato Nostr (nsec), que será usada para fazer backup e restaurar seu wallet. Lembre-se de salvar essa chave imediatamente (veja a próxima seção).





- Aparecerá o ecrã "Your new wallet is live!", que confirma que o seu wallet está pronto a ser utilizado. Clique em **"GO TO WALLET "** para aceder à interface principal.



Uma vez no seu wallet, é encaminhado para a interface principal da Arkade. Aqui encontrará o seu saldo, botões para enviar e receber fundos e um separador "Apps" que dá acesso a aplicações integradas, tais como Boltz (câmbio Lightning), LendaSat e LendaSwap (serviços de empréstimo) e Fuji Money (activos sintéticos).



![wallet interface](assets/fr/04.webp)



### Ligação ao ASP


Por defeito, o portefólio é automaticamente configurado para se ligar ao ASP oficial da Arkade Labs. Pode verificar a que servidor está ligado indo a **Configurações** > **Sobre** onde verá o endereço do servidor (atualmente `https://arkade.computer`).



Na versão atual da Arkade (Beta), não é possível modificar manualmente o servidor ASP. O aplicativo se conecta automaticamente ao ASP oficial da Arkade Labs. No futuro, os utilizadores poderão escolher entre diferentes ASPs de acordo com as suas preferências, mas esta funcionalidade ainda não está disponível.



### Fazer uma cópia de segurança da sua chave privada


**O Arkade usa uma chave privada no formato Nostr (nsec) como método de backup e recuperação. Para efetuar uma cópia de segurança da sua chave privada :





- Aceda a **Definições** no ecrã principal.
- Selecionar **"Cópia de segurança e privacidade "**.
- Você verá a sua **chave privada** exibida no formato `nsec...`. Esta longa sequência de caracteres é o único meio de restaurar o seu wallet.
- Prima **"COPY NSEC TO CLIPBOARD "** para copiar a sua chave privada.
- Guarde esta chave num local seguro**: escreva-a num papel, guarde-a num gestor de palavras-passe seguro ou utilize qualquer outro método de cópia de segurança que lhe convenha.
- A Arkade também oferece a opção **"Habilitar backups Nostr "**. Esta funcionalidade utiliza o protocolo Nostr (uma rede descentralizada) para efetuar automaticamente cópias de segurança de determinados dados do seu wallet, de forma encriptada, para retransmissores Nostr. Isto facilita a sincronização entre vários dispositivos e permite uma recuperação mais simples do estado do seu wallet.



**Importante**: Os backups do Nostr são apenas uma funcionalidade de **conforto**. Eles não substituem o backup da sua chave nsec. Os relés do Nostr não garantem o armazenamento permanente de dados. A sua chave privada nsec é a única garantia de recuperação dos seus fundos.



![backup private key](assets/fr/05.webp)




## Utilizar a Arkade



Depois de configurar seu wallet, você está pronto para explorar os recursos da Arkade. A interface foi projetada para unificar os diferentes tipos de pagamentos do Bitcoin (On-chain, Lightning, Ark) sem problemas.



### Receber fundos



Para financiar a sua carteira, prima **"Receber "**. A Arkade oferece três métodos de recebimento:





- Pagamento Ark**: Se o remetente também utiliza a Arkade, partilhe o seu endereço Ark para uma transferência instantânea, confidencial e praticamente gratuita.
- Depósito em cadeia (embarque)**: Usar o endereço Bitcoin (`bc1p...`) para receber de um wallet clássico ou de uma bolsa. Aguarde a confirmação (~10 min) antes que os fundos sejam convertidos em VTXOs.
- Troca do Lightning**: Gere uma fatura Lightning e pague-a a partir de um wallet Lightning externo. Os fundos chegam instantaneamente através de uma troca automática.



![receive amount](assets/fr/06.webp)



O ecrã de recibo apresenta todas as opções disponíveis: Código QR, endereço Ark, endereço Bitcoin (BIP21) e fatura Lightning. Para pagamentos Lightning, mantenha a aplicação aberta durante a transação.



![receive confirmation](assets/fr/07.webp)



### Envio de fundos



Para enviar fundos, prima **"Enviar "** e cole o endereço do destinatário ou leia o código QR. A Arkade detecta automaticamente o tipo de pagamento necessário:





- Pagamento Ark**: Para um endereço Arca, a transferência é instantânea, privada e praticamente gratuita (0 taxa SATS). O destinatário não precisa de estar online.
- Pagamento Lightning**: Digitalize uma fatura Lightning (`lnbc...`) e a Arkade efectua automaticamente uma troca. O ASP paga a fatura por si e debita o seu saldo Arkade.
- Pagamento em cadeia**: Para um endereço clássico do Bitcoin (`bc1q...` ou `bc1p...`), a Arkade inicia uma "Saída Colaborativa" que será incluída na próxima rodada do on-chain.



Verificar os dados no ecrã "Assinar transação" e confirmar com **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Limitação atual (Beta)**: Os VTXOs criados há menos de 24 horas não podem ser utilizados para saídas on-chain. Se encontrar um erro, aguarde até que os seus VTXOs estejam "maduros".



**Confidencialidade da saída on-chain**: O exemplo abaixo mostra uma [transação de saída Ark em mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Observamos uma entrada distribuída para 4 saídas diferentes, como um CoinJoin. Para um observador externo, é impossível determinar que quantidade pertence a que utilizador.



![transaction ark mempool](assets/fr/11.webp)



## Funcionalidades avançadas



### Gestão da expiração do VTXO


Uma caraterística técnica do protocolo Ark é o facto de os VTXOs terem um **tempo de vida limitado**. Essa restrição de tempo é inerente ao design do protocolo. O tempo de expiração é configurável por cada servidor ASP; no ASP oficial da Arkade Labs, este período é de cerca de **4 semanas (≈30 dias)**.



**Esta limitação permite ao servidor Ark gerir eficazmente a liquidez e limpar os VTXOs de utilizadores inactivos. Após a expiração, o servidor Ark pode tecnicamente reivindicar os fundos restantes na árvore VTXO.



**Para manter os seus VTXOs activos, é necessário "actualizá-los" antes de expirarem. O refrescamento consiste em participar numa nova "ronda" em que os seus VTXOs prestes a expirar são trocados por novos VTXOs com um novo período de validade completo (≈30 dias no ASP da Arkade Labs).



A carteira Arkade gere este processo automaticamente: a aplicação monitoriza constantemente o estado dos seus VTXOs e actualiza-os automaticamente alguns dias antes de expirarem. Desde que abra a sua aplicação regularmente (pelo menos uma vez por semana), os seus VTXOs serão automaticamente mantidos activos.



**Se não abrir a sua carteira durante mais de 4 semanas, os seus VTXOs expiram. No entanto, não perde os seus fundos: tem a possibilidade de os recuperar através de uma **saída unilateral** (ver secção seguinte). Este procedimento é mais dispendioso e mais lento, mas garante que os seus fundos continuam a ser recuperáveis.



A necessidade de abrir regularmente a aplicação faz da Arkade um **"Hot Wallet"** concebido para as despesas do dia a dia e não um cofre para poupanças a longo prazo. Para armazenar bitcoins sem os utilizar durante longos períodos, prefira um hardware wallet frio.



**Verificar o estado dos seus VTXOs**: Pode monitorizar o estado dos seus VTXOs em **Configurações** > **Avançado**. Consulte "Próxima renovação" para ver quando será efectuada a próxima renovação automática e "Moedas virtuais" para ver uma lista detalhada de todos os seus VTXOs com a respectiva data de expiração.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Saída Unilateral)



A saída unilateral é uma **garantia criptográfica fundamental** do protocolo Ark que lhe garante a devolução dos seus fundos, mesmo que o ASP desapareça, censure as suas transacções ou se recuse a cooperar. Tecnicamente, os seus VTXOs são **transacções Bitcoin pré-assinadas** que lhe pertencem. Numa emergência absoluta, pode transmitir estas transacções na cadeia de blocos Bitcoin para recuperar os seus fundos sem a autorização de ninguém.



**Como é que funciona? O processo ocorre em duas etapas. Primeiro, o **Unrolling**: transmite sequencialmente as transacções pré-assinadas que constituem os seus VTXOs na árvore de transacções. Em seguida, a **Finalização**: uma vez que os timelocks tenham expirado (geralmente 24 horas), você coleta seus bitcoins de um endereço padrão.



**Estado atual na Arkade**: Na versão Beta, ainda não existe um botão ou uma interface de utilizador simples para a saída unilateral. Esta funcionalidade requer atualmente a utilização do SDK da Arkade e conhecimentos técnicos de programação TypeScript.



**Mesmo que o procedimento não esteja acessível com o toque de um botão, a garantia criptográfica está lá. Os seus VTXOs contêm transacções pré-assinadas que lhe pertencem legitimamente. É esta garantia técnica que faz do Ark um protocolo **não custodial**: mesmo na pior das hipóteses, os seus fundos permanecem tecnicamente recuperáveis. Uma interface simplificada será provavelmente adicionada em futuras versões da Arkade.



## Vantagens e limitações



Para colocar a Arkade no contexto correto, vamos resumir os seus actuais pontos fortes e fracos.



### Destaques




- Experiência do utilizador (UX)**: Sem gerenciamento de canais, capacidade de entrada ou backups complexos de canais como no Lightning. Basta instalar e usar.
- Privacidade** : A arquitetura CoinJoin predefinida oferece um nível de anonimato muito mais elevado do que as transacções on-chain ou Lightning normais.
- Interoperabilidade**: Pague qualquer código QR Bitcoin (On-chain ou Lightning) a partir de uma única interface.



### Restrições




- Protocolo jovem**: Ark é uma tecnologia muito recente. Podem existir bugs. É aconselhável não utilizar o Ark para armazenar somas cuja perda possa ser crítica.
- Dependência de ASP**: Embora não seja obrigatório, o sistema depende da disponibilidade do ASP para a fluidez. Se o ASP estiver offline, deixará de poder efetuar transacções instantâneas (apenas os seus fundos on-chain).
- Apenas Hot Wallet** : A necessidade de abrir regularmente a aplicação para atualizar os VTXOs não é adequada para o armazenamento a frio (armazenamento Cold).



## Comparação: Arkade vs Lightning vs Cashu



Para entender melhor o posicionamento da Arkade, vamos compará-la com as outras duas principais soluções de escalabilidade.




| Critério | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modelo** | UTXO compartilhado coordenado por servidor (ASP) | Rede P2P de canais de pagamento | Tokens cegos emitidos por um banco (Mint) |
| **Custódia** | **Não-custodial** (você tem as chaves) | **Não-custodial** (você tem as chaves) | **Custodial** (o Mint tem os fundos) |
| **Privacidade** | **Elevada** (CoinJoin nativo, cego para o público) | **Média** (Roteamento cebola, mas canais visíveis) | **Muito Elevada** (Cego até para o Mint) |
| **Escalabilidade** | Excelente (Batching massivo on-chain) | Excelente (Transações infinitas off-chain) | Excelente (Assinaturas de servidor simples) |
| **Experiência** | Simples (próximo de uma wallet on-chain) | Complexa (gestão de canais, liquidez) | Muito simples (como dinheiro digital) |
| **Risco principal** | Disponibilidade do ASP e Expiração | Gestão de canais e Backups | Confiança no Mint (risco de roubo) |

*o *Arkade** é o compromisso ideal: a simplicidade e a confidencialidade do Cashu, mas com a soberania (sem custódia) do Lightning.



## Apoio e assistência



Se tiver problemas ou dúvidas durante a utilização da Arkade, a aplicação oferece várias opções de assistência:





- Aceder a **Configurações** > **Apoio**.
- Encontrará várias opções:
  - Apoio ao cliente**: Obtenha ajuda com a sua carteira, comunique erros ou faça perguntas.
  - Conversa segura**: As suas conversas são seguras e privadas, com o histórico mantido entre sessões.
  - Relatórios de erros**: Relate quaisquer problemas que encontrar, incluindo os passos para os reproduzir.
  - Acompanhe o progresso**: Acompanhe sempre os seus bilhetes e conversas de apoio.



![support](assets/fr/10.webp)



A equipa da Arkade também está ativa no Telegram através do canal @arkade_os para obter apoio e oportunidades de integração.



## Nota importante: Aplicação em Beta



**⚠️ A Arkade está atualmente em fase de Beta Pública no mainnet Bitcoin**. Embora a aplicação seja funcional com bitcoins reais, é importante tomar certas precauções.



### Recomendações de utilização




- Utilizar pequenas quantidades**: Evite armazenar grandes somas na Arkade. Utilize este wallet para as suas despesas diárias e guarde as suas poupanças num hardware wallet frio.
- Possíveis bugs e limitações**: Como acontece com qualquer aplicação em desenvolvimento ativo, a Arkade pode apresentar erros ou comportamentos inesperados. Relate qualquer problema através do suporte integrado.
- Evolução rápida** : A aplicação e o protocolo estão constantemente a ser melhorados. Algumas caraterísticas podem ser alteradas ou acrescentadas em versões futuras.



### Limitações actuais conhecidas




- atraso de 24 horas nos VTXOs** : Os VTXOs recém-criados não podem ser utilizados imediatamente para saídas on-chain.
- ASP único**: Ainda não é possível alterar o servidor ASP na aplicação.
- Saída unilateral técnica**: Ainda não existe uma interface simplificada para a saída unilateral (requer SDK).



A equipa da Arkade Labs está a trabalhar ativamente para atenuar estas limitações em versões futuras.



## Conclusão



O ArkadeOS representa um grande avanço no ecossistema Bitcoin. Ao implementar o protocolo Ark, prova que é possível conciliar a simplicidade de utilização com os princípios fundamentais do Bitcoin: não confiar, verificar.



Embora ainda esteja a dar os primeiros passos, a Arkade oferece um vislumbre fascinante do que poderá ser o futuro dos pagamentos Bitcoin: instantâneo, privado e acessível a todos, sem pré-requisitos técnicos. É a ferramenta perfeita para as suas despesas diárias, complementando a sua solução de poupança segura (Cold Wallet).



Encorajamo-lo a testar a Arkade com pequenas quantidades para descobrir este novo protocolo por si próprio. O ecossistema está a evoluir rapidamente e a Arkade está na vanguarda desta inovação.



## Recursos



Para mais informações, consultar os recursos oficiais:





- Sítio Web da Arkade**: [arkadeos.com](https://arkadeos.com)
- Documentação**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protocolo Ark**: [ark-protocol.org](https://ark-protocol.org)
- Código fonte** : [GitHub Arkade](https://github.com/arkade-os)