---
name: Proton Authenticator
description: Como posso utilizar o Proton Authenticator para proteger as minhas contas com 2FA?
---
![cover](assets/cover.webp)



A autenticação de dois factores (2FA) acrescenta uma barreira de segurança extra às suas contas, exigindo, para além da sua palavra-passe, uma prova adicional de que só você a possui. A ativação da 2FA reduz drasticamente o risco de pirataria informática, mesmo que a sua palavra-passe seja comprometida através de phishing ou de uma fuga de dados. Sem a 2FA, um atacante só precisaria da sua palavra-passe para aceder às suas contas; com a 2FA, precisaria também do seu segundo fator, impedindo a maioria das tentativas de roubo de contas.



Existem vários tipos de 2FA. Os códigos SMS são melhores do que nada, mas permanecem vulneráveis a ataques de troca de SIM e interceção. Não recomendamos o SMS como 2FA principal. Aplicações de autenticação (TOTP) generate códigos temporários localmente no seu dispositivo, tornando-os muito mais difíceis de intercetar. As chaves de segurança físicas oferecem a melhor segurança, mas requerem hardware dedicado.



O Proton Authenticator é um autenticador TOTP. É a resposta da Proton às limitações das aplicações existentes: muitas são proprietárias, contêm rastreadores de anúncios e não oferecem backup encriptado. O Proton Authenticator distingue-se por fornecer uma aplicação de código aberto, livre de anúncios e rastreadores, com cópia de segurança encriptada de ponta a ponta.



## Apresentação do Proton Authenticator



O Proton Authenticator é uma aplicação de autenticação TOTP para telemóvel e computador desenvolvida pela Proton, conhecida pelos seus serviços centrados na privacidade. Como todos os produtos da Proton, a aplicação é de código aberto e foi submetida a auditorias de segurança independentes. Está disponível gratuitamente em todas as plataformas (Android, iOS, Windows, macOS, Linux).



O Proton Authenticator oferece as seguintes caraterísticas principais:





- Geração de códigos **TOTP** para as suas contas 2FA, compatível com a maioria dos sítios que utilizam o Google Authenticator, Authy, etc.





- **Cópia de segurança encriptada na nuvem** opcional: pode ligar a aplicação à sua conta Proton para fazer cópias de segurança e sincronizar os seus códigos com encriptação de ponta a ponta. Se perder o seu dispositivo, basta voltar a ligar um novo para restaurar todos os seus códigos.





- **Sincronização multi-dispositivo**: ao iniciar sessão no Proton na aplicação, os seus códigos 2FA sincronizam-se automaticamente entre vários dispositivos através de encriptação de ponta a ponta. No iOS, uma alternativa é a sincronização via iCloud.





- **Bloqueio local por palavra-passe ou biometria**: a aplicação oferece bloqueio por PIN e/ou impressão digital/identificação facial. Assim, mesmo que alguém aceda fisicamente ao seu telemóvel desbloqueado, não conseguirá abrir o Proton Authenticator.





- **Sem recolha de dados ou rastreadores**: A Proton compromete-se a não recolher dados pessoais através da aplicação. Não há publicidade oculta ou análise comportamental.





- **Importação/exportação fácil**: um dos pontos fortes do Proton Authenticator é o seu assistente de importação de contas existentes, compatível com outras aplicações (Google Authenticator, Authy, Aegis, etc.). Também pode exportar os seus códigos para um ficheiro, se necessário.



Em suma, o Proton Authenticator pretende ser uma solução 2FA sem compromissos: segura, privada e flexível.



## Instalação



O Proton Authenticator está disponível gratuitamente em todas as plataformas. Para descarregar a aplicação, aceda à página oficial: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Página oficial do Proton Authenticator que mostra as principais funcionalidades da aplicação e o Interface*



Nesta página, encontrará ligações de transferência para todos os sistemas operativos: Android, iOS, Windows, macOS e Linux. Basta clicar no sistema operativo da sua escolha e seguir os passos de instalação padrão.



Neste tutorial, mostraremos como instalar e configurar o aplicativo no macOS e, em seguida, veremos como instalar o aplicativo no iOS e sincronizar seus códigos entre os dois dispositivos.



### Instalação no macOS



Depois de ter descarregado e instalado a aplicação, inicie o Proton Authenticator. No primeiro lançamento, a aplicação guia-o através de alguns ecrãs de configuração inicial:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Ecrã de boas-vindas do Proton Authenticator com a mensagem "Segurança em cada código" e o botão "Começar "*



### Importação inicial



