---
term: HASHCASH
---

HashCash to system Proof-of-Work zaprojektowany przez Adama Back'a w 1997 roku w celu zwalczania spamu i ataków DoS. Opiera się on na zasadzie, że nadawca musi wykonać zadanie obliczeniowe (w szczególności znaleźć częściową kolizję w kryptograficznej funkcji Hash), aby udowodnić swoją pracę. Zadanie to jest kosztowne pod względem czasu i energii dla nadawcy, ale weryfikacja wyniku przez odbiorcę jest szybka i prosta. Protokół ten okazał się szczególnie odpowiedni do zwalczania spamu w komunikacji e-mail, ponieważ jest minimalnie uciążliwy dla legalnych użytkowników, stanowiąc jednocześnie znaczną przeszkodę dla spamerów. Rzeczywiście, wysłanie pojedynczej wiadomości e-mail wymaga kilku sekund obliczeń, ale powtórzenie tej operacji miliony razy staje się niezwykle kosztowne pod względem energii i czasu, co często neguje ekonomiczny interes kampanii spamowych, niezależnie od tego, czy są one prowadzone w celach marketingowych, czy złośliwych. Co więcej, pozwala to na zachowanie anonimowości nadawcy.


HashCash został szybko przyjęty przez cypherpunks, którzy chcieli opracować anonimowy system waluty elektronicznej bez pośredników. Rzeczywiście, innowacja Adama Backa po raz pierwszy wprowadziła koncepcję niedoboru w cyfrowym świecie. Koncepcję Proof of Work można następnie znaleźć w kilku systemach walut elektronicznych poprzedzających Bitcoin, w tym:


- b-money autorstwa Wei Dai opublikowany w 1998 roku;
- R-POW autorstwa Hala Finneya wydany w 2004 roku;
- BitGold autorstwa Nicka Szabo opublikowany w 2005 roku.


Zasada działania HashCash znajduje się również w protokole Bitcoin, gdzie jest wykorzystywana jako mechanizm ochrony przed atakami Sybil.