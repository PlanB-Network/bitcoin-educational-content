---
name: Electrum Airgap
description: Ein erster Schritt zur Sicherheit, ein Cold Wallet mit Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



In diesem Tutorial erkläre ich Ihnen, wie Sie Ihr erstes Airgap-Signiergerät erstellen können, das nicht mit dem Internet verbunden ist, auch wenn Sie keinen eigenen Hardware Wallet haben. Alles, was Sie brauchen, ist, dass Sie zwei Computer zur Verfügung haben:




- ein altes Gerät für immer daran zu hindern, sich mit dem Internet zu verbinden;
- ihren Computer für den täglichen Gebrauch.



Diese Konfiguration bietet ein höheres Maß an Sicherheit als das klassische "Hot Wallet": Der alte Computer - ohne Netzverbindung - ist der Hüter Ihrer privaten Schlüssel, die niemals im Internet veröffentlicht, sondern offline gespeichert werden ("airgap" oder "Cold").



Stattdessen installieren Sie ein Wallet-Display ("watch-only") auf Ihrem täglichen Computer, das mit dem Netzwerk verbunden ist und mit dem Sie z. B. Salden prüfen und Quittungstransaktionen vorbereiten können.



## Wallet-Luftspalt: Was und wie



Indem wir die Schritte in dieser Anleitung ausführen, werden wir zwei Software Wallet Electrum auf zwei verschiedenen Computern installieren und schließlich zwei Wallets mit unterschiedlichen Schlüsselspeichern erstellen: der Wallet airgap wird die gesamte Hierarchie des Wallet HD verwenden, während der Wallet display mit dem öffentlichen Hauptschlüssel generiert wird.



Diese beiden Geldbörsen werden sich in jeder Hinsicht stark voneinander unterscheiden. Das Einzige, was sie gemeinsam haben, sind die Adressen, wie wir sehen werden:




- gW-13 auf dem airgap-Computer kann nur unterschreiben, kennt aber, da er vom Netz getrennt ist, die verwendete Waage und die Adressen nicht;
- der Wallet auf dem Tagesrechner kann in Ermangelung der privaten Schlüssel nur Transaktionen vorbereiten und weiterleiten, ohne über die Ausgaben verfügen zu können.



## Vorläufige Vorbereitung



Um Electrum herunterzuladen, empfehle ich dir, die ersten Schritte in diesem Tutorial zu befolgen:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Überprüfen Sie nach dem Herunterladen immer die Version, bevor Sie sie installieren, und fahren Sie dann mit der "One Server"-Konfiguration fort, die Sie in der Hilfe unter `Start with a Dummy Wallet` finden.



Der Konfigurationsvorgang "Ein Server" ist nur für den Wallet erforderlich, der auf dem täglichen Computer installiert ist, da der andere Computer immer offline sein wird.



Bei den folgenden Vorgängen geht es darum, auf zwei verschiedenen Computern (und Geldbörsen) zu üben. Aus Gründen der Bequemlichkeit und der Konzentration habe ich mich daher dafür entschieden, den Wallet airgap mit dem hellen Thema einzustellen, während das Wallet-Display das dunkle Thema hat.



## Wallet Luftspaltbildung



Nach dem Herunterladen und Überprüfen des Downloads von Electrum, nehmen Sie eine Kopie der ausführbaren Datei und bringen Sie sie offline auf Ihren Computer. Starten Sie sie dann und installieren Sie Electrum.



Doppelklicken Sie, um Electrum zu starten: Der Computer, auf dem Sie dieses Wallet verwenden werden, ist offline. Ignorieren Sie die Netzwerkeinstellungen und gehen Sie zur Erstellung des Wallet, das wir in diesem Leitfaden "Airgap" nennen.



![image](assets/en/01.webp)



Wählen Sie _Standard Brieftasche_.



![image](assets/en/02.webp)



Wählen Sie dann _Neues Saatgut erstellen_, damit die Software generate das Mnemonic verwendet.



![image](assets/en/03.webp)