Se o Proton Authenticator detetar que estava a utilizar anteriormente outra aplicação 2FA, poderá aparecer um assistente de importação. Este suporta a importação direta de determinadas aplicações (Google Authenticator, 2FAS, Authy, Aegis, etc.). Em alternativa, pode saltar este passo e adicionar as suas contas manualmente mais tarde.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Assistente de importação para transferir códigos de outras aplicações de autenticação*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Aplicações de importação compatíveis: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth e Google Authenticator*



### Proteção de aplicações locais



Defina um PIN de desbloqueio ou active o desbloqueio biométrico (Touch ID), se disponível. Este passo é crucial para evitar que qualquer pessoa que utilize o Mac tenha acesso livre aos seus códigos 2FA.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Ecrã de configuração do Touch ID com a mensagem "Proteja os seus dados" e o botão "Ativar Touch ID "*



### Opções de sincronização



A aplicação também lhe permite ativar a sincronização do iCloud para fazer cópias de segurança dos seus dados entre os seus dispositivos Apple.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Opção de sincronização do ICloud com a mensagem "Faça uma cópia de segurança dos seus dados com a sincronização encriptada do iCloud "*



Uma vez concluídos estes passos, o Proton Authenticator está pronto a ser utilizado.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface Autenticador de protões principal vazio com as opções "Criar um novo código" e "Importar códigos "*



## Adicionar uma conta 2FA com o ProtonMail



Vamos agora ver como adicionar o seu primeiro código 2FA, utilizando o ProtonMail como exemplo. Este método funciona de forma idêntica para todos os serviços que suportam a autenticação de dois factores.



### Ativar a 2FA no ProtonMail



Antes de mais, pode consultar o nosso guia do ProtonMail para obter mais informações:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Inicie sessão na sua conta ProtonMail e aceda às definições de segurança. Procure a opção "Autenticação de dois factores" e active-a.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Página de definições do ProtonMail com a opção "Authenticator app" na secção "Two-fator authentication "* (Autenticação de dois factores)



Clique no botão para ativar o autenticador e o ProtonMail pedir-lhe-á que escolha uma aplicação de autenticação.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Janela de configuração do ProtonMail 2FA com os botões "Cancelar" e "Seguinte "*



O ProtonMail apresentará então um código QR para ser digitalizado com a sua aplicação de autenticação.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Código QR do ProtonMail para digitalizar com a sua aplicação de autenticação, com a opção "Introduzir a chave manualmente" disponível*



Se preferir introduzir a chave manualmente, clique em "Introduzir a chave manualmente" para ver a chave secreta.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Introdução manual de informações 2FA: Chave, Intervalo (30) e Dígitos (6)*



### Digitalizar o código QR com o Proton Authenticator



No Proton Authenticator no macOS, clique em "Criar um novo código". A aplicação oferece-lhe várias opções: **Digitalizar um código QR** ou **Inserir a chave manualmente**.



Utilize a câmara do seu Mac para digitalizar o código QR apresentado no ecrã do ProtonMail. Depois de ter digitalizado o código QR, será levado para o ecrã de configuração do novo código.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Nova janela de criação de registo com os campos Título (ProtonMail), Segredo, Remetente (Proton), parâmetros de dígitos e intervalo*



O Proton Authenticator preencherá automaticamente as informações. Pode personalizar o nome, se desejar, e depois clicar em "Guardar".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Código TOTP gerado para o ProtonMail (848 812) com indicação do tempo restante*



### Validar a configuração



O ProtonMail irá pedir-lhe para introduzir um código de 6 dígitos gerado pelo Proton Authenticator para confirmar que o 2FA está a funcionar corretamente.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Ecrã de validação do ProtonMail pedindo-lhe para introduzir o código de 6 dígitos (848812)*



Copie o código da aplicação (clicando no mesmo) e cole-o no ProtonMail para concluir a ativação.



Uma vez validado, o ProtonMail pedir-lhe-á para descarregar os seus códigos de recuperação. É essencial guardá-los cuidadosamente.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Ecrã dos códigos de recuperação do ProtonMail com a lista de códigos de recuperação e o botão "Download "*



### Códigos de emergência



Ao adicionar uma conta, guarde os códigos de recuperação fornecidos pelo serviço. A maioria dos sites oferece códigos de recuperação estáticos e de utilização única para guardar num local seguro. Mantenha estes códigos de backup fora do Proton Authenticator para que possa aceder à sua conta se perder o acesso à aplicação 2FA.



## Instalação do IOS e importação de código



