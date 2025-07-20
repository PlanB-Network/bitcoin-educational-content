---
name: Ledger U2F & FIDO2
description: Melhore a sua segurança online com o Ledger
---
![cover](assets/cover.webp)



Os dispositivos Ledger são carteiras de hardware originalmente concebidas para proteger um Bitcoin Wallet, mas também incluem opções avançadas para uma autenticação forte na Web. Graças à sua compatibilidade com os protocolos **U2F** e **FIDO2**, permitem-lhe proteger o acesso às suas contas online através da criação de um segundo fator de autenticação.



O protocolo U2F (Universal 2nd Fator) foi introduzido pela Google e pela Yubico em 2014, tendo sido depois normalizado pela FIDO Alliance. Permite adicionar um segundo fator de autenticação física (2FA) aquando do início de sessão. Uma vez ativado, para além da palavra-passe clássica, o utilizador deve aprovar cada tentativa de ligação à sua conta premindo um botão no seu Ledger. Neste contexto, o Ledger funciona de forma semelhante a um Yubikey. O U2F é, de facto, um subcomponente da norma FIDO2, englobando-a e trazendo melhorias significativas, incluindo suporte nativo para navegadores modernos e maior flexibilidade na gestão de chaves de autenticação.



Estes métodos baseiam-se em criptografia assimétrica: não são transmitidos dados secretos, tornando ineficazes os ataques de phishing ou de interceção. O U2F e o FIDO2 são atualmente suportados por muitos serviços online.



Neste tutorial, vamos mostrar-lhe como ativar U2F e FIDO2 para autenticação de dois factores com o seu Ledger.



**Nota:** O U2F e o FIDO2 são suportados em todos os dispositivos Ledger equipados com firmware recente: a partir da versão 2.1.0 para o Nano X e o Nano S classic, e a partir da versão 1.1.0 para o Nano S Plus. Os modelos Stax e Flex são nativamente compatíveis.



## Instalar a aplicação Ledger Security Key



Se estiver a utilizar um dispositivo Ledger, provavelmente sabe que o firmware por si só não contém todas as funcionalidades necessárias para gerir carteiras criptográficas. Por exemplo, para utilizar um Bitcoin Wallet, é necessário instalar a aplicação "*Bitcoin*". Da mesma forma, para gerir chaves MFA, é necessário instalar a aplicação "*Security Key*".



Antes de começar, certifique-se de que configurou o seu Bitcoin Wallet no seu Ledger. É importante guardar corretamente o seu Mnemonic, uma vez que as chaves utilizadas para 2FA são derivadas deste Mnemonic. Se o seu Ledger for perdido ou danificado, pode recuperar o acesso às suas chaves introduzindo a sua frase Mnemonic noutro dispositivo Ledger (de momento, os identificadores FIDO2 no modo "*sem palavras-passe*" ainda não são suportados nos Ledgers, pelo que não existem identificadores residentes).



Ligue o Ledger ao seu computador e desbloqueie-o.



![Image](assets/fr/01.webp)



Para instalar a aplicação, abra o software [Ledger Live] (https://www.Ledger.com/Ledger-live) e, em seguida, aceda ao separador "*My Ledger*". Procure a aplicação "*Security Key*" e instale-a no seu dispositivo.



![Image](assets/fr/02.webp)



A aplicação "*Security Key*" deve agora aparecer juntamente com as outras aplicações instaladas no seu Ledger.



![Image](assets/fr/03.webp)



Clique na aplicação para a deixar aberta para os passos seguintes do tutorial.



![Image](assets/fr/04.webp)



## Utilizar U2F/FIDO2 para 2FA com um Ledger



Aceda à conta que pretende proteger com a autenticação de dois factores. Por exemplo, vou utilizar uma conta Bitwarden. Normalmente, encontra a opção 2FA nas definições do serviço, nos separadores "*autenticação*", "*segurança*", "*login*" ou "*palavra-passe*".



![Image](assets/fr/05.webp)



Na secção dedicada à autenticação de dois factores, selecione a opção "*Passkey*" (o termo pode variar consoante o sítio que está a utilizar).



![Image](assets/fr/06.webp)



Ser-lhe-á frequentemente pedido que confirme a sua palavra-passe atual.



![Image](assets/fr/07.webp)



Dê um nome à sua chave de segurança para facilitar o reconhecimento e, em seguida, clique em "*Read Key*".



![Image](assets/fr/08.webp)



Os dados da sua conta aparecerão no ecrã do Ledger. Prima o botão "*Registar*" para confirmar (ou ambos os botões em simultâneo, consoante o modelo que estiver a utilizar).



![Image](assets/fr/09.webp)



A chave de acesso foi registada com sucesso.



![Image](assets/fr/10.webp)



Registar esta chave de segurança.



![Image](assets/fr/11.webp)



A partir de agora, quando iniciar sessão na sua conta, para além da sua palavra-passe habitual, ser-lhe-á pedido que ligue o seu Ledger.



![Image](assets/fr/12.webp)



Pode então premir o botão "*Log in*" no ecrã do seu Ledger para confirmar a autenticação (ou ambos os botões em simultâneo, dependendo do modelo que estiver a utilizar).



![Image](assets/fr/13.webp)



A vantagem de utilizar um Hardware Wallet Ledger para a autenticação de dois factores é que pode recuperar facilmente as suas chaves graças à frase Mnemonic. Para além desta cópia de segurança de base, pode também utilizar um código de emergência fornecido por cada serviço em que tenha ativado a 2FA. Este código de emergência permite-lhe ligar-se à sua conta se perder a sua chave de segurança. Substitui assim a 2FA para uma ligação, se necessário.



Na Bitwarden, por exemplo, pode aceder a este código clicando em "*Ver código de recuperação*".



![Image](assets/fr/14.webp)



Recomendo que guarde este código num local diferente daquele onde guarda a sua palavra-passe principal, para evitar que sejam roubados em conjunto. Por exemplo, se a sua palavra-passe estiver guardada num gestor de palavras-passe, guarde o seu código de emergência 2FA em papel, separadamente.



Esta abordagem oferece-lhe dois níveis de cópia de segurança em caso de perda do seu Ledger para autenticação 2FA: uma primeira cópia de segurança utilizando a frase Mnemonic para todas as suas contas e uma segunda cópia de segurança específica da conta utilizando os códigos de emergência. No entanto, é importante **não confundir o papel do Mnemonic com o do código de emergência**:




- A frase Mnemonic de 12 ou 24 palavras dá-lhe acesso não só às chaves utilizadas para 2FA em todas as suas contas, mas também aos seus bitcoins protegidos com o seu Ledger ;
- O código de emergência permite-lhe contornar temporariamente o pedido de 2FA apenas na conta em causa (neste exemplo, apenas na Bitwarden).



Parabéns, agora já sabe como utilizar o seu Ledger para o MFA! Se achou este tutorial útil, ficaria muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual analisamos outra solução para a autenticação U2F e FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e