---
name: Aegis Authenticator
description: Como é que pode utilizar o Aegis Authenticator para proteger as suas contas com autenticação dupla?
---

![cover](assets/cover.webp)



Atualmente, a autenticação de dois factores (2FA) é essencial para proteger as contas online. Para além da palavra-passe, adiciona um segundo fator (frequentemente um código de 6 dígitos) que expira ao fim de 30 segundos, tornando-a consideravelmente mais difícil para os piratas informáticos. A utilização de uma aplicação TOTP (*Time-based One-Time Password*) dedicada é mais segura do que o SMS, que pode ser desviado por ataques de troca de SIM.



No entanto, nem todas as aplicações de autenticação são iguais. Muitas soluções proprietárias (Google Authenticator, Authy, etc.) colocam problemas: são proprietárias e de código fechado (impossível de auditar a sua segurança), por vezes integram rastreadores de publicidade, não oferecem cópias de segurança encriptadas dos seus códigos e podem até impedir a exportação das suas contas para o prender no seu ecossistema.



O Aegis Authenticator, por outro lado, apresenta-se como uma alternativa gratuita e ética a estas aplicações. O Aegis é uma aplicação gratuita, segura e de código aberto para gerir os seus tokens de verificação em dois passos no Android. O seu desenvolvimento centra-se em funcionalidades essenciais que outras aplicações não oferecem, incluindo a encriptação robusta de dados locais e a possibilidade de efetuar cópias de segurança seguras. Em suma, o Aegis oferece uma solução de dupla autenticação local e auditável, ideal para quem deseja manter um controlo total sobre os seus códigos 2FA.



## Apresentação do Aegis Authenticator



O Aegis Authenticator é uma aplicação 2FA de código aberto para Android, lançada sob a licença GPL v3. Destaca-se pela sua filosofia de "privacidade desde a conceção": a aplicação funciona totalmente offline e não requer ligação a um serviço remoto. Como resultado, os seus tokens permanecem armazenados localmente no seu dispositivo, num cofre seguro do qual só você tem a chave.



### Caraterísticas principais



**Cofre encriptado:** todos os seus códigos OTP são guardados num cofre encriptado AES-256 (modo GCM), protegido por uma palavra-passe mestra definida pelo utilizador. Pode desbloquear este cofre através de uma palavra-passe ou de dados biométricos (impressão digital, reconhecimento facial) para maior comodidade. Na ausência de uma palavra-passe, os dados não seriam encriptados, pelo que recomendamos vivamente que defina uma.



**Organização avançada:** O Aegis mantém as suas várias contas 2FA bem organizadas. Pode ordenar as entradas por ordem alfabética ou por ordem à sua escolha, agrupá-las por categoria (por exemplo, Pessoal, Trabalho, Social) para facilitar a recuperação e atribuir a cada entrada um ícone personalizado. Está incluída uma barra de pesquisa para encontrar instantaneamente um serviço ou conta pelo nome.



**Cópias de segurança locais encriptadas:** Para garantir que nunca perde o acesso às suas contas, o Aegis oferece cópias de segurança automáticas do seu cofre. Estas são encriptadas (através de uma palavra-passe) e podem ser guardadas no local da sua escolha (armazenamento interno, pasta na nuvem, etc.). A aplicação também pode exportar manualmente a sua base de dados de contas, em formato encriptado ou não encriptado, conforme necessário. A importação de contas de outras aplicações 2FA é igualmente fácil (o Aegis suporta a importação de Authy, Google Authenticator, FreeOTP, andOTP, etc.).



**Segurança e privacidade:** a aplicação está completamente offline por defeito. Não requer permissões de rede - o que significa que não transmite dados para o mundo exterior e não possui rastreadores de anúncios ou módulos de análise comportamental. O Aegis não exibe anúncios e não requer uma conta de utilizador: assim que é instalado, está pronto a funcionar sem registo. Como o seu código-fonte é público no GitHub, a comunidade pode auditá-lo livremente, garantindo a ausência de funcionalidades maliciosas ou ocultas.



**Interface moderno:** O Aegis adopta um design de material elegante, com suporte de temas escuros (incluindo um modo AMOLED) e até uma vista de mosaico opcional para apresentar os seus códigos como grelhas. O Interface é simples, sem frescuras, e impede a captura de ecrã dos códigos como medida de segurança.



## Instalação



Como o Aegis Authenticator é de código aberto, os seus criadores favorecem canais de distribuição que respeitam a privacidade. Existem duas formas principais de o instalar:



### Via F-Droid (recomendado)



