---
name: Kali
description: Instalación de Kali Linux en VirtualBox, como una memoria USB de arranque, o como arranque dual, paso a paso.
---

![cover-kali](assets/cover.webp)



## Introducción



### ¿Por qué Kali Linux?



**Kali Linux** es una distribución Linux especializada en seguridad informática.


He aquí por qué utilizamos Kali Linux:





- Está preconfigurado con una amplia gama de herramientas de pentesting (pruebas de seguridad de sistemas y redes).
- Es **de código abierto y gratuito**, por lo que puede utilizarlo y modificarlo libremente.
- Es **fiable y seguro**, ideal para aprender sobre ciberseguridad.
- Permite aprender a utilizar Linux en un entorno preparado para pruebas.
- Se puede instalar de diferentes maneras: **VirtualBox**, **llave USB de arranque**, o **arranque dual**.



## Instalación y configuración



### 1. Requisitos previos



**Equipo necesario:**





- procesador de 64 bits** (Intel o AMD).
- 8 GB de RAM como mínimo** (4 GB pueden ser suficientes para una instalación ligera o VM).
- 50 GB de espacio libre en disco** para instalar Kali Linux.
- Conexión a Internet** para descargar la imagen ISO y las actualizaciones.
- Una llave USB** de 8 GB como mínimo para crear medios de arranque (si desea instalar Kali en un PC o probarlo en Live USB).



Es importante hacer una copia de seguridad de los datos antes de instalar en un PC existente.



### 2. Descargar





