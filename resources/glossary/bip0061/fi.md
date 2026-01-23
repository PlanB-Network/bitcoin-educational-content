---
term: BIP0061

definition: Solmujen välinen hylkäysviesti, joka kertoo, miksi siirto tai lohko on virheellinen. Poistettu käytöstä Bitcoin Core 0.20.0 -versiossa.
---
Otettiin käyttöön hylkäämisviesti solmujen välisessä viestintäprotokollassa. BIP61:n tavoitteena on lisätä palautemekanismi, kun solmu vastaanottaa toiselta solmulta transaktion tai lohkon, jota se pitää virheellisenä. Hylkäysviestin avulla solmu voisi ilmoittaa lähettäjälle syyn, miksi se hylättiin. Tämäntyyppisen viestinnän tarkoituksena oli parantaa eri asiakkaiden välistä yhteentoimivuutta sekä täysien solmujen ja SPV-asiakkaiden välistä viestintää. BIP61:n mukanaan tuomista toiminnallisuuksista luovuttiin lopulta Bitcoin Coren versiosta 0.20.0 alkaen, koska niitä pidettiin tarpeettomina, koska ne lisäsivät kaistanleveyden tarvetta.