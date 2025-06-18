---
name: Alby Hub
description: Como lançar facilmente o seu próprio nó Lightning?
---
![cover](assets/cover.webp)

Alby Hub é o mais recente software de código aberto da Alby, a empresa por trás da popular extensão web Lightning. Alby Hub é uma carteira auto-custodiada com o nó Lightning mais fácil de usar, acessível de qualquer lugar para integrar com dezenas de aplicativos. Alby Hub é uma interface fácil de usar para gerenciar nós Lightning.

Neste tutorial, vamos explorar diferentes maneiras de usar o Alby Hub e como conectá-lo ao Alby Go, o aplicativo móvel da Alby, ou à extensão do navegador Alby. Isso permitirá que você gaste seus sats em movimento enquanto mantém autonomia na gestão do seu nó.


![ALBY HUB](assets/fr/01.webp)

## O que é o Alby Hub?

Alby Hub está configurado para ser a nova ferramenta principal no ecossistema Alby. Este software permite aos usuários gerenciar facilmente sua própria carteira auto-custodial com um nó Lightning integrado, mantendo a propriedade de suas chaves (auto-custódia).

O Alby Hub é uma ferramenta altamente adaptável. Pode satisfazer as necessidades tanto de principiantes como de utilizadores avançados. Os principiantes utilizá-lo-ão para operar facilmente um nó Lightning real por conta própria, sem terem de lidar com a complexidade subjacente. Para os utilizadores mais experientes, o Alby Hub pode ser utilizado como uma interface completa para a gestão avançada de um nó Lightning existente.

Em função das suas necessidades, o Alby Hub está disponível em 4 configurações:


- Alby Hub Cloud :**

Ideal para iniciantes, esta primeira opção é a opção em nuvem da Alby. Ela permite implantar um Hub diretamente em um servidor gerido pela Alby, acessível através da sua interface Alby Hub. Embora a Alby gerencie o servidor, você mantém a soberania sobre seus fundos, pois suas chaves são criptografadas com uma senha conhecida apenas por você. No entanto, suas chaves devem permanecer descriptografadas na RAM para que o nó funcione, o que teoricamente as expõe a riscos se alguém acessar fisicamente o servidor. É um compromisso interessante para iniciantes, mas é importante estar ciente dos riscos.

A principal vantagem dessa opção é que você obtém um nó do Lightning em funcionamento 24 horas por dia, 7 dias por semana, sem precisar gerenciar a hospedagem por conta própria. Além disso, as cópias de segurança do seu Lightning node são simplificadas e automatizadas, em comparação com as opções auto-hospedadas em que tem de gerir as cópias de segurança do canal.

