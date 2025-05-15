---
term: HTLC
---

Skrót od "*Hashed Timelock Contract*". Jest to mechanizm Smart contract używany głównie w Lightning. Czasami można go również znaleźć w swapach atomowych. Zasadniczo HTLC uzależnia transfer pieniędzy od ujawnienia sekretu, a także zawiera warunek czasowy, aby chronić pieniądze nadawcy w przypadku nieudanej transakcji.


W Lightning, HTLC umożliwia wysyłanie bitcoinów do węzła, z którym nie masz bezpośredniego kanału, przechodząc przez kilka kanałów, bez potrzeby zaufania po drodze. Płatność między każdym węzłem jest uzależniona od dostarczenia obrazu wstępnego (sekretu, który po zaszyfrowaniu odpowiada uzgodnionej wartości). Jeśli odbiorca końcowy dostarczy ten obraz wstępny, może żądać środków i koniecznie umożliwia każdemu węzłowi pośredniemu kaskadowe żądanie środków.


Na przykład, jeśli Alice chce wysłać 1 BTC do Davida, ale nie ma z nim bezpośredniego kanału, musi przejść przez Boba i Carol, którzy mają ze sobą kanały płatności. Oto jak działa transakcja:




- Dawid przedstawia Alicji Invoice Błyskawicę. Zawiera on Hash $h$ sekretnego $s$ (obraz wstępny), który zna tylko Dawid. Mamy więc: $h = \text{Hash}(s)$ ;
- Alice tworzy HTLC z Bobem, który oferuje jej wysłanie 1 BTC pod warunkiem, że Bob dostarczy jej sekret $s$ (obraz wstępny), który odpowiada Hash $h$;
- Bob tworzy HTLC z Carol, która oferuje mu wysłanie 1 BTC pod warunkiem, że dostarczy ten sam sekret $s$;
- Carol tworzy HTLC z Davidem, który oferuje kolejny 1 BTC, jeśli ujawni preimage $s$;
- David ujawnia $s$ (które zna tylko on) Carol, aby otrzymać 1 BTC. Carol może teraz użyć $s$, aby otrzymać BTC od Boba. Bob, który teraz zna $s$, robi to samo z Alicją.


Na koniec Alice wysłała 1 BTC do Davida za pośrednictwem Boba i Carol (neutralne działanie dla tej ostatniej), bez konieczności wzajemnego zaufania, ponieważ wszystko jest zabezpieczone kaskadowo przez warunki HTLC.


HTLC umożliwiają zatem tak zwane "atomowe" wymiany: albo transfer jest całkowicie udany, albo nieudany, a środki są zwracane. Gwarantuje to bezpieczeństwo transakcji, nawet między wieloma uczestnikami bez potrzeby zaufania.