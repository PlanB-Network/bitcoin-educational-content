---
term: P2PKH
---

P2PKH to skrót od *Pay to Public Key Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydawania na UTXO. Pozwala on na zablokowanie bitcoinów na Hash klucza publicznego, czyli na odbierającym Address. Skrypt ten jest powiązany ze standardem Legacy i został wprowadzony we wczesnych wersjach Bitcoin przez Satoshi Nakamoto.


W przeciwieństwie do P2PK, gdzie klucz publiczny jest wyraźnie zawarty w skrypcie, P2PKH wykorzystuje kryptograficzny odcisk palca klucza publicznego. Ten skrypt zawiera `RIPEMD160` Hash z `SHA256` klucza publicznego i stanowi, że aby uzyskać dostęp do środków, odbiorca musi dostarczyć klucz publiczny, który pasuje do tego Hash, a także ważny podpis cyfrowy wygenerowany z powiązanego klucza prywatnego. Adresy P2PKH są kodowane przy użyciu formatu `Base58Check`, który zapewnia im odporność na błędy typograficzne poprzez użycie sumy kontrolnej. Adresy te zawsze zaczynają się od cyfry `1`.