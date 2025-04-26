---
term: MASTER FINGERPRINT

---
4bajtový (32bitový) otisk hlavního soukromého klíče v hierarchické deterministické (HD) peněžence. Získává se výpočtem hashe `SHA256` hlavního soukromého klíče a následným výpočtem hashe `RIPEMD160`, což je proces označovaný v Bitcoinu jako `HASH160`. Master Fingerprint se používá k identifikaci HD peněženky nezávisle na odvozovacích cestách, ale s přihlédnutím k přítomnosti či nepřítomnosti přístupové fráze. Jedná se o stručnou informaci, která umožňuje odkazovat na původ sady klíčů, aniž by byly odhaleny citlivé informace o peněžence.