A forma mais segura e fácil é através do F-Droid, a loja alternativa gratuita. Se o F-Droid ainda não estiver instalado no seu telemóvel, comece por transferi-lo a partir do sítio Web oficial [F-Droid.org] (https://f-droid.org). Depois :





- Abra o F-Droid e certifique-se de que actualizou os seus repositórios para obter a lista de aplicações mais recente
- Procure por "Aegis Authenticator" no F-Droid. A aplicação oficial deve aparecer (editor: Beem Development)
- Iniciar a instalação premindo Instalar. Como o Aegis é uma das aplicações verificadas pelo F-Droid, beneficia de um download fiável e seguro



A instalação através do F-Droid oferece a vantagem de receber actualizações automáticas da aplicação assim que estas são lançadas. Além disso, o F-Droid garante que a aplicação está livre de componentes proprietários indesejados.



### Via GitHub (APK assinado)



Se preferir instalar a aplicação sem passar por uma loja, pode descarregar o APK oficial diretamente da página do projeto no GitHub. No repositório Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), vá para a secção Releases, onde são publicadas as versões estáveis.





- Descarregar a versão mais recente do APK
- Antes de instalar o APK, certifique-se de que autorizou a instalação de aplicações de fontes desconhecidas no seu dispositivo (nas Definições do Android)
- O APK fornecido no GitHub é assinado pelo programador com a mesma chave que no F-Droid



Após a instalação manual, a aplicação funcionará de forma idêntica. Tenha em atenção que as actualizações não serão automáticas: terá de consultar periodicamente o GitHub para obter novas versões.



### Google Play Store vs F-Droid



O Aegis Authenticator está disponível na Google Play Store e no F-Droid, permitindo-lhe escolher o método de instalação:



**Google Play Store:**




- actualizações automáticas integradas no sistema Android
- instalação simples e familiar
- o mesmo APK assinado que nos outros canais



**F-Droid (recomendado) :**




- loja gratuita e de código aberto
- construção reprodutível e verificável
- não é necessário um serviço Google
- ✅ Respeito pela filosofia do software livre



A escolha entre estas duas opções depende das suas preferências relativamente ao ecossistema Google. Se preferir simplicidade, a Play Store é ideal. Se pretende uma abordagem mais favorável à privacidade, independente dos serviços Google, o F-Droid é a melhor escolha.



## Primeira configuração



Quando o Aegis é lançado pela primeira vez, é proposto um procedimento de configuração inicial para proteger o seu código 2FA:



![Configuration initiale Aegis](assets/fr/01.webp)



*Processo de configuração inicial do Aegis: ecrã de boas-vindas, opções de segurança, definição e finalização da palavra-passe mestra*



### Definir uma palavra-passe mestra



O Aegis pedir-lhe-á primeiro que escolha uma palavra-passe mestra. Esta palavra-passe será utilizada para encriptar todos os seus tokens de autenticação armazenados no cofre. Recomendamos vivamente que defina uma palavra-passe forte e única que só você saiba.



**⚠️ Atenção:** não se esqueça desta palavra-passe - se a perder, os seus códigos 2FA encriptados ficarão inacessíveis (não existe backdoor). O Aegis pedir-lhe-á que introduza a palavra-passe duas vezes para confirmação.



### Ativar o desbloqueio biométrico (opcional)



Se o seu dispositivo Android estiver equipado com um leitor de impressões digitais ou outro sensor biométrico, o Aegis solicitará a ativação do desbloqueio biométrico. Esta opção é opcional, mas muito prática: permite-lhe desbloquear rapidamente a aplicação com a sua impressão digital ou rosto, em vez de digitar a palavra-passe de cada vez.



Note que a biometria é uma conveniência adicional: a sua palavra-passe mestra continua a ser necessária se a biometria for alterada ou se o dispositivo for reiniciado.



### Descobrir as definições da aplicação



Quando estiver dentro da aplicação (o Interface principal está inicialmente vazio), familiarize-se com as opções de configuração disponíveis. Aceda às definições através do menu pendente no canto superior direito do ecrã (três pontos verticais) e, em seguida, selecione "Definições".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface Aegis principal vazio no início, acesso ao menu de parâmetros e visão geral das opções disponíveis*



O menu de definições do Aegis agrupa várias secções importantes:





- **Aparência**: Personalizar o tema (claro, escuro, AMOLED), o idioma e outras definições visuais
- **Comportamento**: Configurar o comportamento da aplicação ao interagir com a lista de entradas
- **Pacotes de ícones**: gerir e importar pacotes de ícones para personalizar o aspeto das suas contas
- **Segurança**: Definições para encriptação, desbloqueio biométrico, bloqueio automático e outros parâmetros de segurança
- **Cópias de segurança**: Configurar cópias de segurança automáticas para uma localização à sua escolha
- **Importar e exportar**: Importar cópias de segurança de outras aplicações de autenticação e exportar manualmente o cofre do Aegis
- **Registo de auditoria**: Registo detalhado de todos os eventos significativos na aplicação



