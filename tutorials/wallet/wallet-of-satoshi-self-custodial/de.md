---
name: Wallet of Satoshi - Selbstbehauptung
description: Erfahren Sie, wie Sie den Selbstverwahrungsmodus eines Wallet of Satoshi-Portfolios konfigurieren
---

![cover](assets/cover.webp)



***Nicht deine Schlüssel, nicht deine Münzen* ist mehr als ein Sprichwort, es ist ein grundlegendes Prinzip von Bitcoin, was bedeutet, dass, wenn Sie nicht die Kontrolle über die **privaten Schlüssel** haben, die Ihre Bitcoins aufschließen, Sie sie nicht wirklich besitzen.



Viele Nutzer beginnen in der Regel mit einem **Vertrauens-wallet** und wechseln dann zu einem **Selbst-Vertrauens-wallet**, wo sie ihre privaten Schlüssel selbst kontrollieren.


In diesem Lernprogramm werden wir Ihnen keinen neuen wallet mit Selbstverwaltung vorstellen. Stattdessen werden wir Ihnen eine neue Funktion des ***Wallet of Satoshi*** wallet vorstellen: **den selbstverwaltenden Modus**.



Ziel dieser neuen Integration ist es, dass die Nutzer die Kontrolle über ihre privaten Schlüssel behalten und gleichzeitig von der Einfachheit und einem flüssigen Nutzererlebnis profitieren können.



Bevor wir zum Kern der Sache kommen, wollen wir uns einen Moment Zeit nehmen, um den speziellen Selbstverwahrungsmodus von Wallet of Satoshi (WoS) zu untersuchen.



## Die Besonderheit des Self-Custody-Modus



Durch die Einfachheit und Flüssigkeit des WoS-Selbstverwaltungsmodus entfällt die Komplexität des Öffnens von Lightning-Kanälen, der Verwaltung von Knotenpunkten... Aber wie ist das möglich?



Der Selbstverwahrungsmodus von Wallet of Satoshi wird von **Spark** betrieben. Dies ist eine Layer 2-Lösung für Bitcoin, die von Lightspark unter Verwendung der **Statechains**-Technologie entwickelt wurde.



Sie wickeln also Ihre Transaktionen nicht direkt auf dem Lightning Network ab. Die Interaktionen zwischen dem **LN**-Netzwerk und **Spark** erfolgen über **atomare Swaps**.



Beispiel: Bob möchte eine Lightning-Rechnung mit WoS bezahlen. Er überträgt seine satoshis, aber im Hintergrund werden diese an einen **Spark Service Provider (SSP)** auf Spark weitergeleitet, der wiederum die Zahlung im Lightning-Netzwerk ausführt.



Umgekehrt möchte Alice Mittel direkt aus seinem WoS-Portfolio beziehen. In diesem Fall erhält der **SSP** sats über LN und schreibt es sofort dem Portfolio von Alice gut.



Es ist also wichtig zu wissen, dass Sie von den Spark-Servern abhängig sein müssen, um von der Einfachheit und Flüssigkeit von WoS zu profitieren. Wenn ein SSP jedoch böswillig oder nicht verfügbar ist, steht Ihnen der **unilaterale Exit**-Mechanismus zur Verfügung, eine Sicherheitsmaßnahme, die es Ihnen ermöglicht, Ihre Gelder auf Bitcoin on-chain wiederzuerlangen (auch wenn dies langsam und kostspielig sein kann), und die eine mit einem privaten Lightning-Knoten vergleichbare Selbstverwaltungserfahrung garantiert.



Unter Berücksichtigung all dieser Parameter können Sie dann entscheiden, wie viel sats Sie in Ihrem WoS-Selbstverwahrer aufbewahren möchten.



Wenn Sie neu im Wallet of Satoshi sind, müssen Sie natürlich die mobile Anwendung wallet herunterladen. Wenn Sie diese jedoch bereits nutzen und wissen möchten, wie Sie den **Selbstverwahrungsmodus** nutzen können, gehen Sie bitte direkt zum Abschnitt **Konfiguration des Selbstverwahrungsmodus** in dieser Anleitung.



## Erste Schritte mit Wallet of Satoshi



Gehen Sie zu Ihrem Anwendungsspeicher und laden Sie WoS herunter.



![screen](assets/fr/03.webp)



Öffnen Sie die Anwendung, sobald der Download abgeschlossen ist, und drücken Sie **Start**.



![screen](assets/fr/04.webp)



Sie werden dann zur Hauptschnittstelle der Anwendung weitergeleitet. Wenn Sie zum ersten Mal auf WoS zugreifen, ist das Portfolio bereits funktionsfähig und wird standardmäßig im Verwahrungsmodus geöffnet.



![screen](assets/fr/05.webp)



