---
name: Bitcoin Keeper
description: Bitcoin móvel wallet para segurança e multi-sig
---

![cover](assets/cover.webp)



A gestão segura de bitcoins representa um grande desafio para qualquer detentor consciente dos desafios envolvidos na soberania financeira. Entre a simplicidade de um wallet móvel e a robustez de uma solução multi-sig, a lacuna técnica pode parecer assustadora para muitos utilizadores. O Bitcoin Keeper está posicionado precisamente nesta intersecção, oferecendo uma abordagem progressiva à segurança que acompanha os utilizadores à medida que evoluem.



O Bitcoin Keeper é uma aplicação móvel de código aberto, exclusivamente dedicada ao Bitcoin, desenvolvida pela equipa BitHyve. A sua ambição é tornar acessível a gestão avançada de carteiras, especialmente as configurações com várias assinaturas, mantendo uma interface intuitiva para os principiantes. A aplicação adopta o slogan "Secure today, Plan for tomorrow", reflectindo a sua filosofia de apoio a longo prazo.



Ao contrário das carteiras generalistas que gerenciam várias criptomoedas, o Bitcoin Keeper mantém um foco estrito no Bitcoin. Esta abordagem apenas ao bitcoin reduz a superfície de ataque potencial e simplifica muito a experiência do utilizador. A aplicação também se destaca pela sua integração nativa das carteiras de hardware mais difundidas e pelas suas funcionalidades avançadas de gestão do UTXO.



## O que é o Bitcoin Keeper?



### Filosofia e objectivos



O Bitcoin Keeper foi concebido para satisfazer as necessidades específicas dos bitcoiners que desejam manter o controlo total das suas chaves privadas. O projeto abraça totalmente os princípios fundamentais do Bitcoin: código fonte aberto e auditável, respeito pela privacidade e soberania do utilizador. Não é necessário qualquer registo ou informação pessoal para utilizar a aplicação, e esta pode mesmo ser executada offline para operações de assinatura.



O objetivo central é oferecer uma ferramenta flexível e preparada para o futuro para armazenar BTC durante vários anos, ou mesmo várias gerações, graças às funcionalidades herdadas. A aplicação permite que os utilizadores comecem simplesmente com um wallet móvel e depois evoluam gradualmente para soluções mais seguras com várias assinaturas.



### Arquitetura da aplicação



O Bitcoin Keeper organiza a gestão dos fundos em torno de dois conceitos distintos. O **Hot Wallet** é um wallet simples de chave única, guardado no telemóvel, concebido para despesas quotidianas e montantes modestos. Os cofres** são cofres com várias assinaturas (Multi-Key) que requerem várias chaves para autorizar uma despesa, concebidos para armazenamento seguro a longo prazo.



### Principais caraterísticas



O Bitcoin Keeper suporta quase todas as carteiras de hardware do mercado: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport e Tapsigner da Coinkite. A integração é efectuada através de diferentes métodos, consoante o dispositivo: Leitura de código QR, ligação NFC ou importação de ficheiros.



A aplicação também oferece uma gestão avançada do UTXO com etiquetagem de transacções, controlo de moedas para selecionar manualmente as entradas durante o envio e suporte do formato PSBT para transacções parcialmente assinadas.



## Instalação e configuração inicial



O Bitcoin Keeper está disponível gratuitamente no Android através da Google Play Store e no iOS através da App Store. O editor listado é o BitHyve. Antes de instalar, certifique-se de que o seu dispositivo está livre de malware, atualizado e não está enraizado ou desbloqueado.



No primeiro arranque, a aplicação pede-lhe para criar um código PIN de segurança. Este código protege o acesso ao seu wallet e encripta localmente os dados sensíveis. Escolha um código forte e memorize-o. Pode então ativar a autenticação biométrica (impressão digital ou Face ID) para um desbloqueio mais rápido.



![Installation et configuration du PIN](assets/fr/01.webp)



A aplicação apresenta então vários ecrãs introdutórios que explicam os seus três pilares: Criação de wallet para enviar e receber bitcoins, gestão de chaves com compatibilidade de hardware wallet e planeamento de legado para transmitir bitcoins. Prima "Get Started" e, em seguida, escolha "Start New" para criar uma nova configuração.



