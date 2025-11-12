---
name: Ashigaru
description: O fork da Samourai Wallet para proteger, gerir e misturar os seus bitcoins
---

![cover](assets/cover.webp)



Ashigaru é uma aplicação Bitcoin mobile wallet que dá continuidade ao projeto Samourai Wallet, mas sob uma nova forma. Este software nasceu num contexto particular: em abril de 2024, os fundadores do Samourai Wallet foram presos pelas autoridades americanas e os seus servidores foram apreendidos. Embora a própria aplicação Samurai tenha permanecido utilizável, atualmente já não é mantida. Ashigaru é uma versão gratuita para o fork do Samurai Wallet, mantida por uma equipa anónima para garantir a continuidade da funcionalidade do Samurai e salvaguardar a sua filosofia original: defender a privacidade e a soberania dos utilizadores do Bitcoin.



O Ashigaru retoma muito do ADN do Samourai: uma interface semelhante, uma abordagem obviamente autocustodial, código aberto e um enfoque na privacidade. O código é distribuído sob a licença GNU GPLv3, que garante que qualquer pessoa pode auditar, modificar ou redistribuir o software.



A aplicação Ashigaru integra um conjunto de ferramentas avançadas para a confidencialidade e a gestão dos seus UTXOs:




- Whirlpool**, um protocolo de junção de moedas baseado no Zerolink, que permite quebrar as ligações determinísticas entre entradas e saídas de transacções, sem perder a soberania sobre os seus fundos.
- PayNym**, que implementa códigos de pagamento reutilizáveis (BIP47), agora representados através de um sistema de avatar "*Pepehash*".
- Ricochete**, uma funcionalidade que adiciona saltos intermédios às transacções para as tornar mais difíceis de localizar.
- E, claro, o ***Coin Control*** para selecionar, congelar e rotular os seus UTXOs com precisão.
- Despesas em lote***, para reduzir os custos agrupando vários pagamentos numa única transação.
- O **Modo furtivo**, que esconde a aplicação no seu telemóvel atrás de um lançador fictício para passar despercebido durante uma inspeção física do seu telemóvel.
- Ferramentas avançadas de despesas para otimizar a sua confidencialidade (payjoin, stonewall...).
- Um sistema de recuperação optimizado utilizando a frase-chave BIP39.
- Um sistema para otimizar automaticamente a escolha das taxas de transação.



![Image](assets/fr/01.webp)



A Ashigaru destina-se, portanto, a utilizadores que estão conscientes das questões relacionadas com a rastreabilidade das transacções no Bitcoin. Quer seja um utilizador preocupado com a privacidade, um bitcoiner experiente empenhado na auto-custódia ou um indivíduo exposto aos riscos de uma vigilância acrescida, esta aplicação wallet fornece-lhe as ferramentas necessárias para recuperar o controlo da sua atividade no Bitcoin.



O Ashigaru está disponível numa versão móvel através da sua aplicação, que exploraremos neste tutorial. Mas também pode ser utilizado no PC com o ***Ashigaru Terminal***, que apresentaremos num futuro tutorial.



![Image](assets/fr/02.webp)



Neste tutorial, gostaria de vos apresentar a utilização básica do Ashigaru: instalação, ligação ao Dojo, cópia de segurança, receção e envio de bitcoins. As ferramentas avançadas serão apresentadas noutros tutoriais dedicados.



## 1. Pré-requisitos para Ashigaru



A aplicação requer alguns pré-requisitos para funcionar corretamente. Em primeiro lugar, não se trata de uma aplicação disponível em lojas clássicas como a Google Play Store ou a App Store. É instalada manualmente no seu telefone apenas a partir do seu ficheiro `.apk`, que pode ser descarregado através da rede Tor. Por isso, se estiver a utilizar um iPhone, este método não funcionará: precisará de um dispositivo Android.



