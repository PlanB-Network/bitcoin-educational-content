---
term: MASTER FINGERPRINT
---

4-bajtový (32-bitový) otisk hlavního soukromého klíče v Hierarchické Deterministické (HD) peněžence. Získá se výpočtem `SHA256` hash hlavního soukromého klíče, následovaným `RIPEMD160` hash, proces, který se na Bitcoinu označuje jako `HASH160`. Master Fingerprint se používá k identifikaci HD peněženky, nezávisle na cestách derivace, ale s přihlédnutím k přítomnosti nebo absenci hesla. Jedná se o stručnou informaci, která umožňuje odkazovat na původ sady klíčů, aniž by odhalila citlivé informace o peněžence.