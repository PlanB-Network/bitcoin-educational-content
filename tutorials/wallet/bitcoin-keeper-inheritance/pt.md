---
name: Bitcoin Keeper - Plano sucessório
description: Planeie a sua transmissão de bitcoin com o Bitcoin Keeper
---

![cover](assets/cover.webp)



A transferência de activos do Bitcoin é um dos desafios mais subestimados pelos titulares. Ao contrário de uma conta bancária, onde a instituição financeira pode passar os fundos para os herdeiros legítimos, o Bitcoin depende inteiramente da posse de chaves privadas. Um herdeiro legal perfeitamente legítimo nunca poderá aceder aos fundos sem estas chaves, enquanto um indivíduo malicioso na posse dos segredos poderá gastá-los sem qualquer formalidade.



Neste segundo tutorial do Bitcoin Keeper, exploramos as funcionalidades premium dedicadas ao planeamento do património. A aplicação oferece ferramentas avançadas para a criação de cofres-fortes melhorados, com mecanismos de proteção temporizados graças ao Miniscript, bem como documentos de acompanhamento para orientar os seus entes queridos.



Este guia pressupõe que já domina as noções básicas do Bitcoin Keeper (criação de carteiras, multisig clássico, adição de chaves de hardware), conforme explicado no nosso primeiro tutorial :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Planos de subscrição do Bitcoin Keeper



O Bitcoin Keeper funciona segundo um modelo freemium com três níveis de subscrição que oferecem funcionalidades progressivas. Para aceder aos planos, vá ao separador **Mais** e, em seguida, toque no seu plano atual (a predefinição é "Pleb") para abrir o ecrã **Gerir subscrição**.



