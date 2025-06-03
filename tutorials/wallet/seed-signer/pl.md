---
name: Sygnatariusz seed

description: Konfiguracja sygnatariusza seed
---

![cover](assets/cover.webp)


## Materiał:


**Raspberry Pi Zero (wersja 1.3)**


Aby uzyskać rozwiązanie z całkowicie zamkniętym dostępem do powietrza, należy użyć wersji 1.3 bez możliwości korzystania z WiFi lub Bluetooth, ale każdy model Raspberry Pi 2/3/4 lub Zero będzie działał.


Uwaga: Raspberry Pi, które zwykle nie są dostarczane z dołączonymi pinami; piny będą musiały być przylutowane lub można użyć czegoś, co nazywa się "młotkiem GPIO".

Młotek GPIO


Jeśli nie potrafisz lutować lub po prostu nie masz jeszcze lutownicy, możesz użyć "GPIO Hammer" jako alternatywy dla lutowania.


**Hat LCD WaveShare 1,3 cala z ekranem 240 × 240 pikseli**


WaveShare LCD Hat 1.3″ 240×240 pxl LCD


**Uwaga:** Ekran Waveshare należy wybierać ostrożnie; upewnij się, że kupujesz model o rozdzielczości 240×240 pikseli.


**Moduł kamery kompatybilny z Pi Zero**


Kamera Raspberry Pi Aokin/AuviPal 5MP 1080p z modułem kamery wideo z czujnikiem OV5647; inne marki z modułem czujnika OV5647 również powinny działać, ale mogą nie być kompatybilne z obudową Orange Pill.


**Uwaga:** Potrzebny będzie kabel taśmowy kamery kompatybilny z Raspberry Pi Zero.


**Karta microSD o pojemności co najmniej 4 GB**


obszerne zasoby: https://seedsigner.com/explainers/


## Oprogramowanie:


Instalacja oprogramowania


1. Pobierz najnowszy plik "seedsigner_x_x_x.img.zip"

najnowsze wydanie

2. Rozpakuj plik "seedsigner_x_x_x.img.zip"

3. Użyj programu Balena Etcher lub podobnego narzędzia, aby zapisać rozpakowany plik obrazu .img na karcie microsd

BALENA ETCHER

4. Zainstaluj kartę microsd w SeedSigner.

Klucz publiczny GPG SeedSigner

seedsigner_pubkey.gpg


## Film instruktażowy


_przewodnik zaczerpnięty z Southerbitcoiner, stworzony przez Cole_


### Zbiór poradników wideo na temat SeedSigner: otwartoźródłowego, samodzielnego urządzenia Hardware Wallet/Signing


![image](assets/1.webp)


SeedSigner to urządzenie do podpisywania Bitcoin, które można zbudować od podstaw. Brzmi trudno, ale ta 4-częściowa seria powinna ci pomóc :) Proponuję obejrzeć część 1 i 2, a następnie zdecydować, czy chcesz używać komputera stacjonarnego (obejrzyj część 3), czy urządzenia mobilnego (obejrzyj część 4).


Wszystko, co musisz wiedzieć, znajdziesz poniżej. Inne przydatne linki obejmują stronę internetową SeedSigner, ich Github, bazę kluczy, najnowszą wersję i wymagania sprzętowe.


### Część 1: Jak zbudować SeedSigner:


W tym filmie pokazuję, jak pobrać i zweryfikować oprogramowanie SeedSigner, jakie części są potrzebne i jak złożyć SeedSigner.


![video](https://youtu.be/mGmNKYOXtxY)


### Część 2: Testowanie aplikacji SeedSigner


Zanim użyłem mojego SeedSignera, przeprowadziłem kilka testów, aby upewnić się, że nie robi nic złośliwego. Pomyślałem, że podzielę się również tym krokiem. Oto jak sprawdzić, czy SeedSigner eksportuje prawidłowy Wallet (xpub), jak zweryfikować matematykę rzutów kośćmi SeedSigners i jak zweryfikować nasiona potomne bip-85 SeedSigners.


![video](https://youtu.be/34W1IyTyXZE)


### Część 3: Jak używać SeedSigner ze Sparrow Wallet (desktop)


SeedSigner jest w stanie generować nasiona i podpisywać transakcje Bitcoin. Samodzielnie nie jest jednak w stanie tworzyć transakcji. Musisz użyć "koordynatora" Wallet ze swoim SeedSigner. Oto jak używać Sparrow Wallet z SeedSigner:


![video](https://youtu.be/IQb8dh-VTOg)


Część 4: Jak używać SeedSigner z Blue Wallet (mobile)


SeedSigner jest w stanie generować nasiona i podpisywać transakcje Bitcoin. Samodzielnie nie jest jednak w stanie tworzyć transakcji. Musisz użyć "koordynatora" Wallet ze swoim SeedSigner. Oto jak używać Blue Wallet z SeedSigner:


![video](https://youtu.be/x0Ee35Ct0r4)


To na razie wszystkie przewodniki po SeedSigner! Daj mi znać, jeśli uważasz, że czegoś brakuje. Są one na mojej liście potencjalnych filmów:



- Ogólna recenzja SeedSigner. Czy jest to dobry wybór na urządzenie do podpisywania? Plusy/minusy?
- Jak używać Bip-85 z SeedSigner
- Jak zostać wujkiem Jimem dzięki SeedSigner


Uznałeś je za wartościowe? Rozważ wysłanie napiwku, który pomoże sfinansować przyszłe filmy:

https://www.southernbitcoiner.com/donate/