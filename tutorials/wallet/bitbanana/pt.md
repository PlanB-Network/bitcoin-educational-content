---
name: BitBanana
description: Gestor móvel para o seu nó Lightning
---

![cover](assets/cover.webp)



Neste tutorial, você aprenderá como instalar e configurar o BitBanana no Android para controlar seu nó Lightning a partir do seu smartphone. Veremos como conectar o aplicativo à sua infraestrutura existente (Umbrel, RaspiBlitz, myNode ou qualquer nó LND/Core Lightning), fazer pagamentos Lightning, gerenciar seus canais remotamente, visualizar sua receita de roteamento e fazer backup de suas configurações. Você também aprenderá sobre as práticas de segurança recomendadas para proteger o acesso ao seu nó e como ele se compara ao Zeus, uma alternativa popular.



## Apresentando a BitBanana



BitBanana é uma aplicação móvel Android de código aberto que transforma o seu smartphone num painel completo para controlo remoto do seu nó Lightning. Ao contrário das carteiras Lightning, que incorporam um nó local no telefone, a BitBanana adopta uma filosofia de controlo 100% remoto: a aplicação não possui satoshi e liga-se apenas à sua infraestrutura existente.



Desenvolvida por Michael Wünsch sob a licença MIT, a aplicação garante total transparência com zero coleta de dados pessoais e compilações reproduzíveis verificadas. A BitBanana suporta nativamente LND e Core Lightning através de URIs padrão (`lndconnect://` e `clngrpc://`), simplificando drasticamente a configuração inicial. O aplicativo também reconhece LndHub e Nostr Wallet Connect para usuários sem um nó pessoal, embora esses modos operem de forma custodial com funcionalidade limitada.



A interface oferece acesso total a todas as funções críticas do seu nó: envio e receção de pagamentos (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), gestão de canais Lightning (abertura, fecho, ajuste de taxas, reequilíbrio), controlo avançado de moedas e gestão de torres de vigia. A BitBanana também implementa várias camadas de segurança robustas: bloqueio biométrico, modo furtivo, PIN de emergência e suporte nativo ao Tor para tornar as conexões anónimas.



## Plataformas suportadas e instalação



### Instalação



A BitBanana está disponível exclusivamente para Android 8.0 ou superior. A aplicação não existe em iOS e não está prevista nenhuma versão. Esta limitação é explicada pela história do projeto: A BitBanana é a sucessora direta do Zap Android, originalmente desenvolvido por Michael Wünsch, que decidiu continuar o seu trabalho sob a sua própria marca. O Zap era uma família de aplicações separadas (Zap Android, Zap iOS, Zap Desktop) desenvolvidas por diferentes colaboradores com bases de código separadas. A BitBanana está a desenvolver apenas o ramo Android.



Além disso, o ecossistema iOS apresenta restrições regulamentares e técnicas significativas para aplicações Lightning sem custódia. Em 2023, a Apple rejeitou uma atualização do Zeus por "violações de licença" e, em 2024, o Phoenix Wallet abandonou a App Store dos EUA face às incertezas regulamentares relativas aos fornecedores de serviços Lightning. Estes obstáculos explicam por que razão muitos programadores Lightning preferem o Android, que oferece uma política mais aberta para aplicações sem custódia.



Estão disponíveis três métodos de instalação para Android: Google Play Store (mais de 5000 instalações, actualizações automáticas), F-Droid (compilações reproduzíveis, verificação do código-fonte) ou APK manual a partir do GitHub.



![BitBanana](assets/fr/01.webp)



O sítio Web oficial da bitbanana.app (à esquerda) gaba-se de ser "100% autocustodial com ZERO recolha de dados". O ecrã central mostra as três opções de download: F-Droid (recomendado), Google Play e APK. O ecrã da direita mostra a permissão de notificações para alertas de pagamento.



A aplicação solicita permissões: rede (ligação ao nó), câmara (códigos QR), NFC (LNURL), serviços em segundo plano (notificações), biometria (segurança) e VPN WireGuard. Sem localizadores, sem recolha de dados. Ativar o bloqueio por palavra-passe ou biométrico para proteger o acesso.



## Configuração inicial



### Ligação a um nó LND



Para conectar o BitBanana ao seu nó LND (Umbrel, RaspiBlitz, myNode), obtenha um URI `lndconnect` ou código QR contendo o endereço, certificado TLS e macaroon de autenticação.



Para este tutorial, estamos a utilizar um nó LND através de umbrel. Para obter mais detalhes, consulte nosso tutorial dedicado :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Na aplicação Lightning Node, aceda ao menu no canto superior direito e selecione "Connect wallet".



![BitBanana](assets/fr/04.webp)



