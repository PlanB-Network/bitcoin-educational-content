---
term: Address spoofing
definition: Atak, w którym złośliwy aktor tworzy adres bardzo podobny do adresu ofiary, aby ją oszukać i przenieść jej płatności.
---

Atak, w którym złośliwy aktor tworzy Address (lub inny identyfikator płatności) bardzo przypominający identyfikator ofiary. Celem jest nakłonienie użytkownika do skopiowania tego błędnego Address podczas transakcji, co skutkuje wysłaniem bitcoinów do atakującego zamiast do zamierzonego miejsca docelowego.



Atakujący wykorzystuje pośpiech użytkownika do skopiowania niewłaściwego Address, jeśli przeprowadza on transakcję bez sprawdzenia jej dokładności. Ogólnie rzecz biorąc, aby wdrożyć ten atak, atakujący dokonuje płatności niewielkimi kwotami na Wallet ofiary, aby zintegrować fałszywy Address z jego historią transakcji. Atak ten jest zwykle stosowany w przypadku altcoinów, gdzie powszechną praktyką jest ponowne wykorzystywanie tych samych adresów odbiorczych, w przeciwieństwie do Bitcoin, gdzie używanie pustych adresów dla każdej transakcji jest bardziej powszechną praktyką. Jednak użytkownicy Bitcoin nie są odporni na ten atak.



Inną metodą przedstawienia ofierze błędnego adresu jest użycie oszukańczego oprogramowania do zarządzania portfelami, które imituje legalne oprogramowanie, lub modyfikacja adresu w sytuacji, gdy urządzenie zostało skompromitowane, pomiędzy momentem jego skopiowania a momentem skonstruowania transakcji. Czasami określa się to mianem '"*address swapping*"'.



Aby zabezpieczyć się przed tymi różnymi metodami ataku, ważne jest sprawdzenie kilku znaków Address, zwłaszcza jego sumy kontrolnej (na końcu), na ekranie urządzenia podpisującego przed podpisaniem transakcji.



Ten atak bywa również określany jako '"*address poisoning*"'.