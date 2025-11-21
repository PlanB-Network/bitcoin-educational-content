---
term: BIP0330
---

Propozycja znana jako "*Erlay*", której celem jest optymalizacja propagacji niepotwierdzonych transakcji w sieci Bitcoin. Obecnie transakcje są rozgłaszane do wszystkich węzłów równorzędnych, co powoduje redundancję i nadmierne wykorzystanie przepustowości. BIP330 proponuje domyślnie ograniczyć tę transmisję do 8 peerów, a następnie użyć mechanizmu uzgadniania, aby efektywnie udostępniać brakujące transakcje. Erlay zmniejsza zużycie przepustowości o około 40%. Pozwala również uniknąć liniowego wzrostu zużycia przepustowości wraz z liczbą peerów podłączonych do węzła.