Agora que já configurou o Proton Authenticator no macOS, pode também querer utilizá-lo no iPhone ou iPad. Veja como obter os seus códigos 2FA em vários dispositivos.



### Descarregar a aplicação no iOS



Aceda à App Store e procure por "Proton Authenticator". Descarregue e instale a aplicação no seu dispositivo iOS.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Processo de instalação no iOS: ecrã de boas-vindas, assistente de importação, seleção de aplicações compatíveis e ecrã final "Importar códigos do Proton Authenticator "*



### Método 1: Exportar/Importar através de um ficheiro JSON



Se não utilizar a sincronização automática (conta iCloud ou Proton), terá de transferir manualmente os códigos do Mac para o iPhone:



**Passo 1 - Exportar do macOS** :



No seu Mac, abra o Proton Authenticator e aceda a Definições (ícone da engrenagem). No menu, clique em "Exportar".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Menu de definições do Proton Authenticator no macOS com a opção "Exportar" visível*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Janela de exportação com o nome de ficheiro "Proton_Authenticator_backup_2025" e botão "Save "*



Guarde o ficheiro JSON no seu Mac. Pode enviá-lo por correio eletrónico seguro ou guardá-lo no iCloud Drive para aceder a partir do iPhone.



**Passo 2 - Importar no iOS** :



No seu iPhone, instale o Proton Authenticator e, durante a configuração, selecione importar códigos. Selecione "Proton Authenticator" na lista e importe o ficheiro JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Processo de importação no iOS: Localização de ficheiros JSON, confirmação de importação e ecrãs de configuração com opções de Face ID e iCloud*



### Método 2: Sincronização automática



**Via conta Proton (para sincronização multiplataforma)** :



Se ainda não tiver configurado uma conta Proton e pretender sincronizar entre diferentes sistemas operativos, a aplicação irá pedir-lhe que crie ou ligue uma conta Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Ecrã de sincronização do dispositivo que solicita a criação de uma conta Proton gratuita ou a ligação a uma conta existente*



**Via iCloud (apenas para o ecossistema Apple)** :


Se utilizar apenas dispositivos Apple, pode escolher a sincronização iCloud nas definições da aplicação. Este método sincronizará automaticamente e de forma segura os seus códigos entre todos os seus dispositivos Apple, sem necessidade de uma conta Proton.



## Cópia de segurança e restauro encriptados



Uma das principais caraterísticas do Proton Authenticator é a cópia de segurança de ponta a ponta dos códigos 2FA, garantindo que a perda ou mudança de dispositivo não significa que tem de começar tudo de novo.



### Encriptação de ponta a ponta



Quando se trata de backup encriptado na nuvem com o Proton Authenticator, os seus segredos TOTP são encriptados localmente no seu dispositivo antes de serem enviados para o servidor Proton. A desencriptação só é possível por si, nos seus dispositivos ligados à sua conta Proton. A Proton AG não tem a chave para ler os seus códigos registados.



No iOS, se optar pelo iCloud em vez da conta Proton, os seus dados são encriptados de acordo com as normas da Apple. A cópia de segurança local no Android permite-lhe encriptar o ficheiro de cópia de segurança com uma palavra-passe à sua escolha.



### Restauração em caso de perda



Se o telemóvel se perder, for roubado ou se mudar de aparelho :



**Com o backup do Proton ativado**: Instale o Proton Authenticator no novo dispositivo. Durante a configuração inicial, inicie sessão na mesma conta Proton. Imediatamente, a aplicação irá sincronizar e descarregar todos os seus códigos 2FA a partir da cópia de segurança encriptada.



**Com a cópia de segurança do iCloud (iOS)**: Ligue o novo iPhone/iPad com o mesmo ID Apple e certifique-se de que ativa o iCloud Keychain. Depois de instalar o Proton Authenticator, ligue-se ao iCloud. Os seus códigos devem ser sincronizados através do iCloud e aparecer.



**Não há backup na nuvem**: Terá de importar as suas contas manualmente. Se tiver exportado um ficheiro de cópia de segurança, utilize a função Importar no Proton Authenticator. Na pior das hipóteses, se não tiver uma cópia de segurança, terá de utilizar os códigos de cópia de segurança para cada serviço ou contactar o suporte.



O Proton Authenticator permite-lhe exportar as suas contas a qualquer momento, quer como um ficheiro encriptado, quer como um código QR de várias contas. Estas opções dão-lhe mais segurança.



## Melhores práticas



A utilização de um autenticador 2FA aumenta consideravelmente a sua segurança, mas devem ser observadas determinadas práticas recomendadas:



### Guarde os seus códigos de emergência



Quando ativa a 2FA num serviço, é-lhe frequentemente fornecida uma lista de códigos de recuperação. Mantenha-os fora do seu telemóvel (em papel, num gestor de palavras-passe encriptadas, etc.). Em caso de perda total do seu autenticador, estes códigos estáticos irão salvá-lo.



### Não misture as suas palavras-passe e códigos 2FA



É tentador utilizar um gestor de palavras-passe que também armazene TOTPs. No entanto, manter a palavra-passe e o código 2FA no mesmo local cria um ponto único de falha e enfraquece a autenticação dupla. Para uma segurança máxima, muitos especialistas recomendam a separação dos dois factores: as palavras-passe num gestor seguro e os códigos 2FA numa aplicação separada, como o Proton Authenticator. No entanto, utilizar um gestor integrado continua a ser melhor do que não ter qualquer 2FA.



### Ativar vários métodos 2FA



Idealmente, utilize mais do que um segundo fator nas suas contas críticas. Não hesite em adicionar uma chave de segurança física se o serviço o permitir. Consulte o nosso tutorial sobre chaves físicas Yubikey para obter mais informações:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Da mesma forma, mantenha à mão códigos de emergência impressos.



### Seja discreto e proteja o seu dispositivo



Não deixe que ninguém procure no seu telemóvel desbloqueado. Com o Proton Authenticator, os seus códigos estão protegidos por PIN/biometria - não divulgue este PIN. Da mesma forma, tenha cuidado com o phishing: mesmo com a 2FA, se fornecer um código a um site fraudulento em tempo real, este pode ser utilizado por um atacante.



### Actualizações e auditorias



Manter o Proton Authenticator atualizado (as actualizações corrigem possíveis falhas). Como o código é aberto, a comunidade efectua auditorias informais e a Proton publica os resultados das auditorias formais.



## Comparação com outras aplicações



Como é que o Proton Authenticator se compara com outras aplicações de autenticação? Aqui está um resumo comparativo:



**Proton Authenticator**: Código aberto, cópia de segurança encriptada E2EE opcional na nuvem, sincronização de vários dispositivos, bloqueio local, sem rastreio, disponível em dispositivos móveis e no ambiente de trabalho.



**Google Authenticator**: Proprietário, cópia de segurança através da conta Google desde 2023, mas sem encriptação de ponta a ponta (as chaves podem ser vistas pela Google), sincronização de vários dispositivos adicionada em 2023, sem bloqueio de aplicações por predefinição, contém localizadores Google.



**Aegis Authenticator**: Código aberto, apenas cópia de segurança local, sem sincronização na nuvem, bloqueio por código/biométrico, sem rastreio, apenas para Android.



**Authy**: Proprietário, cópia de segurança na nuvem encriptada por palavra-passe, mas código fechado, sincronização de vários dispositivos, bloqueio de PIN/impressão digital, recolha de número de telefone, aplicação de ambiente de trabalho descontinuada em março de 2024.



Encontrará o nosso guia para Authy abaixo:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

O Proton Authenticator é uma das soluções mais abrangentes e seguras disponíveis: código aberto, sincronização encriptada para vários dispositivos, sem acompanhamento comercial.



## Recursos e apoio



### Documentação oficial




- **Sítio Web oficial**: [proton.me/authenticator](https://proton.me/authenticator) - Apresentação do produto e transferências
- **Página de descarregamento**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Ligações para todos os sistemas operativos
- **Suporte do Proton**: [proton.me/support/two-fator-authentication-2fa](https://proton.me/support/two-fator-authentication-2fa) - Guia oficial de ativação do 2FA
- **Blogue do Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Anúncio e caraterísticas pormenorizadas



### Código-fonte e transparência




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Código-fonte aberto
- **Auditorias de segurança**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Relatórios de auditoria independentes



### Ensaios de segurança recomendados


Após a configuração, teste a sua instalação:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Verifique se as suas contas foram comprometidas
- [Diretório 2FA](https://2fa.diretory/) - Lista de serviços que suportam a 2FA



### Comunidades e debates




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Comunidade oficial do Proton
- **Fórum dos guias de privacidade**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Discussões técnicas sobre questões de privacidade
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Dicas gerais sobre privacidade



### Outros




- [Have I Been Pwned](https://haveibeenpwned.com/) - Verifique se as suas contas foram comprometidas
- [Diretório 2FA](https://2fa.diretory/) - Lista de serviços que suportam a 2FA