Auch wenn Sie WoS nicht im Verwahrungsmodus verwenden möchten, empfehlen wir Ihnen, es zunächst zu konfigurieren. Lesen Sie dazu dieses Tutorial.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Kommen wir nun zur Konfiguration unserer WoS in Eigenverantwortung.



## Konfiguration des Selbstverwahrungsmodus



Klicken Sie auf das Hamburger-Menü (3-Balken-Symbol) in der oberen rechten Ecke der Hauptschnittstelle.



![screen](assets/fr/06.webp)



Klicken Sie dann im angezeigten Menü auf das Untermenü **Selbstverwaltung Wallet öffnen**.



![screen](assets/fr/07.webp)



WoS teilt Ihnen sofort mit, dass der *Selbstverwahrungsmodus mit einer Wiederherstellungsphrase einhergeht. Außerdem sind Sie allein für die Sicherheit Ihres Geldes verantwortlich*.



![screen](assets/fr/08.webp)



Kreuzen Sie die Schaltfläche **Ich verstehe**" (1) an, und drücken Sie dann die Schaltfläche **Selbstverwahrung Wallet öffnen** (2), die in leuchtendem Gelb erscheint.



![screen](assets/fr/09.webp)



### Erstellung eines Selbstverwaltungsportfolios



Nachdem Sie auf die Schaltfläche **Selbstverwaltung Wallet öffnen** geklickt haben, klicken Sie auf die Schaltfläche **Neue Wallet erstellen**.



![screen](assets/fr/10.webp)



WoS erstellt dann für Sie ein Selbstverwaltungsportfolio, wiederum innerhalb derselben Anwendung. Sie können jederzeit zwischen dem **Verwahrungsmodus** (in bestimmten Regionen verfügbar) und dem **Selbstverwahrungsmodus** wechseln.



![screen](assets/fr/11.webp)



Nach dem Anlegen werden Sie auf die Hauptschnittstelle des WoS-Selbstdepots weitergeleitet. Sie werden feststellen, dass es keine Unterschiede zwischen der allgemeinen Übersicht und den Schnittstellen eines WoS-Depots und eines WoS-Selbstverwaltungsportfolios gibt.



### Mnemonische Phrase abspeichern



Tippen Sie auf das Symbol **Schlüsselbund + Sicherung Wallet**, das sich oben auf dem Bildschirm zwischen dem Namen des Wallet of Satoshi und dem Hamburger-Menü befindet.



![screen](assets/fr/12.webp)



WoS bietet zwei verschiedene Möglichkeiten zum Speichern Ihrer 12 Wörter (Eselsbrücke): **Sicherung über Google Drive** und **manuelle Sicherung**.



Obwohl wir eine manuelle Sicherung empfehlen, die am sichersten ist, zeigen wir Ihnen auch, wie Sie eine Sicherung über Google Drive durchführen können.



#### Sicherung über Google Drive



Klicken Sie auf die Schaltfläche **Google Drive Backup**.



![screen](assets/fr/13.webp)



Wenn Sie sich für die Sicherung mit Google Drive entscheiden, besteht ein hohes Risiko, dass Ihr Google-Konto kompromittiert wird. Eine böswillige Person hätte Zugriff auf die Datei mit Ihren 12 Wörtern und könnte sich so Zugang zu Ihrem wallet verschaffen.



Das Hinzufügen eines Passworts zur Verschlüsselung der Datei mit den 12 Wörtern ist sicherlich eine gute Möglichkeit, eine zusätzliche Sicherheitsebene zu schaffen.



Aktivieren Sie daher die Schaltfläche **Mit Passwort verschlüsseln** in den erweiterten Optionen.



![screen](assets/fr/14.webp)



Legen Sie auf der neu erscheinenden Oberfläche ein sicheres Passwort fest und bestätigen Sie es erneut.



![screen](assets/fr/15.webp)



Wenn Sie ein Passwort gewählt haben, dürfen Sie es nicht vergessen oder das Medium, auf dem Sie es geschrieben haben, verlieren. Wenn Sie es vergessen oder verlieren, können Sie nie wieder auf Ihre 12 Wörter und damit auf Ihr Geld zugreifen.



Nachdem Sie Ihr Passwort gewählt haben, wählen Sie ein Google-Konto für die Datensicherung aus und gewähren Sie die von WoS geforderten Zugriffsrechte.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Warten Sie ein paar Sekunden. Bingo! Ihr Backup wurde erfolgreich abgeschlossen.



![screen](assets/fr/18.webp)



Sie haben immer die Möglichkeit, eine zusätzliche Sicherung zu erstellen, indem Sie die zweite Sicherungsmethode wählen: die manuelle Sicherung.


#### Manuelle Sicherung



