---
name: BIP-39 Passphrase
description: Begrijpen hoe een passphrase werkt
---
![cover](assets/cover.webp)


## Wat is een BIP39 passphrase?


HD wallets worden meestal gegenereerd uit een Mnemonic zin bestaande uit 12 of 24 woorden. Deze zin is erg belangrijk omdat het de mogelijkheid biedt om alle sleutels van een Wallet te herstellen in het geval dat het fysieke medium (zoals een Hardware Wallet, bijvoorbeeld) verloren gaat. Het is echter een enkelvoudig faalpunt, want als het gecompromitteerd wordt, kan een aanvaller alle bitcoins stelen.


![PASSPHRASE BIP39](assets/notext/01.webp)


Hier komt de passphrase om de hoek kijken. Het is een optioneel wachtwoord dat je vrij kunt kiezen en dat wordt toegevoegd aan de Mnemonic zin in het sleutelafleidingsproces om de veiligheid van de Wallet te verbeteren.


![PASSPHRASE BIP39](assets/notext/02.webp)


Verwar de passphrase niet met de PIN-code van je Hardware Wallet of het wachtwoord dat gebruikt wordt om de toegang tot je Wallet op je computer te ontgrendelen. In tegenstelling tot al deze Elements, speelt de passphrase een rol in de afleiding van de sleutels van je Wallet. **Dit betekent dat je zonder de passphrase nooit je bitcoins terug kunt krijgen.**


De passphrase werkt samen met de Mnemonic zin en verandert de seed waaruit de sleutels worden gegenereerd. Dus, zelfs als iemand je 12 of 24-woorden zin bemachtigt, zonder de passphrase, kunnen ze geen toegang krijgen tot je fondsen. **Het gebruik van een passphrase creëert in wezen een nieuwe Wallet met verschillende sleutels. Als je de passphrase (zelfs maar een beetje) wijzigt, wordt de generate een andere Wallet.**


## Waarom zou je een passphrase gebruiken?


De passphrase is willekeurig en kan elke combinatie van tekens zijn die de gebruiker kiest. Het gebruik van een passphrase biedt dus verschillende voordelen. Ten eerste vermindert het alle risico's die gepaard gaan met het compromitteren van de Mnemonic zin door een tweede factor nodig te hebben om toegang te krijgen tot het geld (inbraak, toegang tot je huis, etc.).


Vervolgens kan het strategisch gebruikt worden om een afleidings Wallet te maken, om fysieke beperkingen om je fondsen te stelen, zoals de beruchte "*$5 wrench attack*", het hoofd te bieden. In dit scenario is het de bedoeling om een Wallet zonder passphrase te hebben, die slechts een kleine hoeveelheid bitcoins bevat, genoeg om een potentiële aanvaller tevreden te stellen, terwijl je een verborgen Wallet hebt. Deze laatste gebruikt dezelfde Mnemonic zin, maar is beveiligd met een extra passphrase.


Tenslotte is het gebruik van een passphrase interessant als je de willekeurigheid van de HD Wallet's seed generatie wilt controleren.


## Hoe kies je een goede passphrase?

Om de passphrase effectief te laten zijn, moet hij lang en willekeurig genoeg zijn. Net als bij een sterk wachtwoord, raad ik aan een passphrase te kiezen die zo lang en willekeurig mogelijk is, met een variatie aan letters, cijfers en symbolen om een brute force aanval onmogelijk te maken.


Volgens [een onderzoek uitgevoerd door Trezor in 2019](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) zou een aanvaller met toegang tot je seed en met behulp van een high-end GPU gehuurd op AWS (NVIDIA Tesla V100) bijna 620 miljoen wachtzinnen kunnen testen voor 1 dollar. Als ruwe schatting, met de mogelijkheden van 2019, zou een passphrase bestaande uit 12 willekeurige kleine letters gemiddeld **77 miljoen dollar** kosten om te kraken.


Ik raad echter af om jezelf te beperken tot 12 tekens. Streef in plaats daarvan naar de huidige standaarden voor sterke wachtwoorden: streef in 2025 naar ten minste 13 willekeurige tekens, inclusief cijfers, kleine letters en hoofdletters, en symbolen; of 14 tekens als je alleen kleine letters en hoofdletters gebruikt. Natuurlijk raad ik aan om hoger te mikken, bijvoorbeeld door te kiezen voor een passphrase met 20 tekens en symbolen, om te anticiperen op toekomstige ontwikkelingen en rekening te houden met menselijke risico's die in deze onderzoeken buiten beschouwing blijven.


Het is ook belangrijk om deze passphrase goed op te slaan, op dezelfde manier als de Mnemonic zin. **Verlies betekent verlies van toegang tot je bitcoins**. Ik raad ten zeerste af om het alleen in je hoofd te onthouden, omdat dit het risico op verlies onredelijk vergroot. Het ideale is om het op te schrijven op een fysieke drager (papier of metaal), los van de Mnemonic zin. Deze back-up moet uiteraard op een andere plaats bewaard worden dan waar uw Mnemonic zin bewaard wordt om te voorkomen dat beide tegelijkertijd gecompromitteerd worden.


## Lesmateriaal


Om een passphrase in te stellen op een Ledger apparaat (Stax, Flex of Nano), kun je deze tutorial raadplegen:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Op een COLDCARD:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Op een Jade Plus:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Op een paspoort (batch-2):


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Op een Trezor-apparaat (Safe 3, Safe 5 of Model One):


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42