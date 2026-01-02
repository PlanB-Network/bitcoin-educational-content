---
name: Plano sucessório Bitcoin
description: Como transferir bitcoins para os seus entes queridos
---

![cover](assets/cover.webp)



A transmissão de bitcoins representa um grande desafio técnico que muitos detentores ignoram. Ao contrário dos activos bancários tradicionais, em que uma instituição financeira pode remeter os fundos para os legítimos proprietários, o Bitcoin funciona sem intermediários. Os seus entes queridos nunca poderão aceder aos seus fundos sem as informações técnicas necessárias, independentemente da sua legitimidade legal.



Este tutorial orienta-o na criação de um plano de herança técnica. Aprenderá como funcionam os mecanismos on-chain para a transmissão automática, como documentar as suas configurações e como escolher as soluções certas para garantir que o seu legado Bitcoin permanece acessível aos seus entes queridos.



## Porque é que um plano de património técnico é essencial



O Bitcoin baseia-se num princípio criptográfico fundamental: quem detém as chaves privadas controla os fundos. Esta soberania torna-se uma grande vulnerabilidade quando o detentor desaparece sem ter transmitido as informações necessárias.



Um plano de herança do Bitcoin deve cumprir dois objectivos aparentemente contraditórios: permitir que os seus entes queridos acedam aos seus fundos quando chegar a altura, ao mesmo tempo que impede qualquer outra pessoa de aceder aos mesmos prematuramente. Este equilíbrio delicado baseia-se nas capacidades de programação nativas do Bitcoin.



A complexidade técnica acrescenta uma camada extra de dificuldade. Os seus herdeiros terão de manipular conceitos como frases de recuperação, descritores de carteiras ou caminhos de derivação. Sem uma preparação adequada, mesmo um herdeiro bem intencionado arrisca-se a cometer erros irreversíveis.



## Como funciona a herança on-chain



O Bitcoin utiliza a sua linguagem de scripting para codificar as condições de despesa diretamente nas transacções. A herança do on-chain explora esta capacidade de programação para criar vias de recuperação alternativas que se activam automaticamente.



### Relógios de ponto



Os relógios de tempo são o mecanismo fundamental da herança Bitcoin. Permitem que os fundos sejam bloqueados até que uma condição de tempo seja cumprida.



**CLTV (CheckLockTimeVerify)**: Este bloqueio de tempo absoluto verifica se uma determinada hora (data ou altura do bloco) foi atingida antes de autorizar a despesa. Por exemplo, "estes fundos só podem ser gastos após o bloco 900000" ou "após 1 de janeiro de 2026". A vantagem do CLTV é que permite grandes atrasos (vários anos), mas a data é fixa e aplica-se de forma idêntica a todos os UTXOs da carteira. Para manter o controlo dos seus fundos, deve criar periodicamente uma nova carteira com uma data de expiração alargada e transferir os seus fundos para ela.



**CSV (CheckSequenceVerify)**: Este bloqueio de tempo relativo verifica se decorreu um determinado número de blocos desde a criação do UTXO. Por exemplo, "estes fundos só podem ser gastos 52560 blocos (~1 ano) após a sua receção". A vantagem do CSV é que cada UTXO tem seu próprio contador independente. Sempre que se efectua uma transação, os UTXOs recém-criados reiniciam o seu próprio limite de tempo. No entanto, o limite técnico de 65535 blocos (~15 meses no máximo) restringe os prazos possíveis. Esta abordagem é mais natural para a utilização quotidiana, uma vez que a sua atividade normal atrasa automaticamente os prazos.



### Várias vias de despesa



Uma carteira de herança combina várias vias de despesa em cada endereço:





- Caminho principal** : O proprietário pode gastar os seus fundos em qualquer altura com a sua chave principal, sem restrições de tempo.
- Via(s) de recuperação**: Uma ou mais chaves alternativas só podem gastar fundos depois de decorrido um determinado período de tempo.



Cada transação efectuada pelo proprietário "refresca" o UTXO, criando novas saídas com relógios de reinicialização. Este mecanismo garante que, enquanto o proprietário permanecer ativo, os caminhos de recuperação nunca são activados.



### Miniscript e Taproot



