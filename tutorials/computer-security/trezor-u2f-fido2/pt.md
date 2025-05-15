---
name: Trezor U2F e FIDO2
description: Reforce a sua segurança online com o Trezor
---
![cover](assets/cover.webp)



Os dispositivos Trezor são carteiras de hardware originalmente concebidas para proteger um Bitcoin Wallet, mas também dispõem de opções avançadas para uma autenticação forte na Web. Graças à sua compatibilidade com os protocolos **U2F** e **FIDO2**, permitem-lhe proteger o acesso às suas contas online sem depender apenas de palavras-passe.



O protocolo U2F (*Universal 2nd Fator*) foi introduzido pela Google e pela Yubico em 2014, tendo sido depois normalizado pela FIDO Alliance. Permite adicionar um segundo fator de autenticação física (2FA) ao início de sessão. Uma vez ativado, para além da palavra-passe clássica, os utilizadores devem aprovar cada tentativa de ligação à sua conta premindo um botão no seu Trezor. Neste contexto, o Trezor funciona de forma semelhante a um Yubikey.



Este método baseia-se numa criptografia assimétrica: não são transmitidos dados secretos, o que torna ineficazes os ataques de phishing ou de interceção. O U2F é atualmente suportado por muitos serviços em linha.



Para além do U2F, que permite a autenticação de dois factores, os Trezors também suportam o FIDO2 (*Fast IDentity Online 2.0*), uma evolução do U2F. Este é um protocolo de autenticação normalizado de 2018, que alarga a lógica do U2F e visa substituir completamente as palavras-passe. Baseia-se em dois componentes: *WebAuthn* (lado do navegador) e *CTAP2* (lado da chave física). O FIDO2 permite a autenticação "sem palavra-passe": os utilizadores identificam-se apenas através do seu dispositivo Trezor, que funciona como um token criptográfico único, sem qualquer palavra-passe adicional. Este protocolo é agora compatível com uma série de serviços online, particularmente os orientados para as empresas.



Para além da funcionalidade "sem palavra-passe*", o FIDO2 também permite a autenticação de dois factores de forma semelhante à U2F.



O FIDO2 introduz igualmente a noção de credenciais residentes, ou seja, identificadores armazenados diretamente no Trezor, que incluem tanto a chave privada que permite a ligação como as informações de identificação do utilizador. Este mecanismo permite uma autenticação verdadeiramente livre de palavras-passe: basta ligar o Trezor e confirmar o acesso, sem ter de introduzir o ID ou a palavra-passe. Por outro lado, as credenciais não residentes, que são mais convencionais, armazenam apenas a chave privada no dispositivo; a ID do utilizador permanece armazenada no lado do servidor e, por conseguinte, tem de ser introduzida em cada ligação. Mais adiante, veremos como guardá-las com o Trezor.



Neste tutorial, vamos descobrir como ativar o U2F ou o FIDO2 para a autenticação de dois factores e, em seguida, como configurar o FIDO2 para aceder às suas contas sem uma palavra-passe, diretamente com o Trezor.



**Nota:** O U2F é compatível com todos os modelos Trezor, mas o FIDO2 só é suportado no Safe 3, Safe 5 e Model T, não no Model One.



## Utilizar U2F/FIDO2 para 2FA num Trezor



Antes de começar, certifique-se de que configurou o seu Bitcoin Wallet no seu Trezor. É importante guardar corretamente o seu Mnemonic, uma vez que as chaves utilizadas para U2F e FIDO2 na autenticação de dois factores são derivadas deste Mnemonic. Se o seu Trezor se perder ou ficar danificado, pode recuperar o acesso às suas chaves introduzindo a sua frase Mnemonic noutro dispositivo Trezor (note que para as credenciais FIDO2 no modo "*sem palavra-passe*", o seed sozinho não é suficiente, como veremos nas próximas secções).



Ligue o Trezor ao seu computador e desbloqueie-o.



![Image](assets/fr/01.webp)



Aceda à conta que pretende proteger com a autenticação de dois factores. Por exemplo, vou utilizar uma conta Bitwarden. Normalmente, encontra a opção 2FA nas definições do serviço, nos separadores "*autenticação*", "*segurança*", "*login*" ou "*palavra-passe*".