![Écrans d'introduction](assets/fr/02.webp)



## Descobrir a interface



A interface do Bitcoin Keeper está organizada em torno de quatro separadores principais acessíveis a partir da barra de navegação inferior:



![Les quatre onglets de l'application](assets/fr/03.webp)



O separador **Carteiras** apresenta as suas carteiras e os respectivos saldos. É aqui que acede às suas carteiras para enviar e receber bitcoins. As etiquetas "Hot Wallet" e "Single-Key" ou "Multi-Key" permitem-lhe identificar rapidamente o tipo de cada wallet.



O separador **Keys** centraliza a gestão das suas chaves de assinatura. Aqui encontra a chave móvel gerada pela aplicação, bem como todas as chaves importadas de carteiras de hardware. É também aqui que adiciona novos dispositivos de assinatura.



O separador **Concierge** oferece serviços de apoio: envie perguntas à equipa de apoio e contacte os consultores Bitcoin para obter assistência personalizada.



O separador **Mais** (Mais opções) dá acesso a definições como a ligação ao servidor pessoal, cópia de segurança de chaves, documentos de herança, preferências de visualização e gestão do wallet.



## Ligação ao seu próprio servidor



Para reforçar a sua confidencialidade, o Bitcoin Keeper permite-lhe ligar a aplicação ao seu próprio servidor Electrum, em vez de utilizar os servidores públicos predefinidos.



![Configuration du serveur Electrum](assets/fr/04.webp)



No separador Mais, desloque-se para baixo para encontrar as definições do servidor. Prima "Adicionar servidor" para configurar uma nova ligação. Pode escolher entre "Servidor público" (servidores públicos pré-configurados) e "Electrum privado" (o seu próprio servidor).



Para um servidor privado, introduza o URL (por exemplo, umbrel.local para um nó Umbrel) e o número da porta (normalmente 50001). Active o SSL se o seu servidor o suportar. Pode também digitalizar um código QR de configuração. Depois de ter introduzido os parâmetros, prima "Connect to Server" (Ligar ao servidor).



Se ainda não tem o seu próprio nó Bitcoin, veja o nosso tutorial sobre o Umbrel, uma forma simples e económica de fazer o seu próprio nó:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Receber bitcoins



No separador Carteiras, selecione o wallet do qual pretende receber fundos, premindo-o. O ecrã wallet apresenta o saldo e três botões de ação: Enviar Bitcoin, Receber Bitcoin e Ver todas as moedas.



![Réception de bitcoins](assets/fr/05.webp)



Premir "Receber Bitcoin". O Bitcoin Keeper gera um novo endereço de receção no formato Bech32 (começando por bc1...), juntamente com o seu código QR. Pode acrescentar uma etiqueta a este endereço para identificar a origem dos fundos. Partilhe o endereço com o remetente, exibindo o código QR ou copiando o endereço de texto.



A aplicação gera automaticamente um novo endereço para cada receção, preservando a sua privacidade. Utilize "Get New Address" para obter um endereço em branco, se necessário.



## Gestão do UTXO



O Bitcoin Keeper oferece uma visibilidade completa do UTXO (Unspent Transaction Outputs) que compõe o seu saldo. A partir de um ecrã wallet, prima "Ver todas as moedas" para aceder ao gestor de cantos.



![Gestion des UTXO](assets/fr/06.webp)



O ecrã "Gerir moedas" lista cada UTXO individualmente com a sua quantidade e etiqueta. Esta vista permite-lhe localizar a origem das suas moedas e organizá-las. Pode selecionar UTXOs específicos através de "Select to Send" para enviar com controlo de moedas, evitando assim misturar moedas de diferentes origens.



## Enviar bitcoins



Para enviar, selecionar a carteira de origem e premir "Enviar Bitcoin". Introduza o endereço de destino (colado ou digitalizado através de um código QR) e, opcionalmente, adicione uma etiqueta para identificar o destinatário.



![Envoi de bitcoins](assets/fr/07.webp)



O ecrã seguinte permite-lhe introduzir o montante a enviar. A interface apresenta o seu saldo disponível e a conversão da moeda fiduciária. Selecione a prioridade de carregamento: Baixa (económica, ~60 minutos), Média ou Alta (prioritária). Os custos estimados em sats/vbyte são apresentados em tempo real. Prima "Enviar" para continuar.



![Confirmation et envoi](assets/fr/08.webp)



Um ecrã de resumo apresenta todos os detalhes: wallet origem, endereço de destino, prioridade da transação, encargos de rede, montante enviado e total. Verifique cuidadosamente estas informações, uma vez que as transacções Bitcoin são irreversíveis. Prima "Confirm & Send" (Confirmar e enviar) para enviar a transação.



Aparece uma confirmação "Enviar com êxito" com o resumo completo. A transação é visível no histórico "Transacções recentes" com a sua etiqueta.



## Guardar as suas chaves



Fazer uma cópia de segurança da sua chave de recuperação é um passo fundamental. No separador Mais, vá para a secção "Cópia de segurança e recuperação" e clique em "Chave de recuperação".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



O ecrã apresenta o estado das suas cópias de segurança. Para verificar a sua cópia de segurança, a aplicação pede-lhe que confirme uma palavra específica da sua frase (por exemplo, a 7ª palavra). Esta verificação garante que escreveu corretamente a sua frase de recuperação.



Em "Recovery Key Settings" (Definições da chave de recuperação), pode ver a sua frase completa através de "View Recovery Key" (Ver chave de recuperação) e ver a impressão digital do signatário da sua chave. Guarde a sua frase de 12 palavras num papel, num local seguro, longe da humidade e do fogo. Nunca a guarde num dispositivo ligado.



## Adicionar uma chave externa (hardware wallet)



Uma das principais vantagens do Bitcoin Keeper é a integração de carteiras de hardware. No separador Keys (Chaves), prima "Add key" (Adicionar chave) para adicionar um novo dispositivo de assinatura.



![Ajout d'une clé hardware](assets/fr/10.webp)



Selecione "Adicionar chave de um hardware" para ligar um hardware wallet. A aplicação suporta uma vasta gama de dispositivos: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner e Specter Solutions.



### Configuração do Tapsigner



O Tapsigner é um cartão NFC da Coinkite particularmente adaptado à utilização móvel. Se quiser saber mais, temos um tutorial dedicado :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Para adicionar a Tapsigner, selecione-a na lista de carteiras de hardware.



![Configuration du Tapsigner](assets/fr/11.webp)



Primeiro, introduza o código PIN de 6-32 dígitos impresso no verso do seu cartão (predefinição nos cartões novos) ou o seu PIN, se já estiver configurado. Prima "Prosseguir" e aproxime o seu Tapsigner da parte de trás do seu telemóvel quando for apresentada a mensagem "Pronto para digitalizar". A comunicação NFC importa automaticamente a chave pública. Pode então acrescentar uma descrição (por exemplo, "Cartão Métro") para identificar esta chave.



## Criar uma carteira multisig



Depois de ter configurado as suas chaves, pode criar um wallet com várias assinaturas, combinando vários dispositivos. No separador Carteiras, clique em "Adicionar Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Tem três opções: "Create Wallet" (Criar Wallet) para uma nova carteira, "Import Wallet" (Importar Wallet) para restaurar um wallet existente ou "Collaborative Wallet" (Wallet colaborativo) para uma abóbada partilhada. Selecione "Create Wallet" (Criar Wallet) e depois "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



O ecrã seguinte oferece diferentes configurações: "Tecla única", "2 de 3 teclas múltiplas" ou "3 de 5 teclas múltiplas". Para um multi-sig personalizado, prima "Selecionar configuração personalizada". Por exemplo, escolha "1 de 2": é necessária uma única assinatura de duas teclas possíveis.



Em seguida, selecione as chaves que constituirão o seu cofre. No nosso exemplo, combinamos a "Mobile Key" (chave de software do telemóvel) com o "TAPSIGNER" (Metro Card). Esta configuração oferece redundância: se uma das chaves ficar inacessível, pode sempre gastar os seus fundos com a outra.



![Finalisation du wallet multisig](assets/fr/14.webp)



Dê um nome ao seu wallet (por exemplo, "Plano de Teste B"), adicione uma descrição opcional e verifique as teclas selecionadas. Prima "Create Your Wallet" (Criar o seu Wallet). Aparece uma mensagem de confirmação "Wallet Created Successfully" (Wallet criado com sucesso), lembrando-o de guardar o ficheiro de recuperação do wallet.



O seu novo wallet multisig aparece agora no separador Carteiras com a etiqueta "Multi-key" e a indicação "1 of 2".



### Guardar ficheiro de configuração



**Ao contrário de um wallet simples, onde a frase de recuperação é suficiente para restaurar o acesso, um wallet multisig requer também o ficheiro de configuração que descreve a estrutura do cofre (que chaves participam, quantas assinaturas são necessárias). Sem este ficheiro, mesmo com todas as frases de recuperação, não será possível reconstruir o seu wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Para exportar este ficheiro, selecione o seu multisig wallet no separador Carteiras e, em seguida, prima o ícone Definições (engrenagem) no canto superior direito. Em "Wallet Settings" (Definições do Wallet), clique em "Wallet configuration file" (Ficheiro de configuração do Wallet). Estão disponíveis várias opções de exportação:





- Exportar PDF**: gera um documento PDF com todas as informações do wallet
- Mostrar QR**: apresenta um código QR digitalizável para importar a configuração para outro dispositivo
- Airdrop / Exportação de ficheiros**: exporta o ficheiro através das opções de partilha do seu telemóvel
- NFC**: partilha através de NFC com um dispositivo compatível



Mantenha este ficheiro de configuração separado das suas frases de recuperação, de preferência num suporte encriptado ou impresso. Se perder o seu telefone, este ficheiro combinado com as frases de recuperação para cada chave participante permitir-lhe-á reconstruir o seu wallet multisig no Bitcoin Keeper ou em qualquer outro software compatível.



## Melhores práticas



### Organização do fundo



Estruture os seus bitcoins de acordo com a sua utilização: uma wallet Single-Key quente para despesas correntes com montantes limitados, e um ou mais Vaults Multi-Key para poupanças a longo prazo. A etiquetagem sistemática UTXO ajudá-lo-á a manter um registo da origem dos seus fundos, o que é particularmente útil para gerir a confidencialidade e evitar misturar moedas de diferentes origens.



Mantenha o seu telemóvel seguro: active o bloqueio biométrico, efectue actualizações do sistema regularmente e mantenha-se atento às aplicações instaladas. E mantenha o Bitcoin Keeper atualizado com os patches de segurança.



### Segurança das cópias de segurança



Mantenha pelo menos duas cópias de cada frase de recuperação em papel, guardadas em locais geograficamente separados. Para grandes quantias, considere a possibilidade de gravar em metal resistente a desastres. Nunca guarde estas frases num dispositivo ligado à Internet e nunca as fotografe.



Para os cofres multi-sig, guarde também o ficheiro de configuração (Wallet Recovery File), que contém as chaves públicas participantes e a estrutura do cofre. Este ficheiro, combinado com as frases de recuperação de chaves, permite que o wallet seja reconstruído em qualquer software compatível, como o Sparrow ou o Specter.



## Vantagens e limitações



### Destaques





- A aplicação exclusiva Bitcoin reduz a complexidade e o risco
- Integração nativa de cofres multisig com orientação passo-a-passo
- Suporte alargado de hardware wallet (Tapsigner, Coldcard, Ledger, Jade, etc.)
- Gestão avançada do UTXO e controlo das moedas
- Pode ser ligado a um servidor pessoal Electrum
- Código-fonte aberto e auditável



### Restrições a considerar





- Interface principalmente em inglês
- Algumas funcionalidades premium (Cloud Backup, Servidor Assistido) requerem uma atualização
- A configuração do Multisig requer formação inicial



## Conclusão



O Bitcoin Keeper destaca-se como uma solução escalável para gerir os seus bitcoins. A sua abordagem progressiva, desde o simples wallet quente até aos Vaults com várias assinaturas, significa que a segurança pode ser actualizada à medida que as necessidades mudam. A capacidade de integrar facilmente carteiras de hardware como o Tapsigner abre caminho para configurações robustas sem complexidade excessiva.



A orientação exclusiva para bitcoin, o código-fonte aberto e o respeito pela privacidade fazem com que seja uma escolha alinhada com os valores fundamentais do ecossistema Bitcoin.



Este tutorial cobre as funcionalidades essenciais do Bitcoin Keeper na sua versão gratuita. A aplicação também oferece funcionalidades premium (Cloud Backup, Assisted Server Backup, Canary Wallets) que serão objeto de um tutorial dedicado. Num próximo guia, iremos também explorar a funcionalidade de Planeamento de Heranças, que lhe permite preparar a transmissão dos seus bitcoins aos seus entes queridos, graças aos cofres melhorados e aos documentos de acompanhamento integrados na aplicação.



## Recursos





- Sítio Web oficial: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centro de ajuda: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Código fonte: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)