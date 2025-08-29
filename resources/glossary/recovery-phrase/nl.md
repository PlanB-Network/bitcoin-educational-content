---
term: HERSTELZIN
---

Een herstelzin, soms ook Mnemonic, seed of geheime zin genoemd, is een reeks die meestal bestaat uit 12 of 24 woorden die op een pseudo-willekeurige manier gegenereerd wordt uit een bron van entropie. De pseudo-willekeurige reeks wordt altijd aangevuld met een controlesom. De Mnemonic zin, samen met een optionele passphrase, wordt gebruikt om deterministisch alle sleutels geassocieerd met een HD (Hierarchical Deterministic) Wallet af te leiden. Dit betekent dat het vanuit deze zin mogelijk is om deterministisch generate en alle private en publieke sleutels van de Bitcoin Wallet te recreëren, en dus toegang te krijgen tot de fondsen die ermee geassocieerd zijn. Het doel van de herstelzin is om een veilige en gebruiksvriendelijke manier van back-up en herstel van bitcoins te bieden.


Het is belangrijk om deze zin op een veilige plaats te bewaren, want iedereen die in het bezit is van de Mnemonic heeft toegang tot de fondsen van de overeenkomstige Wallet. Als het gebruikt wordt in de context van een traditionele Wallet, en zonder een optionele passphrase, vormt het vaak een SPOF (Single Point Of Failure). De herstelzin is dus een codering van de pseudo-willekeurige reeks en de controlesom in alledaagse woorden om de notatie en leesbaarheid voor mensen te vergemakkelijken. Ze wordt opgebouwd volgens de BIP39 standaard, die een lijst van 2048 woorden definieert en ordent die gebruikt worden voor deze codering.


> ► *De lijst met 2048 woorden van BIP39 is beschikbaar in verschillende talen, maar het is aan te raden om alleen de Engelse versie te gebruiken, omdat die het meest ondersteund wordt door Wallet software.*