Esta organização clara permite-lhe configurar o Aegis de acordo com as suas preferências e necessidades de segurança.



## Adicionar uma conta 2FA



Com o Aegis configurado, vamos passar ao essencial: adicionar as suas contas de dois factores. O processo é simples e o Aegis oferece vários métodos para integrar seus códigos de autenticação.



### Os três métodos de adição disponíveis



No ecrã principal do Aegis Interface, prima o botão **+** no canto inferior direito para aceder às opções de adição. Existem três opções:





- **Digitalizar o código QR**: Digitalizar diretamente o código QR apresentado pelo serviço Web
- **Digitalizar imagem**: Digitalizar um código QR a partir de uma imagem guardada no seu dispositivo
- **Introduzir manualmente**: Introduzir manualmente as informações da conta 2FA



### Exemplo prático: configurar o Bitwarden



Vejamos o exemplo concreto da ativação 2FA no Bitwarden para ilustrar o processo:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Exemplo de ativação de 2FA no Bitwarden: Interface web com opções de autenticação e recomendação Aegis*





- **Iniciar sessão e aceder às definições**: Inicie sessão na sua conta Bitwarden e aceda às definições, separador "Segurança"
- **Secção Fornecedores**: Aceda à secção "Providers" (Fornecedores) e clique em "Manage" (Gerir) na secção "Authenticator app" (Aplicação de autenticação)



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Processo completo para adicionar uma conta: Código QR apresentado pelo serviço, chave secreta visível e código de verificação introduzido*





- **Digitalizar o código QR**: Abre-se uma janela pop-up com o código QR e a chave secreta
- **No Aegis**: Utilizar "Scan QR code" para captar informações automaticamente
- **Verificação**: Introduzir o código de 6 dígitos gerado pelo Aegis no campo "Código de verificação"
- **Ativação**: Clique em "Ligar" para finalizar a ativação



### Adicionar detalhes manualmente



Se preferir ou não puder digitalizar o código QR, utilize a opção "Introduzir manualmente". O formulário permite-lhe introduzir :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Processo para adicionar uma nova conta 2FA: Interface vazio, adicionar opções, formulário de introdução manual e conta adicionada com êxito*





- **Nome**: Nome do serviço (por exemplo, Bitwarden, GitHub...)
- **Emitente**: O emitente (frequentemente idêntico ao nome)
- **Grupo**: Opcional, para organizar as suas contas por categoria
- **Nota**: Observações pessoais sobre esta conta
- **Segredo**: A chave secreta fornecida pelo serviço (mascarada por defeito)
- **Avançado**: Parâmetros avançados (algoritmo, período, número de dígitos)



Uma vez adicionada, a conta aparece na sua lista com o seu código atual e um indicador de tempo que mostra o tempo que falta para a renovação.



### Compatibilidade universal



O Aegis é compatível com todos os serviços que utilizam as normas TOTP e HOTP, incluindo praticamente todos os sítios que oferecem 2FA: redes sociais, bancos, gestores de palavras-passe, plataformas criptográficas, etc.



### Organização da entrada



Depois de ter adicionado várias contas, irá apreciar as ferramentas organizacionais do Aegis:





- **Ordenação personalizada:** Por predefinição, as contas são listadas por ordem alfabética, mas pode alterar a ordem manualmente
- **Grupos e categorias:** Crie grupos para separar as suas contas pessoais das suas contas profissionais, ou agrupe-as por tipo de serviço (bancário, correio eletrónico, redes sociais, etc.)
- **Ícones personalizados:** O Aegis tenta atribuir automaticamente um ícone adequado, se disponível; caso contrário, pode escolher entre muitos ícones genéricos ou importar uma imagem
- **Pesquisa rápida:** A barra de pesquisa no topo permite-lhe escrever algumas letras para filtrar instantaneamente as entradas correspondentes



Ao tocar numa entrada, o código OTP é apresentado em tamanho real (se estiver oculto) e pode copiá-lo para a área de transferência com um toque longo - útil para o colar na aplicação a que se pretende ligar.



## Segurança e cópias de segurança



Com a segurança no centro do Aegis, é importante compreender como os seus códigos 2FA são protegidos e como garantir a sua persistência em caso de problema.



### Arquitetura de segurança



**Criptografia robusta**: Todos os seus códigos são armazenados num cofre encriptado utilizando o algoritmo **AES-256 em modo GCM**, combinado com a sua palavra-passe mestra. A derivação da chave baseia-se no **scrypt**, oferecendo uma proteção melhorada contra ataques de força bruta.



**Desbloqueio seguro** : A palavra-passe mestra é necessária para desencriptar os seus dados. A biometria (opcional) utiliza o **Android Secure Keystore** e o TEE (Trusted Execution Environment) para proteger a chave de encriptação.