Wenn Sie sich für ein manuelles Backup entscheiden, empfehlen wir Ihnen dringend, dieses Tutorial zu lesen, in dem die besten Methoden für ein sicheres Backup Ihrer mnemonischen Phrase beschrieben werden, damit Sie den Zugriff auf Ihre Bitcoins nicht verlieren.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Drücken Sie die Taste **Manuelle Sicherung**.



![screen](assets/fr/19.webp)



Auf der folgenden Oberfläche weist WoS Sie auf einige Sicherheitsvorkehrungen hin, die Sie beachten sollten, bevor Sie mit der manuellen Sicherung fortfahren.



Aktivieren Sie die Schaltfläche **Ich verstehe** und drücken Sie die Schaltfläche **Weiter**.



![screen](assets/fr/20.webp)



Daraufhin werden Ihnen Ihre 12 Wörter angezeigt. Speichern Sie sie und klicken Sie dann auf die Schaltfläche **Next**.



![screen](assets/fr/21.webp)



Drücken Sie auf dieser neuen Oberfläche die Wörter in der richtigen Reihenfolge.



![screen](assets/fr/22.webp)



Klicken Sie abschließend auf die Schaltfläche **Next**. Herzlichen Glückwunsch! Ihre Sicherung ist nun abgeschlossen.



![screen](assets/fr/23.webp)



## Wiederherstellung des selbstverwahrten Portfolios



Wenn Sie Ihr WoS-Selbstverwahrungs-wallet nach einem Telefonwechsel oder aus einem anderen Grund wiederherstellen möchten, gehen Sie wie folgt vor.



Um das WoS-Portfolio zu öffnen, klicken Sie auf das Hamburger-Menü in der oberen rechten Ecke der Hauptschnittstelle.


Klicken Sie in dem daraufhin angezeigten Menü auf das Untermenü **Selbstverwaltung Wallet öffnen**.


Drücken Sie auf der neuen Oberfläche, die angezeigt wird, die Schaltfläche **Vorhandenes Wallet wiederherstellen**.



![screen](assets/fr/24.webp)



Wählen Sie eine Wiederherstellungsmethode und fahren Sie mit dem nächsten Schritt fort.



![screen](assets/fr/25.webp)



### Wiederherstellung über Google Drive



1. Drücken Sie die Schaltfläche **Wiederherstellen von Google Drive**.


2. Wählen Sie ein Google-Konto und lassen Sie WoS die auf Ihrem Google Drive gespeicherten Wiederherstellungsdaten abrufen.


3. Geben Sie dann Ihr Verschlüsselungspasswort (natürlich nur, wenn Sie es vorher festgelegt haben) aus der Datei mit den 12 Wörtern ein.


4. Warten Sie ein paar Augenblicke, bis die Wiederherstellung wirksam wird, und Sie können wieder auf Ihr Portfolio zugreifen.



### Manuelle Restaurierung



1. Drücken Sie die Taste **Manuell wiederherstellen**.


2. Geben Sie dann die 12 Wörter Ihrer Gedächtnisstütze ein, indem Sie jedes Wort vor seine Anfangszahl schreiben.


3. Warten Sie ein paar Augenblicke, bis die Wiederherstellung wirksam wird, und Sie können wieder auf Ihr Portfolio zugreifen.




### Übertragung von Bitcoins zwischen WoS-Verwahrung und WoS-Selbstverwahrung



Wenn Sie Bitcoins (sats) in Ihrem WoS-Depot wallet haben und ein WoS-Selbstdepot wallet anlegen, verlieren Sie Ihr Geld nicht. Besser noch, Sie können sie in Ihr Selbstverwahrungsportfolio übertragen und umgekehrt.



Um dies zu tun:


Sie können Ihre blitzschnelle WoS-Selbstabholadresse oder eine von Ihnen erstellte Rechnung kopieren.



![screen](assets/fr/26.webp)



Öffnen Sie nun Ihr wallet und drücken Sie die Taste **Envoyer**.



Fügen Sie dann die Adresse oder Rechnung ein. Drücken Sie **Envoyer** ein zweites Mal.



Gehen Sie zurück zu Ihrem Selbstverwahrungsportfolio und Sie werden sehen, dass Sie die Mittel tatsächlich erhalten haben.



![screen](assets/fr/27.webp)



## Senden und Empfangen von Bitcoins



Was das Senden und Empfangen von Bitcoins im Selbstverwahrungsmodus betrifft, so unterscheiden sie sich, wie die allgemeine Übersicht und die Schnittstellen, nicht vom Senden und Empfangen von Bitcoins über einen WoS-Verwahrungs-wallet.



Bitte lesen Sie die grundlegende Anleitung zur Verwendung von Wallet of Satoshi im Plan₿-Netzwerk.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Sie können Wallet of Satoshi jetzt selbst konfigurieren und im Self-Custody-Modus betreiben.



Wenn Sie diese Anleitung nützlich fanden, hinterlassen Sie mir bitte einen grünen Daumen. Herzlichen Dank!