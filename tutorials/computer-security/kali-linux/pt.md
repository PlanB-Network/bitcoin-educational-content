---
name: Kali
description: Instalar o Kali Linux no VirtualBox, como uma pen USB de arranque ou como um dual boot, passo a passo.
---

![cover-kali](assets/cover.webp)



## Introdução



### Porquê o Kali Linux?



**O Kali Linux** é uma distribuição Linux especializada em segurança de TI.


Eis a razão pela qual utilizamos o Kali Linux:





- Está pré-configurado com uma vasta gama de ferramentas de pentesting (testes de segurança do sistema e da rede).
- É de **fonte aberta e gratuita**, pelo que pode utilizá-la e modificá-la livremente.
- É **fiável e seguro**, ideal para aprender sobre cibersegurança.
- Permite-lhe aprender a utilizar o Linux num ambiente preparado para testes.
- Pode ser instalado de diferentes formas: **VirtualBox**, **chave USB inicializável**, ou **boot duplo**.



## Instalação e configuração



### 1. Pré-requisitos



**Equipamento necessário





- processador de 64 bits** (Intel ou AMD).
- 8 GB de RAM no mínimo** (4 GB podem ser suficientes para uma instalação leve ou VM).
- 50 GB de espaço livre em disco** para instalar o Kali Linux.
- Ligação à Internet** para transferir a imagem ISO e as actualizações.
- Uma chave USB de pelo menos 8 GB** para criar um suporte de arranque (se pretender instalar o Kali num PC ou testá-lo num Live USB).



É importante fazer uma cópia de segurança dos seus dados antes de instalar num PC existente.



### 2. Descarregar