**Permissões mínimas**: O Aegis funciona offline por defeito, requerendo apenas acesso à câmara (leitura QR), biometria e vibrador. Nenhum dado é recolhido ou partilhado.



### Opções de cópia de segurança



O Aegis oferece várias estratégias de cópia de segurança para satisfazer diferentes necessidades de segurança e conveniência:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface completo com conta adicionada, alerta de cópia de segurança, definições de cópia de segurança automática e estratégias de cópia de segurança*



**1. Cópias de segurança locais automáticas**




- Configurar uma pasta de destino à sua escolha
- Frequência personalizável (após cada mudança, diariamente, etc.)
- Ficheiros encriptados protegidos por palavra-passe (.aesvault)
- Compatível com pastas sincronizadas (Nextcloud, Dropbox, etc.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Processo de seleção da pasta de cópia de segurança: explorador de ficheiros, pasta de destino e autorização de acesso*



**2. Cópias de segurança na nuvem para Android**




- Integração opcional com o sistema de apoio Android
- Disponível apenas para cofres encriptados (segurança preservada)
- Cópia de segurança transparente com outros dados do Android
- Restauro automático aquando da mudança de dispositivo



**3. Exportações manuais**




- Exportar a pedido através de **Configurações > Importar e exportar**
- Escolha de formato encriptado (recomendado) ou claro
- Útil para migrações ou cópias de segurança ocasionais



### Boas práticas de segurança





- Mantenha várias versões de **cópia de segurança** para evitar a corrupção
- Teste regularmente **as suas cópias de segurança**, tentando efetuar um restauro
- Guarde os códigos de recuperação fornecidos pelo serviço separadamente
- A sua **palavra-passe mestra** continua a ser necessária mesmo com cópias de segurança na nuvem
- **Proteja a sua palavra-passe principal**: utilize uma palavra-passe única e forte guardada num gestor de palavras-passe
- Mantenha a sua aplicação **actualizada** com os patches de segurança mais recentes
- Ativar o **bloqueio automático** nas definições para proteger o acesso à aplicação
- Desativar as capturas de ecrã (opção predefinida) para evitar que os seus códigos sejam interceptados
- **Utilizar a biometria com moderação**: preferir palavras-passe para acessos críticos



## Comparação com outras aplicações



Como é que o Aegis se compara com outras aplicações de autenticação populares?



### Aegis vs Google Authenticator



**Aegis :**




- código aberto e auditável
- cópia de segurança local encriptada
- organização avançada (grupos, ícones, pesquisa)
- ✅ Sem recolha de dados
- apenas Android



**Google Authenticator :**




- disponível para Android e iOS
- sincronização na nuvem (desde 2023)
- código fonte fechado
- funcionalidade limitada
- potencial recolha de dados do Google



### Aegis vs Authy



**Aegis :**




- ✅ Código aberto
- ✅ Não é necessária conta
- possibilidade de exportação de códigos
- controlo total dos dados
- sem sincronização nativa com vários dispositivos



**Authy :**




- sincronização de vários dispositivos
- disponível para Android e iOS
- código fonte fechado
- requer um número de telefone
- não é possível exportar códigos
- aplicações de ambiente de trabalho removidas em março de 2024



O Aegis é excelente para utilizadores de Android que valorizam a transparência, a segurança local e o controlo total sobre os seus dados. Alternativas como o Authy são mais adequadas se necessitar absolutamente de sincronização automática entre dispositivos.




## Conclusão



O Aegis Authenticator é uma excelente solução para quem procura uma aplicação 2FA que respeite a privacidade, seja segura e transparente. A sua abordagem de código aberto, combinada com uma encriptação robusta e um Interface elegante, faz dele uma escolha de primeira classe para proteger as suas contas online.



Embora limitado ao Android e sem sincronização nativa na nuvem, o Aegis mais do que compensa estas limitações com a sua filosofia de "privacidade desde a conceção" e controlo total dos dados. Para os utilizadores preocupados com a sua privacidade digital, o Aegis oferece uma alternativa credível e poderosa às soluções proprietárias dominantes no mercado.



A segurança das suas contas online não tem de depender da boa vontade de empresas comerciais. Com o Aegis, mantém o controlo dos seus códigos de autenticação, num cofre digital cuja chave só você tem.



## Recursos



### Sítios Web oficiais




- **Sítio Web oficial**: [getaegis.app](https://getaegis.app/) - Apresentação e transferência da candidatura
- **Código-fonte**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Repositório oficial do GitHub
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Instalação através da loja gratuita



### Documentação técnica




- **Documentação da Vault**: [Conceção da abóbada](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Descrição técnica da encriptação e da arquitetura segura
- **FAQ oficial**: [getaegis.app/#faq](https://getaegis.app/#faq) - Respostas às perguntas mais frequentes
- **Wiki do projeto**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Documentação completa do utilizador