---
name: Ashigaru - Stonewall x2
description: Stonewall x2-Transaktionen auf Ashigaru verstehen und nutzen
---
![cover stonewall x2](assets/cover.webp)



> *Jede Ausgabe zu einem Coinjoin machen

## Was ist eine Stonewall x2-Transaktion?



Stonewall x2 ist eine spezielle Form der Bitcoin-Transaktion, die darauf abzielt, die Vertraulichkeit der Ausgaben der Nutzer zu erhöhen, indem sie mit einer dritten Partei zusammenarbeitet, die nicht an den Ausgaben beteiligt ist. Diese Methode simuliert einen Mini-Coinjoin zwischen zwei Teilnehmern, während eine Zahlung an eine dritte Partei erfolgt. Stonewall x2-Transaktionen sind in der Ashigaru-Anwendung verfügbar, einem fork von Samourai Wallet (dem Team, das diese Art von Transaktion entwickelt hat).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Die Funktionsweise ist relativ einfach: Sie verwenden ein UTXO in Ihrem Besitz, um die Zahlung vorzunehmen, und nehmen die Hilfe eines Dritten in Anspruch, der ebenfalls mit einem UTXO beiträgt. Die Transaktion endet mit vier Ausgaben: zwei davon in gleicher Höhe, eine für die Adresse des Zahlungsempfängers, die andere für eine Adresse des Mitarbeiters. Ein drittes UTXO wird an eine andere Adresse des Mitarbeiters zurückgeschickt, damit er den ursprünglichen Betrag zurückerhalten kann (eine für ihn neutrale Aktion, modulo der mining-Kosten), und ein letztes UTXO geht an eine Adresse, die uns gehört, was den Zahlungsaustausch darstellt.



Bei Stonewall x2-Transaktionen werden also drei verschiedene Rollen definiert:




- Der Emittent, der die eigentliche Zahlung vornimmt;
- Der Kollaborateur, der Bitcoins zur Verfügung stellt, um die Anonymität der Transaktion zu verbessern, während er am Ende seine Gelder in voller Höhe zurückerhält (eine für ihn neutrale Aktion, modulo der mining-Kosten);
- Der Empfänger, der möglicherweise nicht weiß, worum es sich bei der Transaktion handelt, und einfach eine Zahlung vom Absender erwartet.



Nehmen wir ein Beispiel. Alice ist beim Bäcker, um ihr Baguette zu kaufen, das 4.000 sats" kostet. Sie möchte mit Bitcoins bezahlen, wobei sie eine gewisse Vertraulichkeit über ihre Zahlung wahren möchte. Also wendet sie sich an ihren Freund Bob, der ihr dabei helfen wird.



![image](assets/fr/01.webp)



