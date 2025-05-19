---
term: ADDRV2
---

Proponowana ewolucja wraz z BIP155 wiadomości `addr` w sieci Bitcoin. Wiadomość `addr` była używana do nadawania adresów węzłów, które akceptowały połączenia przychodzące, ale była ograniczona do 128-bitowych adresów. Rozmiar ten był odpowiedni dla adresów IPv6, IPv4 i Tor V2, ale niewystarczający dla innych protokołów. Zaktualizowana wersja `addrv2` została zaprojektowana do obsługi dłuższych adresów, w tym 256-bitowych ukrytych usług Tor v3, a także innych protokołów sieciowych, takich jak I2P lub przyszłych protokołów.