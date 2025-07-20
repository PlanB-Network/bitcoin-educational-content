---
term: SHARDS (RGB)
---

U kontekstu RGB protokola, Shard predstavlja posebnu granu unutar acikličnog usmerenog grafa (DAG) koja prati istoriju prelaza stanja Contract. Ona čini koherentan podskup skupa prelaza, koji odgovara, na primer, nizu operacija potrebnih za potvrdu validnosti određenog sredstva od Genesis. Ovaj mehanizam omogućava izolaciju specifičnih segmenata ukupne istorije, kako bi se olakšala verifikacija na strani klijenta.