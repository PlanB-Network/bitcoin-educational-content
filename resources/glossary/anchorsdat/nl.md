---
term: Anchors.dat
definition: Een Bitcoin Core-bestand dat IP-adressen van knooppunten opslaat waarmee de client voor afsluiting was verbonden, om herverbinding bij herstart te vergemakkelijken.
---

Bestand dat gebruikt wordt in de Bitcoin core client om de IP adressen op te slaan van uitgaande knooppunten waarmee een client verbonden was voordat hij werd afgesloten. Anchors.dat wordt dus iedere keer aangemaakt als het knooppunt wordt gestopt en verwijderd als het weer wordt opgestart. De knooppunten waarvan het IP adres in dit bestand staat, worden gebruikt om snel verbindingen tot stand te brengen als het knooppunt opnieuw wordt opgestart.