---
name: Ente Auth
description: Um autenticador 2FA encriptado de ponta a ponta e de código aberto
---
![cover](assets/cover.webp)



A autenticação de dois factores (2FA) tornou-se indispensável para proteger as nossas contas em linha. Para além da sua palavra-passe habitual, requer um código temporário, normalmente gerado por uma aplicação dedicada. Este mecanismo, conhecido como TOTP (Time-Based One-Time Password), garante que, mesmo que a sua palavra-passe seja comprometida, um atacante não conseguirá aceder à sua conta sem possuir este segundo fator, renovado a cada 30 segundos.



No entanto, a escolha da aplicação de autenticação correta não é trivial. O Google Authenticator, embora popular, tem grandes limitações: código proprietário impossível de auditar, sincronização sem encriptação de ponta a ponta e risco de perda total dos códigos em caso de problema com o telemóvel. Outras soluções, como o Authy, requerem um número de telefone e não garantem total confidencialidade.



*o *Ente Auth** destaca-se como uma alternativa moderna e segura. Esta aplicação gratuita, de código aberto e multiplataforma, desenvolvida pela equipa responsável pelo [Ente Photos] (https://ente.io), oferece cópias de segurança encriptadas de ponta a ponta na nuvem e uma sincronização perfeita entre todos os seus dispositivos. Ao contrário das soluções proprietárias, o Ente Auth dá-lhe controlo total sobre os seus códigos de autenticação sem comprometer a sua privacidade.



Neste tutorial, mostraremos passo a passo como instalar e usar o Ente Auth, e por que essa solução difere dos autenticadores tradicionais.



## Apresentação do Ente Auth



O Ente Auth foi desenvolvido pela equipa responsável pelo Ente Photos, um serviço de armazenamento de fotografias encriptado de ponta a ponta e amigo da privacidade. Fiel à filosofia Ente ("Ente" significa "meu" em Malayalam, simbolizando o controlo sobre os seus dados), o Ente Auth foi concebido para devolver aos utilizadores o controlo total sobre os seus códigos de autenticação de dois factores.



### Principais caraterísticas



**Códigos TOTP padrão**: O Ente Auth gera códigos temporários compatíveis com a maioria dos serviços (GitHub, Google, Binance, ProtonMail, etc.). Pode adicionar quantas contas 2FA precisar, e a aplicação calcula os códigos com base nos segredos fornecidos.



**Cópia de segurança encriptada de ponta a ponta na nuvem**: Os seus códigos são armazenados online de forma segura. Só você os pode desencriptar - a chave de encriptação é derivada da sua palavra-passe e só você a conhece. O Ente (o servidor) não tem conhecimento dos seus segredos, nem mesmo dos títulos da sua conta, uma vez que tudo é encriptado no lado do cliente utilizando uma arquitetura de conhecimento zero.



**Sincronização em vários dispositivos**: Pode instalar o Ente Auth em vários dispositivos (smartphone, tablet, computador) e aceder aos seus códigos em todos eles. Todas as alterações são automaticamente e instantaneamente propagadas para os seus outros dispositivos através da nuvem encriptada, dando-lhe uma grande flexibilidade no seu trabalho diário.



**Interface minimalista e intuitivo**: A aplicação oferece um Interface simplificado, fácil de aprender mesmo para utilizadores não técnicos. as contas 2FA são apresentadas com o nome do serviço, o seu início de sessão e o código de 6 dígitos, atualizado em tempo real. O Ente Auth também apresenta o próximo código com alguns segundos de antecedência para evitar ser apanhado em falta por expiração.



**Fonte aberta e auditada**: O código fonte do Ente Auth é [público no GitHub](https://github.com/ente-io/auth) sob a licença AGPL v3.0. Qualquer programador pode auditá-lo para verificar se existem falhas ou comportamentos indesejáveis. A criptografia implementada foi objeto de uma [auditoria externa independente](https://ente.io/blog/cryptography-audit/), uma garantia da seriedade da segurança da aplicação.



### Vantagens e limitações



**Benefícios




- Privacidade desde a conceção com encriptação de ponta a ponta
- Sincronização segura entre todos os seus dispositivos
- Código-fonte aberto auditável
- Interface utilizador claro e intuitivo Interface
- Cópia de segurança automática para evitar a perda de códigos
- Disponível em todas as plataformas (telemóvel e computador)



**Limites:**




- Ligação à Internet necessária para a sincronização
- Os utilizadores avançados podem preferir soluções 100% offline como o Aegis (apenas para Android)
- Relativamente recente em comparação com as soluções estabelecidas



## Instalação



O Ente Auth está disponível nas plataformas mais populares. Pode descarregar a aplicação a partir do [sítio Web oficial] (https://ente.io/auth) ou das lojas oficiais.



![Installation d'Ente Auth](assets/fr/01.webp)



*Página de transferência do Ente Auth com todas as plataformas disponíveis*



### Android


Tem várias opções:




- Google Play Store**: Procurar por "Ente Auth" para a instalação clássica
- F-Droid**: Disponível a partir do catálogo de aplicações de código aberto para Android, com garantia de construção verificada e sem conteúdo proprietário
- Instalação manual** : Os ficheiros APK podem ser descarregados a partir da [página do projeto no GitHub] (https://github.com/ente-io/auth/releases) com notificação integrada de novas versões



### iOS (iPhone/iPad)


Instale o Ente Auth diretamente a partir da Apple App Store, procurando o nome da aplicação. A aplicação iOS também pode ser executada em Macs equipados com chips Apple Silicon (M1/M2) através da Mac App Store.



### Computadores (Windows, macOS, Linux)


O Ente Auth oferece aplicações de ambiente de trabalho nativas. Visite [ente.io/download](https://ente.io/download) ou a secção [Releases do GitHub](https://github.com/ente-io/auth/releases) :





- Windows**: É fornecido um instalador EXE
- macOS**: Arrastar e largar imagem de disco DMG em Aplicações
- Linux** : Vários formatos disponíveis (AppImage portable, .deb para Debian/Ubuntu, .rpm para Fedora/Red Hat)



**Nota:** Este tutorial é baseado no Ente Auth v4.4.4 e posterior. As versões anteriores podem ter pequenas diferenças no Interface.



### Interface Web


Sem instalação, pode aceder aos seus códigos através de [auth.ente.io] (https://auth.ente.io) a partir de qualquer navegador. O Interface web limita-se à visualização dos códigos (útil para a resolução de problemas), uma vez que a adição de contas requer a aplicação móvel ou de computador por razões de segurança.



## Primeira configuração



### Criação de conta



Quando inicia o Ente Auth pela primeira vez, tem duas opções:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ecrã inicial do Ente Auth com opções de criação de conta*



**Com conta (recomendado)**: Escolha "Criar conta" e introduza o seu e-mail Address e uma palavra-passe. **Importante**: esta palavra-passe serve como palavra-passe mestra para encriptar os seus dados. Escolha uma palavra-passe forte e única, uma vez que não existe um procedimento de reposição convencional sem perda de dados. Se a perder, os seus dados encriptados serão irrecuperáveis.



**Modo offline**: Selecione "Utilizar sem cópias de segurança" para utilizar a aplicação localmente sem uma nuvem. Neste modo, os seus códigos permanecem no dispositivo, mas terá de os exportar manualmente para evitar perdê-los.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Processo de verificação de correio eletrónico e geração de uma chave de recuperação de 24 palavras*



Pode ser solicitada uma verificação por correio eletrónico para validar a criação da conta e permitir a recuperação num novo dispositivo. A Ente Auth também lhe fornecerá uma chave de recuperação de 24 palavras (baseada no método BIP39). **É imperativo que guarde esta chave** num local seguro: é a única forma de recuperar os seus dados se se esquecer da sua palavra-passe.



### Segurança local



Recomendo vivamente a ativação da proteção local por código ou biometria. Vá a **Definições → Segurança → Ecrã de bloqueio** e configure :





- Desbloqueio biométrico**: ID facial, impressão digital, dependendo das capacidades do seu dispositivo
- PIN/palavra-passe específico da aplicação**
- Atraso do bloqueio automático**: por exemplo, "Imediatamente" ou após 30 segundos de inatividade



Esta proteção impede o acesso não autorizado aos seus códigos se alguém tiver acesso ao seu telemóvel desbloqueado. Note que este bloqueio é uma barreira adicional: os seus dados permanecem encriptados de ponta a ponta mesmo sem esta proteção.



## Adicionar contas 2FA



### Procedimento normal



Para adicionar uma nova conta 2FA, vejamos o exemplo concreto da ativação da 2FA no Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*O Interface principal da Ente Auth está pronto para adicionar a primeira conta 2FA*



**Lado do serviço (Bull Bitcoin)**: Inicie sessão na sua conta Bull Bitcoin, aceda às definições de segurança e active a autenticação de dois factores.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* menu de definições de segurança



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Opção para ativar a autenticação de dois factores no Bull Bitcoin*



O serviço apresentará então um código QR que deve ser digitalizado com a sua aplicação de autenticação:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Código QR gerado pelo Bull Bitcoin para ser digitalizado com o seu autenticador*



**Em Ente Auth**: Clique em "Introduzir uma chave de configuração" e, em seguida, digitalize o código QR apresentado pelo Bull Bitcoin. O Ente Auth reconhecerá automaticamente a conta e preencherá os campos.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Configurar os dados da conta Bull Bitcoin no Ente Auth*



Pode personalizar o nome do serviço e o seu início de sessão para o tornar mais fácil de encontrar. As definições avançadas (algoritmo SHA1, período de 30s, 6 dígitos) estão geralmente corretas por predefinição.



**Validação do lado do serviço**: Regresse ao touro Bitcoin e introduza o código de 6 dígitos gerado pelo Ente Auth para finalizar a ativação.



![Saisie du code 2FA](assets/fr/09.webp)



*Introduza o código gerado pela Ente Auth para validar a ativação da 2FA*



![2FA activée](assets/fr/10.webp)



*Confirmação da ativação bem sucedida da 2FA no Bull Bitcoin*



**Códigos de recuperação**: O Bull Bitcoin fornecer-lhe-á códigos de recuperação. **Guarde-os num local seguro, separado do seu autenticador.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Opção para códigos de emergência generate no touro Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Lista de códigos de recuperação para guardar num local seguro*



### Organização e gestão



O Ente Auth oferece várias funcionalidades práticas:



**Cópia rápida**: Prima o código para o copiar automaticamente para a área de transferência.



**Acções sensíveis ao contexto**: Prima e mantenha premido (ou clique com o botão direito do rato no ambiente de trabalho) para editar, eliminar, partilhar ou fixar uma entrada.



**Etiquetas e pesquisa**: Organize as suas contas com etiquetas (pessoal/profissional, por categoria de serviço) e utilize a barra de pesquisa para filtrar rapidamente.



![Création d'un tag](assets/fr/17.webp)



*Processo de criação de etiquetas: menu contextual e diálogo de criação*



![Tag appliqué](assets/fr/18.webp)



*Etiqueta "Bitcoin" aplicada com sucesso na conta Bull Bitcoin*



**Ícones automáticos**: Cada entrada pode ser ilustrada com o logótipo do serviço, graças à integração do pacote de ícones [Simple Icons] (https://simpleicons.org/).



**Partilha segura temporária**: Uma funcionalidade exclusiva do Ente Auth, a partilha segura permite-lhe transmitir um código 2FA a um colega sem revelar o segredo subjacente. generate uma ligação encriptada válida durante 2, 5 ou 10 minutos no máximo - o destinatário vê o código em tempo real, mas não pode exportá-lo nem aceder aos dados da conta. Este método é ideal para assistência técnica ou colaboração temporária, oferecendo um nível de segurança que não é possível com uma simples captura de ecrã ou mensagem de texto.



![Partage sécurisé](assets/fr/19.webp)



*Interface partilha segura temporária: escolher a duração (5 min)*



**Exportação/importação segura**: O Ente Auth permite-lhe exportar os seus códigos para outras aplicações, ou importá-los do Google Authenticator e de outras soluções. A exportação é feita através de um ficheiro encriptado ou de um código QR, garantindo a portabilidade dos seus dados sem comprometer a segurança.



**Chave de recuperação BIP39**: A aplicação gera automaticamente uma frase de recuperação de 24 palavras de acordo com o padrão BIP39 (Bitcoin Improvement Proposal), idêntico ao das carteiras de criptomoedas. Esta frase é a sua chave de recuperação definitiva, permitindo-lhe restaurar todos os seus códigos mesmo que se esqueça da sua palavra-passe mestra.



## Configuração e definições



O Ente Auth oferece inúmeras opções de personalização acessíveis através das definições da aplicação:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Visão geral dos parâmetros disponíveis no Ente Auth*



### Gestão de contas e dados



![Paramètres de sécurité](assets/fr/14.webp)



*Opções de segurança avançadas: verificação por correio eletrónico, código PIN, sessões activas*



As definições de segurança permitem-lhe :




- Ativar a verificação de correio eletrónico para novas ligações
- Ativar a chave de acesso
- Ver sessões activas nos seus vários dispositivos
- Configurar um código PIN ou dados biométricos



### Interface e opções de utilização



![Paramètres généraux](assets/fr/15.webp)



*Parâmetros Interface e personalização da aplicação*



As definições gerais incluem :




- Língua**: Interface multilingue
- Ecrã**: Ícones grandes, modo compacto
- Privacidade**: Ocultar códigos, pesquisa rápida
- Telemetria**: Relatório de erros (pode ser desativado)



## Cópia de segurança e sincronização



### Como funciona a encriptação



Quando adiciona uma conta com uma conta Ente ligada, a aplicação encripta imediatamente estes dados sensíveis localmente utilizando a sua chave mestra (derivada da sua palavra-passe). Os dados encriptados são então enviados para o servidor Ente para armazenamento.



Graças a este mecanismo, está sempre disponível uma cópia de segurança encriptada de ponta a ponta na nuvem dos seus códigos. Se perder o seu dispositivo, basta reinstalar o Ente Auth e voltar a ligar-se: a aplicação descarregará e desencriptará automaticamente todos os seus códigos.



### Sincronização de vários dispositivos



Se utilizar o Ente Auth no smartphone e no computador, quaisquer adições ou alterações num dispositivo aparecem em segundos no outro. Esta sincronização passa pela nuvem da Ente, mas como os dados são encriptados de ponta a ponta, o servidor só vê conteúdo encriptado ilegível.



![Synchronisation mobile](assets/fr/16.webp)



*Demonstração de sincronização: a mesma conta Bull Bitcoin acessível no telemóvel e no computador*



A sincronização é perfeita: instale o Ente Auth no seu smartphone, inicie sessão com as suas credenciais e todos os seus códigos 2FA (aqui Bull Bitcoin) aparecem automaticamente. O exemplo acima mostra uma sincronização perfeita entre o computador e o telemóvel - o mesmo código Bull Bitcoin está acessível em ambos os dispositivos.



Em termos de confidencialidade, nem a Ente nem terceiros têm acesso aos seus segredos 2FA. Mesmo os metadados (etiquetas, notas, nomes de serviços) são encriptados antes de serem enviados. Esta arquitetura de conhecimento zero garante que só você pode decifrar os seus códigos.



### Utilização offline



A sincronização requer a Internet, mas o Ente Auth funciona perfeitamente offline em todos os dispositivos, uma vez que todos os dados são armazenados localmente. As alterações offline são colocadas em fila de espera e sincronizadas assim que a ligação é restabelecida.



## Segurança e privacidade



### Garantias criptográficas



O Ente Auth baseia-se numa encriptação robusta de ponta a ponta com uma arquitetura de conhecimento zero. Os seus códigos são encriptados com uma chave que só você possui, derivada da sua palavra-passe mestra utilizando funções avançadas de derivação de chaves.



**Arquitetura de conhecimento zero: A Ente não pode aceder fisicamente aos seus dados. Mesmo os metadados (nomes de serviços, etiquetas, notas) são encriptados no lado do cliente antes da transmissão. Esta abordagem garante que, no caso de um ataque aos seus servidores ou de um pedido governamental, a Ente apenas pode divulgar dados encriptados que não podem ser lidos sem a sua palavra-passe.



**Encriptação local**: O processo de encriptação ocorre inteiramente no seu dispositivo antes de ser enviado para a nuvem. Os servidores da Ente recebem e armazenam apenas dados encriptados, tornando impossível o acesso não autorizado, mesmo para administradores de serviços.



### Transparência e auditorias



Como o código é [open source] (https://github.com/ente-io/auth), a comunidade pode verificar a ausência de backdoors. A Ente foi objeto de [múltiplas auditorias externas](https://ente.io/blog/cryptography-audit/) para validar a segurança da sua implementação:





- Cure53** (Alemanha): Auditoria de segurança criptográfica e de aplicações
- Symbolic Software** (França): Experiência criptográfica especializada
- Fallible** (Índia): Teste de penetração e análise de vulnerabilidade



Estas auditorias independentes, efectuadas por empresas reconhecidas, garantem que a implementação criptográfica da Ente Auth está em conformidade com as melhores práticas de segurança e não apresenta falhas críticas.



### Política de privacidade



A Ente Auth aplica uma [política de privacidade exemplar] (https://ente.io/privacy/) baseada na recolha mínima de dados. Apenas são conservadas as informações estritamente necessárias para o funcionamento do serviço: o seu e-mail Address para autenticação e recuperação da conta.



**Sem rastreamento ou telemetria**: Ao contrário da maioria das aplicações, o Ente Auth não recolhe métricas de utilização, não identifica dados de colisão nem informações comportamentais. A aplicação funciona sem publicidade intrusiva ou rastreadores analíticos.



**Conformidade com o RGPD**: A Ente está em total conformidade com o Regulamento Geral Europeu de Proteção de Dados. Tem o direito de aceder, corrigir ou eliminar os seus dados em qualquer altura. A exportação de dados] (https://ente.io/take-control/) está apenas a um clique de distância e a eliminação permanente da sua conta elimina todos os seus dados dos servidores.



**Armazenamento descentralizado e seguro**: Os seus dados encriptados são replicados em 3 fornecedores diferentes, em 3 países diferentes, garantindo uma disponibilidade óptima e evitando a dependência de um único fornecedor de serviços na nuvem.



O modelo de negócio da Ente baseia-se no serviço pago Ente Photos, o que nos permite oferecer o Ente Auth **gratuitamente e sem limitações** sem comprometer a sua privacidade através da monetização dos seus dados. Esta abordagem garante a sustentabilidade do serviço sem depender de publicidade ou da revenda de dados pessoais.



## Comparação com outras soluções



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

A Ente Auth destaca-se como uma das poucas soluções que combina todas as vantagens: transparência do código-fonte, cópia de segurança encriptada na nuvem e sincronização entre plataformas.



## Casos de utilização recomendados



### Utilizadores individuais



O Ente Auth é ideal para indivíduos preocupados com a segurança que activam sistematicamente a 2FA. Já não terá de se preocupar com a perda dos seus códigos ao mudar de telemóvel, nem com a necessidade de escolher entre comodidade e segurança.



### Utilização familiar e com vários dispositivos



A aplicação é muito útil se utilizar vários dispositivos. Pode guardar os seus códigos em smartphones e tablets ou partilhar determinados códigos familiares (Netflix, nuvem familiar) de forma síncrona e segura.



### Utilização profissional



Para as equipas que gerem contas sensíveis, o Ente Auth facilita a colaboração preservando a segurança, graças às suas funcionalidades avançadas de partilha integradas na secção "Organização e gestão".



## Melhores práticas





- Guarde os seus códigos de emergência**: Mantenha os códigos de recuperação fornecidos por cada serviço afastados do seu telemóvel.





- Utilize uma palavra-passe mestra forte**: A palavra-passe mestra do Ente Auth deve ser única e robusta, uma vez que protege todos os seus códigos.





- Ativar a proteção local**: Configure o PIN ou a biometria para impedir o acesso físico não autorizado.





- Não personalize demasiado**: Evite modificações avançadas que possam comprometer a sincronização.





- Manter a aplicação actualizada**: As actualizações corrigem falhas de segurança e melhoram a funcionalidade.





- Teste o restauro**: Ocasionalmente, verifique se consegue restaurar os seus códigos noutro dispositivo.



## Conclusão



O Ente Auth representa uma solução moderna e abrangente para a autenticação de dois factores. Ao combinar segurança, transparência e facilidade de utilização, esta aplicação de código aberto satisfaz as necessidades de utilizadores exigentes sem sacrificar a conveniência.



Ao contrário das soluções proprietárias que o prendem a um ecossistema opaco, o Ente Auth devolve-lhe o controlo dos seus dados de autenticação, protegendo-o contra perdas acidentais graças às suas cópias de segurança encriptadas.



Quer seja um indivíduo que procura proteger as suas contas pessoais ou uma equipa que gere o acesso empresarial, o Ente Auth é uma escolha inteligente para modernizar a sua abordagem à segurança digital sem comprometer a privacidade.



## Recursos e apoio



### Documentação oficial




- Sítio Web oficial**: [ente.io/auth](https://ente.io/auth)
- Centro de ajuda**: [help.ente.io/auth] (https://help.ente.io/auth)
- Blogue técnico**: [ente.io/blog](https://ente.io/blog)



### Código-fonte e transparência




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Auditoria de criptografia**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Comunidade




- Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)