Alby Cloud é um serviço pago [Verifique os preços](https://albyhub.com/#pricing) para mais detalhes. A taxa é deduzida automaticamente da sua carteira por meio de uma fatura Lightning emitida pela Alby. Isso é feito através de uma conexão NWC que configura seu nó para pagar automaticamente as faturas da Alby relacionadas à sua assinatura.


- Alby Hub com um nó existente :**

Se já tiver um nó alojado, por exemplo, na Umbrel ou na Start9, o Alby Hub pode ser utilizado como interface de gestão avançada, tal como o ThunderHub ou o RTL.


- Alby Hub local :**

Também é possível instalar o Alby Hub diretamente no seu PC, embora essa opção seja menos prática, pois o seu PC precisa permanecer ativo o tempo todo para acessar o nó Lightning remotamente. No entanto, essa alternativa pode ser adequada para suas necessidades específicas.


- Alby Hub num servidor pessoal :**

Para utilizadores avançados, o Alby Hub pode ser implementado num servidor pessoal com um simples comando. Esta opção não é abordada neste tutorial, mas pode encontrar instruções dedicadas [no GitHub do Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Este tutorial centra-se principalmente na interface, que será a mesma independentemente da opção escolhida. Veremos também como implementar o Alby Hub com a opção de nuvem paga e depois com a opção node-in-box (Umbrel ou Start9).

![ALBY HUB](assets/fr/02.webp)

Para a instalação local no seu PC, [descarregue e instale o software de acordo com o seu sistema operativo] (https://github.com/getAlby/hub/releases), depois siga as mesmas instruções na interface.

![ALBY HUB](assets/fr/03.webp)

## Criar uma conta Alby

O primeiro passo é criar uma conta Alby. Embora esta não seja essencial para utilizar o Alby Hub, permite-lhe tirar o máximo partido das opções disponíveis, incluindo a possibilidade de obter um endereço Lightning.

Aceder ao [sítio Web oficial da Alby] (https://getalby.com/) e clicar no botão "*Criar conta*".

![ALBY HUB](assets/fr/04.webp)

Introduza uma alcunha e um endereço de correio eletrónico e, em seguida, clique em "*Inscrever-se*". Este endereço de correio eletrónico será utilizado para iniciar sessão na sua conta mais tarde.

![ALBY HUB](assets/fr/05.webp)

Introduza o código de verificação que recebeu por correio eletrónico.

![ALBY HUB](assets/fr/06.webp)

Uma vez iniciada a sessão na sua conta online, clique no botão "*Continuar*".

![ALBY HUB](assets/fr/07.webp)

Clique novamente em "*Continuar*".

![ALBY HUB](assets/fr/08.webp)

## A opção de alojamento na nuvem

Você terá então que escolher entre uma opção autogerida, onde você instala o Alby Hub em seu próprio dispositivo, ou opções premium. Vou começar explicando como proceder com a opção Pro Cloud (note que esta é uma opção paga, veja os detalhes na seção anterior).

Clique em "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Confirme clicando em "*Subscrever agora*".

![ALBY HUB](assets/fr/10.webp)

Clique em "*Lançar Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Aguarde alguns momentos enquanto o seu nó é criado.

![ALBY HUB](assets/fr/12.webp)

E é isso, seu Alby Hub está agora configurado. Na próxima seção, vou mostrar como instalar o Alby Hub em um nó existente. Se você ainda não tiver um nó Lightning, pode pular para a próxima seção para configurar o Alby Hub na Alby Cloud.


![ALBY HUB](assets/fr/13.webp)

## A opção de auto-hospedagem

Se preferir utilizar o Alby Hub como interface para o seu nó Lightning existente, tem várias opções: instalá-lo num servidor, localmente no seu computador ou através de um node-in-box (Umbrel ou Start9). A utilização do Alby Hub nestas configurações é gratuita. Vamos concentrar-nos na opção node-in-box, pois considero que a opção de servidor, sem acesso físico, apresenta riscos semelhantes aos da versão em nuvem e que a instalação local num PC é muitas vezes inadequada.

Para configurar isto no Umbrel (os passos para o Start9 são idênticos), é necessário primeiro ter um nó LND já configurado.

Inicie sessão na sua interface Umbrel e aceda à loja de aplicações.

![ALBY HUB](assets/fr/14.webp)

Procurar a aplicação "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Instale-o no seu nó.

![ALBY HUB](assets/fr/16.webp)

A sua interface Alby Hub está agora pronta. Pode seguir o resto do tutorial como se estivesse a utilizar a interface da nuvem, mas sem as opções da versão paga. Além disso, ao contrário da versão na nuvem, as suas chaves são armazenadas localmente no seu nó e não nos servidores da Alby.

![ALBY HUB](assets/fr/17.webp)

## Lançamento do Alby Hub

Clique no botão "*Iniciar*".

![ALBY HUB](assets/fr/18.webp)

O Alby Hub pedir-lhe-á então que escolha uma palavra-passe. Esta palavra-passe é muito importante, pois será utilizada para encriptar a sua carteira. Na versão paga da nuvem, as suas chaves são armazenadas no servidor Alby, encriptadas com esta palavra-passe que só você conhece, depois desencriptadas e armazenadas apenas na RAM para assinar transacções quando necessário.

Portanto, é essencial escolher uma senha forte. Qualquer pessoa com essa senha pode potencialmente obter acesso ao seu nó. Certifique-se também de fazer um ou mais backups físicos dessa senha em um pedaço de papel, ou melhor ainda, em um pedaço de metal para maior segurança.

Depois de ter escolhido e guardado cuidadosamente a sua palavra-passe, clique em "*Criar palavra-passe*".

![ALBY HUB](assets/fr/19.webp)

Agora você tem acesso ao seu Lightning node.

![ALBY HUB](assets/fr/20.webp)

A primeira ação a realizar é salvar sua frase de recuperação, da qual suas chaves são derivadas. Para fazer isso, clique em "Configurações". Essa frase permite que você recupere o acesso à sua carteira se você ativou os backups automáticos.

![ALBY HUB](assets/fr/21.webp)

Em seguida, aceda ao separador "*Backup*". Introduza a sua palavra-passe para aceder ao mesmo.

![ALBY HUB](assets/fr/22.webp)

Terá então acesso à sua frase de recuperação de 12 palavras. Faça uma ou mais cópias de segurança físicas desta frase, em papel ou metal, e guarde-a num local seguro.

![ALBY HUB](assets/fr/23.webp)

Depois de ter guardado a frase, assinale a caixa para confirmar que a guardou e clique em "*Continuar*".

![ALBY HUB](assets/fr/24.webp)

## Como posso recuperar o acesso aos meus bitcoins?

Antes de enviar fundos para o seu Alby Hub, é importante entender como recuperá-los em caso de problema, bem como quais informações são necessárias para essa recuperação. O processo varia de acordo com a natureza dos fundos a serem recuperados e o modo de hospedagem do seu nó.

Para os usuários de nuvem paga, a recuperação completa de seus bitcoins requer três elementos essenciais:

- Sua frase de recuperação;
- Acesso à sua conta Alby, para recuperar os backups automáticos.

A ausência de qualquer uma dessas duas informações tornaria impossível recuperar completamente seus bitcoins.

Para aqueles que executam o Alby Hub em seu próprio dispositivo, o processo de recuperação está documentado [aqui](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Se você instalou o Alby Hub em um nó existente, será necessário seguir o processo de recuperação do sistema operacional específico desse nó. Por exemplo: O Umbrel oferece [uma opção](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) para criptografar o estado mais recente de seus canais Lightning e salvá-lo de maneira dinâmica e anônima através do Tor. Observe que apenas os backups automáticos do Alby permitem que você recupere seu Hub completamente sem fechar nenhum canal.

## Compre seu primeiro canal Lightning

Pode agora seguir as instruções fornecidas pelo Alby Hub. Clique no botão para abrir o seu primeiro canal de entrada de dinheiro.

![ALBY HUB](assets/fr/25.webp)

Selecione "*Open Channel*". Se não tenciona tornar-se um nó de encaminhamento e não precisa especificamente de um, recomendo que opte por canais privados.

![ALBY HUB](assets/fr/26.webp)

O Alby Hub irá gerar uma fatura para pagamento. Este pagamento cobre as taxas de transação necessárias para abrir o seu canal, bem como as taxas de serviço do LSP (*Lightning Service Provider*) que abrirá um canal para o seu nó, permitindo-lhe receber pagamentos imediatamente.

![ALBY HUB](assets/fr/27.webp)

Assim que a fatura tiver sido paga e a transação confirmada, é estabelecido o seu primeiro canal Lightning.

![ALBY HUB](assets/fr/28.webp)

No separador "*Nó*", pode ver que tem agora dinheiro a entrar, o que lhe permite receber pagamentos através do Lightning.

![ALBY HUB](assets/fr/29.webp)

Para receber o pagamento, clique no separador "*Carteira*" e depois em "*Receber*".

![ALBY HUB](assets/fr/30.webp)

Introduza um montante e adicione uma descrição, se necessário, e clique em "*Criar fatura*".

![ALBY HUB](assets/fr/31.webp)

Recebi o meu primeiro pagamento de 120.000 sats.

![ALBY HUB](assets/fr/32.webp)

Ao voltar ao separador "*Carteira*", pode verificar o saldo da sua carteira. Note que o Alby Hub reserva automaticamente 354 sats quando efectua o seu primeiro pagamento. Para cada canal Lightning que abrir a partir daí, o Alby Hub colocará automaticamente de lado uma reserva equivalente a 1% da capacidade do canal. Esta reserva é uma medida de segurança que permite ao seu nó recuperar os fundos do canal em caso de tentativa de fraude por parte do seu par. É por isso que, embora eu tenha enviado 120.000 sats, apenas 119.646 sats são mostrados no meu saldo.

![ALBY HUB](assets/fr/33.webp)

## Depositar bitcoins onchain

Se quiseres ter dinheiro para fazer pagamentos, também podes abrir um canal. Para isso, precisas de bitcoins onchain na tua carteira.

No separador "*Nó*", clique em "*Depósito*".

![ALBY HUB](assets/fr/34.webp)

Enviar bitcoins para o endereço apresentado. Este endereço é derivado da sua frase de recuperação previamente guardada.

![ALBY HUB](assets/fr/35.webp)

Enviei 72.000 sats. Agora estão visíveis em "*Saldo de Poupança*", que inclui todos os fundos que possuo onchain, e não no Lightning.

![ALBY HUB](assets/fr/36.webp)

## Abrir um canal Lightning

Agora que tem fundos onchain, pode abrir um novo canal Lightning. É aconselhável abrir vários canais, com montantes suficientes para garantir que pode sempre efetuar pagamentos sem restrições. A maioria dos LSPs (*Lightning Service Providers*) exige um mínimo de 150.000 sats para abrir um canal consigo.

No separador "*Nó*", clique em "*Abrir canal*".

![ALBY HUB](assets/fr/37.webp)

Selecione o tamanho do seu canal. Recomendo que não abras canais demasiado pequenos, tendo em conta que este é um nó Lightning e a máquina que aloja as tuas chaves não oferece o mesmo nível de segurança que uma carteira de hardware. Por isso, tem cuidado com os montantes que escolhes bloquear.

![ALBY HUB](assets/fr/38.webp)

No menu "*Opções avançadas*", pode escolher com que LSP abrir o seu canal, ou introduzir manualmente outro nó de Lightning.

![ALBY HUB](assets/fr/39.webp)

Em seguida, clique em "*Abrir canal*".

![ALBY HUB](assets/fr/40.webp)

Aguarde enquanto o seu canal é confirmado na cadeia.

![ALBY HUB](assets/fr/41.webp)

O seu novo canal aparecerá agora no separador "*Nó*".

![ALBY HUB](assets/fr/42.webp)

## Gerenciamento de Nós

Gerenciar seus canais Lightning é mais fácil do que você pensa. O Alby Hub permite transferir sats entre o seu saldo de gastos e o seu saldo on-chain. É assim que você pode aumentar sua capacidade de envio ou recebimento.

![ALBY HUB](assets/fr/66.webp)


## Ligar uma aplicação de despesas

Agora que tem um nó Lightning a funcionar, pode utilizá-lo para receber e gastar sats diariamente. Embora a interface Web do Alby Hub seja útil para gerir o seu nó, não é ideal para efetuar transacções rápidas em movimento. Para isso, vamos utilizar uma aplicação de carteira Lightning instalada no nosso smartphone.

Neste tutorial, recomendo que opte pelo Alby Go, que é muito fácil de utilizar, mas também pode utilizar outras aplicações compatíveis, como o Zeus.

![ALBY HUB](assets/fr/43.webp)

Para instalar o Alby Go, aceda à loja de aplicações do seu dispositivo:


- [Para Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Para a Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Os utilizadores do Android também podem instalar a aplicação através do ficheiro `.apk` [disponível no GitHub da Alby] (https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Quando a aplicação for lançada, clique em "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

No seu Alby Hub, na seção App Store, encontre “Alby Go” e clique em “Connect”  
![ALBY HUB](assets/fr/47.webp)  
Clique em “Connect with One-Tab Connections”. Isso permitirá que você conecte seu Alby Hub com um clique a outros aplicativos usando Alby Go.  

![ALBY HUB](assets/fr/48.webp)  

O Alby Hub então gerará um segredo para estabelecer a conexão com o Alby Go.


![ALBY HUB](assets/fr/49.webp)

Regresse à aplicação Alby Go, leia o código QR ou cole o segredo.

![ALBY HUB](assets/fr/50.webp)

Clique em "Concluir*".

![ALBY HUB](assets/fr/51.webp)

Agora você tem acesso remoto ao seu nó Lightning alimentado pelo Alby Hub a partir do seu smartphone, facilitando o envio e recebimento de sats em movimento todos os dias.


![ALBY HUB](assets/fr/52.webp)

Se necessário, pode gerir as permissões para esta ligação diretamente no Alby Hub, clicando nela.

![ALBY HUB](assets/fr/53.webp)

Para receber sats, basta clicar em "*Receber*".

![ALBY HUB](assets/fr/54.webp)

Modifique o montante e a descrição da fatura clicando em "*Fatura*".

![ALBY HUB](assets/fr/55.webp)

Cobrar a fatura para receber sats.

![ALBY HUB](assets/fr/56.webp)

Para enviar sats, clique em "*Enviar*".

![ALBY HUB](assets/fr/57.webp)

Digitalize a fatura que pretende pagar.

![ALBY HUB](assets/fr/58.webp)

Em seguida, clique em "*Pagar*".

![ALBY HUB](assets/fr/59.webp)

A sua transação está confirmada.

![ALBY HUB](assets/fr/60.webp)

Ao clicar na seta pequena, pode aceder ao seu histórico de transacções.

![ALBY HUB](assets/fr/61.webp)

Estas transacções também são visíveis no seu Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Personalize o seu endereço Lightning

A Alby oferece-lhe a opção de um endereço Lightning. Isto permite-lhe receber pagamentos no seu nó sem ter de gerar manualmente uma fatura de cada vez. Por predefinição, a Alby atribui-lhe um endereço Lightning, mas pode personalizá-lo. Inicie sessão na sua conta Alby online, clique no seu nome no canto superior direito e selecione "*Definições*".

![ALBY HUB](assets/fr/63.webp)

Navegar para o menu "*Endereço do raio*".

![ALBY HUB](assets/fr/64.webp)

Modifique o seu endereço e confirme clicando em "*Atualizar o seu endereço relâmpago*".

![ALBY HUB](assets/fr/65.webp)

Tenha em atenção que, após a alteração do seu endereço, este deixa de lhe pertencer. Por isso, certifique-se de que não volta a enviar sats para esse endereço.

E pronto, agora já sabes como utilizar o Lightning com o teu próprio nó utilizando a ferramenta Alby Hub. Se achou este tutorial útil, ficarei muito grato se colocar um polegar verde abaixo. Por favor, sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!

Para compreender em pormenor todos os mecanismos do Relâmpago que manipulámos neste tutorial, aconselho-o vivamente a descobrir a nossa formação gratuita sobre o assunto:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