*o *Miniscript** é uma linguagem estruturada desenvolvida por Andrew Poelstra, Pieter Wuille e Sanket Kanjalkar que facilita a escrita e a análise de scripts Bitcoin complexos. Permite-lhe compor condições de despesa legíveis e verificáveis, essenciais para configurações de herança que envolvam várias chaves e relógios de ponto.



**O Taproot** (ativado em novembro de 2021) melhora significativamente a herança do on-chain. Graças à sua estrutura em árvore (MAST), apenas a condição de gasto utilizada é revelada na blockchain. Se o proprietário gastar os seus fundos normalmente, as condições de herança permanecem invisíveis. Esta confidencialidade também reduz os custos de transação para caminhos complexos.



## A importância crucial dos descritores



Para as carteiras antigas, a frase de recuperação (seed) não é suficiente para restabelecer o acesso aos fundos. O **descriptor** torna-se o elemento crítico.



Um descritor é uma cadeia de caracteres que descreve exaustivamente a estrutura de um portefólio: as chaves públicas envolvidas, as condições de despesa, os caminhos de derivação e os relógios de ponto configurados. Aqui está um exemplo simplificado:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Este descritor diz: "ou a chave mestra pode ser gasta imediatamente, ou a chave de recuperação pode ser gasta após 52560 blocos".



Vamos analisar este exemplo:




- `wsh()` : Witness Script Hash, indica o tipo de endereço (P2WSH)
- or_d()`: condição "ou" com um ramo padrão
- pk([fingerprint/path]xpub...)`: A chave pública mestre com sua impressão digital e caminho de derivação
- and_v()`: condição "and" que combina chave de recuperação com timelock
- mais velho(52560)`: O bloqueio de tempo relativo de 52560 blocos



**Sem o descritor, mesmo com todas as frases de recuperação, os seus herdeiros não conseguirão reconstruir a carteira.** Uma carteira padrão só pode ser restaurada a partir do seed porque segue caminhos de derivação padronizados (BIP44, BIP84). Um portfólio legado, por outro lado, usa scripts personalizados que não podem ser adivinhados. O backup do descritor (ou o arquivo de configuração exportado pelo seu software) deve acompanhar as frases de recuperação no seu plano de herança.



## Componentes documentais de um plano sucessório



Para além dos mecanismos técnicos, um plano de legado eficaz assenta em três pilares de documentação.



### A carta de herança



Esta carta pessoal é o ponto de entrada para o seu plano. Escrita para os seus herdeiros, explica o contexto e as precauções a tomar.



A carta deve incluir regras de segurança explícitas:




- Não se apresse, aprenda com calma antes de avançar com os fundos
- Nunca comunicar uma frase de recuperação completa a uma única pessoa
- Nunca introduza uma frase de recuperação num programa de software ou computador não verificado
- Cuidado com as burlas e com as pessoas que oferecem ajuda não solicitada
- Procurar o conselho de pelo menos duas pessoas da sua confiança antes de tomar qualquer decisão



Esta carta contém igualmente os dados de contacto do notário e a localização do testamento. Nunca deve conter frases de recuperação ou palavras-passe.



### A lista de contactos de confiança



Nenhum herdeiro deve enfrentar sozinho a recuperação de bitcoins. Este diretório lista as pessoas que podem prestar assistência técnica ou jurídica.



Para cada contacto, documente: nome completo, relação consigo, papel no plano, nível de confiança, competências Bitcoin e dados de contacto completos. Regra de base: os seus herdeiros devem sempre consultar pelo menos duas pessoas diferentes antes de tomarem qualquer decisão importante.



### Inventário de activos Bitcoin



Esta secção mapeia todos os seus bitcoins com as informações técnicas necessárias para os recuperar.



Para cada carteira, documentar :




- Tipo de carteira**: hardware, software, configuração (single-sig, multisig, legacy)
- Localização do dispositivo**: localização física do hardware do wallet
- Descriptor/localização do ficheiro de configuração**: crítico para carteiras avançadas
- Localização da frase de recuperação**: separada do descritor
- Códigos de acesso**: onde são guardados os PIN e as frases-chave
- Atrasos configurados**: quando os percursos de recuperação são activados



## Soluções técnicas disponíveis



Vários pacotes de software implementam mecanismos de herança on-chain. Cada um tem as suas próprias caraterísticas técnicas.



### Liana



