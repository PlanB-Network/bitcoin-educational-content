---
term: DIFFIE-HELLMAN

---
Kryptografická metoda, která umožňuje dvěma stranám generovat sdílené tajemství přes nezabezpečený komunikační kanál. Toto tajemství pak lze použít k šifrování komunikace mezi oběma stranami. Diffie-Hellman používá modulární aritmetiku, takže i když útočník může sledovat výměny, nemůže odvodit sdílené tajemství bez vyřešení obtížné matematické úlohy: diskrétního logaritmu. V Bitcoinu se někdy používá varianta DH zvaná ECDH, která používá eliptickou křivku, zejména pro protokoly se statickou adresou, jako jsou Silent Payments nebo BIP47.