Transkribieren Sie die 12 generate-Wörter aus Electrum genau auf eine Papierunterlage und fahren Sie mit dem Verifizierungsschritt fort, indem Sie die Wörter erneut in der richtigen Reihenfolge eingeben, wenn Electrum dies verlangt.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Nachdem die Erstellung des Wallet abgeschlossen ist, legen Sie ein komplexes Passwort (`Strong`) fest, um die Wallet-Datei auf dem Airgap-Gerät zu verschlüsseln. Dieser Schritt ist sehr heikel und wichtig, da das jetzt gewählte Passwort den Zugriff auf das Wallet verhindert, das Verfügungsgewalt hat und in der Lage ist, Geld auszugeben und Transaktionen zu unterzeichnen.



![image](assets/en/06.webp)



Mit einem Klick auf _Finish_ ist der Wallet definiert und erscheint auf dem Bildschirm. Natürlich ist die Netzwerkverbindungsanzeige, d.h. der farbige Punkt in der unteren rechten Ecke, rot, da der Computer nicht verbunden ist und es dem Wallet nicht erlaubt, die Online-Tasten freizugeben.



![image](assets/en/07.webp)



## Erstellung Wallet der Visualisierung



Jetzt, da Ihr Wallet über private Offline-Schlüssel verfügt, müssen Sie einen Anzeige-Wallet oder einen "Nur-Uhr"-Wallet einrichten, der es Ihnen ermöglicht, den Kontostand anzuzeigen und Quittungstransaktionen vorzubereiten, um weiterhin sicher Sats zu sammeln.



Wählen Sie auf dem Wallet, das sich auf dem Offline-Gerät befindet, das Menü _Wallet_ -> _Information_



![image](assets/en/08.webp)



Es erscheint ein Fenster mit allen Informationen zu Ihrem Wallet, in dem Sie "Ableitungspfad" und "Master-Fingerabdruck" ankreuzen können, um sie beispielsweise neben den Wörtern im Mnemonic-Satz zu markieren (dringend empfohlen).



![image](assets/en/09.webp)



Denken Sie daran, dass Sie diese Daten von einem nicht angeschlossenen Computer abrufen, also müssen Sie die "zpub" in eine Textdatei kopieren und auf einem USB-Stick speichern.



Jetzt kannst du zu dem mit dem Internet verbundenen Computer gehen, Electrum starten und einen neuen Wallet erstellen.



Wählen Sie im Menü _Datei_ die Option _Neu/Wiederherstellen_.



![image](assets/en/10.webp)



Der neue Wallet kann nur angesehen werden, daher nennen wir ihn in diesem Leitfaden "nur beobachten".



![image](assets/en/12.webp)



Wählen Sie auf dem nächsten Bildschirm _Standard Brieftasche_ und klicken Sie auf _Weiter_.



![image](assets/en/13.webp)



Achten Sie bei der Auswahl des "Schlüsselspeichers" darauf, dass Sie zur Erstellung der Anzeige Wallet die Option _Hauptschlüssel verwenden_ wählen. Fahren Sie dann mit _Weiter_ fort.



![image](assets/en/14.webp)



Fügen Sie hier das vom Wallet offline kopierte `zpub` ein, das Sie über ein USB-Medium auf diesen Computer gebracht haben.



![image](assets/en/15.webp)



Legen Sie abschließend auch für diesen Wallet ein sicheres Passwort fest, das sich möglicherweise von dem für den entsprechenden Cold unterscheidet.



Es erscheint die Anzeige Wallet mit einer Warnung. Die Meldung erinnert Sie daran, dass es sich um ein reines Anzeige-Wallet handelt und dass Sie damit nicht die zugehörigen Mittel ausgeben können.



**Nebenbei**: **Sie müssen also immer im Besitz der privaten Schlüssel sein, um über die UTXOs dieses Wallet zu verfügen**. Mit einem guten Backup-System wird es für Sie nicht schwierig sein, im vollen Besitz Ihrer Bitcoins zu bleiben.



![image](assets/en/16.webp)



Diese Warnung wird jedes Mal angezeigt, wenn Sie dieses Wallet öffnen. Klicken Sie auf _Ok_ und fahren Sie mit dem Verifizierungsschritt fort.



## Überprüfung der beiden Wallet



Wie wir zu Beginn dieses Leitfadens gelernt haben, sind ein Wallet Airgap und sein Display Wallet zwei Portfolios, die unterschiedliche Fähigkeiten haben, aber **die gleichen Adressen**.