![Plans d'abonnement](assets/fr/01.webp)



O plano **Pleb** (gratuito) dá acesso ao essencial: criação ilimitada de carteiras de chave única e de várias chaves, compatibilidade com todas as principais carteiras de hardware (Coldcard, Trezor, Ledger, Jade, Tapsigner...), controlo de moedas, etiquetagem e ligação a um servidor Electrum pessoal. Este plano é suficiente para uma utilização normal e mesmo para as configurações clássicas do multi-sig.



O **plano Hodler** (9,99 €/mês, com 1 mês grátis se pago anualmente) inclui todas as funcionalidades Pleb e adiciona cópias de segurança encriptadas para a nuvem (iCloud ou Google Drive) para restaurar os seus cofres em qualquer dispositivo, Server Key para adicionar políticas de despesas automáticas e 2FA acima de um determinado limite, e Canary Wallets para detetar o acesso não autorizado às suas chaves.



O **plano Mãos de Diamante** (29,99 euros/mês, com 1 mês grátis se pago anualmente) é o pacote completo para o planeamento sucessório. Inclui todo o plano Hodler e desbloqueia a Chave de Herança (ativação diferida), a Chave de Emergência (chave de emergência para recuperação em caso de perda), as ferramentas e documentos de Planeamento da Herança e uma chamada de apoio com a equipa de Concierge para validar a sua configuração. Esta é a oferta para os bitcoiners que pretendem transmitir a sua herança ao longo de várias gerações.



Ponto importante: os cofres que criou permanecerão acessíveis mesmo que volte a mudar para o plano gratuito. As suas configurações são baseadas em normas abertas (BSMS, Miniscript) e funcionam independentemente da sua subscrição.



## Documentos de herança



Depois de ter ativado a sua subscrição Diamond Hands, aceda à secção **Documentos de herança** no separador Mais. O Bitcoin Keeper fornece cinco exemplos de documentos para estruturar o seu plano de herança, bem como uma secção de dicas:



![Documents d'héritage](assets/fr/02.webp)





- Modelo de palavras-semente**: um modelo para anotar de forma organizada as suas frases de recuperação
- Contactos de confiança**: um modelo para enumerar os dados de contacto das pessoas de confiança envolvidas no seu plano (notário, advogado, herdeiros, guardiões das chaves)
- Chave de Partilha Adicional**: um documento que especifica as informações técnicas de cada chave: Código PIN, caminho de derivação, localização física, tipo de dispositivo e quaisquer outras informações úteis para identificar e utilizar a chave
- Instruções de recuperação**: instruções passo a passo para o herdeiro ou beneficiário recuperar os fundos
- Carta ao advogado**: uma carta pré-preenchida que pode ser adaptada ao seu advogado ou notário



A secção **Dicas sobre herança** oferece conselhos práticos sobre como garantir as chaves para os herdeiros e otimizar o seu plano de herança.



Personalize estes documentos de acordo com a sua situação e guarde-os num local seguro, separado das próprias chaves.



## Configurar o backup na nuvem



Antes de criar o seu cofre legado, active a cópia de segurança na nuvem para proteger os seus ficheiros de configuração. No separador Mais, prima **Cópia de segurança pessoal na nuvem**.



![Configuration Cloud Backup](assets/fr/03.webp)



Escolha uma senha forte para criptografar seus backups. Esta palavra-passe protege apenas os ficheiros de configuração do wallet (não as suas chaves privadas). Confirme a palavra-passe e prima **Confirmar**. Os seus backups serão armazenados no seu iCloud ou Google Drive, dependendo do seu dispositivo. Pressione **Backup Now** para iniciar seu primeiro backup.



## Importar as suas chaves de hardware



Para o nosso exemplo, vamos criar um cofre 2 de 3 com duas chaves adicionais (Herança e Emergência). Vamos começar por importar todas as chaves necessárias para o separador **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Prima **Adicionar tecla** e, em seguida, selecione **Adicionar tecla de um hardware** para ligar um hardware wallet. O Bitcoin Keeper suporta muitos dispositivos: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner e Specter Solutions.



Na nossa configuração, importamos o :




- 2 chaves **Coldcard** (MK4SP e MK4)
- 2 teclas **Tapsigner** (Metro e Genesis)



Para adicionar um Coldcard, selecione-o na lista e siga as instruções no ecrã para exportar a chave pública através de código QR, ficheiro, USB ou NFC. Para mais informações sobre como utilizar um Coldcard ou Tapsigner, consulte os nossos tutoriais dedicados:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Quando todas as suas chaves tiverem sido importadas, encontrá-las-á no separador Chaves com os seus nomes personalizados.



## Criar o legado wallet



Passemos à criação do tronco. No separador **Carteiras**, prima **Adicionar Wallet**, selecione **Bitcoin Wallet** e depois **Criar Wallet**.



![Création du wallet](assets/fr/05.webp)



Selecionar o tipo de wallet. Para o nosso plano antigo, selecione **2 de 3 teclas múltiplas**. Na parte inferior do ecrã, active **Opções de segurança avançadas** e prima **Proceder**.



![Options de sécurité avancées](assets/fr/06.webp)



Na janela pop-up Opções de segurança melhoradas, selecione :




- Chave de herança**: uma chave adicional que será adicionada ao quorum após um período de tempo definido
- Chave de emergência**: uma chave com controlo total diferido para recuperar fundos em caso de perda da chave



Prima **Guardar alterações**. Em seguida, selecione as 3 chaves que irão compor o seu wallet a partir das chaves importadas (por exemplo, Seed Key, Coldcard MK4SP, e Tapsigner Metro).



## Fixação de prazos-chave especiais



O ecrã seguinte permite-lhe configurar a Chave de Emergência e a Chave de Herança. É aqui que se definem os prazos de ativação destas chaves especiais.



![Configuration des délais](assets/fr/07.webp)



Para a **Chave de Emergência**, selecione a chave de hardware que servirá de backup final (aqui Coldcard MK4) e escolha o prazo de ativação (no nosso exemplo: 2 anos). Ao contrário da Chave de Herança, a Chave de Emergência não aumenta o quorum: permite-lhe **contornar completamente o multisig** e dá-lhe controlo total sobre os fundos após o prazo ter expirado. É a sua solução de último recurso: se várias chaves se perderem ou forem destruídas, esta única chave permite-lhe recuperar tudo. Por conseguinte, deve ser protegida com o máximo rigor.



Para a **Chave de herança**, selecionar a chave destinada ao herdeiro (aqui Coldcard MK4SP) e escolher o prazo (no nosso exemplo: 1 ano). Após um ano sem movimento, esta chave **será adicionada ao quorum de assinatura**. Em termos práticos, o seu wallet 2-de-3 tornar-se-á um wallet 2-de-4 após este período, permitindo que o herdeiro participe na assinatura juntamente com as chaves existentes.



### Como é que os relógios de ponto funcionam?



O Bitcoin Keeper utiliza **temporizadores absolutos** (CLTV - CheckLockTimeVerify), possibilitados pelo Miniscript. Ao contrário dos timelocks relativos (CSV), que começam quando cada UTXO é recebido, os timelocks absolutos funcionam com uma **data de expiração fixa** definida quando o wallet é criado.



Em termos concretos, se criar um wallet hoje com uma chave de herança de 1 ano, a data de ativação será "hoje + 1 ano". Todos os fundos depositados neste wallet, independentemente da data de depósito, estarão acessíveis através da chave de herança nesta mesma data.



A vantagem dos relógios de ponto absolutos é que permitem prazos de entrega superiores a 15 meses (o limite dos relógios de ponto CSV relativos), o que explica o facto de o Bitcoin Keeper poder oferecer opções como 2 anos.



### O mecanismo de atualização



Para evitar a ativação de chaves especiais durante a sua vida, deve periodicamente "atualizar" o seu wallet. Com relógios de tempo absolutos, isto envolve **recriar o wallet com uma nova data de expiração** empurrada para o futuro, e depois transferir os seus fundos para este novo wallet.



O Bitcoin Keeper simplifica este processo com uma função de atualização integrada. A aplicação trata automaticamente da complexidade em segundo plano: basta seguir os passos guiados, sem ter de criar manualmente um novo wallet ou transferir os fundos. Planear esta operação regularmente, com bastante antecedência em relação à expiração do prazo mais curto configurado. Por exemplo, com uma chave de herança de 1 ano, actualize a cada 9-10 meses para manter uma margem de segurança.



## Guardar e exportar a configuração



Uma vez criado o wallet, a aplicação recorda-lhe que deve guardar o ficheiro de configuração. **Este passo é fundamental**: sem este ficheiro, os seus herdeiros não poderão reconstituir o wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Prima **Backup Wallet Recovery File**. Estão disponíveis várias opções de exportação:




- Exportação para PDF**: gera um documento completo com todas as informações do wallet
- Mostrar QR**: apresenta um código QR para importar a configuração noutro dispositivo
- Airdrop / Exportação de ficheiros**: exporta o ficheiro através das opções de partilha
- NFC**: partilha através de NFC com um dispositivo compatível



Multiplique as cópias: uma no seu notário, uma no cofre do banco, uma versão digital encriptada. A sua nova wallet aparece agora no separador Carteiras com as etiquetas "Chave múltipla", "2 de 3", "Chave de herança" e "Chave de emergência".



## Criar um canário Wallet



O Canary Wallet é um sistema de alerta precoce. A ideia: cada chave utilizada numa chave múltipla wallet também pode ser utilizada numa chave única wallet separada. Ao depositar uma pequena quantia neste "canário" wallet, qualquer movimento não autorizado assinala o comprometimento da chave.



![Canary Wallets](assets/fr/09.webp)



Existem duas formas de configurar um Canary Wallet. No separador **Mais**, prima **Carteiras Canário** na secção "Chaves e Carteiras". O ecrã explica o princípio: se alguém aceder a uma das suas chaves e encontrar fundos na chave única wallet associada, tentará retirá-los, o que o alertará.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Também é possível configurar o Canary diretamente a partir de uma tecla. No separador **Teclas**, selecione uma tecla (por exemplo, Tapsigner Genesis), prima o ícone **Configurações** (engrenagem) e, em seguida, **Canário Wallet**. O canário wallet associado abre-se, pronto a receber alguns satoshis de vigilância.



Depositar uma pequena quantia (alguns milhares de satoshis) em cada Canary Wallet. Se estes fundos forem movimentados sem o seu acordo, remova imediatamente a chave comprometida dos seus cofres multisig.



## Melhores práticas



**Teste a sua configuração** com uma pequena quantia de dinheiro antes de colocar uma grande quantia. Envie alguns milhares de satoshis para o cofre e, em seguida, experimente fazer uma despesa para verificar se domina o processo de assinatura com cada dispositivo. Teste também a importação do ficheiro de configuração noutro telemóvel para se certificar de que a cópia de segurança funciona.



**Distribuir as chaves de forma inteligente**. Para os Tapsigners, entregue-as num envelope selado com o PIN comunicado separadamente (por exemplo, na carta de Instruções de Recuperação guardada noutro local). Para as carteiras de hardware clássicas, mantenha o dispositivo com um terceiro de confiança e o seed em papel ou metal consigo ou com outro terceiro. Anote a impressão digital de cada chave e o respetivo nome no ficheiro de configuração para evitar confusões.



**Planear testes periódicos** (simulacros de incêndio). Anualmente, verifique se pode reconstruir o cofre a partir de cópias de segurança num telefone vazio. Teste os alertas Canary verificando os saldos. Simular cenários de perda ("e se eu perder o Coldcard?") para confirmar que as combinações de chaves restantes são suficientes.



**Não te esqueças de atualizar. Se definiu a sua chave de herança para 1 ano, actualize-a a cada 9-10 meses. Este é o preço que paga pela transmissão automática sem intervenção de terceiros.



**Manter o plano atualizado**. Qualquer alteração (substituição de uma chave, modificação de herdeiros, alteração do prazo) deve ser reflectida em todas as cópias de segurança e documentos. Gerar novamente os PDFs após cada modificação e redistribuir as novas versões.



## Limites e considerações



Apesar do poder destas ferramentas, é importante reconhecer as suas limitações para as gerir da forma mais eficaz possível.



A **complexidade** de um cofre multisig com relógios de ponto pode ser um risco em si: má configuração, incompreensão por parte dos herdeiros, perda de um elemento crítico entre os muitos componentes. O Bitcoin Keeper simplifica a experiência tanto quanto possível, mas continua a ser uma operação técnica. Este plano só deve ser utilizado se o montante a proteger o justificar. Para pequenos montantes, pode ser suficiente um plano mais simples.



Vale a pena pensar na **dependência da aplicação**. Embora o código seja de código aberto e baseado em padrões abertos (Miniscript, BSMS), certas funcionalidades dependem do ecossistema do Keeper. Mantenha uma cópia do aplicativo (APK para Android ou IPA para iOS) e documente em suas cartas aos herdeiros a possibilidade de usar outras carteiras compatíveis com Miniscript (como a Liana) para recuperar fundos.



Os corretores de confiança** introduzem um risco humano. O que acontece se um familiar mal intencionado utilizar a chave que lhe foi confiada antes do prazo? Ou se o advogado perder os seus documentos? Escolha cuidadosamente estas pessoas, explique claramente as suas responsabilidades e tenha um plano B. As carteiras Canary, as cópias de segurança redundantes e a própria estrutura do multisig continuam a ser a sua melhor proteção contra estes perigos.



## Conclusão



O Bitcoin Keeper, com o seu plano Diamond Hands, oferece uma caixa de ferramentas completa para o planeamento do património: Cofres melhorados com chaves temporizadas, documentos de acompanhamento, carteiras canário e apoio personalizado.



Não se trata apenas de uma questão técnica: é uma questão de conceber a arquitetura do seu património, distribuir inteligentemente as chaves e o conhecimento e testar regularmente o sistema. Um plano de herança Bitcoin bem concebido transforma os seus satoshis num legado real e transferível.