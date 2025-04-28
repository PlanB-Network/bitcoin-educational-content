---
term: SREĆA
---

Indikator koji se koristi u Mining bazenima za merenje performansi bazena u odnosu na njegova teoretska očekivanja. Kao što ime sugeriše, procenjuje sreću bazena u pronalaženju bloka. Sreća se izračunava poređenjem broja deonica koje su teoretski potrebne za pronalaženje validnog bloka, na osnovu trenutne težine Bitcoin, sa stvarnim brojem deonica proizvedenih za pronalaženje tog bloka. Manji broj deonica od očekivanog ukazuje na dobru sreću, dok veći broj ukazuje na lošu sreću.


Korelisanjem težine na Bitcoin sa brojem deonica proizvedenih svake sekunde i težinom svake deonice, bazen može izračunati broj deonica koje su teoretski potrebne za pronalaženje važećeg bloka. Na primer, pretpostavimo da je teoretski potrebno 100.000 deonica da bazen pronađe blok. Ako bazen zapravo proizvede 200.000 pre nego što pronađe blok, njegova sreća je 50%:


```text
100,000 / 200,000 = 0.5 = 50%
```


Suprotno tome, ako je ovaj bazen pronašao važeći blok nakon što je proizveo samo 50.000 deonica, onda je njegova sreća 200%:


```text
100,000 / 50,000 = 2 = 200%
```


Sreća je pokazatelj koji se može ažurirati tek nakon što bazen otkrije blok, što ga čini statičkim pokazateljem koji se periodično ažurira.