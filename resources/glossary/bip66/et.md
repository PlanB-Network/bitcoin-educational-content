---
term: BIP66

---
Viidi sisse tehingute allkirjaformaadi standardimine. See piirmääruse ettepanek tehti vastuseks erinevusele viisis, kuidas OpenSSL käsitles allkirjade kodeerimist erinevates süsteemides. See ebaühtlus kujutas endast plokiahela lõhestamise ohtu. BIP66 standardiseeris allkirjaformaadi kõigi tehingute puhul, kasutades ranget DER-kodeerimist (*eristunud kodeerimiseeskirjad*). See muudatus nõudis soft forki. Aktiveerimiseks kasutas BIP66 seejärel sama mehhanismi nagu BIP34, nõudes, et "nVersion" väli suurendataks versioonini 3, ja lükkas tagasi kõik versioon 2 või madalamad plokid, kui 95% kaevurite künnis oli saavutatud. See künnis ületati 4. juulil 2015. aastal plokis number 363,725.