![Image](assets/fr/02.webp)



Na secção dedicada à autenticação de dois factores, selecione a opção "*Passkey*" (o termo pode variar consoante o sítio que está a utilizar).



![Image](assets/fr/03.webp)



Ser-lhe-á frequentemente pedido que confirme a sua palavra-passe atual.



![Image](assets/fr/04.webp)



Dê um nome à sua chave de segurança para facilitar o reconhecimento e, em seguida, clique em "*Read Key*".



![Image](assets/fr/05.webp)



Os dados da sua conta são apresentados no ecrã do Trezor. Toque no ecrã ou prima o botão para confirmar. Ser-lhe-á também pedido que confirme o seu código PIN.



![Image](assets/fr/06.webp)



Registar esta chave de segurança.



![Image](assets/fr/07.webp)



A partir de agora, quando quiser ligar-se à sua conta, para além da sua palavra-passe habitual, ser-lhe-á pedido que ligue o seu Trezor.



![Image](assets/fr/08.webp)



Pode então premir o ecrã do Trezor para confirmar a autenticação.



![Image](assets/fr/09.webp)



A vantagem de utilizar um Trezor Hardware Wallet para a autenticação de dois factores é que pode recuperar facilmente as suas chaves graças à frase Mnemonic. Para além desta cópia de segurança básica, pode também utilizar um código de emergência fornecido por cada serviço em que tenha ativado a 2FA. Este código de emergência permite-lhe ligar-se à sua conta se perder a sua chave de segurança. Substitui assim a 2FA para uma ligação, se necessário.



Na Bitwarden, por exemplo, pode aceder a este código clicando em "*Ver código de recuperação*".



![Image](assets/fr/10.webp)



Recomendo que guarde este código num local diferente daquele onde guarda a sua palavra-passe principal, para evitar que sejam roubados em conjunto. Por exemplo, se a sua palavra-passe estiver guardada num gestor de palavras-passe, guarde o seu código de emergência 2FA em papel, separadamente.



Esta abordagem oferece-lhe dois níveis de backup em caso de perda do seu Trezor para autenticação 2FA: um primeiro backup utilizando a frase Mnemonic para todas as suas contas, e um segundo específico para cada conta com os códigos de emergência. No entanto, é importante **não confundir o papel do Mnemonic com o do código de emergência** :




- A frase Mnemonic de 12 ou 24 palavras dá-lhe acesso não só às chaves utilizadas para 2FA em todas as suas contas, mas também aos seus bitcoins protegidos com o seu Trezor ;
- O código de emergência permite-lhe contornar temporariamente o pedido de 2FA apenas na conta em causa (neste exemplo, apenas na Bitwarden).



## Utilizar o FIDO2 num Trezor



Para além da autenticação de dois factores, o FIDO2 também permite a autenticação "sem palavra-passe", ou seja, sem ter de introduzir uma palavra-passe ao iniciar sessão num site. Basta ligar o Trezor ao seu computador para aceder à sua conta segura desta forma. Eis como configurar esta funcionalidade.



Antes de começar, certifique-se de que configurou o seu Bitcoin Wallet no seu Trezor. É importante guardar o Mnemonic, uma vez que os identificadores FIDO2 "*sem palavra-passe*" são encriptados com o seed (veremos como guardar corretamente estes identificadores na secção seguinte).



Ligue o Trezor ao seu computador e desbloqueie-o.



![Image](assets/fr/01.webp)



Aceda à conta que pretende proteger no modo "*sem palavra-passe*". Vou utilizar uma conta Bitwarden como exemplo. Esta opção encontra-se normalmente nas definições do serviço, muitas vezes num separador "*autenticação*", "*segurança*" ou "*palavra-passe*".



No Bitwarden, por exemplo, a opção encontra-se no separador "*Senha mestra*". Clique em "*Ligar*" para ativar a autenticação via FIDO2.



![Image](assets/fr/11.webp)



É frequente ser-lhe pedido que confirme a sua palavra-passe.



![Image](assets/fr/12.webp)



Os dados da sua conta são apresentados no ecrã do Trezor. Toque no ecrã ou prima o botão para confirmar. Terá também de confirmar o seu código PIN.



