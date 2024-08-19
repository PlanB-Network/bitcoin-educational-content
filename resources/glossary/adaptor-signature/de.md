---
term: ADAPTOR SIGNATURE
---

Kryptografische Methode, die es ermöglicht, eine echte Signatur mit einer zusätzlichen Signatur (genannt "Adaptor Signature") zu kombinieren, um ein geheimes Stück Daten zu enthüllen. Diese Methode funktioniert so, dass die Kenntnis von zwei Elementen unter der gültigen Signatur, der Adaptor-Signatur und dem Geheimnis das Fehlen des dritten Elements ableiten lässt. Eine der interessanten Eigenschaften dieser Methode ist, dass wir, wenn wir die Adaptor-Signatur unseres Gegenübers und den spezifischen Punkt auf der elliptischen Kurve kennen, der mit dem Geheimnis verbunden ist, das zur Berechnung dieser Adaptor-Signatur verwendet wurde, unsere eigene Adaptor-Signatur ableiten können, die mit demselben Geheimnis übereinstimmt, ohne jemals direkten Zugang zu dem Geheimnis selbst zu haben. In einem Austausch zwischen zwei Stakeholdern, die einander nicht vertrauen, ermöglicht diese Technik die gleichzeitige Enthüllung von zwei sensiblen Informationsstücken zwischen den Teilnehmern. Dieser Prozess eliminiert die Notwendigkeit von Vertrauen in augenblicklichen Transaktionen wie einem Coin Swap oder einem Atomic Swap. Nehmen wir ein Beispiel, um es besser zu verstehen. Alice und Bob möchten sich gegenseitig 1 BTC senden, aber sie vertrauen einander nicht. Sie werden daher Adaptor-Signaturen verwenden, um die Notwendigkeit von Vertrauen in die andere Partei bei diesem Austausch zu negieren (und machen es somit zu einem "atomaren" Austausch). Sie gehen wie folgt vor:
* Alice initiiert diesen atomaren Austausch. Sie erstellt eine Transaktion $m_A$, die 1 BTC an Bob sendet. Sie erstellt eine Signatur $s_A$, die diese Transaktion mit ihrem privaten Schlüssel $p_A$ ($P_A = p_A \cdot G$) validiert, und verwendet einen Nonce $n_A$ und ein Geheimnis $t$ ($N_A = n_A \cdot G$ und $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice berechnet die Adaptor-Signatur $s_A'$ aus dem Geheimnis $t$ und ihrer echten Signatur $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice sendet an Bob ihre Adaptor-Signatur $s_A'$, ihre nicht signierte Transaktion $m_A$, den Punkt, der dem Geheimnis $T$ entspricht, und den Punkt, der dem Nonce $N_A$ entspricht. Wir nennen diese Informationen einen "Adaptor". Beachten Sie, dass Bob mit nur diesen Informationen nicht in der Lage ist, Alices BTC zu erholen.
* Bob kann jedoch überprüfen, dass Alice ihn nicht täuscht. Dazu prüft er, ob Alices Adaptor-Signatur $s_A'$ mit der versprochenen Transaktion $m_A$ übereinstimmt. Wenn die folgende Gleichung korrekt ist, dann ist er überzeugt, dass Alices Adaptor-Signatur gültig ist: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Diese Überprüfung gibt Bob Zusicherungen von Alice, sodass er den Atomic-Swap-Prozess beruhigt fortsetzen kann. Er wird dann seine eigene Transaktion $m_B$ erstellen, die 1 BTC an Alice sendet, und seine eigene Adaptor-Signatur $s_B'$, die mit demselben Geheimnis $t$ verknüpft sein wird, das bisher nur Alice kennt (Bob kennt diesen Wert $t$ nicht, sondern nur den entsprechenden Punkt $T$, den Alice ihm zur Verfügung gestellt hat): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob sendet an Alice seine Adapter-Signatur $s_B'$, seine nicht signierte Transaktion $m_B$, den Punkt, der dem Geheimnis $T$ entspricht, und den Punkt, der dem Nonce $N_B$ entspricht. Alice kann nun Bobs Adapter-Signatur $s_B'$ mit dem Geheimnis $t$, das nur sie kennt, kombinieren, um eine gültige Signatur $s_B$ für die Transaktion $m_B$ zu berechnen, die ihr Bobs BTC sendet: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice sendet diese signierte Transaktion $m_B$ in die Bitcoin-Blockchain, um die BTC zurückzuerhalten, die Bob ihr versprochen hatte. Bob erfährt von dieser Transaktion in der Blockchain. Er kann somit die Signatur $s_B = s_B' + t$ extrahieren. Aus diesen Informationen kann Bob das berühmte Geheimnis $t$ isolieren, das er benötigte:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Jedoch war dieses Geheimnis $t$ die einzige fehlende Information für Bob, um die gültige Signatur $s_A$ aus Alices Adapter-Signatur $s_A'$ zu produzieren, die es ihm ermöglichen wird, die Transaktion $m_A$ zu validieren, die einen BTC von Alice an Bob sendet. Er berechnet dann $s_A$ und sendet die Transaktion $m_A$ seinerseits: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$