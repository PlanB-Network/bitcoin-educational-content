---
term: COOKIE (.COOKIE)
---

Bestand gebruikt voor RPC (*Remote Procedure Call*) authenticatie in Bitcoin core. Wanneer bitcoind start, genereert het een uniek authenticatie-cookie en slaat het op in dit bestand. Clients of scripts die via RPC Interface willen communiceren met bitcoind, kunnen deze cookie gebruiken om zich veilig te authenticeren. Dit mechanisme maakt veilige communicatie mogelijk tussen bitcoind en externe toepassingen (zoals Wallet software), zonder dat handmatig beheer van gebruikersnamen en wachtwoorden nodig is. Het `.cookie` bestand wordt bij elke herstart van bitcoind opnieuw aangemaakt en bij het afsluiten verwijderd.