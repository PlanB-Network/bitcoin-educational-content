---
name: Ashigaru - Stowaway
description: Wie führe ich eine Payjoin-Transaktion auf Ashigaru durch?
---
![cover](assets/cover.webp)



> *Zwingt Blockchain-Spione, alles zu überdenken, was sie zu wissen glauben

Payjoin ist eine Bitcoin-Transaktionsstruktur, die die Vertraulichkeit der Nutzer durch direkte Zusammenarbeit mit dem Zahlungsempfänger erhöhen soll. Es gibt mehrere Implementierungen, die die Umsetzung erleichtern und den Prozess automatisieren. Die bekannteste davon ist zweifellos Stowaway, das ursprünglich vom Wallet-Team von Samurai entwickelt wurde und nun in dessen fork Ashigaru integriert ist.



## Wie funktioniert Stowaway?



Wie bereits erwähnt, ist in Ashigaru ein PayJoin-Tool namens "Stowaway" integriert. Dieses ist in der Ashigaru-App auf Android verfügbar. Damit ein Payjoin durchgeführt werden kann, muss der Empfänger (der auch die Rolle des Mitarbeiters übernimmt) eine mit Stowaway kompatible Software verwenden, d. h. im Moment nur Ashigaru.



Stowaway basiert auf einer Kategorie von Transaktionen, die Samurai als "Cahoots" bezeichnet. Ein Cahoot ist eine kollaborative Transaktion zwischen mehreren Nutzern, die einen Austausch von Informationen außerhalb der Bitcoin-Blockchain beinhaltet. Ashigaru bietet derzeit zwei Cahoots-Tools an: Stowaway (Payjoins) und StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots-Transaktionen erfordern den Austausch von teilweise signierten Transaktionen zwischen den Nutzern. Dieser Vorgang kann langwierig und mühsam sein, insbesondere wenn er aus der Ferne erfolgt. Es ist jedoch auch möglich, dies manuell zu tun, wenn sich die Beteiligten am selben Ort befinden. Konkret bedeutet dies, dass fünf QR-Codes nacheinander gescannt werden müssen, die zwischen den beiden Teilnehmern ausgetauscht werden.



Auf Distanz wird diese Methode zu komplex. Um hier Abhilfe zu schaffen, hat Samourai ein Tor-basiertes verschlüsseltes Kommunikationsprotokoll namens "*Soroban*" entwickelt. Dank Soroban werden die für einen Payjoin erforderlichen Austauschvorgänge automatisiert und finden im Hintergrund statt.



Diese verschlüsselte Kommunikation erfordert eine Verbindung und Authentifizierung zwischen den Teilnehmern von Cahoot. Aus diesem Grund verlässt sich Soroban auf die Paynyms der Nutzer. Wenn Sie noch nicht mit der Funktionsweise von Paynyms vertraut sind, schauen Sie sich dieses spezielle Tutorial an, um mehr zu erfahren:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Kurz gesagt ist ein Paynym eine eindeutige Kennung, die mit Ihrem wallet verknüpft ist und es Ihnen ermöglicht, verschiedene Funktionen zu aktivieren, einschließlich des verschlüsselten Austauschs. Es handelt sich um eine Kennung, die mit einer Abbildung versehen ist. Hier ist zum Beispiel die Kennung, die ich für den Testnet verwende:



![Image](assets/fr/01.webp)



**Zusammenfassend:**





- payjoin" = Spezifische kollaborative Transaktionsstruktur;





- stowaway" = Payjoin-Implementierung auf Ashigaru verfügbar;





- cahoots" = Bezeichnung der Samourai für alle Arten von Kooperationen, insbesondere das Payjoin "Stowaway", das heute auf Ashigaru übernommen wurde;





- soroban = Verschlüsseltes Kommunikationsprotokoll auf Tor, das die Zusammenarbeit mit anderen Nutzern in einer "Cahoots"-Transaktion ermöglicht;





- paynym" = Eindeutige wallet-Kennung, die verwendet wird, um die Kommunikation mit einem anderen Nutzer auf "Soroban" herzustellen, um eine "Chahoots"-Transaktion durchzuführen.



Für einen tieferen Einblick in die Funktionsweise von Payjoins und ihre Nützlichkeit für den Datenschutz in der Onchain empfehle ich dieses andere Tutorial:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Wie kann ich eine Verbindung zwischen Paynyms herstellen?



Um loszulegen, müssen Sie natürlich Ashigaru installieren und eine :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Um eine Cahoots-Ferntransaktion, einschließlich eines PayJoin (*Stowaway*) über Ashigaru durchzuführen, müssen Sie zunächst dem Nutzer, mit dem Sie zusammenarbeiten möchten, über dessen Paynym "folgen". Im Falle eines Stowaways bedeutet dies, dass Sie der Person folgen, der Sie Bitcoins senden möchten. Wenn du noch nicht weißt, wie du einem anderen Paynym folgen kannst, findest du die detaillierte Vorgehensweise in diesem Tutorial:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Wie mache ich einen Payjoin auf Ashigaru?



Um eine Stowaway-Transaktion durchzuführen, klicken Sie auf das Bild Ihres Paynym in der oberen linken Ecke des Bildschirms und öffnen dann das Menü "Zusammenarbeit". Die Person, die mit Ihnen an der Transaktion teilnimmt, muss dasselbe tun, es sei denn, Sie tauschen persönlich QR-Codes aus.



![Image](assets/fr/02.webp)



Sie haben zwei Möglichkeiten: Wählen Sie "Initiate", wenn Sie der Absender der Zahlung sind, oder "Participate", wenn Sie der Zahlungsempfänger dieses Payjoin sind.



![Image](assets/fr/03.webp)



