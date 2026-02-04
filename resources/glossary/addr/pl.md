---
term: Addr
definition: Stara wiadomość sieciowa Bitcoin, która umożliwiała komunikowanie adresów IP węzłów akceptujących połączenia. Zastąpiona przez addrv2 (BIP155) w celu obsługi dłuższych formatów adresów.
---

Wiadomość sieciowa używana wcześniej na Bitcoin do przekazywania adresów węzłów, które akceptują połączenia przychodzące. Ten stary format, ograniczony do 128 bitów na Address, był odpowiedni tylko dla adresów IPv6, IPv4 i Tor w wersji 2. Wraz z pojawieniem się nowych protokołów, takich jak Tor V3 i potrzebą lepszej skalowalności dla przyszłych protokołów sieciowych, format `addr` został zastąpiony przez `addrv2`, wprowadzony w BIP155.