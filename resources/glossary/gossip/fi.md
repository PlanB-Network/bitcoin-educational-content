---
term: GOSSIP
---

Gossip on vertaisverkon (P2P) hajautettu algoritmi, jolla tietoa levitetään epidemianomaisesti kaikille verkon toimijoille. Bitcoin-, Lightning- ja muissa hajautetuissa järjestelmissä tämä protokolla mahdollistaa solmujen Global State:n vaihtamisen ja synkronoinnin muutamassa syklissä. Kukin solmu levittää tietoa yhdelle tai useammalle satunnaiselle tai ei-sattumanvaraiselle naapurille, jotka puolestaan levittävät tietoa muille naapureille ja niin edelleen, kunnes saavutetaan globaalisti synkronoitu tila.


Lightningissa juorut ovat solmujen välinen viestintäprotokolla, jonka avulla jaetaan tietoa verkon nykytilasta ja topologiasta. Juoruprotokollan avulla solmut voivat tietää maksukanavien ja muiden solmujen dynaamisen tilan, mikä helpottaa maksutapahtumien reitittämistä verkon kautta ilman, että kaikkien solmujen välille tarvitaan suoria yhteyksiä.


> ► *Ranskan kielessä "juorupöytäkirja" voidaan kääntää "protocole de bavardage". Lähde: https://dl.acm.org/doi/pdf/10.1145/41840.41841.*