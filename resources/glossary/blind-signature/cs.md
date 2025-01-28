---
term: SLEPÝ PODPIS

---
Chaumovy slepé podpisy jsou formou digitálního podpisu, kdy vystavitel podpisu nezná obsah podepisované zprávy. Podpis však lze později ověřit pomocí původní zprávy. Tuto techniku vyvinul v roce 1983 kryptograf David Chaum.

Vezměme si příklad společnosti, která chce ověřit důvěrný dokument, například smlouvu, aniž by odhalila jeho obsah. Společnost použije proces maskování, který kryptograficky transformuje původní dokument reverzibilním způsobem. Takto upravený dokument je zaslán certifikační autoritě, která použije slepý podpis, aniž by znala základní obsah. Po obdržení maskovaného podepsaného dokumentu společnost zruší maskování podpisu. Výsledkem je původní dokument ověřený podpisem autority, aniž by autorita kdy viděla původní obsah.

Chaumovy slepé podpisy tak umožňují ověřit pravost dokumentu bez znalosti jeho obsahu, čímž je zajištěna jak důvěrnost dat uživatele, tak integrita podepsaného dokumentu.

V Bitcoinu se tento protokol používá v systémech chaumských bank jako překryvný (Cashu, Fedimint atd.), ale zejména v chaumských protokolech coinjoin, aby se zajistilo, že koordinátor nebude schopen propojit vstup s výstupem.