Selecione **gRPC (Tor)** para ligar através do Tor (recomendado). São apresentados o código QR e os detalhes (Host .onion, Port 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



Na BitBanana, prima "CONNECT NODE", leia o código QR ou cole o URI. Autorize o acesso à câmara e verifique o endereço .onion apresentado antes de confirmar.



*ligação *Core Lightning**



Se utilizar o Core Lightning (CLN) em vez do LND, o processo permanece idêntico, com o URI `clngrpc://` contendo os certificados TLS mútuos. O Core Lightning suporta nativamente BOLT12 (ofertas), permitindo faturas reutilizáveis e pagamentos recorrentes não disponíveis no LND.



**Ligação sem nó pessoal (LNbits/hospedado)**



Se você não tiver um nó Lightning, a BitBanana pode se conectar a serviços hospedados via LndHub (o protocolo usado pela BlueWallet e LNbits) ou Nostr Wallet Connect (NWC). Atenção: esses modos operam em modo de custódia (o serviço hospeda seus fundos) com funcionalidade limitada. Não será possível gerenciar canais ou configurar taxas de roteamento, e só será possível enviar e receber pagamentos Lightning.



Para mais detalhes sobre o LNbits ou o Nostr Wallet Connect, consulte os nossos vários tutoriais:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Utilização diária



### Interface principal



O ecrã inicial apresenta o seu saldo Lightning, com o menu no canto superior esquerdo a dar acesso às seguintes secções: Canais, Encaminhamento, Assinar/Verificar, Nós, Contactos, Definições, Cópia de segurança. O ícone do relógio (canto superior direito) abre o histórico de transacções. Os botões "Enviar" e "Receber" na parte inferior permitem-lhe enviar e receber os seus satoshis.



![BitBanana](assets/fr/05.webp)



### Pagamentos do Lightning e do on-chain



![BitBanana](assets/fr/10.webp)



**Enviar um pagamento:** Prima o botão "Enviar" a partir do ecrã inicial. O ecrã de pagamento (à esquerda) permite-lhe colar um endereço ou dados de pagamento no campo "Address ou dados de pagamento", com um scanner QR no canto superior direito para digitalizar códigos. Pode também selecionar um contacto guardado na secção "Contactos" para evitar ter de digitalizar de cada vez.



BitBanana reconhece inteligentemente todos os formatos de pagamento: facturas Lightning clássicas (cadeias de caracteres que começam por `lnbc`), Lightning Address (formato de e-mail como `utilisateur@domaine.com`), códigos LNURL-pay para pagamentos dinâmicos, LNURL-withdraw para levantamento de fundos e até pagamentos Keysend diretamente para uma chave pública Lightning sem uma fatura prévia. A aplicação executa automaticamente as resoluções LNURL necessárias em segundo plano.



Uma vez que a fatura foi carregada, a BitBanana exibe todos os detalhes: valor exato, taxas de roteamento estimadas, descrição do pagamento (se fornecido pelo destinatário) e data de validade da fatura. Após a confirmação, o pagamento é encaminhado através dos seus canais Lightning. É possível visualizar a rota percorrida passo a passo e as taxas realmente pagas nos detalhes da transação.



**Receber o pagamento:** Premir o botão "Receber". Um seletor (ecrã da direita) permite-lhe escolher entre Lightning (pagamento instantâneo através dos seus canais) e On-Chain. Para um recibo Lightning, introduza o montante desejado em satoshis (ou deixe em 0 para criar uma fatura sem montante fixo para o pagador preencher) e adicione uma descrição opcional para aparecer na fatura. A BitBanana gera instantaneamente uma fatura Lightning com código QR para digitalização. Também pode copiar a fatura como texto e enviá-la por correio eletrónico. Assim que o pagamento é recebido, uma notificação push avisa-o e a transação aparece imediatamente no histórico com todos os seus detalhes.



### Canais e encaminhamento



![BitBanana](assets/fr/06.webp)



A secção "Canais" apresenta as suas capacidades de envio/receção e lista os seus canais com avatares únicos. Cada canal mostra a sua liquidez dividida entre saldo local e remoto. Toque num canal para obter todos os detalhes e acções (fechar, alterar taxas de encaminhamento). Os três pontos no canto superior direito dão acesso à opção "Reequilibrar" para reequilibrar a liquidez dos seus canais. O botão "+" abre um novo canal.



A secção de encaminhamento (ecrã central) apresenta as receitas de encaminhamento por período (1D, 1W, 1M, 3M, 6M, 1Y) com um histórico detalhado de encaminhamentos para otimizar a sua estratégia.



Assinar/Verificar (ecrã da direita) permite-lhe assinar/verificar criptograficamente mensagens para provar o controlo do nó.



### Nós múltiplos e parâmetros



![BitBanana](assets/fr/07.webp)



**Gerir nós**: lista os seus nós, com botões para adicionar manualmente, digitalizar QR ou alternar entre nós. Em particular, pode configurar diferentes tipos de ligação ao mesmo nó: LAN, VPN ou Tor.



**Gerir contactos**: armazena os seus contactos Lightning para pagamentos rápidos.



**Definições**: personalizar a moeda, o idioma e os avatares. Secção Segurança e privacidade: App Lock (PIN/biometria), Hide balance (modo furtivo), Tor (anonimização de IP). Configuração de oráculos de preços, exploradores de blocos, estimadores de taxas personalizados.



## Vantagens e limitações



**Destaques




- Mobilidade total: controle seu Lightning node de qualquer lugar
- Funcionalidade completa: pagamentos (LNURL, Lightning Address, BOLT 12), gestão de canais, controlo de moedas, torres de vigilância, multi-nós
- Segurança: PIN/biometria, modo furtivo, PIN de emergência, Tor nativo, bloqueio de capturas de ecrã
- Gratuito, de fonte aberta (MIT), sem comissões, sem recolha de dados



**Limitações:**




- Requer um nó Lightning ativo (ou LNbits em modo de custódia)
- Não está prevista uma versão iOS
- A segurança do acesso ao telemóvel é fundamental (administrador da macaroon = acesso total ao nó)



## Melhores práticas



**Segurança




- Ativar o bloqueio por PIN/biometria (impede o acesso não autorizado ao nó)
- Configurar um PIN de emergência (elimina dados sensíveis em caso de coação)
- Nunca partilhe o seu URI de início de sessão ou macaroon
- Modo furtivo em ambientes hostis



**Início de sessão:**




- Malha VPN (Tailscale, ZeroTier): melhor compromisso entre velocidade e segurança
- Tor: máxima confidencialidade, maior latência
- Clearnet: evitar, exceto se necessário (exposição do IP, portas abertas)



### Cópia de segurança e restauro



Por fim, o menu "Cópia de segurança" permite-lhe guardar as suas configurações para migração telefónica ou reinstalação.



![BitBanana](assets/fr/08.webp)



**Importante:** A cópia de segurança NÃO contém cópias de segurança do seed ou dos canais (a efetuar no nó). Contém: configurações do nó (endereços, certificados, macaroons), etiquetas, contactos, parâmetros. O botão Restaurar permite-lhe importar uma cópia de segurança existente. É necessária uma confirmação antes de guardar.



![BitBanana](assets/fr/09.webp)



Introduzir uma palavra-passe de encriptação (ecrã da direita). O sistema abre o seletor de ficheiros (ecrã da esquerda) para guardar `BitBananaBackup_2025-XX-XX.dat`. Confirmação "Backup created" (cópia de segurança criada).



**Segurança:** Armazene a cópia de segurança encriptada (nuvem pessoal, USB, NAS). Nunca partilhe ficheiros ou palavras-passe. Teste o restauro regularmente. A cópia de segurança recupera ligações, não fundos.



## BitBanana vs Zeus: Qual é a diferença?



Se estiver a explorar aplicações móveis para gerir um nó Lightning, é provável que se depare com o Zeus, uma alternativa popular ao BitBanana. Ao contrário do BitBanana, que se concentra exclusivamente no controlo remoto de um nó existente, o Zeus tem uma abordagem mais abrangente, oferecendo dois modos de funcionamento: um nó Lightning incorporado diretamente na aplicação (modo incorporado com LND integrado) e ligação remota a um nó externo, tal como o BitBanana.



Esta dupla funcionalidade torna o Zeus particularmente atrativo para os principiantes que desejam experimentar o Lightning sem qualquer infraestrutura prévia. O modo incorporado permite o arranque imediato com um nó móvel completo, enquanto os utilizadores avançados podem mudar para a ligação remota depois de o seu nó pessoal ter sido configurado. O Zeus também suporta LND e Core Lightning para conexão remota, como o BitBanana.



Outra grande vantagem do Zeus é a sua disponibilidade em várias plataformas (iOS e Android), enquanto o BitBanana continua a basear-se exclusivamente no Android. O Zeus também incorpora a infraestrutura Olympus LSP para facilitar a receção de pagamentos Lightning através de canais just-in-time, um sistema de ponto de venda para comerciantes e uma funcionalidade de swap integrada para gerir a liquidez.



No entanto, a BitBanana mantém os seus pontos fortes específicos: uma interface mais simples e mais racionalizada, uma melhor experiência do utilizador (UX) graças ao seu foco exclusivo no controlo remoto e uma abordagem educacional com explicações contextuais. A Zeus oferece mais funcionalidades, mas à custa de uma interface mais complexa. A aplicação continua a ser particularmente adequada para os utilizadores que pretendem controlar um nó exclusivamente à distância, sem funções de custódia.



Para saber mais sobre o Zeus, consulte os seguintes tutoriais:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusão



A BitBanana transforma o seu smartphone Android num painel de controlo Lightning completo, oferecendo uma mobilidade sem precedentes aos operadores de nós. A aplicação abrange todas as funcionalidades: pagamentos (todos os formatos), gestão de canais, controlo de moedas, torres de vigilância, multi-nó, com segurança reforçada (PIN/biometria, Tor, PIN de emergência).



Totalmente soberana, a BitBanana não recolhe nenhum dado e não compromete nem a confidencialidade nem o controlo dos seus fundos. O código fonte aberto (MIT) garante a transparência.



## Recursos



### Documentação oficial




- [sítio Web da BitBanana](https://bitbanana.app)
- [Documentação completa](https://docs.bitbanana.app)
- [Código-fonte do GitHub](https://github.com/michaelWuensch/BitBanana)



### Instalação




- [Google Play Store] (https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)