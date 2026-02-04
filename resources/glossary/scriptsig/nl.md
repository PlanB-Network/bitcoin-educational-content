---
term: Scriptsig
definition: Input-element dat de gegevens levert om aan de scriptPubKey-voorwaarden te voldoen.
---

Een element in een Bitcoin transactie dat zich in de ingangen bevindt. De `scriptSig` verschaft de noodzakelijke gegevens om te voldoen aan de voorwaarden gesteld door de `scriptPubKey` van de vorige transactie waaruit fondsen worden uitgegeven. Het speelt dus een aanvullende rol op de `scriptPubKey`. Typisch bevat het `scriptSig` een digitale handtekening en een publieke sleutel. De handtekening wordt gegenereerd door de eigenaar van de bitcoins met behulp van zijn privésleutel en bewijst dat hij toestemming heeft om de UTXO uit te geven. In dit geval toont het `scriptSig` aan dat de houder van de input de private sleutel bezit die overeenkomt met de publieke sleutel die is geassocieerd met de Address die is gespecificeerd in de `scriptPubKey` van de vorige uitgaande transactie.


Als de transactie is geverifieerd, worden de gegevens uit het `scriptSig` uitgevoerd in de corresponderende `scriptPubKey`. Als het resultaat geldig is, betekent dit dat aan de voorwaarden voor het uitgeven van het geld is voldaan. Als alle ingangen van de transactie een `scriptSig` geven die hun `scriptPubKey` valideert, is de transactie geldig en kan deze worden toegevoegd aan een blok voor uitvoering.


Hier is bijvoorbeeld een klassiek P2PKH `scriptSig`:


```text
<signature> <public key>
```


De bijbehorende `scriptPubKey` zou zijn:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```





> ► *Het `scriptSig` wordt in het Engels ook wel een "unlocking script" genoemd.*