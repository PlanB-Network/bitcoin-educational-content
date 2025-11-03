---
name: Cryptomator
description: Encriptar os seus ficheiros na nuvem
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original.*



___



## I. Apresentação



Neste tutorial, vamos utilizar a aplicação Cryptomator para encriptar dados armazenados na Cloud, quer seja no Microsoft OneDrive, Google Drive, Dropbox, Box ou mesmo iCloud.



Encriptar os dados que armazena em soluções de armazenamento online como o Drive é a melhor forma de proteger os seus ficheiros e a sua privacidade. Graças à encriptação, é o único que pode desencriptar e ler os seus dados, mesmo que estejam armazenados num servidor nos EUA ou noutro país do mundo.



Nesta demonstração, será utilizada uma máquina Windows 11 22H2 com o OneDrive, mas o procedimento é idêntico noutras versões do Windows e noutros serviços de armazenamento. Só precisa de instalar o cliente de sincronização e adicionar a sua conta. Isto permitirá ao Cryptomator armazenar os seus dados na caixa-forte.



![Image](assets/fr/020.webp)



O Cryptomator é uma alternativa a outras aplicações, nomeadamente ao Picocrypt apresentado noutro artigo, que tem um aspeto diferente, mas é igualmente simples de utilizar. O Cryptomator é também **open source**, compatível com o RGPD e **encripta dados com o algoritmo de encriptação AES-256 bit**. Em contrapartida, o Picocrypt baseia-se no algoritmo mais rápido XChaCha20 (também de 256 bits).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

A aplicação Cryptomator está disponível para **Windows** (exe / msi), **Linux**, **macOS,** mas também **Android** e **iOS**. A propósito, todas as aplicações são gratuitas, exceto a aplicação para Android, que tem de ser paga (14,99 euros).



No seu computador, o **Cryptomator criará uma pasta na qual criará um cofre**. No cofre, que pode ser armazenado no seu OneDrive, Google Drive ou similar, os seus dados serão encriptados. Assim, se guardar todos os seus dados no cofre alojado no espaço de armazenamento do seu Drive, estes estarão protegidos (porque estão encriptados).



**Nota**: neste artigo, os serviços de armazenamento online são utilizados como exemplo, mas o Cryptomator pode ser utilizado para encriptar dados num disco local, num disco externo ou mesmo num NAS. De facto, não existem restrições.



## II. Instalação do Cryptomator



Para começar, é necessário **descarregar** e **instalar** **Cryptomator**. Quando o download estiver completo, bastam alguns cliques para completar a instalação. Tal como o [Rclone] (https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), o Cryptomator baseia-se no WinFsp para **montar uma unidade virtual na sua máquina Windows**.





- [Descarregar o Cryptomator do sítio Web oficial](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Utilizar o Cryptomator no Windows



### A. Criar um novo cofre



Para criar um novo cofre, clique no botão "**Adicionar**" e selecione "**Novo cofre...**". Os cofres existentes e conhecidos nesta máquina aparecerão então no Interface, à esquerda. **Um cofre criado na máquina A pode ser aberto e modificado na máquina B**, desde que esta esteja equipada com o Cryptomator (e a chave de encriptação seja conhecida).



![Image](assets/fr/015.webp)



Comece por dar um nome à caixa-forte, por exemplo, "**IT-Connect**". Isto irá criar um diretório com o nome "**IT-Connect**" no meu OneDrive.



![Image](assets/fr/011.webp)



Na etapa seguinte, é provável que o Cryptomator **detecte o "Drive "** presente no seu computador: Google Drive, OneDrive, Dropbox, etc.... Para que o utilizador possa selecionar diretamente o fornecedor. Experimentei isto em duas máquinas Windows 11 diferentes, com várias unidades, e não foi detectado. Não há problema, basta definir uma "**Localização personalizada**" e selecionar a raiz do seu espaço de armazenamento. Por exemplo: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Em seguida, pode ajustar uma opção nas definições de especialistas.



![Image](assets/fr/021.webp)



Em seguida, é necessário definir **uma palavra-passe correspondente à chave de encriptação**. Esta palavra-passe permitir-lhe-á **desbloquear o seu cofre Cryptomator** e aceder aos seus dados. **Se a perder, perde o acesso aos seus dados**. Por fim, tem ainda a opção de **criar uma chave de segurança**, marcando a opção "**Sim, mais vale prevenir do que remediar**", no mesmo espírito da chave de recuperação [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Isto é aconselhável, mas não guarde esta chave de cópia de segurança na raiz do seu OneDrive!



Clique em "**Criar um cofre**".



![Image](assets/fr/019.webp)



Copie a chave de recuperação e guarde-a no seu gestor de palavras-passe favorito. Clique em "**Next**" (Seguinte).



![Image](assets/fr/013.webp)



E pronto, o seu novo baú está criado e pronto a ser utilizado!



![Image](assets/fr/014.webp)



### B. Valores de acesso



Para aceder a um cofre e aos seus dados, seja para **ler dados existentes ou adicionar novos dados**, é necessário **desbloqueá-lo**. O Cryptomator lista os cofres conhecidos: o cofre IT-Connect aparece, basta seleccioná-lo e clicar em "**Unlock**".



![Image](assets/fr/016.webp)



Tem de introduzir a sua palavra-passe para desbloquear o cofre. Em seguida, clique em "**Release drive**".



![Image](assets/fr/022.webp)



**Esta unidade, que aqui herda a letra E, dá-lhe acesso aos seus dados (em texto simples, uma vez que o cofre está desbloqueado).**



![Image](assets/fr/017.webp)



No lado do OneDrive, não podemos navegar diretamente no cofre do Cryptomator. Não podemos ver os dados (nem os nomes dos ficheiros nem o seu conteúdo). Isto significa que não é necessário adicionar dados ao cofre do Cryptomator através do atalho habitual do OneDrive. **Tem de adicionar os seus dados utilizando a unidade virtual do Cryptomator.**



![Image](assets/fr/012.webp)



### C. Opções de tronco



As definições do cofre são acedidas através do botão "**Opções de volume encriptado**" (quando bloqueado) e permitem o bloqueio automático em caso de inatividade, tal como pode fazer com o seu cofre de senhas. A opção "**Unlock encrypted volume on startup**", como o nome sugere, desbloqueia a unidade sem qualquer intervenção da sua parte e monta a unidade virtual. Por razões de segurança, é melhor evitar ativar esta opção.



Através do separador "**Montagem**" também pode decidir montá-la apenas para leitura ou atribuir uma letra específica.



![Image](assets/fr/024.webp)



Além disso, nas definições do Cryptomator, pode **ativar o arranque automático da aplicação**.



## IV. Conclusão



Com o **Cryptomator**, pode **criar um cofre encriptado** em apenas alguns minutos para proteger os dados que pretende armazenar no OneDrive e consortes. É muito fácil de utilizar quando se trata de o "emparelhar" com uma unidade: para este efeito, tem a minha preferência em relação ao Picocrypt.