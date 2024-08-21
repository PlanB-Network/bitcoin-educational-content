---
term: BLIND SIGNATURE
---

Slepé podpisy Chauma jsou formou digitálního podpisu, kde vydavatel podpisu nezná obsah zprávy, kterou podepisuje. Podpis lze později ověřit s původní zprávou. Tuto techniku vyvinul kryptograf David Chaum v roce 1983.

Uvažujme příklad společnosti, která chce ověřit pravost důvěrného dokumentu, jako je smlouva, aniž by odhalila jeho obsah. Společnost použije maskovací proces, který kryptograficky transformuje původní dokument reverzibilním způsobem. Tento modifikovaný dokument je poslán certifikační autoritě, která aplikuje slepý podpis, aniž by znala podkladový obsah. Po obdržení maskovaného podepsaného dokumentu společnost odmaskuje podpis. Výsledkem je původní dokument ověřený podpisem autority, aniž by autorita kdy viděla původní obsah.

Takto slepé podpisy Chauma umožňují ověření pravosti dokumentu bez znalosti jeho obsahu, čímž zajišťují jak důvěrnost údajů uživatele, tak integritu podepsaného dokumentu.

V Bitcoinu se tento protokol používá v systémech Chaumových bank jako překryvná vrstva (Cashu, Fedimint atd.), ale zejména v protokolech Chaumian coinjoin, aby se zajistilo, že koordinátor není schopen spojit vstup s výstupem.