- Ir a [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Seleccione la imagen ISO para su aplicación:
  - Imagen de instalación** : para instalación en PC.
  - Imagen virtual**: para instalar Kali en VirtualBox o VMware.
- Descarga la imagen ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Crear una llave USB de arranque



Puede utilizar varias herramientas, como Balena Etcher :





- Descargue e instale [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Abra Balena Etcher y seleccione la imagen ISO de Kali.
- Selecciona la llave USB como soporte de destino.
- Haga clic en Flash y espere a que finalice el proceso.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Instalación y seguridad de Kali Linux



#### 4.1 Arranque desde la memoria USB





- Apaga el ordenador.
- Conecte la llave USB (que contiene Kali Linux).
- Encienda el ordenador. En los PC recientes, el sistema debería reconocer automáticamente la llave de arranque USB. Si no es así, reinicia manteniendo pulsada la tecla de acceso a la BIOS/UEFI (normalmente F2, F12 o Supr, según la marca).
  - En el menú BIOS/UEFI, selecciona tu llave USB como dispositivo de arranque.
  - Guardar y reiniciar.



#### 4.2 Iniciar la instalación



##### Pantalla de inicio



Al arrancar desde la memoria USB, debería aparecer la pantalla de arranque de Kali Linux. Elige entre **instalación gráfica** e **instalación de texto**. En este ejemplo, hemos optado por la instalación gráfica.



![capture](assets/fr/06.webp)



Si utilizas la imagen **Live**, verás otro modo, **Live**, que también es la opción de inicio por defecto.



![Mode Live](assets/fr/07.webp)



##### Selección de idioma



Elige el idioma que prefieras para la instalación y el sistema.



![Sélection de la langue](assets/fr/08.webp)



Especifique su ubicación geográfica.



![Options d'accessibilité](assets/fr/09.webp)



##### Configuración del teclado



Seleccione la distribución de su teclado. Dispone de un campo de prueba para comprobar que las teclas corresponden a su configuración.



![Configuration du clavier](assets/fr/10.webp)



##### Conexión a la red



La instalación escaneará ahora tus interfaces de red, buscará un servicio DHCP y te pedirá que introduzcas un nombre de host para tu sistema. En el siguiente ejemplo, hemos introducido **"kali "** como nombre de host.



![Configuration réseau](assets/fr/11.webp)



Opcionalmente, puede proporcionar un nombre de dominio predeterminado que utilizará este sistema (los valores se pueden recuperar de DHCP o si existe un sistema operativo preexistente).



![Choix du type d'installation](assets/fr/12.webp)



##### Cuentas de usuario



A continuación, cree la cuenta de usuario para el sistema (nombre completo, nombre de usuario y una contraseña segura).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Huso horario



Seleccione su zona geográfica para ajustar la hora del sistema.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Tipo de partición



A continuación, el instalador escanea tus discos y muestra varias opciones en función de tu configuración.



En esta guía, partimos de un **disco en blanco**, lo que da **cuatro opciones posibles**.


Vamos a seleccionar **Guided - use entire disk**, ya que aquí estamos realizando una instalación única de Kali Linux (single boot). Esto significa que no se conservará ningún otro sistema operativo, y que se puede borrar todo el disco.



Si su disco ya contiene datos, puede aparecer una opción adicional **Guiado - utilizar el mayor espacio libre contiguo**.



Esta alternativa le permite instalar Kali Linux sin borrar los datos existentes, por lo que es ideal para el arranque dual con otro sistema.



En nuestro caso, el disco está vacío, por lo que esta opción no aparece.



![Choix du partitionnement](assets/fr/17.webp)



Seleccione el disco a particionar.



![capture](assets/fr/18.webp)



Dependiendo de sus necesidades, puede elegir mantener todos sus archivos en una única partición (comportamiento por defecto) o tener particiones separadas para uno o más directorios de nivel superior.



Si no estás seguro de lo que quieres, elige la opción **Todos los archivos en una sola partición**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Tendrá entonces una última oportunidad de comprobar la configuración de su disco antes de que el programa de instalación realice cambios irreversibles. Una vez que haya hecho clic en _Continuar_, el programa de instalación se iniciará y la instalación estará casi completa.



![capture](assets/fr/21.webp)



##### LVM cifrado



Si esta opción fue habilitada en el paso anterior, Kali Linux ahora realizará un borrado seguro del disco duro antes de pedirle una contraseña LVM.



Por favor, utilice una contraseña segura, de lo contrario se mostrará una advertencia sobre un passphrase débil.



##### Información de representación



Kali Linux utiliza repositorios para distribuir aplicaciones. Tendrá que introducir la información de proxy necesaria si su entorno utiliza uno.



Si **no está seguro** de utilizar un proxy, **deje en blanco**. Introducir información falsa impedirá la conexión a los repositorios.



![capture](assets/fr/22.webp)



##### Metapets



Si no se ha configurado el acceso a la red, deberá **configurar de nuevo** cuando se le solicite.



Si está utilizando la imagen **Live**, no se mostrará el siguiente paso.



A continuación, puede seleccionar los [metapaquetes](https://www.kali.org/docs/general-use/metapackages/) que desea instalar. Las opciones por defecto instalarán un sistema Kali Linux estándar, por lo que no necesitarás modificar nada.



![capture](assets/fr/23.webp)



#### Información inicial



A continuación, confirme la instalación del gestor de arranque GRUB.



![capture](assets/fr/24.webp)



##### Reinicie



Por último, haga clic en Continuar para reiniciar su nueva instalación de Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Actualización y configuración de Kali Linux tras la instalación



Actualizar el sistema es un paso importante tras una nueva instalación. Tiene dos opciones:



##### Opción 1: a través de la interfaz gráfica de usuario (GUI)



Kali, al igual que Debian/Ubuntu, ofrece un gestor gráfico de actualizaciones integrado.



1. Haz clic en el **menú principal** (arriba a la izquierda o abajo, según tu escritorio).


2. Abre **"Software Updater "**.


3. La herramienta :




    - Compruebe los paquetes que deben actualizarse.
    - Verás una lista (con tallas y versiones).
    - Permite lanzar la actualización con un solo clic.


4. Introduzca su contraseña de administrador (`sudo`) cuando se le solicite.


5. Deje que se instale y reinicie si es necesario.



##### Opción 2: A través del terminal



Abra un terminal y ejecute :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



No es aconsejable utilizar la cuenta **root** para el trabajo diario; en su lugar, crea un usuario no root.



En su terminal, escriba estos comandos:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Cierre la sesión y vuelva a iniciarla con el nuevo usuario.



Vamos a resumir algunas tareas básicas de Kali Linux en una tabla.



### Tareas básicas en Kali Linux



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

## Conclusión



Instalar Kali Linux es sólo el primer paso para descubrir este potente entorno dedicado a la ciberseguridad. Dominando las tareas básicas y la gestión del sistema, todo el mundo puede empezar a explorar las herramientas integradas y comprender el funcionamiento interno de un sistema Linux. Kali ofrece una excelente plataforma de aprendizaje, tanto para reforzar los conocimientos técnicos como para desarrollar una auténtica cultura de seguridad informática.