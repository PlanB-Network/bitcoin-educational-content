---
name: Przewodnik po lokalnym uruchamianiu platformy Plan ₿ Network
description: W jaki sposób można uruchomić Plan ₿ Network w środowisku lokalnym, aby przetestować mój wkład w treść lub korektę/przegląd treści edukacyjnych na Plan ₿ Network?
---
![github](assets/cover.webp)


## Podsumowanie


Ten samouczek zawiera instrukcje krok po kroku dotyczące konfigurowania systemu zarządzania nauczaniem Bitcoin z Plan ₿ Network na komputerze lokalnym przy użyciu Dockera, fikcyjnych kluczy i niestandardowych konfiguracji repozytorium.


Jeśli nie zrozumiałeś powyższej części, nie martw się - ten poradnik jest dla Ciebie!


---

## **Jak uruchomić system zarządzania nauczaniem Bitcoin lokalnie**


Ten samouczek zawiera szczegółowe kroki konfiguracji platformy, obsługi fikcyjnych kluczy i dostosowywania repozytoriów. Wykonaj poniższe kroki, aby uniknąć typowych problemów i poprawnie skonfigurować środowisko lokalne.



**1. Wymagania wstępne**


- Maszyna z systemem Linux z zainstalowanymi Docker i Docker Compose (zgłoszono, że działa również w systemie Windows).
- wystarczająca wersja `nodejs` (testowana: 22.12.0)
- `pnpm` zainstalowany w systemie.
- Git skonfigurowany do klonowania repozytoriów.



**2. Sklonuj repozytorium**

Sklonuj repozytorium na komputerze lokalnym:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Konfiguracja zmiennych środowiskowych**


1\. Zduplikuj plik `.env.example`:


```bash
cp .env.example .env
```


1. Edytuj plik `.env`, usuwając część nazwy .example, teraz musisz dołączyć fikcyjne klucze dla wymaganych zmiennych. Przykład:


⚠️ Jest to krok obowiązkowy, pominięcie go spowoduje błędy, takie jak odmowa połączenia między niektórymi kontenerami.


Nie zapomnij dodać również dedykowanego Github PAT w pliku



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Instalowanie zależności**


upewnij się, że zainstalowałeś odpowiednią wersję nodejs. Na dzień 2024-12 udowodniono, że działa wersja 22.12.0 (LTS).



⚠️ Wersja repozytorium nodejs Ubuntu 22.04 to 12.22.9: zbyt stara, aby umożliwić instalację pnpm



Aby zainstalować nodejs, znajdź instrukcje [tutaj](https://nodejs.org/en/download/package-manager); na przykład możesz wybrać metodę instalacji `nvm`.


---

Przed rozpoczęciem fazy instalacji pnpm niezbędnych pakietów, upewnij się, że wszystkie zależności są zainstalowane, możesz to osiągnąć uruchamiając następujące polecenie:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Wewnątrz folderu `../Bitcoin-learning-management-system/` uruchom następujące polecenie, aby zainstalować `pnpm`


```bash
pnpm install
```


__TIP:__Pamiętaj o aktualizowaniu od czasu do czasu zarówno zależności, jak i samego pnpm



**5. Uruchomienie kontenerów**

W folderze `../Bitcoin-learning-management-system/` uruchom środowisko programistyczne za pomocą Dockera:


```bash
docker compose up --build -V
```

Uruchamiając kolejne polecenie w ten sposób, nie zobaczysz logów w terminalu.

```bash
docker compose up -d --build -V
```


Spowoduje to zbudowanie i uruchomienie wszystkich niezbędnych kontenerów z dockerów.


**6. Dostęp do aplikacji**

Po uruchomieniu kontenerów można uzyskać dostęp do frontendu pod adresem:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Uwaga: aplikacja automatycznie przeładuje się, jeśli zmienisz jakiekolwiek pliki źródłowe.



**7.** Konfiguracja bazy danych Schema


Przy pierwszym uruchomieniu konieczne będzie uruchomienie migracji DB.


Aby to zrobić, uruchom skrypt migracji: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Import danych z repozytorium**

Aby zaimportować dane do bazy danych, należy wysłać żądanie do interfejsu API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Napraw problemy z dostępem do woluminów synchronizacji**

Jeśli napotkasz problemy z dostępem do woluminów `cdn` i `sync`, uruchom je:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


potem znowu:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Dostosowanie repozytorium (opcjonalnie)**

Jeśli konieczne jest użycie Fork lub określonej gałęzi:

1. Edytuj plik `.env`, aby zaktualizować następujące zmienne:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Uruchom ponownie usługę Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Ponownie zsynchronizuj dane repozytorium:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Ten samouczek zapewnia prawidłową konfigurację platformy z fikcyjnymi kluczami, zainstalowanymi zależnościami i repozytoriami dostosowanymi w razie potrzeby. powodzenia z konfiguracją!


**Polecenia dodatkowej pomocy**


zatrzymanie wszystkich kontenerów


```
docker compose down
```


przyciąć wszystkie istniejące pojemniki i woluminy


```
docker container prune -f
docker volume prune --all
```


odtworzyć kontenery za pomocą tego samego polecenia, które zostało użyte w oficjalnym przewodniku i skrypcie synchronizacji lunchu:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```