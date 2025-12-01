---
name: Blockstream-Explorer
description: Erkunden Sie die Hauptschicht von Bitcoin und Liquid Network
---

![cover](assets/cover.webp)



Der Blockstream Explorer ist ein Projekt, das die Erforschung von Transaktionen und des globalen Status des Bitcoin-Protokolls sowie des von der Firma Blockstream entwickelten [*Sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid ermöglicht.



Der 2014 von Blockstream, einem von Adam Back gegründeten Unternehmen, ins Leben gerufene [blockstream.info](https://blockstream.info)-Explorer zielt darauf ab, eine robuste Infrastruktur für Bitcoin bereitzustellen, die Interoperabilität und Transaktionsverfolgung zwischen den Schichten (on-chain und Liquid) gewährleistet und gleichzeitig die Sicherheit und den Datenschutz der Nutzer verbessert.



In diesem Tutorial werden wir uns ansehen, was es auszeichnet, welche Dienste es bietet und wie es eine nahtlose Überwachung des Betriebs und des Status der Bitcoin-Schichten on-chain und Liquid ermöglicht.



## Erste Schritte mit dem Blockstream-Explorer



### Navigieren im Hauptkanal



Wenn Sie den Blockstream.info-Explorer aufrufen, ist auf dem "**Dashboard**" standardmäßig die Hauptkette des Bitcoin-Protokolls ausgewählt. Von dieser Schnittstelle aus haben Sie einen Überblick über :





- Größe der Hauptkette: Kürzlich abgebaute Blöcke.



![blocks](assets/fr/01.webp)



Dieser Abschnitt enthält Informationen über die zuletzt geschürften Blöcke, den Zeitstempel, die Anzahl der in jedem Block enthaltenen Transaktionen, die Größe in Kilobytes (kB) und das Maß jedes Blocks in Gewichtseinheiten (**WU** = *Weight Units*). Letzteres ist von Interesse, da es uns ermöglicht, die Optimierung des Blocks zu bewerten, da jeder Block der Hauptkette auf "4.000.000 WU" oder "4.000 kWU" begrenzt ist.





- Jüngste Transaktionen.



![transactions](assets/fr/02.webp)



Der Transaktionsabschnitt enthält Informationen über die eindeutige Kennung der Transaktion, den beteiligten Bitcoin-Wert, die Größe in virtuellen Bytes (vB) - die die Summe aller Daten (Eingabe und Ausgabe) darstellt - und den entsprechenden Gebührensatz. Zum Beispiel, eine Transaktion mit einer Größe von 153 vB bei einer Rate von 2 Sat/vB verursacht eine Gebühr von 306 Satoshis.



### Erforschung von Flüssigkeiten



Über das Menü "**Blöcke**" können Sie die Geschichte der gesamten Hauptkette bis zum letzten abgebauten Block zurückverfolgen.



![blocs](assets/fr/03.webp)



Wenn Sie auf einen bestimmten Block klicken, erhalten Sie weitere Details zu den darin enthaltenen Informationen und Transaktionen. Zum Beispiel für Block 919330: Sie sehen den Hash des Blocks. Sie können auch zum vorherigen Block navigieren, da jeder abgebaute Block (mit Ausnahme von Genesis) mit dem vorherigen verknüpft ist und den Hash seines Vorgängers beibehält.



![metadata](assets/fr/04.webp)



Wenn Sie auf die Schaltfläche **"Details "** klicken, erhalten Sie weitere Informationen zu diesem Block, wie z. B. seinen Status, der bestätigt, dass er zur Hauptkette hinzugefügt und weitergegeben wurde. Sie haben auch die Schwierigkeit, mit der dieser Block abgebaut wird: Diese Schwierigkeit stellt die Rechenleistung dar, die erforderlich ist, um das kryptografische Problem von mining zu lösen, und wird alle 2016 Blöcke (etwa 2 Wochen) angepasst.



![details](assets/fr/05.webp)



Unterhalb dieses Detailbereichs finden Sie alle in diesem Block enthaltenen Transaktionen.



Die allererste Transaktion im Block wird **Transaktionscoinbase** genannt. Sie wird verwendet, um die mining-Belohnung des Miners (alle Gebühren im Zusammenhang mit den im Block enthaltenen Transaktionen und dem Block Grant) zu verteilen. Die durch diese Transaktion erzeugten Bitcoins können erst ausgegeben werden, wenn weitere 100 aufeinanderfolgende Blöcke geschürft worden sind. Mit anderen Worten, um sie verwenden zu können, muss der Miner auf die Produktion von Block **919430** warten. Dies wird als [*"Fälligkeitsperiode "*] (https://planb.academy/fr/resources/glossary/maturity-period) bezeichnet.



Die Coinbase ist eine besondere Transaktion: Sie ist die einzige, bei der es keinen echten Input gibt, da sie keine Bitcoins aus einer vorherigen Transaktion ausgibt.




![coinbase](assets/fr/06.webp)



Alle anderen Transaktionen sind in zwei Abschnitte unterteilt: Inputs und Outputs.



Damit Bitcoins als Input für eine neue Transaktion verwendet werden können, muss der Initiator der Transaktion seinen Besitz durch eine Signatur nachweisen, die einem bestimmten Skript entspricht. Jedes Stück Bitcoins (UTXO) enthält ein Skript, das im Allgemeinen eine bestimmte Signatur erfordert, die nur der private Schlüssel des Inhabers liefern kann. Diese Skripte heißen ***scriptSig*** (in ASM), sind in Bitcoin-Skript geschrieben und können von unterschiedlicher Art sein. In diesem Beispiel sehen wir, dass die verwendeten UTXOs vom Typ P2SH für eine Ausgabe vom Typ P2WPKH (*Pay-to-Witness-Public-Key-Hash*) waren.



Sie können die Geschichte eines bestimmten UTXO mit Hilfe von Heuristiken zurückverfolgen. Wir laden Sie ein, die verschiedenen Bitcoin-Heuristiken und Möglichkeiten zur Stärkung der Vertraulichkeit Ihrer Transaktionen auf Bitcoin zu entdecken:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Nehmen wir das Beispiel der ausgehenden Ausgaben dieser Transaktion. Wenn wir auf die Transaktionskennung klicken, werden wir zum Abschnitt **Transaktionen** auf der Seite mit den Transaktionsdetails weitergeleitet.



![transaction](assets/fr/08.webp)



Auf dieser Seite können Sie herausfinden, in welchem Block die Transaktion enthalten war. Je nach verwendetem Adresstyp kann die Transaktion ihre Daten (*virtuelle Bytes*) optimieren und somit weniger Transaktionsgebühren zahlen. Bei dieser Transaktion wurden beispielsweise 53 % an Gebühren eingespart, indem ein natives SegWit Bech32-Adressformat verwendet wurde, das mit "bc1q" beginnt.



![trx_details](assets/fr/09.webp)



## Liquid-Schicht



Liquid Network ist eine [*Sidechain*](https://planb.academy/en/resources/glossary/sidechain) und eine Open-Source-Level-2-Lösung für das Bitcoin-Protokoll. Es ermöglicht insbesondere schnellere und vertraulichere Bitcoin-Transaktionen.



Klicken Sie im Blockstream.info-Explorer auf die Schaltfläche **"Liquid"**, um zum Liquid-Netz zu wechseln.



![liquid](assets/fr/10.webp)



Wenn wir auf eine der Transaktionen klicken, die wir verfolgen wollen, sehen wir, dass die Bitcoin-Beträge durch die Worte "**Vertraulich**" ersetzt werden. In diesem Netzwerk können Transaktionen vertraulich sein, so dass wir die Beträge der einzelnen UTXO nicht sehen können, weder innerhalb noch außerhalb der Transaktion.



![liquid_trx](assets/fr/11.webp)



Wir stellen jedoch fest, dass die Grundsätze und Mechanismen auf der Hauptebene des Bitcoin-Protokolls dieselben sind: Bitcoin-Sperrskripte und UTXO-Rückverfolgbarkeit.



![liquid_details](assets/fr/12.webp)



Die Liquid Network bietet auch nicht deponierte digitale Vermögenswerte, die von Organisationen genutzt werden können. Im Menü **"Assets "** finden Sie eine Liste der registrierten Assets, ihre Gesamtsumme und den Bereich, auf den sie sich beziehen.



![assets](assets/fr/13.webp)



Für jeden Vermögenswert können Sie die Historie der Ausgabe- und Verbrennungstransaktionen verfolgen (wobei der Gesamtumlauf gelöscht wird).



![assets_trxs](assets/fr/14.webp)




## Mehr Optionen



Der Blockstream.info-Explorer enthält auch Visualisierungen und Verfolgung von Transaktionen auf Testnet, Bitcoin, on-chain und Liquid Network.



![testnet](assets/fr/15.webp)



Wenn Sie zum Testnet-Netzwerk gehen, verwenden Sie keine echten Bitcoins, aber Sie haben alle oben beschriebenen Funktionen.



![liquid_testnet](assets/fr/16.webp)



Dieses Netz verfügt über eine andere Kettenlänge, an die Sie die Mechanismen Bitcoin und Liquid anschließen und deren Funktion testen können.





- Der Bereich API ist für alle gedacht, die bestimmte Explorer-Funktionen in ihre eigene Anwendung integrieren möchten. Über diesen API können Sie die Hauptkette der verschiedenen Schichten (on-chain und Liquid) abfragen, Transaktionen verfolgen und z. B. die durchschnittlichen Gebühren für Transaktionen in einem Block herausfinden.



![api](assets/fr/17.webp)



Sie sind nun bereit, das volle Potenzial des Blockstream Explorers für die Abfrage von Blockchains auf den on-chain- und Liquid-Ebenen zu nutzen. Wir hoffen, dass Sie dieses Tutorial informativ fanden, und empfehlen Ihnen unser Tutorial über einen anderen Bitcoin-Explorer:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f