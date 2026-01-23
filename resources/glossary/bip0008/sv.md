---
term: BIP0008
definition: Metod för att aktivera soft forks som integrerar en automatisk UASF-mekanism om miners inte signalerar sitt stöd inom den angivna tiden.
---

BIP8 utvecklades efter debatterna om SegWit, som använde BIP9 för sin aktivering, och är en Soft Fork-aktiveringsmetod som naturligt innehåller en automatisk UASF-mekanism (*User-Activated Soft Fork*). Precis som BIP9 använder BIP8 Miner-signalering men lägger till parametern `LOT` (*Lock-in On Time out*). Om `LOT` är inställd på `true` utlöses automatiskt en UASF när signaleringsperioden har löpt ut utan att det nödvändiga tröskelvärdet har uppnåtts, vilket tvingar fram aktivering av Soft Fork. Detta tillvägagångssätt tvingar gruvarbetare att samarbeta eller riskera en UASF som införs av användarna. Till skillnad från BIP9 definierar BIP8 dessutom signaleringsperioden baserat på blockhöjd, vilket eliminerar potentiella manipulationer genom Hash-frekvensen av gruvarbetare. BIP8 gör det också möjligt att ställa in en variabel röstningströskel och introducerar en parameter för en minsta blockhöjd för aktivering, vilket ger gruvarbetare tid att förbereda sig och signalera sitt avtal i förväg utan att nödvändigtvis vara redo. När en Soft Fork aktiveras via BIP8 med parametern `LOT=true` används en mycket aggressiv metod mot gruvarbetare som omedelbart utsätts för trycket av en potentiell UASF. Det ger dem faktiskt bara 2 val:


- Var samarbetsvillig och underlätta på så sätt aktiveringsprocessen;
- Inte är samarbetsvillig, i vilket fall användare automatiskt utför en UASF för att införa Soft Fork.