Wenn Sie der Empfänger sind, ist das Verfahren sehr einfach. Für die Fernzusammenarbeit über das Soroban-Netz klicken Sie auf "Teilnehmen", wählen das gewünschte Konto aus und drücken dann auf "Auf Anfragen warten", um die Anfrage des Auftraggebers abzuwarten.



![Image](assets/fr/04.webp)



Für die persönliche Zusammenarbeit über das Scannen von QR-Codes gehen Sie auf die Startseite Ihres wallet, drücken Sie auf das QR-Code-Symbol am oberen Rand des Bildschirms und scannen Sie dann den QR-Code, den der Zahler, der die Transaktion veranlasst, bereitgestellt hat.



![Image](assets/fr/05.webp)



Wenn Sie in der Rolle des Zahlers sind, d.h. derjenige, der die Transaktion veranlasst, gehen Sie zum Menü "Zusammenarbeit" und wählen Sie dann "Veranlassen".



![Image](assets/fr/06.webp)



Da wir einen Payjoin Stowaway machen wollen, wählen Sie diese Option als Transaktionsart.



![Image](assets/fr/07.webp)



Sie können dann zwischen Online-Zusammenarbeit (*Cahoots* über *Soroban*) oder persönlicher Zusammenarbeit mit Austausch von QR-Codes wählen.



![Image](assets/fr/08.webp)



### Cahoots online



Wenn Sie die Option "Online" gewählt haben, wählen Sie den Empfänger aus den Paynyms aus, die Sie verfolgen.



![Image](assets/fr/09.webp)



Klicken Sie auf "Transaktion einrichten" und wählen Sie dann das Konto aus, von dem Sie die Ausgabe tätigen möchten.



![Image](assets/fr/10.webp)



Auf der nächsten Seite geben Sie die Transaktionsdetails ein: den Betrag, der an den Empfänger gesendet werden soll, und den Gebührensatz. Es ist nicht nötig, eine Empfängeradresse einzugeben, da der Empfänger sie beim PSBT-Austausch selbst übermittelt.



Klicken Sie dann auf "Transaktionseinstellungen überprüfen".



![Image](assets/fr/11.webp)



Prüfen Sie die Informationen sorgfältig, stellen Sie sicher, dass Ihr Partner die *Cahoots*-Anfragen hört, und klicken Sie dann auf die grüne Schaltfläche "TRANSAKTION BEGINNEN", um den Austausch von PSBTs über Soroban einzuleiten.



![Image](assets/fr/12.webp)



Warten Sie, bis beide Teilnehmer die Transaktion unterzeichnet haben, und senden Sie sie dann an das Bitcoin-Netz.



![Image](assets/fr/13.webp)



### Persönliche Gespräche



Wenn Sie den Umtausch persönlich vornehmen möchten, wählen Sie die Transaktionsart "STONEWALL X2" und dann die Option "Persönlich / Manuell".



![Image](assets/fr/14.webp)



Klicken Sie auf "Transaktion einrichten" und wählen Sie dann das Konto aus, von dem Sie die Ausgabe tätigen möchten.



![Image](assets/fr/15.webp)



Auf der nächsten Seite geben Sie die Transaktionsdetails ein: den Betrag, der an den Empfänger gesendet werden soll, und den Gebührensatz. Es ist nicht nötig, eine Empfängeradresse einzugeben, da der Empfänger sie beim PSBT-Austausch selbst übermitteln wird.



Klicken Sie dann auf "Transaktionseinstellungen überprüfen".



![Image](assets/fr/16.webp)



Überprüfen Sie die Angaben und drücken Sie dann die grüne Schaltfläche "TRANSAKTION BEGINNEN", um den Austausch von PSBTs über QR-Code-Scanning zu starten.



![Image](assets/fr/17.webp)



Der Austausch erfolgt durch abwechselndes Scannen mit dem Mitarbeiter: Klicken Sie auf `SHOW QR CODE`, um Ihren QR-Code Ihrem Mitarbeiter zu zeigen, der ihn dann scannt. Er klickt dann auf `SHOW QR CODE`, um seinen zu zeigen, und Sie scannen ihn mit `LAUNCH QR Scanner`. Wiederholen Sie diesen Vorgang, bis alle fünf Austauschschritte abgeschlossen sind.



![Image](assets/fr/18.webp)



Wenn alle Umtauschvorgänge abgeschlossen sind, überprüfen Sie die Transaktionsdetails und geben Sie die Transaktion frei, indem Sie den grünen Pfeil am unteren Rand des Bildschirms ziehen.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Sie ist wie folgt aufgebaut:



![Image](assets/fr/20.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Wenn wir diese Transaktion analysieren, sehen wir auf der Eingangsseite meine UTXO in Höhe von 164.211 sats und die UTXO des eigentlichen Empfängers der Zahlung in Höhe von 190.002 sats. Auf der Outputseite erhalte ich im Austausch UTXO in Höhe von 63.995 sats, während der Empfänger UTXO in Höhe von 290.002 sats erhält. Vergleicht man Input und Output, so stellt man fest, dass der Empfänger tatsächlich 100.000 sats" verdient hat, was dem Betrag meiner tatsächlichen Zahlung entspricht, und dass ich 100.000 sats" verloren habe, zu denen ich die mining-Kosten addiert habe.



Offensichtlich kann ich diese Struktur beschreiben, weil ich die Transaktion selbst aufgebaut habe. Aber für einen außenstehenden Beobachter ist es im Allgemeinen unmöglich festzustellen, welche UTXOs zu welchem Teilnehmer gehören, weder bei den Eingängen noch bei den Ausgängen.



Um Ihr Wissen über das Onchain-Datenschutzmanagement auf Bitcoin zu vertiefen, empfehle ich Ihnen, meine BTC 204-Schulung auf der Plan ₿ Academy zu besuchen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c