O Liana é um software de secretária (Linux, macOS, Windows) que utiliza o Miniscript para criar carteiras com caminhos de recuperação temporizados. O projeto é desenvolvido pela Wizardsardine, co-fundada por Antoine Poinsot (colaborador do Bitcoin Core).



**Arquitetura técnica**: O Liana cria carteiras P2WSH (nativas do SegWit) por defeito, com suporte para Taproot disponível dependendo da compatibilidade do seu hardware wallet. A arquitetura baseia-se num caminho principal e em um ou mais caminhos de recuperação. O descritor gerado codifica todas as condições e deve ser guardado.



**Timelocks utilizados**: O Liana usa timelocks relativos (CSV), limitados a 65535 blocos (~15 meses). Para manter o controlo, é necessário efetuar uma transação de atualização antes de o timelock expirar.



**Integração do hardware wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY e outros dispositivos são compatíveis para assinar transacções.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



O Bitcoin Keeper é uma aplicação móvel (iOS, Android) que combina multisig e relógios de ponto através dos seus "Enhanced Vaults". A abordagem móvel com orientação integrada torna-a acessível a utilizadores menos técnicos.



**Arquitetura técnica**: Os cofres melhorados utilizam o Miniscript para criar configurações multisig, onde as chaves adicionais são activadas após atrasos definidos. A Chave de Herança adiciona ao quorum existente, enquanto a Chave de Emergência pode contornar completamente o multisig.



**Relógios utilizados**: O Bitcoin Keeper utiliza relógios de tempo absolutos (CLTV), permitindo prazos de entrega superiores a 15 meses. A data de ativação é fixada aquando da criação do wallet e aplica-se a todos os UTXOs. A aplicação incorpora uma função de "revaulting" que gere automaticamente a atualização: o utilizador segue simplesmente os passos guiados, sem ter de criar manualmente um novo wallet.



**Funcionalidades adicionais**: Documentos de herança integrados, Canary Wallets para detetar o comprometimento de chaves e lembretes de atualização.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Património



Heritage é uma aplicação de ambiente de trabalho que utiliza scripts Taproot para codificar condições de herança. A utilização do Taproot oferece uma maior confidencialidade, uma vez que os caminhos não utilizados permanecem invisíveis na cadeia de blocos.



**Arquitetura técnica**: Cada endereço de herança integra um percurso principal e percursos alternativos para cada herdeiro, com prazos progressivos. A estrutura hierárquica permite definir um backup pessoal a 6 meses e os herdeiros familiares a 12-15 meses.



**Modos de utilização**: Versão autónoma com o seu próprio nó (gratuito) ou serviço gerido que adiciona lembretes e notificações aos herdeiros (0,05%/ano).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## O processo de recuperação do herdeiro



Compreender o processo de recuperação ajuda a preparar um plano eficaz. Eis os passos técnicos que um herdeiro terá de seguir.



### Requisitos de recuperação



O herdeiro precisa de :


1. **O ficheiro descritor ou de configuração** da carteira original (formato JSON ou texto, consoante o software)


2. **A sua frase de recuperação** (a que está associada à sua chave de herança, normalmente 12 ou 24 palavras)


3. **Software compatível** (Liana, Bitcoin Keeper, Heritage ou Sparrow/Specter para descritores padrão)


4. **Uma ligação a um nó Bitcoin** para verificar o estado do timelock e transmitir a transação



### Etapas de recuperação



1. **Instalar o software** num dispositivo seguro e configurar a ligação à rede Bitcoin (nó pessoal ou servidor Electrum)


2. **Importar o descritor** para reconstruir a estrutura da carteira. O software irá automaticamente generate todos os endereços utilizados


3. **Restaurar chave de herança** da frase de recuperação. O software verificará se esta chave corresponde a uma das chaves autorizadas no descritor


4. **Sincronizar a carteira** para descobrir todos os UTXOs e as suas condições de despesa


5. **Verificar a expiração do timelock**: o software indicará para cada UTXO se o caminho de recuperação está ativo


6. **Criar a transação de recuperação** para um endereço controlado exclusivamente pelo herdeiro (idealmente um novo e único wallet)


7. **Assinar e transmitir** a transação na rede Bitcoin



Se o timelock ainda não tiver expirado, o herdeiro terá de esperar. O software indica a data ou o bloco a partir do qual a recuperação é possível. Durante este período de espera, os fundos permanecem seguros na cadeia de blocos.



