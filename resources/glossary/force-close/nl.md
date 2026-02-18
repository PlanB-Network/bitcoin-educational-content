---
term: Geforceerde sluiting
definition: Eenzijdige sluiting van een Lightning-kanaal door de laatst getekende commitment-transactie uit te zenden.
---

Mechanisme voor het sluiten van niet-coöperatieve Lightning-kanalen. Wanneer twee gebruikers een kanaal openen met een Multisig 2/2, kan elk van hen het kanaal eenzijdig sluiten door de laatste Commitment Transaction uit te zenden die al ondertekend is, om zo hun onchain bitcoins terug te krijgen. Dit staat bekend als "geforceerd sluiten".


Deze methode wordt meestal gebruikt als een van de deelnemers niet meer reageert, of als coöperatief sluiten van het kanaal onmogelijk is. Als geforceerd sluiten kan worden vermeden, is dat het beste, omdat het langer duurt om onchain fondsen terug te krijgen en veel duurder kan zijn in termen van vergoedingen.


Bij een gedwongen sluiting zendt één van de twee gebruikers de Commitment Transaction uit, die de laatst bekende toestand van het Lightning-kanaal weergeeft. Er is dan een tijdslot voordat de bitcoins onchain kunnen worden opgehaald, waardoor de andere partij tijd heeft om te verifiëren dat de transactie overeenkomt met de laatste kanaalstatus. Als een gebruiker probeert vals te spelen door een verouderde Commitment Transaction te publiceren, kan de andere partij het herroepingsgeheim gebruiken om de valsspeler te straffen en alle fondsen in het kanaal terug te krijgen.