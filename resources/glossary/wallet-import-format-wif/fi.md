---
term: (WIF)

---
Menetelmä Bitcoinin yksityisen avaimen koodaamiseksi siten, että se voidaan tuoda tai viedä helpommin eri lompakoiden välillä. WIF perustuu `Base58Check`-koodaukseen, joka sisältää tiedot versiosta, vastaavan julkisen avaimen pakkauksen ja tarkistussumman virheiden havaitsemista varten kirjoittamisessa. WIF-avain alkaa merkillä `5` pakkaamattomien avainten osalta tai `K` ja `L` pakattujen avainten osalta, ja se sisältää kaikki merkit, joita tarvitaan alkuperäisen yksityisen avaimen rekonstruoimiseksi. WIF-muoto tarjoaa standardoidun keinon siirtää yksityinen avain eri lompakko-ohjelmistojen välillä.