---
name: Průvodce místním spuštěním platformy Plan ₿ Network
description: Jak můžete spustit Plan ₿ Network v místním prostředí, abyste otestovali můj příspěvek k obsahu nebo korekturu/revizi vzdělávacího obsahu na Plan ₿ Network?
---
![github](assets/cover.webp)

## Shrnutí

Tento návod obsahuje pokyny krok za krokem pro nastavení systému pro správu výuky Bitcoin z Plan ₿ Network na místním počítači pomocí nástroje Docker, fiktivních klíčů a vlastních konfigurací úložiště.

Pokud jste nerozuměli části výše, nezoufejte - tento návod je určen právě vám!

---
## **Jak spustit systém řízení výuky Bitcoin lokálně**

Tento návod obsahuje podrobné kroky k nastavení platformy, práci s fiktivními klíči a přizpůsobení úložišť. Postupujte podle níže uvedených kroků, abyste se vyhnuli běžným problémům a správně nakonfigurovali místní prostředí.

**1. Předpoklady**


- Linuxový počítač s nainstalovaným Dockerem a Docker Compose (bylo hlášeno, že funguje i ve Windows).
- dostatečná verze `nodejs` (testováno: 22.12.0)
- `pnpm` nainstalovaný ve vašem systému.
- Konfigurace systému Git pro klonování repozitářů.

**2. Klonování úložiště**

Klonujte úložiště do místního počítače:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Nastavení proměnných prostředí**

1\. Duplikujte soubor `.env.example`:

```bash
cp .env.example .env
```

1. Upravte soubor `.env` a vymažte část názvu .example, nyní je třeba vložit fiktivní klíče pro požadované proměnné. Příklad:

⚠️ Tento krok je povinný, jeho vynechání povede k chybám, jako je odmítnutí spojení mezi některými kontejnery.

Nezapomeňte do souboru přidat také svůj vyhrazený PAT Githubu

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Instalace závislostí**

`Ujistěte se`, že máte nainstalovanou vhodnou verzi nodejs. Od 2024-12 se osvědčila verze 22.12.0 (LTS).

⚠️ Ubuntu 22.04 repozitář nodejs verze je 12.22.9: příliš stará, aby vám umožnila instalaci pnpm

Pro instalaci nodejs najdete návod [zde](https://nodejs.org/en/download/package-manager); můžete například zvolit metodu instalace `nvm`.

---
Před zahájením fáze instalace potřebných balíčků pnpm se ujistěte, že máte nainstalovány všechny závislosti, čehož dosáhnete spuštěním následujícího příkazu:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Ve složce `../Bitcoin-learning-management-system/` spusťte následující příkaz pro instalaci `pnpm`

```bash
pnpm install
```

__TIP:__ Nezapomeňte čas od času aktualizovat závislosti i samotné pnpm

**5. Spuštění kontejnerů**

Ve složce `../Bitcoin-learning-management-system/` spusťte vývojové prostředí pomocí nástroje Docker:

```bash
docker compose up --build -V
```

Tímto způsobem spustíte i tento další příkaz, v terminálu se vám nezobrazí protokoly.

```bash
docker compose up -d --build -V
```

Tím se sestaví a spustí všechny potřebné kontejnery z dockerů.

**6. Přístup k aplikaci**

Jakmile jsou kontejnery spuštěny, přistupte k frontendu na adrese:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Poznámka: aplikace se automaticky znovu načte, pokud změníte zdrojové soubory.

**7.** Nastavení databáze Schema

Při prvním spuštění je třeba spustit migraci DB.

Spusťte migrační skript: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Import dat z úložiště**

Chcete-li importovat data do databáze, zadejte požadavek na rozhraní API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Oprava problémů s přístupem k synchronizaci svazků**

Pokud narazíte na problémy s přístupem ke svazkům `cdn` a `sync`, spusťte:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

pak znovu:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Přizpůsobení úložiště (volitelné)**

Pokud potřebujete použít Fork nebo určitou větev:

1. Upravte soubor `.env` a aktualizujte následující proměnné:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Restartujte Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Znovu synchronizujte data úložiště:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Tento návod zajistí správné nastavení platformy s fiktivními klíči, nainstalovanými závislostmi a repozitáři upravenými podle potřeby. 🎉 Hodně štěstí s nastavením!

**Příkazy pro další pomoc**

zastavit všechny kontejnery

```
docker compose down
```

ořezat všechny existující kontejnery a svazky

```
docker container prune -f
docker volume prune --all
```

znovu vytvořte kontejnery pomocí stejného příkazu, který je uveden v oficiálním průvodci a skriptu pro synchronizaci oběda:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
