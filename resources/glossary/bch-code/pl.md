---
term: KOD BCH
---

Klasa kodów korekcji błędów używanych do wykrywania i korygowania błędów w sekwencji danych. Innymi słowy, kody korekcji błędów BCH są używane do znajdowania i korygowania losowych błędów w przesyłanych informacjach, aby zapewnić, że dotrą one do miejsca przeznaczenia w nienaruszonym stanie. Skrót "BCH" oznacza inicjały nazwisk wynalazców tych kodów: Bose, Ray-Chaudhuri i Hocquenghem.


Narzędzie to jest wykorzystywane w wielu obszarach informatyki, w tym w dyskach SSD, DVD i kodach QR. Na przykład, dzięki tym kodom korygującym błędy, nawet jeśli kod QR jest częściowo zakryty, nadal możliwe jest odzyskanie zakodowanych w nim informacji.


Jako część Bitcoin, kody BCH są używane do sumy kontrolnej w formatach Bech32 i Bech32m (post-SegWit) Address. Stanowią one lepszy kompromis między rozmiarem sumy kontrolnej a możliwościami wykrywania błędów niż proste funkcje Hash używane wcześniej w adresach Legacy. W kontekście Bitcoin kody BCH są używane tylko do wykrywania błędów, a nie do korekcji błędów. W związku z tym oprogramowanie portfela Bitcoin zidentyfikuje i zgłosi użytkownikowi wszelkie błędy w odbierającym Address, ale nie zmieni automatycznie nieprawidłowego Address. Wybór ten wynika z faktu, że integracja korekcji błędów nieuchronnie wpływa na możliwości wykrywania błędów przez algorytm.