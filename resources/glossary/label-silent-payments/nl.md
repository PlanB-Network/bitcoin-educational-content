---
term: LABEL (STILLE BETALINGEN)
---

Binnen het Silent Payments protocol zijn labels gehele getallen die worden gebruikt om de initiële statische Address te wijzigen om zo vele andere statische adressen te creëren. Het gebruik van deze labels maakt het mogelijk om betalingen die via Stille Betalingen worden verzonden te scheiden, door verschillende statische adressen te gebruiken voor elk gebruik, zonder de operationele last voor het detecteren van deze betalingen (scannen) al te zeer te verhogen. Bob gebruikt een statische Address $B$, samengesteld uit twee publieke sleutels: $B_{scan}}$ voor scannen en $B_{spend}}$ voor uitgeven. De Hash van $b_{\text{scan}}$ en een geheel getal $m$, scalair vermenigvuldigd met het generatorpunt $G$, wordt toegevoegd aan de openbare sleutel $B_{\text{spend}}$ voor uitgaven om een soort nieuwe openbare sleutel $B_m$ voor uitgaven te maken:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{scan}} \text{ ‖ } m) \cdot G $$


De eerste sleutel $B_1$ wordt bijvoorbeeld op deze manier verkregen:


$$ B_1 = B_{{\text{spend}}} + \text{Hash}(b_{scan}} \text{ ‖ } 1) \cdot G $$


De statische Address gepubliceerd door Bob zal nu bestaan uit $B_{{scan}}$ en $B_m$. Bijvoorbeeld, de eerste statische Address met het label $1$ zal zijn:


$$ B = B_{{scan}} \‖ } B_1 $$


We beginnen alleen bij label $1$, omdat label $0$ gereserveerd is voor wisselgeld. Alice, die bitcoins wil sturen naar de gelabelde statische Address van Bob, zal de unieke betaling Address $P_0$ afleiden door de nieuwe $B_1$ te gebruiken in plaats van $B_{text{spend}}$:


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{scan}} \text{ ‖ } 0) \cdot G $$


In werkelijkheid weet Alice misschien niet eens dat Bob een gelabelde Address heeft, want ze gebruikt gewoon het tweede deel van de statische Address die hij heeft verstrekt, wat in dit geval de waarde $B_1$ is in plaats van $B_{\text{spend}}$. Om betalingen te scannen, zal Bob altijd de waarde van zijn initiële statische Address met $B_{text{spend}}$ op deze manier gebruiken:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Vervolgens trekt hij de waarde die hij vindt voor $P_0$ één voor één af van elke uitgang. Vervolgens controleert hij of een van de resultaten van deze aftrekkingen overeenkomt met de waarde van een van de labels die hij op zijn Wallet gebruikt. Als het overeenkomt, bijvoorbeeld voor uitgang #4 met het label $1$, betekent dit dat deze uitgang een Stille Betaling is die hoort bij zijn statische Address met het label $B_1$:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Dit werkt omdat:


$$ B_1 = B_{\text{spend}}} + \text{Hash}(b_{scan}} \text{ ‖ } 1) \cdot G $$


Dankzij deze methode kan Bob een veelheid aan statische adressen gebruiken (met $B_1$, $B_2$, $B_3$...), allemaal afgeleid van zijn basisstatica Address ($B = B_{{scan}} ‖ } B_{{scan}}$), om het gebruik goed te scheiden.


Deze scheiding van statische adressen is echter alleen geldig vanuit een persoonlijk Wallet beheerperspectief, maar staat de scheiding van identiteiten niet toe. Aangezien ze allemaal dezelfde $B_{{scan}}$ hebben, is het heel eenvoudig om alle statische adressen met elkaar te associëren en af te leiden dat ze tot één entiteit behoren.