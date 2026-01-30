---
term: BCH-code
definition: Foutcorrectiecodes gebruikt in Bech32- en Bech32m-adressen om invoerfouten te detecteren.
---

Een klasse foutcorrectiecodes die worden gebruikt om fouten in een gegevensreeks op te sporen en te corrigeren. Met andere woorden, BCH foutcorrectiecodes worden gebruikt om willekeurige fouten in verzonden informatie op te sporen en te corrigeren, zodat de informatie intact aankomt op de plaats van bestemming. Het acroniem "BCH" staat voor de initialen van de namen van de uitvinders van deze codes: Bose, Ray-Chaudhuri en Hocquenghem.


Dit hulpmiddel wordt op veel gebieden van computers gebruikt, waaronder SSD's, dvd's en QR-codes. Dankzij deze foutcorrigerende codes is het bijvoorbeeld nog steeds mogelijk om de gecodeerde informatie te achterhalen, zelfs als een QR-code gedeeltelijk bedekt is.


Als onderdeel van Bitcoin worden BCH codes gebruikt voor de controlesom in Bech32 en Bech32m (post-SegWit) Address formaten. Ze vormen een beter compromis tussen de grootte van de controlesom en de mogelijkheden voor foutdetectie dan de eenvoudige Hash functies die voorheen op Legacy adressen werden gebruikt. In de context van Bitcoin worden BCH codes alleen gebruikt voor foutdetectie, niet voor foutcorrectie. Dus, Bitcoin portfoliosoftware zal fouten in een ontvangende Address identificeren en rapporteren aan de gebruiker, maar zal niet automatisch de onjuiste Address veranderen. Deze keuze is gemotiveerd door het feit dat de integratie van foutcorrectie onvermijdelijk de foutdetectiecapaciteiten van het algoritme beïnvloedt.