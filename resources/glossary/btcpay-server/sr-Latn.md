---
term: BTCPay Server
definition: Open-source procesor plaćanja koji omogućava prihvatanje bitkoin plaćanja bez posrednika.
---

⚠️ **Kritično bezbednosno upozorenje (7. avgust 2026):** kritična ranjivost koja pogađa BTCPay Server se aktivno zloupotrebljava i može dovesti do gubitka sredstava. Odmah ažurirajte svoju instancu na **verziju 2.4.2** putem `Admin Dashboard > Server > Maintenance > Update`, a zatim proverite da li podnožje stranice prikazuje `2.4.2`. Ako ne možete odmah da ažurirate, ugasite svoj BTCPay Server. Nakon ažuriranja, morate takođe u potpunosti osvežiti svoje macaroons i svoj `macaroons.db`, u potpunosti osvežiti autentifikacione stringove svakog drugog Lightning backend-a, a ako ste unutar BTCPay Server-a generisali „vruć" on-chain novčanik, prebacite ta sredstva i ponovo kreirajte novčanik. Integratori bi takođe trebalo da ažuriraju NBXplorer na verziju 2.6.10. Izvor: [Napomene uz izdanje BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server je open-source procesor plaćanja koji omogućava trgovcima i korisnicima da prihvate Bitcoin plaćanja bez oslanjanja na treću stranu za obradu transakcija. Pokrenut 2017. godine, BTCPay Server pruža rešenje za integraciju Bitcoin plaćanja za e-commerce sajtove, sa naprednim funkcijama kao što su podrška za hardverske novčanike, alati za fakturisanje i računovodstvo, kao i kompatibilnost sa Lightning Network. Njegov razvoj je inicirao Nicolas Dorier, kao odgovor na akcije Bitpay-a koji je, prema njegovim rečima, obmanuo svoje korisnike gurajući ih ka usvajanju SegWit2x, koji je kompanija pogrešno smatrala "pravim" Bitcoin. Ova opozicija je bila sažeta u sada već čuvenom tvitu Nicolasa Doriera iz avgusta 2017:


> "_Ovo su laži, moje poverenje u tebe je slomljeno, učiniću te zastarelim_".

