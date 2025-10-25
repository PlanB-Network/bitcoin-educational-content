---
name: Braiins Mini Miner
description: Mining einfach von zu Hause aus herstellen.
---
![cover](assets/cover.webp)



## Einführung



Der Mini Miner braiins BMM 100 ist ein Produkt von Mining pool Braiins. Dieses Gerät hat ein attraktives Design und ist extrem leise. Es erzeugt eine Rechenleistung von 1,1 Th/s und verbraucht etwa 40 Watt. Im Gegensatz zu anderen Geräten ist es nicht quelloffen, aber es ist wirklich einfach zu installieren, es braucht wirklich nur ein paar Klicks! Der Mini Miner BMM 100 ist die erste veröffentlichte Version. Jetzt ist die Version 2 in Produktion, genannt BMM 101, die sich von der ersten Version durch ein größeres Display und das Vorhandensein von Wi-Fi unterscheidet, aber die Installationsverfahren sind die gleichen.



Viele weitere wichtige Informationen finden Sie auch in der vollständigen Anleitung direkt auf der [Herstellerseite] (https://braiins.com/hardware/mini-Miner-bmm-100).



## Überblick über BMM 100



das Gerät sieht aus wie ein Parallelepiped mit einem Display auf der Vorderseite



![image](assets/en/01.webp)



einen Ventilator auf der Oberseite



![image](assets/en/02.webp)



auf der Rückseite befinden sich: die Öffnung für den Stromanschluss, Platz für eine SD-Karte (die für eventuelle Updates benötigt wird), eine kleine Taste mit der Aufschrift "IP REPORT", mit der man die IP Address des Mini-Miner abfragen kann, welche Address für den Zugriff auf das Geräte-Dashboard benötigt wird. Sobald die Taste gedrückt wird, wird die IP Address für etwa 5 Sekunden angezeigt, dann verschwindet sie und der Einstellungsbildschirm wird wieder angezeigt. Wenn Sie jedoch einige Einstellungen ändern müssen, drücken Sie einfach erneut auf die betreffende Taste, und das IP Address erscheint wieder auf dem Bildschirm. Weiter in der Liste finden wir einen Ethernet-Anschluss und einen Zugang zum Zurücksetzen des Geräts, wofür Sie einen Stift ergreifen und 10 Sekunden lang gedrückt halten müssen, um alle Einstellungen des Mini-Miner zurückzusetzen. Schließlich finden wir zwei Kontrollleuchten, eine Green und eine rote, die uns den Status des Miner anzeigen.



![image](assets/en/03.webp)



## Anschließen des Mini Miner



Sie müssen das Gerät über Ethernet mit dem Internet verbinden. Beachten Sie, dass dies bei der neuen Version (BMM 101) nicht mehr notwendig ist. Zurück zu diesem Mini-Miner: Sobald wir den Standort gefunden haben, müssen wir ihn zuerst an die Internetleitung und dann an die Stromversorgung anschließen: Das Gerät schaltet sich automatisch ein und zeigt seine IP Address auf dem Bildschirm an.



## Konfiguration



Wir müssen einen Browser öffnen und die IP Address, die uns den mini Miner zeigt, in die Suchleiste eingeben. Ich erinnere Sie daran, dass Sie, um das Gerät im Netzwerk zu finden, lokal sein müssen, d.h. der Computer, den Sie verwenden, muss mit demselben Netzwerk verbunden sein wie der mini Miner. Sobald wir die IP Address eingegeben haben, drücken wir die Eingabetaste und die Anmeldeseite für das Betriebssystem des mini Miner, Braiins OS, erscheint auf dem Bildschirm.



![image](assets/en/06.webp)



Um sich anzumelden, müssen Sie `root` als Benutzernamen eingeben, während Sie das Passwort leer lassen können. Klicken Sie auf "Anmelden" und Ihr Mini-Miner-Dashboard wird angezeigt.



![image](assets/en/07.webp)



## Allgemeine Einstellungen



Gehen wir zu System



![image](assets/en/24.webp)



in den Einstellungen finden wir einige allgemeine Einstellungen wie Thema (hell oder dunkel), Sprache, Zeitzone und Passwortänderung.



![image](assets/en/25.webp)



Wenn wir stattdessen zu "Mini-Miner-Bildschirm" gehen, haben wir die Einstellungen unseres Mini-Miner, wie z. B. die Bildschirmanzeige. Wir können wählen, ob die Uhrzeit oder der Preis des Bitcoin angezeigt werden soll, oder der Bildschirm mit den Maschinenstatusinformationen wie Produkt Hash, Temperatur, verbrauchte Watt und so weiter. Hier können Sie selbst entscheiden, was Sie auf dem Bildschirm sehen möchten; wir können auch die Helligkeit des Bildschirms ändern, den Nachtmodus einstellen und die Zeit im 12- oder 24-Stunden-Format anzeigen.



![image](assets/en/26.webp)



Wenn Sie die Änderungen vorgenommen haben, klicken Sie auf "Änderungen speichern" und Sie sehen die Änderungen auf dem Bildschirm Ihres Geräts



![image](assets/en/27.webp)



## Anschluss an Mining pool



Jetzt sind wir noch nicht einsatzbereit, denn wir müssen uns mit einem Pool verbinden, um Mining zu starten, also müssen wir zu "Konfiguration" gehen



![image](assets/en/08.webp)



und der erste Eintrag ist einfach `Pools`.



![image](assets/en/09.webp)



Hier müssen wir entscheiden, welchen Pool wir verwenden wollen. In diesem Tutorial werde ich Ihnen zwei Optionen zeigen. Die erste ist, uns mit Mining pool Braiins zu verbinden, der auch von professionellen Minern genutzt wird, wie Sie in diesem Tutorial sehen können:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Die zweite Möglichkeit besteht darin, uns mit einem Mining pool zu verbinden, der im Alleingang mina, wie Public Pool, folgen Sie diesem Leitfaden zu tun:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins Pool



Um sich mit diesem Pool zu verbinden, müssen wir ein Konto erstellen. Dieser Pool macht auch Zahlungen mit Lightning Network, so werden wir in der Lage sein, ein paar Sats pro Tag zu erhalten. Um dies zu tun, müssen wir einen Address Blitz einrichten, auf dem die Belohnungen zu erhalten. Wenn Sie nicht wissen, wie Sie ein Konto bei braiins pool erstellen oder wie Sie Ihren Address Blitz einrichten, können Sie dieser Anleitung folgen:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Sobald dies geschehen ist, befinden wir uns im Dashboard des Braiins-Pools. Wir müssen dem Pool mitteilen, dass wir eine Verbindung mit einem unserer Miner herstellen wollen, daher finden Sie auf der linken Seite des Bildschirms eine Reihe von Einträgen. Wir müssen auf "Arbeiter" gehen



![image](assets/en/04.webp)



und wir müssen auf die violette Schaltfläche auf der rechten Seite klicken, auf der "Arbeiter verbinden" steht



![image](assets/en/05.webp)



Hier erscheint das Fenster mit den Informationen, die wir benötigen, um unseren Mini-Miner an den Pool anzuschließen. Die einzige Änderung, die wir hier vornehmen können, ist die Auswahl von Stratum V2. Um herauszufinden, was Stratum v2 ist, lesen Sie diesen Eintrag im [Glossar] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nun müssen wir diese Zeichenfolge, die mit stratumv2 beginnt, kopieren. Wir klicken also auf das kleine "Kopieren"-Symbol, dann gehen wir zum Dashboard unseres Mini-Miner, das wir in Konfiguration und Pools gelassen hatten. Wir klicken auf "Add new pool



![image](assets/en/11.webp)



und fügen Sie die kopierte Zeichenfolge in das Feld unter Pool URL ein.



![image](assets/en/12.webp)



Jetzt müssen wir den Benutzernamen und das Passwort hinzufügen. Gehen wir zurück zum Pool Dashboad. Darunter haben wir auch eine UserID und ein Passwort. Die userID und unser Benutzername, den wir bei der Erstellung des Kontos angegeben haben, sowie der Name des Miner, den wir eingeben wollen. Sie können entscheiden, ob Sie dem Gerät, das Sie mit dem Pool verbinden, einen Namen geben wollen oder nicht, es ist optional, aber es ist ratsam, ihn einzugeben, damit es einfacher ist, sie sofort zu identifizieren, wenn Sie mehrere Geräte verbinden. Wenn Sie nichts angeben wollen, können Sie `workerName` stehen lassen.



![image](assets/en/13.webp)



Wir gehen dann zu unserem Mini-Miner und geben den Benutzernamen ein. Hier geben wir in meinem Fall "finalstepbitcoin" ein, das ist meine UserID, miniminer Punkt. Dies ist der Name, den ich dem Gerät gegeben habe. Wenn Sie es nicht benennen wollen, schreiben Sie einfach userid dot workername. In meinem Fall wäre es finalstepbitcoin.workername. Sobald Sie den Benutzernamen eingegeben haben, können Sie ein Passwort wählen und es in das leere Feld schreiben. Sie können auch anithing123 eingeben, was auch auf dem Pool-Bildschirm angezeigt wird, aber es soll nur darauf hinweisen, dass Sie jedes beliebige Passwort eingeben können.



Wenn Sie alle Daten eingegeben haben, müssen Sie die Speichertaste auf der rechten Seite drücken (die, die wie eine Diskette geformt ist), und auf diese Weise haben Sie die Pool-Daten im Mini-Miner konfiguriert.



![image](assets/en/14.webp)



Jetzt müssen Sie zurück zum Pool-Dashboard gehen und auf "Verbunden! Zurückgehen"



![image](assets/en/15.webp)



Wir haben unseren Mini-Miner an den Braiins-Pool angeschlossen! Sie können ihn jetzt in der Liste der Arbeiter sehen. Wenn er nicht angezeigt wird, aktualisieren Sie einfach die Liste und warten Sie ein paar Augenblicke. Sobald er erscheint, überprüfen Sie, ob er den Status "OK" mit einem Green-Symbol hat.



![image](assets/en/17.webp)



wenn Sie zurück zum Dashboard gehen, sollten Sie anfangen, Bewegung auf dem Diagramm zu sehen und den Hashrate unseres Geräts zu sehen. Dies bedeutet, dass der Pool unsere Arbeit empfängt und wir daher in jeder Hinsicht unterminiert sind.



![image](assets/en/16.webp)



### Öffentliches Schwimmbad



Über diesen Pool kann man sein Glück versuchen und allein abbauen, indem man sich auf einen Pool stützt. In diesem Fall erhalten wir keine Belohnung, aber wir werden die volle Belohnung erhalten, wenn wir es jemals schaffen, einen Block abzubauen. Wir werden uns dann mit dem öffentlichen Pool verbinden, einem Mining-Pool, der vollständig quelloffen ist. Wir öffnen ein neues Browserfenster und gehen zu [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



es erscheint eine Seite mit allen Informationen, die wir benötigen. Dort kopieren wir dann die Schicht Address



![image](assets/en/19.webp)



dann kehren wir zum Dashboard unseres Mini-Miner zurück, gehen zur Konfiguration und zu den Pools, klicken auf "Add new pool" (derselbe Prozess wie oben) und fügen das "stratum Address" unter pool url ein.



![image](assets/en/20.webp)



Gehen wir nun zurück zur Pool-Seite und sehen wir, dass wir als Benutzernamen einen Bitcoin Address eingeben müssen, der derjenige sein wird, bei dem wir die Belohnung erhalten, falls wir eine Sperre unterlaufen, dann einen Punkt und dann den Namen unseres Geräts, wie wir es zuvor mit Braiins Pool gemacht haben, während wir das Passwort selbst wählen können.



![image](assets/en/21.webp)



Wir gehen zurück zum Mini-Miner und fügen unter username ein Address Bitcoin ein, gefolgt von einem Punkt und dem Namen, ich werde `miniminer` eingeben. In das Passwort füge ich stattdessen test ein, Sie geben ein, was Sie wollen.



![image](assets/en/22.webp)



Jetzt speichern wir die Einstellungen und deaktivieren den Braiins-Pool.



![image](assets/en/23.webp)



Gut! Wir sind jetzt Mining im öffentlichen Schwimmbad!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)