Wenn wir die beiden Wallets nebeneinander betrachten, stellen wir fest, dass in der Wallet-Luftspalte ein "seed"-Symbol zu sehen ist, während es in der reinen Uhr nicht zu sehen ist. Auch dieses Detail wird Ihnen helfen, sich daran zu erinnern, dass das Wallet-Display Wallet keine privaten Schlüssel hat.



![image](assets/en/17.webp)



Für eine genaue erste Überprüfung wählen Sie jedoch in beiden Brieftaschen das Menü "Adressen": Da sie dieselben Adressen haben, sollte die Liste der Adressen bei beiden identisch sein.



![image](assets/en/18.webp)



⚠️ **ACHTUNG**: **Es kann keinen Mittelweg geben; die Adressen müssen übereinstimmen. Wenn sie unterschiedlich sind, muss die gesamte bisherige Arbeit gelöscht und von vorne begonnen werden**.



Nun können Sie zwei verschiedene Prüfungen durchführen. Versuchen Sie zunächst, die beiden Brieftaschen zu löschen und sie auf dem entsprechenden Computer von Grund auf wiederherzustellen. Falls Sie diese Überprüfung durchführen, sind die Verfahren für die Anzeige Wallet identisch mit den oben beschriebenen.



Für den Wallet-Luftspalt müssen Sie jedoch auf dem Bildschirm "Keystore" die Option _Ich habe bereits ein Saatgut_ wählen und die Wörter eingeben, indem Sie sie von Ihrer Papiersicherung kopieren.



Nach Ablauf der Probezeit können Sie versuchen, einen kleinen Betrag zu überweisen und ihn sofort auszugeben.



## Einnahme- und Ausgabetransaktionen



Um mit der Nutzung Ihres Electrum-Airgaps zu beginnen, können Sie eine Quittungstransaktion mit einem kleinen Betrag durchführen und diesen dann für ein eigenes Address ausgeben. Sie können sich dann mit dem Verfahren vertraut machen und sicherstellen, dass Sie die volle Kontrolle über das Geld haben.



**Hinweis**: Ich empfehle Ihnen nicht, einen größeren Geldbetrag auf Wallet einzuzahlen, bevor Sie sich sicher sind, dass Sie alle Vorgänge reibungslos durchführen können.



Die im Folgenden beschriebenen Schritte mögen auf den ersten Blick kompliziert erscheinen. Lassen Sie sich davon nicht entmutigen: Wenn Sie sie zum ersten Mal ausprobiert haben, werden Sie feststellen, dass sie nur wenige Minuten in Anspruch nehmen.



Um Gelder zu erhalten, müssen Sie unbedingt die Anzeige Wallet auf Ihrem Computer mit dem Internet verbunden befindet verwenden. Klicken Sie im Menü `Empfangen` auf _Anfrage erstellen_, um Electrum generate das erste verfügbare Address zu haben und es zu benutzen, um uns ein paar Satss zu schicken.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Sobald die Transaktion übertragen wurde, können Sie bereits sehen, dass sie - wie selbstverständlich - nur auf dem Display Wallet und nicht auf dem Wallet airgap sichtbar ist.



![image](assets/en/21.webp)



Nachdem Ihre Transaktion eine Bestätigung erhalten hat, können Sie die Ausgabe vorbereiten und so das Unterschriftsverfahren vom Wallet außerhalb des Netzes ausprobieren. Bereiten Sie dann die Transaktion auf der Nur-Überwachung vor und drücken Sie auf _Vorschau_, um sie zu prüfen



![image](assets/en/22.webp)



Sie erhalten das erweiterte Transaktionsfenster, in dem Sie das sehen können:




- die Transaktion ist nicht signiert (`Status: Unsigned);
- die Befehle `Sign` und `Broadcast` sind gesperrt.



Das Einzige, was Sie tun können, ist, den Vorgang so zu exportieren, wie er ist, ihn zum Wallet-Luftspalt zu bringen und zu unterschreiben.



Schließen Sie ein USB-Flash-Laufwerk an Ihren Computer an und wählen Sie im Menü unten links _Freigeben_.



![image](assets/en/23.webp)



Wählen Sie dann _Speichern in Datei_.



![image](assets/en/24.webp)



Speichern Sie die Transaktion auf dem USB-Stick.



Sie werden feststellen, dass Electrum der Datei einen Namen gibt, der die ersten Ziffern von transaction ID trägt, und die Dateierweiterung ist `.PSBT`, was `Partially Signed Bitcoin Transaction` bedeutet.



Entpacken Sie den Datenträger mit der Datei `.PSBT` und schließen Sie ihn offline an den Computer an.



Wählen Sie nun im Wallet airgap das Menü _Tools_, dann _Load transaction_ und anschließend From file_.



![image](assets/en/25.webp)



Wählen Sie mit dem Dateimanager die Datei `.PSBT` aus.



![image](assets/en/29.webp)



Die netzferne Computersoftware öffnet automatisch das erweiterte Transaktionsfenster, das völlig identisch ist mit dem, das Sie auf dem Wallet-Display sehen. Der Status ist "Unsigned", aber der Unterschied ist, dass der Befehl "Sign" hier aktiv ist. Und das ist genau das, was Sie ausführen müssen.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Da die Transaktion nun signiert ist, sollten Sie daran denken, dass sich Ihr Wallet auf einem Offline-Rechner befindet. Selbst wenn der Befehl "Broadcast" aktiv ist, kann Ihr Wallet die Transaktion nicht an das Bitcoin-Netzwerk weiterleiten.



Nun müssen Sie den Vorgang des Exports der signierten Transaktion auf den USB-Stick wiederholen, damit Sie sie auf einen mit dem Internet verbundenen Computer importieren und weitergeben können.



Wählen Sie im Menü unten links erneut _Freigeben_ und dann _Als Datei speichern_.



![image](assets/en/28.webp)



Jetzt hat die Datei eine andere Erweiterung: **Anstatt `.PSBT` hat die Transaktion jetzt die Erweiterung `.txn`. Von nun an wird Electrum Sie signierte Transaktionen von unsignierten unterscheiden lassen**.



![image](assets/en/30.webp)



Für die endgültige Übertragung der Transaktion nehmen Sie den USB-Stick aus dem Offline-Computer und stecken ihn in den mit dem Internet verbundenen Computer.



Wiederholen Sie in der Einzelüberwachung den Importvorgang, d. h. wählen Sie im Menü _Tools_ die Option _Transaktion laden_ und schließlich _Aus Datei_.



![image](assets/en/31.webp)



Electrum öffnet das Transaktionsfenster für Sie, das sich deutlich von dem zuvor auf diesem Wallet gezeigten unterscheidet, da es jetzt signiert ist (`Status: Signed`) und der Befehl `Broadcast` zugänglich ist.



Die letzte Operation, die Sie durchführen müssen, ist genau das:



![image](assets/en/32.webp)



## Schlussfolgerungen



Ihre Tests sind nun abgeschlossen. Wenn Sie der Anleitung gefolgt sind und die gleichen Ergebnisse erhalten haben, haben Sie einen Wallet Cold mit Electrum auf zwei verschiedenen Computern erstellt, den Sie im Airgap-Modus verwenden können, um Ihre Bitcoins zu speichern.



Es gibt nur zwei Dinge, auf die Sie besonders achten müssen:


1) **Niemals Wallet Airgap an generate Empfangsadressen verwenden**. Da er offline ist, wird er Ihnen immer den ersten Address anbieten, der mit dem übereinstimmt, den Sie gerade für die Testtransaktion verwendet haben;



![image](assets/en/33.webp)



wie Sie aus dem Bild oben ersehen können, kennt der Offline-Wallet seine eigene Address-Geschichte nicht. Er ist in dieser Hinsicht völlig blind. **Die einzige Aufgabe, die er für Sie übernehmen kann, ist das Speichern Ihrer Offline-Schlüssel und das Signieren Ihrer Transaktionen.**



2) Verwenden Sie ein USB-Flash-Laufwerk, das nur für diesen Zweck bestimmt ist, **nicht ein Medium, das Sie häufig benutzen**. Alltägliche Hilfsmittel sind anfälliger für Cyberangriffe, und ungewollt könnten Sie sogar den Computer angreifen, den Sie vom Netz getrennt halten. Ein USB-Stick, den Sie nur zu diesem Zweck verwenden, hat nur sehr wenige Möglichkeiten, mit Ihrem PC online in Kontakt zu treten, vor allem, wenn Sie ein Hodler sind, der nicht viel ausgeben muss, wodurch die Wahrscheinlichkeit des Empfangs und der anschließenden Übertragung von Viren, Malware usw. verringert wird.