### Pontos a ter em conta para o herdeiro



O herdeiro deve prestar especial atenção a :




- Verificar a autenticidade do software descarregado** (somas de verificação, assinaturas)
- Nunca partilhe a sua frase de recuperação** com ninguém que lhe ofereça ajuda
- Consultar pelo menos duas pessoas da sua confiança** antes de efetuar uma recuperação
- Transferir os fundos para uma carteira simples** que ele controla completamente após a recuperação



## Melhores práticas



### Separação de informações



Nunca guardar todas as informações num único local. O descritor deve ser separado das frases de recuperação, que por sua vez são separadas dos códigos PIN. Esta distribuição complica o acesso de um atacante, mantendo-se reconstituível pelos seus herdeiros legítimos.



### Ensaios de recuperação



Antes de depositar fundos significativos, teste todo o processo de recuperação com uma pequena quantia. Verifique se consegue restaurar a carteira a partir do descritor e das frases de recuperação num dispositivo vazio. Documente os passos para os seus herdeiros.



### Manutenção do fecho de correr



Planeie atualizar os seus relógios de ponto muito antes de estes expirarem. Para um relógio de 12 meses, efectue uma transação a cada 9-10 meses. Normalmente, o software oferece lembretes ou funções de atualização automática.



### Atualização do plano



A configuração do Bitcoin evolui. Cada alteração significativa (nova carteira, modificação de prazos, adição de herdeiros) deve ser reflectida na sua documentação. Estabeleça uma rotina de revisão anual.



## Escolher a sua abordagem



A escolha entre as diferentes soluções depende do seu perfil técnico e das suas necessidades específicas.



*o *Liana** é adequado para utilizadores de computadores de secretária que preferem software de fonte aberta com controlo total através do seu próprio nó. A configuração permanece acessível graças à interface guiada. Os relógios de tempo relativos (CSV) simplificam a manutenção, uma vez que a sua atividade normal atrasa automaticamente os prazos. Limitação: atraso máximo de cerca de 15 meses (65535 blocos).



*a aplicação *Bitcoin Keeper** destina-se a utilizadores móveis que procuram uma interface intuitiva com documentos de acompanhamento integrados. A aplicação oferece dois tipos de chaves especiais: a chave de herança (que aumenta o quórum) e a chave de emergência (que o ignora completamente). Os relógios de ponto absolutos (CLTV) permitem prazos de entrega superiores a 15 meses, com uma função de revaulting integrada que simplifica a atualização. O plano Mãos de Diamante desbloqueia funcionalidades avançadas do legado.



*o *Inheritance** destina-se a utilizadores técnicos que apreciam a confidencialidade do Taproot e a herança hierárquica com atrasos progressivos. A estrutura em árvore do Taproot oculta as condições de herança durante as transacções normais, revelando apenas a condição utilizada durante a recuperação.



As três soluções têm uma coisa em comum: exigem uma atualização periódica para evitar a ativação prematura das vias de recuperação. Essa restrição é tanto o preço quanto a garantia do legado não confiável do on-chain. Programe lembretes regulares e torne esta manutenção parte da sua rotina de gestão do Bitcoin.



## Conclusão



Um plano técnico de legado Bitcoin combina mecanismos criptográficos (timelocks, Miniscript, Taproot) com uma documentação rigorosa. As carteiras avançadas permitem-lhe transmitir os seus bitcoins automaticamente após um período de inatividade, sem intervenção de terceiros.



Os elementos essenciais a transmitir aos seus herdeiros são: o ficheiro descritor ou de configuração, a frase de recuperação, as instruções de recuperação detalhadas e os contactos de pessoas competentes que os possam ajudar.



Comece por escolher uma solução técnica adaptada ao seu perfil, teste-a com uma pequena quantidade, depois documente o conjunto num plano estruturado. A complexidade inicial garante que o seu património Bitcoin será transmitido com toda a confiança.



## Recursos



### Modelo de plano sucessório





- [Modelo de plano de herança Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Modelo de documentação Plan ₿ Network



### Referências técnicas





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Especificação de relógios temporizadores absolutos (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Especificação de relógios de ponto relativos (CSV)
- [Referência Miniscript](https://bitcoin.sipa.be/miniscript/) - Documentação oficial do Miniscript por Pieter Wuille



### Sítios Web oficiais da solução





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7