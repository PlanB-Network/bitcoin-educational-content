---
term: BIP0143
definition: Ny hash-algoritm för SegWit-signaturer, som löser kvadratisk tillväxt och inkluderar värdet på inputs.
---

Introducerar ett nytt sätt att hasha transaktionen för signaturverifiering i post-SegWit-skript. Målet är att minimera överflödiga operationer under verifieringen och att inkludera värdet på UTXO:erna i indata i signaturen. Detta löser två stora problem med den ursprungliga algoritmen för transaktionshashning:


- Den kvadratiska tillväxten av datahashing med antalet signaturer;
- Avsaknaden av att inkludera ingångsvärdet i signaturen, vilket utgjorde en risk för hårdvaruplånböcker, särskilt när det gäller kunskapen om uppkomna transaktionsavgifter.

Eftersom SegWit uppdateringen, som förklaras i BIP141, introducerar en ny form av transaktioner vars manus inte kommer att verifieras av gamla noder, tar BIP143 tillfället i akt att Address denna fråga utan att kräva en Hard Fork. Därför är BIP143 en del av SegWit Soft Fork.