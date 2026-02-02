---
term: Invoice lightning
definition: Lightning-Zahlungsaufforderung, die alle für die Durchführung der Transaktion erforderlichen Informationen enthält.
---

Vom Empfänger erstellte Blitzzahlungsanforderung, die alle für den Abschluss der Transaktion erforderlichen Informationen enthält.


Ein Invoice Lightning enthält das Zahlungsziel in Form des öffentlichen Schlüssels des Empfängerknotens, aber auch ein "LN"-Präfix, den Betrag, eine Zeit bis zum Verfall, den Hash des in HTLCs verwendeten Geheimnisses und andere Metadaten, von denen einige optional sind, wie z. B. Routing-Optionen. Diese Rechnungen werden durch den BOLT11-Standard definiert. Einmal bezahlt, kann ein Invoice Lightning nicht wiederverwendet werden.


