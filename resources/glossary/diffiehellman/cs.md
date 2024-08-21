---
term: DIFFIE-HELLMAN
---

Kryptografická metoda, která umožňuje dvěma stranám generovat sdílené tajemství prostřednictvím nezabezpečeného komunikačního kanálu. Toto tajemství pak může být použito pro šifrování komunikace mezi oběma stranami. Diffie-Hellman využívá modulární aritmetiku, takže i když útočník může pozorovat výměny, nemůže bez řešení obtížného matematického problému - diskrétního logaritmu - odvodit sdílené tajemství. V Bitcoinu se někdy používá varianta DH nazvaná ECDH, která využívá eliptickou křivku, zejména pro protokoly se statickými adresami jako jsou Silent Payments nebo BIP47.