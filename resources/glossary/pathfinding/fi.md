---
term: PATHFINDING
---

Prosessi, jota solmu käyttää määrittääkseen optimaalisen reitin maksun reitittämiseksi Lightning-kanavaverkon kautta. Polunmäärityksen suorittaa maksajan solmu, jonka on valittava sopivimmat välityssolmut vastaanottajan tavoittamiseksi. Tämä valinta perustuu useisiin kriteereihin, kuten maksuihin, kanavakapasiteettiin ja aikarajoihin.


Polunhakualgoritmit rakentavat verkkotopologian graafin juorutiedoista ja arvioivat erilaisia mahdollisia reittejä maksajan ja vastaanottajan solmun välillä. Nämä reitit asetetaan paremmuusjärjestykseen parhaasta huonoimpaan eri kriteerien perusteella. Tämän jälkeen solmu testaa näitä reittejä, kunnes se onnistuu suorittamaan maksun jollakin niistä.