---
name: Ashigaru - Ricochet
description: Verstehen und Verwenden von Ricochet-Transaktionen
---
![cover ricochet](assets/cover.webp)



> *Ein Premium-Tool, das Ihrer Transaktion einen zusätzlichen Schritt in der Geschichte hinzufügt. Überlisten Sie die schwarzen Listen und schützen Sie sich vor ungerechtfertigten Kontosperrungen durch Dritte

## Was ist ein Querschläger?



Ricochet ist eine Technik, die darin besteht, mehrere fiktive Transaktionen an sich selbst durchzuführen, um eine Übertragung von Bitcoin-Eigentum zu simulieren. Dieses Tool unterscheidet sich von den anderen Transaktionen von Ashigaru (die von Samurai Wallet übernommen wurden), da es keine prospektive Anonymität, sondern eher eine Form der retrospektiven Anonymität bietet. In der Tat verwischt Ricochet die Besonderheiten, die die Fungibilität eines Bitcoin-Teils beeinträchtigen können.



Wenn Sie z. B. einen Coinjoin durchführen, wird Ihr Teil, das aus dem Mix kommt, als solches identifiziert. Kettenanalysewerkzeuge sind in der Lage, die Paterns von Coinjoin-Transaktionen zu erkennen und den Stücken, die aus ihnen hervorgehen, ein Etikett zuzuweisen. Coinjoin zielt darauf ab, die historischen Verbindungen einer Münze zu unterbrechen, aber ihre Passage durch Coinjoins bleibt nachweisbar. In Analogie dazu ist dieses Phänomen mit der Verschlüsselung eines Textes vergleichbar: Obwohl der Originaltext nicht im Klartext zugänglich ist, lässt sich leicht erkennen, dass eine Verschlüsselung vorgenommen wurde.



Die Bezeichnung "coinjoined" kann die Fungibilität eines UTXO beeinträchtigen. Aufsichtsbehörden, wie z. B. Börsenplattformen, können sich weigern, einen coinjoined UTXO zu akzeptieren, oder sogar Erklärungen von seinem Besitzer verlangen, mit dem Risiko, dass Ihr Konto gesperrt oder Ihr Geld eingefroren wird. In einigen Fällen kann die Plattform Ihr Verhalten sogar den staatlichen Behörden melden.



Hier kommt die Ricochet-Methode ins Spiel. Um den Abdruck, den ein Coinjoin hinterlässt, zu verwischen, führt Ricochet vier aufeinanderfolgende Transaktionen durch, bei denen der Nutzer sein Geld an verschiedene Adressen überweist. Nach dieser Abfolge von Transaktionen leitet das Ricochet-Tool die Bitcoins schließlich an ihren endgültigen Bestimmungsort weiter, z. B. an eine Tauschplattform. Ziel ist es, einen Abstand zwischen der ursprünglichen Coinjoin-Transaktion und der endgültigen Ausgabe zu schaffen. Auf diese Weise gehen die Blockchain-Analysetools davon aus, dass nach dem Coinjoin wahrscheinlich eine Eigentumsübertragung stattgefunden hat und daher keine Maßnahmen gegen den Emittenten ergriffen werden müssen.



![image](assets/fr/01.webp)



Angesichts der Ricochet-Methode könnte man annehmen, dass eine Kettenanalysesoftware ihre Untersuchung über vier Prellungen hinaus vertiefen würde. Allerdings stehen diese Plattformen bei der Optimierung der Erkennungsschwelle vor einem Dilemma. Sie müssen einen Schwellenwert für die Anzahl der Sprünge festlegen, ab dem sie davon ausgehen, dass wahrscheinlich ein Eigentümerwechsel stattgefunden hat und dass die Verbindung zu einem früheren Coinjoin ignoriert werden sollte. Die Festlegung dieses Schwellenwerts ist jedoch riskant: Mit jeder Erhöhung der Anzahl der beobachteten Sprünge steigt die Anzahl der falsch-positiven Fälle exponentiell an, d. h. Personen, die fälschlicherweise als Teilnehmer an einem Coinjoin markiert werden, obwohl der Vorgang in Wirklichkeit von jemand anderem durchgeführt wurde. Dieses Szenario stellt für diese Unternehmen ein großes Risiko dar, da falsch positive Ergebnisse zu Unzufriedenheit führen, die die betroffenen Kunden zur Konkurrenz treiben kann. Langfristig führt eine zu ehrgeizige Erkennungsschwelle dazu, dass eine Plattform mehr Kunden verliert als ihre Konkurrenten, was ihre Existenz bedrohen könnte. Für diese Plattformen ist es daher kompliziert, die Zahl der festgestellten Bounces zu erhöhen, und 4 ist oft eine ausreichende Zahl, um ihre Analysen zu widerlegen.



