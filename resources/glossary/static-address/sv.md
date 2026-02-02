---
term: Statisk adress
definition: Unik identifierare för Silent Payments som gör det möjligt att ta emot betalningar utan adressåteranvändning eller synlig on-chain-koppling.
---

I samband med tysta betalningar avser en unik identifierare som gör det möjligt att ta emot betalningar utan Address-återanvändning, utan interaktion och utan en synlig On-Chain-länk mellan de olika betalningarna och den statiska Address. Denna teknik eliminerar behovet av att generate nya, oanvända mottagningsadresser för varje transaktion, och därmed undviker man de vanliga interaktionerna i Bitcoin där mottagaren måste tillhandahålla en ny Address till betalaren. Det motsvarar i viss mån den återanvändbara betalningskoden i samband med BIP47.


Denna Address består av två offentliga nycklar: $B_{\text{scan}}$ för skanning och $B_{\text{spend}}$ för utgifter, sammanlänkade för att bilda den statiska Address $B = B_{\text{scan}} \text{ ‖ } B_{\text{spendera}}$. Mottagaren publicerar denna Address, vilket gör att avsändarna kan härleda unika betalningsadresser utan ytterligare interaktion med mottagaren. För att hantera flera olika betalningskällor kan en etikett läggas till $B_{\text{spend}}$, vilket skapar flera etiketterade statiska adresser från $B_1$, $B_2$ osv. Detta gör det möjligt att separera betalningar samtidigt som man använder en enda bas Address, vilket minskar arbetsbelastningen för Blockchain-skanning. Alla statiska adresser för en enhet kan dock lätt associeras på grund av den gemensamma användningen av $B_{\text{scan}}$.