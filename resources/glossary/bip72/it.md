---
term: BIP72

---
Completa BIP70 e BIP71 definendo l'estensione di Bitcoin URI (BIP21) con un parametro aggiuntivo `r`. Questo parametro consente di includere un link a una richiesta di pagamento sicuro firmata dal certificato SSL del commerciante. Quando un cliente clicca su questo URI esteso, il suo portafoglio contatta il server del commerciante per richiedere i dettagli del pagamento. Questi dettagli vengono automaticamente inseriti nell'interfaccia di transazione del portafoglio e il cliente può essere informato che sta pagando il proprietario del dominio corrispondente al certificato di firma (ad esempio, "pandul.fr"). Poiché questa miglioria è inclusa nel BIP70, non è mai stata adottata su larga scala.