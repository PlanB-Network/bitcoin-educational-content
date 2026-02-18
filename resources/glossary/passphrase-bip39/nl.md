---
term: Passphrase (BIP39)
definition: Optioneel wachtwoord toegevoegd aan de herstelzin om een HD-wallet te beveiligen.
---

Een optioneel wachtwoord dat, in combinatie met de herstelzin, een extra Layer beveiliging biedt voor deterministische en hiërarchische Bitcoin wallets. HD wallets worden meestal gegenereerd met een herstelzin bestaande uit 12 of 24 woorden. Deze herstelzin is erg belangrijk, omdat hiermee alle sleutels in een Wallet hersteld kunnen worden in geval van verlies. Het is echter een Single Point of Failure (SPOF). Als het gecompromitteerd is, lopen de bitcoins gevaar. Hier komt de passphrase om de hoek kijken. Het is een optioneel wachtwoord, gekozen door de gebruiker, dat wordt toegevoegd aan de herstelzin om de beveiliging van de Wallet te verbeteren. Niet te verwarren met een pincode of een gewoon wachtwoord, speelt de passphrase een rol bij het afleiden van cryptografische sleutels.


Het werkt samen met de herstelzin en wijzigt de seed waaruit de sleutels worden gegenereerd. Dus zelfs als iemand uw herstelzin bemachtigt, heeft hij zonder de passphrase geen toegang tot uw fondsen. Het gebruik van een passphrase creëert in wezen een nieuwe Wallet met verschillende sleutels. Als je de passphrase (ook al is het maar een klein beetje) wijzigt, ontstaat er een andere Wallet.


De passphrase is willekeurig en kan elke combinatie van tekens zijn die de gebruiker kiest. Het gebruik van een passphrase biedt verschillende voordelen. Ten eerste vermindert het de risico's die gepaard gaan met het compromitteren van de herstelzin door een tweede factor nodig te hebben om toegang te krijgen tot de fondsen. Daarnaast kan het strategisch gebruikt worden om decoy wallets te maken met kleine hoeveelheden bitcoins, in het geval van fysieke dwang om je fondsen te stelen. Tot slot is het gebruik ervan interessant wanneer men de willekeurigheid van de HD Wallet seed generatie wil controleren. De passphrase moet voldoende complex zijn om brute force aanvallen te weerstaan en moet betrouwbaar worden opgeslagen. Het verlies van de passphrase kan leiden tot het onvermogen om toegang te krijgen tot fondsen, net als het verlies van de herstelzin.


> *De passphrase wordt soms ook aangeduid als: "twee-factor seed zinsdeel," "wachtwoord," "seed uitbreiding," "uitbreidingswoord," of zelfs "13e of 25e woord." Het is goed om te weten dat er twee soorten wachtzinnen zijn op Bitcoin. De meest bekende is die hierboven beschreven. De meest bekende is de hierboven beschreven, die afhankelijk is van BIP-39, en waarmee een hele HD Wallet beveiligd kan worden. BIP-38 had echter ook een manier gespecificeerd om een unieke private sleutel met een passphrase te beveiligen. Dit tweede type passphrase wordt tegenwoordig bijna niet meer gebruikt.*