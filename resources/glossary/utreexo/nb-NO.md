---
term: UTREEXO

---
Protokoll utviklet av Tadge Dryja for å komprimere Bitcoin-nodenes UTXO-sett ved hjelp av en akkumulator basert på Merkle-trær. I motsetning til det klassiske UTXO-settet, som krever betydelig lagringsplass, reduserer Utreexo minnebehovet drastisk ved kun å lagre røttene til Merkle-treet. Dette gjør at noden kan verifisere eksistensen av UTXO-er som brukes i transaksjonsinndata, uten å måtte lagre hele settet av UTXO-er. Ved å bruke Utreexo beholder hver node bare et kryptografisk fingeravtrykk som kalles en Merkle-rot. Når en transaksjon gjennomføres, leverer brukeren bevis på eierskap til UTXO-ene og de tilhørende Merkle-stiene. Dermed kan noden verifisere transaksjoner uten å lagre hele UTXO-settet. La oss ta et eksempel med et diagram for å forstå denne mekanismen:

![](../../dictionnaire/assets/15.webp)

I dette eksempelet har jeg med vilje redusert UTXO-settet til 4 UTXOer for å gjøre det lettere å forstå. I virkeligheten er det viktig å forestille seg at det finnes nesten 140 millioner UTXOer på Bitcoin når disse linjene skrives. I dette diagrammet trenger Utreexo-noden bare å oppbevare Merkle Root i RAM. Hvis den mottar en transaksjon som bruker UTXO nr. 3 (i svart), vil beviset bestå av følgende elementer:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Med denne informasjonen fra transaksjonsavsenderen utfører Utreexo-noden følgende verifiseringer:


- Den beregner avtrykket til UTXO 3, noe som gir den HASH 3;
- Den sammenkjeder HASH 3 med HASH 4;
- Den beregner avtrykket deres, noe som gir den HASH 3-4;
- Den sammenkjeder HASH 3-4 med HASH 1-2;
- Den beregner avtrykket deres, noe som gir den Merkle-roten.

Hvis Merkle-roten den får gjennom prosessen, er den samme som Merkle-roten den har lagret i RAM-minnet, er den overbevist om at UTXO nr. 3 faktisk er en del av UTXO-settet.

Denne metoden reduserer RAM-kravene for operatører med full node. Utreexo har imidlertid begrensninger, blant annet en økning i blokkstørrelsen på grunn av ekstra bevis og Utreexo-nodenes potensielle avhengighet av bronoder for å få tak i manglende bevis. Bronoder er tradisjonelle fullstendige noder som leverer de nødvendige bevisene til Utreexo-noder, og dermed muliggjør full verifisering. Denne tilnærmingen er et kompromiss mellom effektivitet og desentralisering, og gjør transaksjonsvalidering mer tilgjengelig for brukere med begrensede ressurser.