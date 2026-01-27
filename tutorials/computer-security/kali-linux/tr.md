---
name: Kali
description: Kali Linux'u VirtualBox'a, önyüklenebilir bir USB belleğe veya çift önyükleme olarak adım adım kurmak.
---

![cover-kali](assets/cover.webp)



## Giriş



### Neden Kali Linux?



**Kali Linux** BT güvenliği konusunda uzmanlaşmış bir Linux dağıtımıdır.


İşte neden Kali Linux kullandığımız:





- Çok çeşitli pentesting araçları (sistem ve ağ güvenlik testleri) ile önceden yapılandırılmıştır.
- Açık kaynak kodlu ve ücretsizdir**, bu nedenle özgürce kullanabilir ve değiştirebilirsiniz.
- Güvenilir ve güvenlidir**, siber güvenlik hakkında bilgi edinmek için idealdir.
- Linux'u teste hazır bir ortamda nasıl kullanacağınızı öğrenmenizi sağlar.
- Farklı şekillerde kurulabilir: **VirtualBox**, **bootable USB key** veya **dual boot**.



## Kurulum ve yapılandırma



### 1. Ön Koşullar



**Gerekli ekipman:**





- 64 bit işlemci** (Intel veya AMD).
- minimum 8 GB RAM** (hafif bir kurulum veya sanal makine için 4 GB yeterli olabilir).
- kali Linux'u kurmak için 50 GB boş disk alanı**.
- ISO görüntüsünü ve güncellemeleri indirmek için internet bağlantısı**.
- Önyüklenebilir medya oluşturmak için en az 8 GB USB anahtarı** (Kali'yi bir PC'ye yüklemek veya Canlı USB'de test etmek istiyorsanız).



Mevcut bir bilgisayara yüklemeden önce verilerinizi yedeklemeniz önemlidir.



### 2. İndir





- Kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms) adresine gidin
- Uygulamanız için ISO görüntüsünü seçin:
  - Kurulum Görüntüsü** : PC kurulumu için.
  - Sanal Görüntü**: Kali'yi VirtualBox veya VMware üzerine kurmak için.
- ISO görüntüsünü indirin.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Önyüklenebilir bir USB anahtarı oluşturma



Balena Etcher gibi çeşitli araçlar kullanabilirsiniz:





- Balena Etcher](https://etcher.balena.io/) dosyasını indirin ve yükleyin.



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Balena Etcher'ı açın, ardından Kali ISO görüntüsünü seçin.
- Hedef ortam olarak USB anahtarını seçin.
- Flash'a tıklayın ve işlemin bitmesini bekleyin.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kali Linux'u kurma ve güvenliğini sağlama



#### 4.1 USB anahtarında önyükleme





- Bilgisayarı kapatın.
- USB anahtarını (Kali Linux içeren) takın.
- Bilgisayarınızı açın. Yeni bilgisayarlarda, sistem USB önyükleme anahtarını otomatik olarak tanımalıdır. Durum böyle değilse, BIOS/UEFI erişim tuşunu (markaya bağlı olarak genellikle F2, F12 veya Delete) basılı tutarak yeniden başlatın.
  - BIOS/UEFI menüsünde, önyükleme aygıtı olarak USB anahtarınızı seçin.
  - Kaydedin ve yeniden başlatın.



#### 4.2 Kurulumun başlatılması



##### Başlangıç ekranı



USB bellekten önyükleme yaparken, Kali Linux önyükleme ekranı görünmelidir. Grafiksel kurulum** ve **metin kurulumu** arasında seçim yapın. Bu örnekte, biz grafiksel kurulumu seçtik.



![capture](assets/fr/06.webp)



Eğer **Live** imajını kullanırsanız, varsayılan başlangıç seçeneği olan **Live** modunu da göreceksiniz.



![Mode Live](assets/fr/07.webp)



##### Dil seçimi



Kurulum ve sistem için tercih ettiğiniz dili seçin.



![Sélection de la langue](assets/fr/08.webp)



Lütfen coğrafi konumunuzu belirtiniz.



![Options d'accessibilité](assets/fr/09.webp)



##### Klavye yapılandırması



Klavye düzeninizi seçin. Tuşların yapılandırmanıza uygun olup olmadığını kontrol etmek için bir test alanı mevcuttur.



![Configuration du clavier](assets/fr/10.webp)



##### Ağ bağlantısı



Kurulum şimdi ağ arayüzlerinizi tarayacak, bir DHCP hizmeti arayacak ve ardından sisteminiz için bir ana bilgisayar adı girmenizi isteyecektir. Aşağıdaki örnekte, ana bilgisayar adı olarak **"kali "** girdik.



![Configuration réseau](assets/fr/11.webp)



İsteğe bağlı olarak bu sistemin kullanacağı varsayılan bir etki alanı adı sağlayabilirsiniz (değerler DHCP'den veya önceden var olan bir işletim sistemi varsa alınabilir).



![Choix du type d'installation](assets/fr/12.webp)



##### Kullanıcı hesapları



Ardından, sistem için kullanıcı hesabı oluşturun (tam ad, kullanıcı adı ve güçlü bir parola).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Saat dilimi



Sistem saatini ayarlamak için coğrafi bölgenizi seçin.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Bölümleme türü



Yükleyici daha sonra disklerinizi tarar ve yapılandırmanıza bağlı olarak çeşitli seçenekler görüntüler.



Bu kılavuzda, **dört olası seçenek** sunan bir **boş diskten** başlıyoruz.


Burada tek seferlik bir Kali Linux kurulumu (tek önyükleme) gerçekleştirdiğimiz için **Güdümlü - tüm diski kullan** seçeneğini seçeceğiz. Bu, başka hiçbir işletim sisteminin tutulmayacağı ve tüm diskin silinebileceği anlamına gelir.



Diskiniz zaten veri içeriyorsa, **Güdümlü - en büyük bitişik boş alanı kullan** ek seçeneği görüntülenebilir.



Bu alternatif, Kali Linux'u mevcut verileri silmeden kurmanıza olanak tanır ve başka bir sistemle çift önyükleme yapmak için idealdir.



Bizim durumumuzda disk boş olduğundan bu seçenek görünmez.



![Choix du partitionnement](assets/fr/17.webp)



Bölümlenecek diski seçin.



![capture](assets/fr/18.webp)



İhtiyaçlarınıza bağlı olarak, tüm dosyalarınızı tek bir bölümde tutmayı (varsayılan davranış) veya bir veya daha fazla üst düzey dizin için ayrı bölümlere sahip olmayı seçebilirsiniz.



Ne istediğinizden emin değilseniz, **Tüm dosyalar tek bir bölümde** seçeneğini seçin.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Daha sonra, kurulum programı geri dönüşü olmayan değişiklikler yapmadan önce disk yapılandırmanızı kontrol etmek için son bir fırsatınız olacaktır. Devam_ butonuna tıkladığınızda kurulum programı başlayacak ve kurulum neredeyse tamamlanmış olacaktır.



![capture](assets/fr/21.webp)



##### Şifrelenmiş LVM



Bu seçenek bir önceki adımda etkinleştirildiyse, Kali Linux artık sizden bir LVM parolası istemeden önce güvenli bir sabit disk silme işlemi gerçekleştirecektir.



Lütfen güçlü bir parola kullanın, aksi takdirde zayıf bir passphrase ile ilgili bir uyarı görüntülenecektir.



##### Proxy bilgileri



Kali Linux uygulamaları dağıtmak için depoları kullanır. Ortamınız bir proxy kullanıyorsa gerekli proxy bilgilerini girmeniz gerekecektir.



Proxy kullanıp kullanmayacağınızdan **emin değilseniz**, **boş bırakın**. Yanlış bilgi girilmesi depolara bağlantıyı engelleyecektir.



![capture](assets/fr/22.webp)



##### Metapetler



Ağ erişimi yapılandırılmamışsa, istendiğinde **daha fazla yapılandırma** yapmanız gerekecektir.



Eğer **Canlı** görüntüyü kullanıyorsanız, bir sonraki adım görüntülenmeyecektir.



Daha sonra yüklemek istediğiniz [metapackages](https://www.kali.org/docs/general-use/metapackages/)'ı seçebilirsiniz. Varsayılan seçenekler standart bir Kali Linux sistemi kuracaktır, bu nedenle herhangi bir değişiklik yapmanız gerekmeyecektir.



![capture](assets/fr/23.webp)



#### Başlangıç bilgileri



Ardından GRUB önyükleme yükleyicisinin kurulumunu onaylayın.



![capture](assets/fr/24.webp)



##### Yeniden Başlat



Son olarak, yeni Kali Linux kurulumunuzu yeniden başlatmak için Devam'a tıklayın.



![capture](assets/fr/25.webp)



#### 4.3 Kurulumdan sonra Kali Linux'un güncellenmesi ve yapılandırılması



Yeni bir kurulumdan sonra sisteminizi güncellemek önemli bir adımdır. İki seçeneğiniz vardır:



##### Seçenek 1: Grafik kullanıcı arayüzü (GUI) aracılığıyla



Kali, Debian/Ubuntu gibi, entegre bir grafik güncelleme yöneticisi sunar.



1. Ana menüye** tıklayın (masaüstünüze bağlı olarak sol üst veya alt).


2. "Yazılım Güncelleyici "yi** açın.


3. Araç, :




    - Güncellenecek paketleri kontrol edin.
    - Bir liste göreceksiniz (boyutlar ve sürümlerle birlikte).
    - Güncellemeyi tek bir tıklama ile başlatmanızı sağlar.


4. İstendiğinde yönetici parolanızı (`sudo`) girin.


5. Gerekirse yüklemesine ve yeniden başlatmasına izin verin.



##### Seçenek 2: Terminal üzerinden



Bir terminal açın ve çalıştırın :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Günlük işler için **root** hesabının kullanılması tavsiye edilmez; bunun yerine root olmayan bir kullanıcı oluşturun.



Terminalinizde bu komutları yazın:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Oturumu kapatın ve yeni kullanıcıyla tekrar oturum açın.



Bazı temel Kali Linux görevlerini bir tabloda özetleyelim.



### Kali Linux altında temel görevler



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

## Sonuç



Kali Linux'u kurmak, siber güvenliğe adanmış bu güçlü ortamı keşfetmenin sadece ilk adımıdır. Temel görevlerde ve sistem yönetiminde ustalaşarak, herkes yerleşik araçları keşfetmeye ve bir Linux sisteminin iç işleyişini anlamaya başlayabilir. Kali, hem teknik becerileri güçlendirmek hem de gerçek bir BT güvenliği kültürü geliştirmek için mükemmel bir öğrenme platformu sunar.