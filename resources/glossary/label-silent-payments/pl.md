---
term: ETYKIETA (CICHE PŁATNOŚCI)
---

W protokole Silent Payments etykiety są liczbami całkowitymi używanymi do modyfikacji początkowego statycznego Address w celu utworzenia wielu innych adresów statycznych. Zastosowanie tych etykiet pozwala na segregację płatności wysyłanych za pośrednictwem Silent Payments, poprzez zastosowanie różnych adresów statycznych dla każdego użycia, bez nadmiernego zwiększania obciążenia operacyjnego związanego z wykrywaniem tych płatności (skanowanie). Bob używa statycznego Address $B$, składającego się z dwóch kluczy publicznych: $B_{\text{scan}}$ do skanowania i $B_{\text{spend}}$ do wydawania. Hash $b_{\text{scan}}$ i liczba całkowita $m$, pomnożona skalarnie przez punkt generatora $G$, jest dodawana do klucza publicznego $B_{\text{spend}}$ w celu utworzenia nowego klucza publicznego $B_m$:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$


Na przykład, pierwszy klucz $B_1$ jest uzyskiwany w ten sposób:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Statyczny Address opublikowany przez Boba będzie teraz składał się z $B_{\text{scan}}$ i $B_m$. Na przykład pierwszy statyczny Address z etykietą $1$ będzie miał postać:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


Zaczynamy tylko od etykiety $1$, ponieważ etykieta $0$ jest zarezerwowana dla zmian. Alicja, która chce wysłać bitcoiny do oznaczonego etykietą statycznego Address dostarczonego przez Boba, wyprowadzi unikalną płatność Address $P_0$ używając nowego $B_1$ zamiast $B_{\text{spend}}$:


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


W rzeczywistości Alicja może nawet nie wiedzieć, że Bob ma oznaczony Address, ponieważ po prostu używa drugiej części statycznego Address, który dostarczył, co w tym przypadku jest wartością $B_1$, a nie $B_{\text{spend}}$. Aby skanować w poszukiwaniu płatności, Bob zawsze będzie używał wartości swojego początkowego statycznego Address z $B_{\text{spend}}$ w ten sposób:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Następnie po prostu odejmuje wartość $P_0$ od każdego wyjścia po kolei. Następnie sprawdza, czy jeden z wyników tych odejmowań odpowiada wartości jednej z etykiet, których używa na swoim Wallet. Jeśli pasuje, na przykład, dla wyjścia #4 z etykietą $1$, oznacza to, że to wyjście jest Silent Payment powiązanym z jego statycznym Address oznaczonym $B_1$:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Działa to, ponieważ:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Dzięki tej metodzie Bob może używać wielu statycznych adresów (z $B_1$, $B_2$, $B_3$...), wszystkie wywodzące się z jego bazowego statycznego Address ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), w celu właściwego rozdzielenia zastosowań.


Jednak to rozdzielenie adresów statycznych jest ważne tylko z perspektywy zarządzania osobistym Wallet, ale nie pozwala na oddzielenie tożsamości. Ponieważ wszystkie mają ten sam $B_{\text{scan}}$, bardzo łatwo jest powiązać wszystkie statyczne adresy razem i wywnioskować, że należą one do jednej jednostki.