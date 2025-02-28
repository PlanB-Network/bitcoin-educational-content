---
term: SIGNATUR DES ADAPTERS

---
Kryptografische Methode, die es ermöglicht, eine echte Unterschrift mit einer zusätzlichen Unterschrift (einer so genannten "Anpassungssignatur") zu kombinieren, um ein geheimes Datenelement zu enthüllen. Diese Methode funktioniert so, dass die Kenntnis von zwei Elementen der gültigen Signatur, der Anpassungssignatur und des Geheimnisses die Ableitung des fehlenden dritten Elements ermöglicht. Eine der interessanten Eigenschaften dieser Methode ist, dass wir, wenn wir die Anpassungssignatur unseres Gegenübers und den spezifischen Punkt auf der elliptischen Kurve kennen, der mit dem Geheimnis verbunden ist, das zur Berechnung dieser Anpassungssignatur verwendet wurde, unsere eigene Anpassungssignatur ableiten können, die mit demselben Geheimnis übereinstimmt, ohne jemals direkten Zugang zum Geheimnis selbst zu haben. Bei einem Austausch zwischen zwei Akteuren, die einander nicht vertrauen, ermöglicht diese Technik die gleichzeitige Offenlegung von zwei sensiblen Informationen zwischen den Teilnehmern. Durch diesen Prozess entfällt die Notwendigkeit des Vertrauens bei sofortigen Transaktionen wie einem Coin Swap oder einem Atomic Swap. Nehmen wir ein Beispiel, um es besser zu verstehen. Alice und Bob wollen sich gegenseitig 1 BTC schicken, aber sie vertrauen einander nicht. Sie werden daher Adapter-Signaturen verwenden, um das Vertrauen in die andere Partei bei diesem Austausch zu negieren (wodurch es ein "atomarer" Austausch wird). Sie gehen wie folgt vor:


- Alice initiiert diesen atomaren Austausch. Sie erstellt eine Transaktion $m_A$, die 1 BTC an Bob sendet. Sie erstellt eine Signatur $s_A$, die diese Transaktion mit ihrem privaten Schlüssel $p_A$ ($P_A = p_A \cdot G$) und mit einem Nonce $n_A$ und einem Geheimnis $t$ ($N_A = n_A \cdot G$ und $T = t \cdot G$) bestätigt:

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$

&nbsp;


- Alice berechnet aus dem Geheimnis $t$ und ihrer echten Signatur $s_A$ die Adaptorsignatur $s_A'$:

$$s_A' = s_A - t$$

&nbsp;


- Alice sendet an Bob ihre Adaptor-Signatur $s_A'$, ihre unsignierte Transaktion $m_A$, den Punkt, der dem Geheimnis $T$ entspricht, und den Punkt, der dem Nonce $N_A$ entspricht. Wir nennen diese Informationen einen "Adaptor". Beachten Sie, dass Bob mit diesen Informationen allein nicht in der Lage ist, Alices BTC wiederzuerlangen.
- Bob kann jedoch überprüfen, dass Alice ihn nicht betrügt. Dazu prüft er, ob Alices Adaptor-Signatur $s_A'$ mit der versprochenen Transaktion $m_A$ übereinstimmt. Wenn die folgende Gleichung korrekt ist, dann ist er überzeugt, dass Alices Adapter-Signatur gültig ist:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$

&nbsp;


- Durch diese Verifizierung erhält Bob eine Zusicherung von Alice, so dass er den atomaren Tauschprozess unbesorgt fortsetzen kann. Er wird dann seine eigene Transaktion $m_B$ erstellen, bei der er 1 BTC an Alice und seine eigene Adapter-Signatur $s_B'$ sendet, die mit demselben Geheimnis $t$ verknüpft wird, das vorerst nur Alice kennt (Bob kennt diesen Wert $t$ nicht, sondern nur den entsprechenden Punkt $T$, den Alice ihm mitgeteilt hat): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$

&nbsp;


- Bob sendet Alice seine Anpassungssignatur $s_B'$, seine unsignierte Transaktion $m_B$, den Punkt, der dem Geheimnis $T$ entspricht, und den Punkt, der dem Nonce $N_B$ entspricht. Alice kann nun Bobs Adaptor-Signatur $s_B'$ mit dem Geheimnis $t$, das nur sie kennt, kombinieren, um eine gültige Signatur $s_B$ für die Transaktion $m_B$ zu berechnen, mit der sie Bobs BTC erhält:

$$s_B = s_B' + t$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$

&nbsp;


- Alice sendet diese signierte Transaktion $m_B$ auf der Bitcoin-Blockchain, um die BTC zurückzuholen, die Bob ihr versprochen hat. Bob erfährt von dieser Transaktion in der Blockchain. Er ist somit in der Lage, die Signatur $s_B = s_B' + t$ zu extrahieren. Aus dieser Information kann Bob das berühmte Geheimnis $t$ isolieren, das er brauchte:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- Dieses Geheimnis $t$ war jedoch die einzige fehlende Information für Bob, um aus Alices Adaptor-Signatur $s_A'$ die gültige Signatur $s_A$ zu erzeugen, die es ihm erlaubt, die Transaktion $m_A$ zu validieren, die einen BTC von Alice an Bob sendet. Er berechnet dann $s_A$ und sendet die Transaktion $m_A$ der Reihe nach: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$