Die Analyse dieser Transaktion zeigt, dass der Bäcker tatsächlich 4.000 sats` als Bezahlung für das Baguette erhalten hat. Alice verbrauchte 10.000 sats" als Input und erhielt 6.000 sats" als Output, was einen Nettosaldo von 4.000 sats" ergibt, was dem Preis des Baguettes entspricht. Bob lieferte 15.000 sats" als Input und erhielt zwei Outputs: einen von 4.000 sats" und einen von 11.000 sats", was einen Saldo von 0" ergibt.



In diesem Beispiel habe ich die mining-Gebühren absichtlich vernachlässigt, um es leichter verständlich zu machen. In Wirklichkeit werden die Transaktionsgebühren zu gleichen Teilen zwischen dem Zahlungsaussteller und dem Kooperationspartner aufgeteilt.



## Was ist der Unterschied zwischen Stonewall und Stonewall x2?



Eine StonewallX2-Transaktion funktioniert genauso wie eine Stonewall-Transaktion, mit dem Unterschied, dass erstere kollaborativ ist, während letztere nicht kollaborativ ist. Wie wir gesehen haben, ist an einer Stonewall x2-Transaktion eine dritte Partei beteiligt, die nicht an der Zahlung beteiligt ist und die ihre Bitcoins zur Verfügung stellt, um die Vertraulichkeit der Transaktion zu erhöhen. Bei einer klassischen Stonewall-Transaktion übernimmt der Absender die Rolle des Kollaborateurs.



Kehren wir zu unserem Beispiel von Alice in der Bäckerei zurück. Wenn sie nicht in der Lage gewesen wäre, jemanden wie Bob zu finden, der sie auf ihrem Kaufrausch begleitet, hätte sie einen Stonewall alleine machen können. Auf diese Weise wären die beiden UTXOs auf dem Hinweg ihr zugestanden, und sie hätte auf dem Rückweg 3 aufgesammelt.



![image](assets/fr/02.webp)




Aus der Sicht eines Außenstehenden wäre der Vorgang derselbe geblieben.



![image](assets/fr/05.webp)



Die Logik sollte daher wie folgt aussehen, wenn Sie ein Ashigaru-Ausgabewerkzeug verwenden möchten:




- Wenn der Händler Payjoin Stowaway nicht unterstützt, können Sie eine kollaborative Transaktion mit einer anderen Person außerhalb der Zahlung dank Stonewall x2 machen;
- Wenn Sie niemanden finden, der eine Stonewall x2-Transaktion durchführt, können Sie eine reine Stonewall-Transaktion durchführen, die das Verhalten einer Stonewall x2-Transaktion nachahmt.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Was ist der Sinn einer Stonewall x2-Transaktion?



Die Stonewall x2-Struktur fügt der Transaktion eine enorme Menge an Entropie hinzu, was die Kettenanalyse verwirrt. Von außen betrachtet, könnte eine solche Transaktion als kleiner Coinjoin zwischen zwei Personen interpretiert werden. In Wirklichkeit handelt es sich aber um eine Zahlung. Diese Methode führt daher zu Unsicherheiten in der Kettenanalyse oder sogar zu falschen Hinweisen.



Nehmen wir das Beispiel von Alice, Bob und dem Boulanger. Die Transaktion auf der Blockchain würde wie folgt aussehen:



![image](assets/fr/03.webp)



Ein außenstehender Beobachter, der sich auf die üblichen Heuristiken der Kettenanalyse verlässt, könnte fälschlicherweise zu dem Schluss kommen: "*Alice und Bob haben einen kleinen Coinjoin gemacht, mit je einem UTXO in und zwei UTXOs out*".



![image](assets/fr/04.webp)



Diese Interpretation ist falsch, denn wie Sie wissen, wurde ein UTXO an den Boulanger geschickt, der Alice hat nur einen Austauschausgang und der Bob hat zwei.



![image](assets/fr/01.webp)



Selbst wenn es dem außenstehenden Beobachter gelingt, den Vater der Stonewall x2-Transaktion zu identifizieren, wird er nicht über alle Informationen verfügen. Er wird nicht in der Lage sein, festzustellen, welcher der beiden UTXOs mit den gleichen Beträgen der Zahlung entspricht. Er wird auch nicht feststellen können, ob Alice oder Bob die Zahlung getätigt hat. Schließlich wird er nicht feststellen können, ob die beiden eingegebenen UTXO von zwei verschiedenen Personen stammen oder ob sie einer einzigen Person gehören, die sie zusammengelegt hat. Dieser letzte Punkt ergibt sich aus der Tatsache, dass die oben beschriebenen klassischen Stonewall-Transaktionen genau demselben Muster folgen wie die Stonewall x2-Transaktionen. Von außen betrachtet und ohne zusätzliche Kontextinformationen ist es unmöglich, eine Stonewall-Transaktion von einer Stonewall x2-Transaktion zu unterscheiden. Bei ersteren handelt es sich nicht um kollaborative Transaktionen, bei letzteren hingegen schon. Dies erhöht die Zweifel an den Kosten noch weiter.



![image](assets/fr/05.webp)




## Wie kann ich eine Verbindung zwischen Paynyms herstellen?



Wie bei anderen kollaborativen Transaktionen auf Ashigaru (*Cahoots*) beinhaltet Stonewall x2 den Austausch von teilweise signierten Transaktionen zwischen dem Sender und dem Kollaborateur. Dieser Austausch kann manuell erfolgen, wenn Sie mit Ihrem Partner physisch anwesend sind, oder automatisch über das Soroban-Kommunikationsprotokoll.



Wenn Sie sich für die zweite Option entscheiden, müssen Sie eine Verbindung zwischen Paynyms herstellen, bevor Sie einen Stonewall x2 durchführen können. Dazu muss dein Paynym dem Paynym deines Mitspielers "folgen", und umgekehrt. Um herauszufinden, wie das geht, kannst du dem Anfang dieses anderen Tutorials folgen:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Wie führe ich eine Stonewall x2-Transaktion auf Ashigaru durch?



Um eine Stonewall x2-Transaktion durchzuführen, klicken Sie auf das Bild Ihres Paynym in der oberen linken Ecke des Bildschirms und öffnen Sie dann das Menü "Zusammenarbeit". Die Person, die mit Ihnen an der Transaktion teilnimmt, muss dasselbe tun, es sei denn, Sie tauschen persönlich QR-Codes aus.



![Image](assets/fr/06.webp)



Sie haben zwei Möglichkeiten: Wählen Sie "Initiieren", wenn Sie der Absender der Zahlung sind, oder "Teilnehmen", wenn Sie die Person sind, die an der Transaktion mitarbeitet, aber weder der Zahler noch der eigentliche Empfänger ist.



![Image](assets/fr/07.webp)



Wenn Sie die Rolle des Kollaborateurs haben, ist das Verfahren sehr einfach. Für die Fernzusammenarbeit über das Soroban-Netz klicken Sie auf "Teilnehmen", wählen Sie das Konto, das Sie verwenden möchten, und drücken Sie dann auf "Auf Anfragen warten", um auf die Anfrage des Auftraggebers zu warten.



![Image](assets/fr/08.webp)



Für die persönliche Zusammenarbeit über das Scannen von QR-Codes gehen Sie auf die Startseite Ihres wallet, drücken Sie auf das QR-Code-Symbol am oberen Bildschirmrand und scannen Sie dann den QR-Code, den der Zahler, der die Transaktion veranlasst, zur Verfügung stellt.



![Image](assets/fr/09.webp)



Wenn Sie in der Rolle des Zahlers sind, d.h. derjenige, der die Transaktion veranlasst, gehen Sie zum Menü "Zusammenarbeit" und wählen Sie dann "Veranlassen".



![Image](assets/fr/10.webp)



Da wir eine Stonewall x2 durchführen wollen, wählen Sie diese Option für die Transaktionsart.



![Image](assets/fr/11.webp)



Sie können dann zwischen Online-Zusammenarbeit (*Cahoots* über *Soroban*) oder persönlicher Zusammenarbeit mit Austausch von QR-Codes wählen.



![Image](assets/fr/12.webp)



### Cahoots online



Wenn Sie die Option "Online" gewählt haben, wählen Sie Ihren Mitarbeiter aus den Paynyms, die Sie verfolgen.



![Image](assets/fr/13.webp)



Klicken Sie auf "Transaktion einrichten" und wählen Sie dann das Konto aus, von dem Sie die Ausgabe tätigen möchten.



![Image](assets/fr/14.webp)



Auf der nächsten Seite geben Sie die Transaktionsdetails ein: die Adresse des tatsächlichen Empfängers der Zahlung, den zu überweisenden Betrag und den Gebührensatz. Klicken Sie dann auf "Transaktionseinstellungen überprüfen".



![Image](assets/fr/15.webp)



Prüfen Sie die Informationen sorgfältig, stellen Sie sicher, dass Ihr Partner die *Cahoots*-Anfragen hört, und klicken Sie dann auf die grüne Schaltfläche "TRANSAKTION BEGINNEN", um den Austausch von PSBTs über Soroban einzuleiten.



![Image](assets/fr/16.webp)



Warten Sie, bis beide Teilnehmer die Transaktion unterzeichnet haben, und senden Sie sie dann an das Bitcoin-Netz.



![Image](assets/fr/17.webp)



### Persönliche Gespräche



Wenn Sie den Umtausch persönlich vornehmen möchten, wählen Sie die Transaktionsart "STONEWALL X2" und dann die Option "Persönlich / Manuell".



![Image](assets/fr/18.webp)



Klicken Sie auf "Transaktion einrichten" und wählen Sie dann das Konto aus, von dem Sie die Ausgabe tätigen möchten.



![Image](assets/fr/19.webp)



Auf der nächsten Seite geben Sie die Transaktionsdetails ein: die Adresse des tatsächlichen Empfängers der Zahlung, den zu überweisenden Betrag und den Gebührensatz. Klicken Sie dann auf "Transaktionseinstellungen überprüfen".



![Image](assets/fr/20.webp)



Überprüfen Sie die Angaben und drücken Sie dann die grüne Schaltfläche "TRANSAKTION BEGINNEN", um den Austausch von PSBTs über QR-Code-Scanning zu starten.



![Image](assets/fr/21.webp)



Der Austausch erfolgt durch abwechselndes Scannen mit dem Mitarbeiter: Klicken Sie auf `SHOW QR CODE`, um Ihren QR-Code Ihrem Mitarbeiter zu zeigen, der ihn dann scannt. Er klickt dann auf `SHOW QR CODE`, um seinen zu zeigen, und Sie scannen ihn mit `LAUNCH QR Scanner`. Wiederholen Sie diesen Vorgang, bis alle fünf Austauschschritte abgeschlossen sind.



![Image](assets/fr/22.webp)



Wenn alle Umtauschvorgänge abgeschlossen sind, überprüfen Sie die Transaktionsdetails und geben Sie die Transaktion frei, indem Sie den grünen Pfeil am unteren Rand des Bildschirms ziehen.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Sie ist wie folgt aufgebaut:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Wir können zwei Eingänge aus meinem Portfolio beobachten, nämlich 91.869 sats" und 64.823 sats", während die anderen beiden Eingänge aus dem wallet meines Mitarbeiters stammen. Auf der Ausgabeseite wird ein UTXO in Höhe von 100.000 sats" an den tatsächlichen Zahlungsempfänger gesendet, und zwei UTXOs in Höhe von 100.000 sats" und 159.578 sats" kehren in das Portfolio meines Mitarbeiters zurück. Für ihn ist der Vorgang neutral, da er den vollen Betrag der Mittel zurückerhält, die er in den Input investiert hatte (ohne die Kosten für mining, zu denen er beigetragen hat). Schließlich erhalte ich einen Austausch-UTXO von 56.270 sats", der der Differenz zwischen meinen gesamten Inputs und der Zahlung von 100.000 sats" an den Empfänger entspricht.



Offensichtlich kann ich diese Struktur beschreiben, weil ich die Transaktion selbst aufgebaut habe. Aber für einen außenstehenden Beobachter ist es im Allgemeinen unmöglich festzustellen, welche UTXOs zu welchem Teilnehmer gehören, weder bei den Eingängen noch bei den Ausgängen.



Um Ihr Wissen über das Onchain-Datenschutzmanagement auf Bitcoin zu vertiefen, empfehle ich Ihnen die Teilnahme an meiner BTC 204-Schulung auf der Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