- Ir para [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Selecione a imagem ISO para a sua aplicação:
  - Imagem de instalação** : para instalação no PC.
  - Imagem virtual**: para instalar o Kali no VirtualBox ou VMware.
- Descarregar a imagem ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Criar uma chave USB de arranque



É possível utilizar várias ferramentas, como o Balena Etcher :





- Transfira e instale o [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Abra o Balena Etcher e selecione a imagem ISO do Kali.
- Selecione a chave USB como suporte de destino.
- Clique em Flash e aguarde a conclusão do processo.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Instalando e protegendo o Kali Linux



#### 4.1 Arranque a partir da chave USB





- Desligar o computador.
- Ligue a chave USB (que contém o Kali Linux).
- Ligue o seu computador. Em PCs recentes, o sistema deve reconhecer automaticamente a chave de arranque USB. Se não for esse o caso, reinicie mantendo premida a tecla de acesso à BIOS/UEFI (normalmente F2, F12 ou Delete, dependendo da marca).
  - No menu BIOS/UEFI, selecione a sua chave USB como dispositivo de arranque.
  - Guardar e reiniciar.



#### 4.2 Iniciar a instalação



##### Ecrã de arranque



Ao arrancar a partir da pen USB, deve aparecer o ecrã de arranque do Kali Linux. Escolha entre **instalação gráfica** e **instalação de texto**. Neste exemplo, optámos pela instalação gráfica.



![capture](assets/fr/06.webp)



Se utilizar a imagem **Live**, verá outro modo, **Live**, que é também a opção de arranque predefinida.



![Mode Live](assets/fr/07.webp)



##### Seleção da língua



Escolha a sua língua preferida para a instalação e o sistema.



![Sélection de la langue](assets/fr/08.webp)



Indique a sua localização geográfica.



![Options d'accessibilité](assets/fr/09.webp)



##### Configuração do teclado



Selecione a disposição do seu teclado. Está disponível um campo de teste para verificar se as teclas correspondem à sua configuração.



![Configuration du clavier](assets/fr/10.webp)



##### Ligação de rede



A instalação irá agora analisar as suas interfaces de rede, procurar um serviço DHCP e, em seguida, pedir-lhe para introduzir um nome de anfitrião para o seu sistema. No exemplo abaixo, nós inserimos **"kali "** como o nome do host.



![Configuration réseau](assets/fr/11.webp)



Opcionalmente, pode fornecer um nome de domínio predefinido que este sistema irá utilizar (os valores podem ser obtidos a partir do DHCP ou se existir um sistema operativo pré-existente).



![Choix du type d'installation](assets/fr/12.webp)



##### Contas de utilizador



Em seguida, crie a conta de utilizador para o sistema (nome completo, nome de utilizador e uma palavra-passe forte).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Fuso horário



Selecione a sua área geográfica para definir a hora do sistema.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Tipo de partição



O instalador analisa os seus discos e apresenta várias opções, dependendo da sua configuração.



Neste guia, partimos de um **disco em branco**, o que dá **quatro escolhas possíveis**.


Vamos selecionar **Guided - use entire disk** (Guiado - utilizar todo o disco), uma vez que estamos a efetuar uma instalação única do Kali Linux (arranque único). Isto significa que nenhum outro sistema operativo será mantido e que todo o disco pode ser apagado.



Se o disco já contiver dados, pode ser apresentada uma opção adicional **Guided - use largest contiguous free space**.



Esta alternativa permite-lhe instalar o Kali Linux sem apagar os dados existentes, tornando-o ideal para o arranque duplo com outro sistema.



No nosso caso, o disco está vazio, pelo que esta opção não aparece.



![Choix du partitionnement](assets/fr/17.webp)



Selecione o disco a ser particionado.



![capture](assets/fr/18.webp)



Dependendo das suas necessidades, pode optar por manter todos os seus ficheiros numa única partição (comportamento predefinido) ou ter partições separadas para um ou mais diretórios de nível superior.



Se não tiver a certeza do que pretende, escolha a opção **Todos os ficheiros numa única partição**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Terá então uma última oportunidade para verificar a configuração do seu disco antes que o programa de instalação efectue quaisquer alterações irreversíveis. Depois de clicar em _Continuar_, o programa de instalação será iniciado e a instalação estará quase concluída.



![capture](assets/fr/21.webp)



##### LVM encriptado



Se esta opção foi activada no passo anterior, o Kali Linux irá agora executar um apagamento seguro do disco rígido antes de lhe pedir uma palavra-passe LVM.



Utilize uma palavra-passe forte, caso contrário será apresentado um aviso sobre um passphrase fraco.



##### Informações de procuração



O Kali Linux usa repositórios para distribuir aplicativos. Terá de introduzir as informações de proxy necessárias se o seu ambiente utilizar um.



Se **não tiver a certeza** de utilizar um proxy, **deixe em branco**. A introdução de informações falsas impedirá a ligação aos repositórios.



![capture](assets/fr/22.webp)



##### Metafetos



Se o acesso à rede não tiver sido configurado, terá de **configurar mais** quando lhe for pedido.



Se estiver a utilizar a imagem **Live**, o passo seguinte não será apresentado.



Pode então selecionar os [metapacotes](https://www.kali.org/docs/general-use/metapackages/) que deseja instalar. As opções predefinidas irão instalar um sistema Kali Linux padrão, por isso não precisa de modificar nada.



![capture](assets/fr/23.webp)



#### Informações de arranque



Em seguida, confirme a instalação do gestor de arranque GRUB.



![capture](assets/fr/24.webp)



##### Reiniciar



Por fim, clique em Continuar para reiniciar a sua nova instalação do Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Atualização e configuração do Kali Linux após a instalação



A atualização do sistema é um passo importante após uma nova instalação. Existem duas opções:



##### Opção 1: Através da interface gráfica do utilizador (GUI)



Kali, tal como Debian/Ubuntu, oferece um gestor de actualizações gráfico integrado.



1. Clique no **menu principal** (canto superior esquerdo ou inferior, consoante o ambiente de trabalho).


2. Abrir o **"Atualizador de software "**.


3. A ferramenta irá :




    - Verifique os pacotes a atualizar.
    - É apresentada uma lista (com tamanhos e versões).
    - Permite-lhe lançar a atualização com um único clique.


4. Introduza a sua palavra-passe de administrador (`sudo`) quando lhe for pedido.


5. Deixe-o instalar e reiniciar, se necessário.



##### Opção 2: via terminal



Abra um terminal e execute :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Não é aconselhável utilizar a conta **root** para o trabalho diário; em vez disso, crie um utilizador não-root.



No seu terminal, digite estes comandos:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Termine a sessão e volte a iniciar sessão com o novo utilizador.



Vamos resumir algumas tarefas básicas do Kali Linux numa tabela.



### Tarefas básicas no Kali Linux



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## Conclusão



A instalação do Kali Linux é apenas o primeiro passo para descobrir este poderoso ambiente dedicado à cibersegurança. Ao dominar as tarefas básicas e a gestão do sistema, todos podem começar a explorar as ferramentas incorporadas e a compreender o funcionamento interno de um sistema Linux. O Kali oferece uma excelente plataforma de aprendizagem, tanto para reforçar as competências técnicas como para desenvolver uma verdadeira cultura de segurança informática.