Para fazer o download do arquivo `.apk` via Tor, você precisará de um navegador capaz de acessar sites `.onion`. A forma mais fácil é instalar a aplicação Tor Browser no seu telemóvel, disponível na [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) ou diretamente [através do seu `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Os smartphones mais recentes bloqueiam a instalação de aplicações de fontes desconhecidas por predefinição. Terá de ativar temporariamente esta opção para o Navegador Tor nas definições do seu dispositivo para permitir a instalação. Quando a aplicação estiver instalada, lembre-se de desativar esta função para reforçar a segurança do seu telefone.



Outro pré-requisito essencial para usar Ashigaru é um nó Bitcoin Dojo. Por razões de segurança e soberania, a equipa Ashigaru não mantém um servidor centralizado para ligar a sua aplicação. Por isso, terá de executar a sua própria instância Dojo ou ligar-se a uma instância de confiança.



O Dojo permite que a sua aplicação Ashigaru consulte a informação da cadeia de blocos, veja os seus saldos de endereços e transmita as suas transacções na rede Bitcoin.



Para saber mais sobre o Dojo e aprender a instalá-lo, convido-o a seguir este tutorial dedicado:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Se realmente não tem meios para gerir o seu próprio Dojo, pode encontrar pessoas dispostas a partilhar a sua instância gratuitamente em [dojobay.pw] (https://www.dojobay.pw/mainnet/). Esta pode ser uma solução temporária, mas, a longo prazo, recomendo que utilize o seu próprio Dojo para garantir a sua soberania e confidencialidade.



## 2. Verificar e instalar a aplicação Ashigaru



### 2.1. Descarregar a aplicação Ashigaru



No telemóvel, abra o navegador Tor e aceda ao [site oficial do Ashigaru] (https://ashigaru.rs/download/), na secção `Download`. Em seguida, clique no botão `Download for Android` para baixar o arquivo de instalação.



![Image](assets/fr/04.webp)



Antes de instalar a aplicação no seu dispositivo, vamos verificar a sua autenticidade e integridade. Este é um passo muito importante, especialmente quando se instala uma aplicação diretamente a partir de um ficheiro `.apk'.



### 2.2. Verificar a aplicação Ashigaru



Volta ao [site oficial do Ashigaru] (https://ashigaru.rs/download/) na secção `Download`, depois copia a mensagem apresentada sob o título `SHA-256 Hash do ficheiro APK`. Copie todo o bloco, desde `BEGIN PGP SIGNED MESSAGE` até `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Ainda no seu telefone, abra uma nova aba no Navegador Tor e vá para [a ferramenta de verificação Keybase] (https://keybase.io/verify). Cola a mensagem que acabaste de copiar no campo fornecido, depois clica no botão `Verificar`.



![Image](assets/fr/06.webp)



Se a assinatura for genuína, o Keybase mostrará uma mensagem confirmando que o arquivo foi assinado pelos desenvolvedores do Ashigaru. Também pode clicar no perfil `ashigarudev` indicado pelo Keybase e verificar se a impressão digital da chave corresponde exatamente a : `A138 06B1 FA2A 676B`.



No entanto, se aparecer um erro nesta fase, isso significa que a assinatura é inválida. Neste caso, **não instale o APK**. Recomece do início ou peça ajuda à comunidade antes de continuar.



![Image](assets/fr/07.webp)



O Keybase forneceu-lhe o hash da aplicação. Vamos agora verificar se o hash do ficheiro `.apk` que descarregou corresponde ao verificado no Keybase. Para isso, acede a [HASH FILE ONLINE] (https://hash-file.online/).



![Image](assets/fr/08.webp)



Clique no botão `BROWSE...` e selecione o ficheiro `.apk` descarregado no passo 2.1.


Em seguida, escolha a função hash `SHA-256` e clique em `CALCULATE HASH` para calcular o hash do seu ficheiro.



![Image](assets/fr/09.webp)



O site mostrará o hash do seu ficheiro `.apk`. Compare-o com o hash que verificou em Keybase.io. Se os dois hashes forem idênticos, a verificação de autenticidade e integridade foi bem-sucedida. Pode agora proceder à instalação da aplicação.



![Image](assets/fr/10.webp)



### 2.3. instalar a aplicação Ashigaru



Para instalar a aplicação, abra o gestor de ficheiros do seu telefone e vá para a pasta de downloads. Em seguida, clique no ficheiro `.apk` que acabou de verificar e confirme a instalação quando lhe for pedido.



![Image](assets/fr/11.webp)



Ashigaru agora está instalado no seu telefone.



## 3. Inicializar a aplicação e criar uma carteira Bitcoin



Ao lançar a aplicação pela primeira vez, selecionar `MAINNET`.



![Image](assets/fr/12.webp)



Em seguida, clique em "Começar".



![Image](assets/fr/13.webp)



Vamos agora criar um novo portefólio Bitcoin. Prima o botão `Criar um novo wallet`.



![Image](assets/fr/14.webp)



### 3.1. criar uma carteira Bitcoin



Ashigaru necessita de um passphrase BIP39. Escolhe o teu passphrase e insere-o nos campos apropriados. Deve ser tão longo e aleatório quanto possível para resistir a um ataque de força bruta.



Faça imediatamente uma cópia de segurança física deste passphrase. Este é um passo muito importante: se perder o seu telemóvel, **se já não tiver este passphrase, já não poderá aceder aos seus bitcoins** guardados com o seu Ashigaru wallet. Este mesmo passphrase é também utilizado para encriptar o ficheiro de recuperação do wallet.



Se não sabe o que é um passphrase, ou não compreende totalmente o seu funcionamento, recomendo vivamente que leia este tutorial adicional. Isto é importante, porque o passphrase é um elemento crítico da sua segurança: uma utilização incorrecta pode resultar na perda permanente dos seus fundos.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Depois de ter introduzido o seu passphrase, clique em `NEXT`.



![Image](assets/fr/15.webp)



De seguida, escolha um código PIN. Este código será utilizado para desbloquear o seu Ashigaru wallet, protegendo-o contra o acesso físico não autorizado. Não está envolvido na derivação criptográfica das chaves do seu wallet. Isto significa que, mesmo sem conhecer o código PIN, qualquer pessoa com a sua frase mnemónica e o passphrase poderá recuperar o acesso aos seus bitcoins.



Opte por um código PIN longo e aleatório. Lembre-se de manter uma cópia de segurança num local separado do seu telemóvel, para evitar que sejam comprometidos simultaneamente.



![Image](assets/fr/16.webp)



Uma vez criado o código PIN, Ashigaru mostra a frase mnemónica do teu wallet. Atenção: esta frase, combinada com o teu passphrase, dá acesso total aos teus bitcoins. Qualquer pessoa que a detenha pode apoderar-se dos seus fundos, mesmo que não tenha acesso ao seu telemóvel. Esta sequência de 12 palavras pode ser utilizada para restaurar o seu wallet em caso de perda, roubo ou quebra do seu telemóvel. Por conseguinte, é importante guardá-la com o máximo cuidado num suporte físico (papel ou metal).



Nunca guarde esta frase em formato digital, ou arrisca-se a expor os seus fundos a roubo. Dependendo da sua estratégia de segurança, pode criar várias cópias físicas, mas nunca as divida. Mantenha as palavras na sua ordem exacta e certifique-se de que estão numeradas.



Finalmente, nunca guarde a mnemónica e o passphrase no mesmo local. Se ambos forem comprometidos simultaneamente, um atacante pode obter acesso ao seu wallet.



![Image](assets/fr/17.webp)



Para saber mais sobre como proteger a sua frase mnemónica, consulte este tutorial complementar :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru pede-te então para reconfirmares o teu passphrase. Aproveita esta oportunidade para verificar se a tua cópia de segurança física está correta.



![Image](assets/fr/18.webp)



### 3.2. ligar um dojo



Segue-se o passo de ligação ao teu Dojo. Como explicado na introdução, o Ashigaru tem de estar ligado a um Dojo para poder interagir com a rede Bitcoin.



Aceda à "Ferramenta de Manutenção" do seu Dojo e abra o menu "APRESENTAÇÃO".



![Image](assets/fr/19.webp)



No Ashigaru, prima o botão `Scan QR` e, em seguida, digitalize o código QR de ligação apresentado pelo seu DMT. De seguida, clique em `Continuar` para confirmar.



![Image](assets/fr/20.webp)



Introduza o seu código PIN para desbloquear o wallet. Isto levá-lo-á para a página de sincronização. É normal que surjam erros *PayNym* nesta fase, uma vez que o wallet é novo. Basta clicar em `Continuar`.



![Image](assets/fr/21.webp)



Será então encaminhado para a página inicial do seu portefólio.



![Image](assets/fr/22.webp)



Antes de prosseguir, recomendo que efectue uma recuperação de teste enquanto o wallet ainda não contém bitcoin. Isto permitir-lhe-á verificar se as suas cópias de segurança em papel estão a funcionar corretamente. Para saber como, siga este tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Configurar a aplicação Ashigaru



Para aceder às definições da aplicação, clique na imagem do seu *PayNym* no canto superior esquerdo e selecione "Definições".



![Image](assets/fr/23.webp)



Aqui encontra várias opções para adaptar o funcionamento do Ashigaru às suas necessidades. No entanto, recomendo vivamente que actives 2 parâmetros importantes desde o início.



Comece por abrir o menu `Segurança > Modo invisível` e, em seguida, active esta função se precisar dela. Esta função esconde a aplicação Ashigaru por detrás do nome, do logótipo e da interface de uma aplicação normal instalada no seu telefone. O objetivo é impedir que alguém identifique a Ashigaru no caso de uma inspeção física do seu telefone.



![Image](assets/fr/24.webp)



Cada aplicação falsa oferecida tem um método específico para desbloquear a verdadeira interface Ashigaru. Por exemplo, se escolheres a calculadora, a aplicação Ashigaru desaparece do teu ecrã inicial e é substituída por uma calculadora falsa. Quando a abres, vês uma interface clássica de calculadora a funcionar, mas para acederes ao Ashigaru, só tens de tocar no símbolo `=` cinco vezes rapidamente.



O segundo parâmetro importante a ativar é [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Esta opção permite-lhe aumentar o custo de uma transação se esta ficar presa nos mempools porque o custo é demasiado baixo. Pode activá-la através do menu `Transacções > Gastar usando RBF`.



![Image](assets/fr/25.webp)



Dica: Pode alterar a unidade de visualização da sua carteira de `BTC` para `sat` simplesmente clicando no saldo total apresentado na página inicial.



## 5. Receber bitcoins em Ashigaru



Agora que a sua carteira está operacional, pode receber satss. Para o fazer, prima o botão `+` no canto inferior direito da interface e, em seguida, o botão verde `Receber`.



![Image](assets/fr/26.webp)



Ashigaru mostra-lhe então o primeiro endereço de receção não utilizado no seu wallet, para evitar a reutilização de endereços (a reutilização de endereços é uma prática muito má para a sua privacidade). Podes então reencaminhar este endereço para a pessoa ou serviço que precisa de te enviar bitcoins.



![Image](assets/fr/27.webp)



Uma vez transmitida a transação na rede, esta aparecerá automaticamente na página inicial da aplicação.



![Image](assets/fr/28.webp)



## 6. Enviar bitcoins com Ashigaru



Agora que tens bitcoins no teu Ashigaru wallet, também podes enviá-los. Para o fazer, prima o botão `+` no canto inferior direito, e depois selecione o botão vermelho `Send`.



![Image](assets/fr/29.webp)



De seguida, escolha a conta a partir da qual pretende efetuar a despesa. De momento, ainda não abordámos a conta `Postmix`, reservada às junções de moedas, que veremos num tutorial posterior. Por isso, vamos enviar fundos a partir da conta de depósito principal.



![Image](assets/fr/30.webp)



Introduza os dados da transação: o montante a enviar e o endereço Bitcoin do destinatário.



![Image](assets/fr/31.webp)



Ao clicar nos três pequenos pontos no canto superior direito e depois em "Mostrar resultados não gastos", também pode escolher exatamente quais os UTXOs que pretende gastar, para aumentar a sua privacidade.



![Image](assets/fr/32.webp)



Quando tiver preenchido todos os dados, clique na seta branca na parte inferior da interface para continuar.



Será então conduzido a uma página de resumo que apresenta todos os pormenores da sua transação. São apresentados vários elementos importantes:




- No bloco `Destino`, verifique uma última vez se o endereço do destinatário e o montante enviado estão corretos;
- No bloco `Taxas`, é possível visualizar a taxa de taxa selecionada automaticamente pela Ashigaru e, se necessário, modificá-la clicando em `GESTÃO` ;
- O bloco `Transaction` indica o tipo de transação que está prestes a realizar. Aqui, estamos a falar de uma transação simples, mas Ashigaru também suporta outros tipos de transacções optimizadas para a privacidade, que abordaremos em detalhe num futuro tutorial;
- O bloco vermelho "Alerta de transação" avisa-o se a sua transação apresentar padrões que possam ser reconhecidos pelas ferramentas de análise da cadeia e que possam comprometer a sua privacidade. Ao clicar nele, pode ver os pormenores. Por exemplo, no meu caso, o Ashigaru diz-me que o montante enviado é redondo (`3000 sats`), o que me permite deduzir qual a saída que corresponde à despesa e qual a troca. Para saber mais sobre essas heurísticas de análise de cadeia, convido você a seguir meu treinamento BTC 204 na Plan ₿ Academy ;
- Por último, pode acrescentar uma etiqueta à sua transação para manter um registo da sua finalidade.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Depois de verificares toda a informação, usa a seta verde para enviar os bitcoins. Mantém a seta premida e arrasta-a para a direita para confirmar o envio.



![Image](assets/fr/33.webp)



A sua transação foi transmitida na rede Bitcoin.



![Image](assets/fr/34.webp)



## 7. Recuperando seu Ashigaru wallet



A recuperação de um Ashigaru wallet difere ligeiramente da de um Bitcoin wallet clássico, uma vez que a aplicação utiliza os mesmos métodos que o Samurai Wallet. Se perderes o acesso ao teu wallet (seja porque te esqueceste do PIN, porque o desinstalaste ou porque perdeste o telemóvel), há várias formas de recuperar os teus bitcoins.



Se ainda tiver acesso ao seu telemóvel, ou se tiver feito uma cópia de segurança deste ficheiro, o método mais simples é utilizar o ficheiro de cópia de segurança `ashigaru.txt`. Este ficheiro contém toda a informação necessária para restaurar a sua carteira numa nova instância de Ashigaru (ou em Sparrow Wallet), mas está encriptado com o passphrase que definiu no passo 3.1 deste tutorial. Portanto, é necessário ter o ficheiro `ashigaru.txt` e o seu passphrase para usar este método.



Com estes dois elementos, pode, por exemplo, restaurar a sua carteira no Sparrow Wallet.



![Image](assets/fr/35.webp)



Se não tiver acesso ao ficheiro `ashigaru.txt`, pode ainda assim recuperar o acesso aos seus fundos usando a sua frase mnemónica passphrase, tal como faria para qualquer outra carteira Bitcoin. Recomendo que efectue este restauro numa nova instância Ashigaru, ou diretamente no Sparrow Wallet, para recuperar facilmente os caminhos de bypass do Whirlpool se o estiver a usar. Em alternativa, pode importar esta informação para qualquer outro software compatível com o BIP39, introduzindo manualmente os caminhos de derivação.



Para mais informações sobre este processo, consultar o tutorial completo que escrevi sobre a recuperação de um Wallet Samurai wallet. Como o Ashigaru é um fork, o procedimento é idêntico:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Como pode ver, independentemente do método de restauro que utilizar, o passphrase é indispensável. Por isso, certifique-se de que efectua uma cópia de segurança com cuidado. Também pode fazer várias cópias, dependendo da sua estratégia de segurança.



## 8. Atualizar a aplicação



Para atualizar a aplicação Ashigaru, uma vez que a instalou a partir de um ficheiro `.apk` e não através da Play Store como uma aplicação normal, terá de transferir o novo ficheiro `.apk` correspondente à versão actualizada e, em seguida, instalá-lo manualmente.



Repita os passos descritos na secção 2 deste tutorial, exceto que quando clicar no ficheiro `.apk` para iniciar a instalação, **o seu telemóvel Android deve oferecer-lhe a opção `Atualizar` e não `Instalar`**.



![Image](assets/fr/41.webp)



Este é um ponto muito importante: se o Android apresentar `Instalar` em vez de `Atualizar`, é provável que esteja a instalar uma versão fraudulenta. Neste caso, interrompa imediatamente o processo de instalação.



Tal como na primeira instalação, verifique a autenticidade e a integridade do ficheiro `.apk` antes de proceder à atualização.



Para saber quando uma nova versão está disponível, consulte o sítio Web oficial do Ashigaru de vez em quando. Fique descansado, o Ashigaru é uma aplicação estável e madura, herdada do Samourai Wallet, e as actualizações são relativamente pouco frequentes em comparação com software mais recente.



## 9. Doar para o projeto Ashigaru



Ashigaru é um projeto de código aberto. Se quiser apoiar o seu desenvolvimento, pode fazer um donativo diretamente a partir da aplicação através do PayNym.



Para isso, clique no seu PayNym no canto superior direito da interface e selecione o seu código de pagamento que começa por "PM...".



![Image](assets/fr/36.webp)



Em seguida, prima o botão "+" no canto inferior direito do ecrã.



![Image](assets/fr/37.webp)



Selecione `Ashigaru Open Source Project` como destinatário.



![Image](assets/fr/38.webp)



Clique no botão `CONNECT` para estabelecer o canal de comunicação BIP47 (mais informações sobre este protocolo no tutorial abaixo).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Uma vez confirmada a transação da notificação, pode enviar os seus donativos para o projeto clicando na pequena seta branca no canto superior direito da interface.



![Image](assets/fr/40.webp)



Agora já sabes como utilizar as funcionalidades básicas da aplicação Ashigaru. Nos próximos tutoriais, veremos como tirar partido das transacções de despesas avançadas, bem como do Whirlpool, a implementação de coinjoin herdada do Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
