---
term: chain code
---

In de context van hiërarchische deterministische (HD) afleiding van Bitcoin wallets, is de chain code een 256-bit cryptografische zoutwaarde die gebruikt wordt om generate kindsleutels af te leiden van een oudersleutel, volgens de BIP32 standaard. De chain code wordt gebruikt in combinatie met de oudersleutel en de index van het kind om deterministisch generate een nieuw sleutelpaar (private sleutel en publieke sleutel) te maken zonder de oudersleutel of andere afgeleide kindsleutels te onthullen.


Daarom is er een unieke chain code voor elk sleutelpaar. De chain code wordt verkregen door de seed van de Wallet te hashen en de rechterhelft van de bits te nemen. In dit geval wordt het een master chain code genoemd, geassocieerd met de master private sleutel. Het kan ook verkregen worden door een oudersleutel te hashen met zijn chain code en een index, en dan de juiste bits te houden. Dit wordt dan een child chain code genoemd.


Het is onmogelijk om sleutels af te leiden zonder de chain code geassocieerd met elk ouderpaar te kennen. Het introduceert pseudo-willekeurige gegevens in het afleidingsproces om ervoor te zorgen dat het genereren van cryptografische sleutels onvoorspelbaar blijft voor aanvallers, terwijl het deterministisch is voor de Wallet houder.


> ► *In het Engels wordt een "code de chaîne" een "chain code" genoemd, en een "code de chaîne maître" een "master chain code".*