Der **häufigste Anwendungsfall für Ricochet ergibt sich also, wenn es notwendig ist, eine frühere Beteiligung an einem Coinjoin auf einem UTXO, das Ihnen gehört, zu verbergen.** Idealerweise ist es am besten, die Übertragung von Bitcoins, die einem Coinjoin unterzogen wurden, an regulierte Einrichtungen zu vermeiden. Sollte es jedoch keine andere Möglichkeit geben, insbesondere bei der dringenden Notwendigkeit, Bitcoins in staatlicher Währung zu liquidieren, bietet Ricochet eine effektive Lösung.



## Wie funktioniert Ricochet bei Ashigaru?



Ricochet ist einfach eine Methode, um Bitcoins an sich selbst zu senden, die ursprünglich von den Entwicklern von Samurai Wallet erfunden wurde. Es ist daher durchaus möglich, einen Ricochet manuell zu simulieren, ohne ein spezielles Tool zu benötigen. Für diejenigen, die den Prozess automatisieren und dabei ein ausgefeilteres Ergebnis erzielen möchten, ist das Ricochet-Tool, das über die Ashigaru-Anwendung (ein Samourai fork) verfügbar ist, eine gute Lösung.



Da Ashigaru für seinen Service Gebühren erhebt, kostet ein Querschläger 100.000 sats als Servicegebühr, zuzüglich einer mining-Gebühr. Seine Verwendung wird daher für Überweisungen von größeren Beträgen empfohlen.



Die Ashigaru-Anwendung bietet zwei Ricochet-Varianten:





- Verstärkter Abprall oder "gestaffelte Zustellung", die den Vorteil bietet, dass die Servicegebühren von Ashigaru auf die fünf aufeinander folgenden Transaktionen verteilt werden. Diese Option stellt auch sicher, dass jede Transaktion zu einem separaten Zeitpunkt gesendet und in einem anderen Block aufgezeichnet wird, wodurch das Verhalten eines Eigentümerwechsels so genau wie möglich nachgeahmt wird. Obwohl diese Methode langsamer ist, ist sie für diejenigen, die es nicht eilig haben, vorzuziehen, da sie die Effizienz von Ricochet maximiert, indem sie seine Widerstandsfähigkeit gegenüber Kettenanalysen stärkt;





- Die klassische Ricochet-Methode, die auf eine schnelle Ausführung des Vorgangs ausgelegt ist, sendet alle Transaktionen in einem verkürzten Zeitintervall. Diese Methode bietet daher weniger Vertraulichkeit und weniger Widerstand gegen Analysen als die verstärkte Methode. Sie sollte nur für dringende Sendungen verwendet werden.



## Wie macht man einen Querschläger auf Ashigaru?



Einen Abpraller auf Ashigaru zu machen ist sehr einfach: Aktivieren Sie einfach die entsprechende Option beim Erstellen einer Sendetransaktion. Um zu beginnen, klicken Sie auf die Schaltfläche "+", dann auf "Senden" und wählen Sie das Konto aus, von dem Sie das Geld senden möchten.



![Image](assets/fr/02.webp)



Geben Sie die Transaktionsdaten ein: den zu sendenden Betrag und die endgültige Adresse des Empfängers nach den Ricochet-Sprüngen. Markieren Sie dann die Option "Ricochet".



![Image](assets/fr/03.webp)



Sie können dann zwischen den beiden im Theorieteil besprochenen Ricochet-Modi wählen: entweder klassisches Ricochet, bei dem alle Transaktionen im selben Block enthalten sind, oder gestaffelte Zustellung, die die Ricochet-Qualität auf Kosten einer längeren Verzögerung verbessert.



Wenn Sie Ihre Wahl getroffen haben, drücken Sie zur Bestätigung auf den Pfeil am unteren Rand des Bildschirms.



![Image](assets/fr/04.webp)



Auf dem nächsten Bildschirm sehen Sie eine vollständige Übersicht über Ihre Transaktion. Hier können Sie auch den Gebührensatz für Ihre Ricochet-Transaktionen an die Marktbedingungen anpassen. Wenn alles zu Ihrer Zufriedenheit ist, ziehen Sie den grünen Pfeil, um Ricochet-Transaktionen zu unterzeichnen und zu verteilen.



![Image](assets/fr/05.webp)



Warten Sie, während die verschiedenen Sprünge automatisch ablaufen.



![Image](assets/fr/06.webp)



Ihre Transaktionen wurden erfolgreich übertragen.



![Image](assets/fr/07.webp)



Sie sind nun vollständig mit der Ricochet-Option in der Ashigaru-Anwendung vertraut. Um noch weiter zu gehen, empfehle ich Ihnen meinen BTC 204 Trainingskurs, in dem Sie im Detail lernen, wie Sie Ihre Onchain-Vertraulichkeit stärken können.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