![Image](assets/fr/13.webp)



No sítio, adicione um nome para se lembrar da sua chave de segurança e clique em "*Ligar*".



![Image](assets/fr/14.webp)



Em seguida, ser-lhe-á pedido que se identifique para verificar se a chave está a funcionar corretamente.



![Image](assets/fr/15.webp)



A partir de agora, ao iniciar sessão na sua conta, já não será necessário introduzir o seu e-mail Address ou iniciar sessão. Basta clicar no botão para se autenticar com uma chave física no formulário de início de sessão.



![Image](assets/fr/16.webp)



Confirme a ligação ao seu Trezor introduzindo o seu PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Será ligado à sua conta sem ter de introduzir a sua palavra-passe.



![Image](assets/fr/18.webp)



**Tenha em atenção que mesmo que active a autenticação "*sem palavra-passe*" através de FIDO2 no seu Trezor, a palavra-passe principal da sua conta online continuará a ser válida para efeitos de início de sessão**



## Guardar as suas credenciais FIDO2 (residentes de credenciais)



Se estiver a utilizar FIDO2 ou U2F para autenticação de dois factores, ou seja, para iniciar sessão em contas que requerem uma palavra-passe para além da validação 2FA através do seu Trezor, então a frase Mnemonic por si só recuperará o acesso às suas chaves. No entanto, se estiver a utilizar o FIDO2 no modo "*sem palavra-passe*", tal como descrito na secção anterior, será necessário fazer uma cópia das suas credenciais FIDO, para além de fazer uma cópia de segurança da sua frase Mnemonic que encripta estas credenciais.



Para tal, é necessário um computador com Python instalado. Abra um terminal e execute o seguinte comando para instalar o software Trezor necessário:



```shell
pip3 install --upgrade trezor
```



Ligue o Trezor ao computador através de USB e desbloqueie-o utilizando o seu código PIN.



![Image](assets/fr/01.webp)



Para obter a lista de identificadores FIDO2 armazenados no Trezor, execute o seguinte comando:



```shell
trezorctl fido credentials list
```



Confirme a exportação no seu Trezor.



![Image](assets/fr/19.webp)



As suas informações de início de sessão FIDO2 serão apresentadas no seu terminal. Por exemplo, para a minha conta Bitwarden, obtive esta informação:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Copie e guarde todas estas informações num ficheiro de texto. Não existe qualquer risco significativo associado a esta cópia de segurança, para além de revelar que está a utilizar estes serviços com FIDO2. A "*ID de credencial*" é encriptada utilizando o seed do Wallet, o que significa que um atacante que obtivesse esta cópia de segurança não seria capaz de se ligar às suas contas, mas apenas de perceber que está a utilizar estas contas. Para desencriptar estas IDs, é necessário o seed no seu Wallet.



Assim, pode criar várias cópias deste ficheiro de texto e armazená-las em diferentes locais, por exemplo, localmente no seu computador, num serviço de alojamento de ficheiros e num suporte externo, como uma pen USB. No entanto, tenha em atenção que esta cópia de segurança não é actualizada automaticamente, pelo que terá de a renovar sempre que estabelecer uma nova ligação "*sem palavra-passe*" com o Trezor.



Agora vamos imaginar que avariou o seu Trezor. Para recuperar as suas credenciais FIDO2, terá primeiro de recuperar o seu Wallet utilizando a sua frase Mnemonic num novo dispositivo Trezor compatível com FIDO2.



Quando a recuperação estiver concluída, para importar os seus identificadores FIDO2 no novo dispositivo, execute o seguinte comando no seu terminal:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Basta substituir `<CREDENTIAL_ID>` por um dos seus identificadores. Por exemplo, no meu caso, isso daria :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



O Trezor pede-lhe para importar o seu identificador FIDO2. Confirme premindo no ecrã.



![Image](assets/fr/20.webp)



O seu login FIDO2 está agora operacional no seu Trezor. Repita este procedimento para cada um dos seus identificadores.



Parabéns, agora já sabes como utilizar o teu Trezor com U2F e FIDO2! Se este tutorial lhe foi útil, ficar-lhe-ia muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual analisamos outra solução para a autenticação U2F e FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e