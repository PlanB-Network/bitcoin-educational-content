---
name: Picocrypt
description: Uno strumento open source per criptare i vostri dati
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Florian BURNEL pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Sono state apportate modifiche al contenuto originale



___



## I. Presentazione



In questa guida daremo un'occhiata a Picocrypt, un software di crittografia semplice, leggero ed efficace per crittografare i dati con un elevato livello di sicurezza.



Adatto alla **crittografia dei file**, è possibile utilizzarlo per proteggere i **dati sul computer, su una chiavetta USB**, ma anche i dati archiviati nel Cloud. Ad esempio, è possibile criptare i dati e memorizzarli su **Microsoft OneDrive, Google Drive, iCloud o Dropbox**, anche se per questo scopo preferisco un altro software che verrà presentato in un prossimo articolo.



Potete utilizzarlo anche quando dovete **condividere i dati con terzi**: grazie a Picocrypt e alla chiave di decrittazione, questi ultimi saranno in grado di decrittare i dati sul loro computer. In questo modo, se il vostro account o computer viene compromesso, i vostri dati sono protetti.



Per seguire il progetto Picocrypt, esiste solo un Address:





- [Picocrypt su GitHub](https://github.com/Picocrypt/Picocrypt)



Totalmente **libero e open source**, PicoCrypt è disponibile per **Windows,** **Linux** e **macOS**. Su Windows, è possibile installarlo sul proprio computer o utilizzare la versione portatile.



## II. Picocrypt, software di crittografia open source



Il software di crittografia Picocrypt** si presenta come **un'alternativa** ad altre soluzioni ben note come **VeraCrypt** e **Cryptomator** (*progettati per crittografare i dati su ambienti Cloud*), o **AxCrypt**. A proposito, sul GitHub ufficiale di Picocrypt è possibile trovare un confronto con alcuni concorrenti:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Fonte: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt è **molto leggero**, pesa solo **3 MB**, e non ha bisogno di essere installato: è un'applicazione **portatile** con il vantaggio di non richiedere i diritti di amministratore! Tuttavia, non trascura la sicurezza, poiché si basa su **algoritmi robusti e affidabili**:





- Algoritmo di crittografia XChaCha20**
- Funzione di bypass dei tasti **Argon2**



Al di là dei vantaggi appena citati, ciò che attira davvero è la **facilità d'uso**!



Ha bisogno solo di una cosa: **una verifica del codice**, ma è prevista, come si può vedere dalla tabella di confronto qui sopra (ultima riga). Ma poiché è open source, nulla vieta di dare un'occhiata al suo codice sorgente.



Anche se viene paragonato a BitLocker nella tabella precedente, **a mio parere BitLocker e Picocrypt sono destinati a usi diversi**: BitLocker per la crittografia di un volume completo (quello di Windows, ad esempio) e Picocrypt per la crittografia di una struttura ad albero o di uno spazio di archiviazione di tipo "Drive".



## III. Utilizzo di Picocrypt



Per questa dimostrazione verrà utilizzato un computer Windows 11.



### A. Crittografia dei dati con Picocrypt



Prima di tutto, è necessario scaricare Picocrypt.exe dal sito ufficiale GitHub ([vedi questa pagina](https://github.com/Picocrypt/Picocrypt/releases)).



Aprire l'applicazione per visualizzare il suo Interface minimalista sullo schermo. Per crittografare i dati, siano essi **un file, più file o una cartella**, è sufficiente **trascinarli e rilasciarli nel Interface di Picocrypt**. In questo modo si selezioneranno i dati da crittografare.



![Image](assets/fr/020.webp)



Per la crittografia dei dati si ha accesso a diverse opzioni, tra cui la chiave di crittografia. Può essere **una password forte** o **una chiave di crittografia sotto forma di file chiave**, o **entrambi**. Se prendiamo l'esempio di una password, si può scegliere tra la creazione di una password personale o la generazione di una password con Picocrypt.



La password deve essere forte, in quanto può essere utilizzata per decifrare i dati. Inserirla in "**Password**" e "**Confirm Password**", quindi fare clic su "**Encrypt**" per criptare i dati! Prima di ciò, è possibile fare clic sul pulsante "**Change**" accanto a "**Save output as**" per specificare la directory di output.



**Nota**: per utilizzare una chiave in formato file, fare clic su "**Create**" a destra di "**Keyfiles**" per creare una chiave. Quindi selezionarla facendo clic su "**Modifica**" e trascinando il file della chiave nell'area appropriata.



![Image](assets/fr/019.webp)



I due file selezionati vengono **crittografati e raggruppati insieme** nel file "**Encrypted.zip.pcv**", poiché **PCV** è l'estensione utilizzata da Picocrypt. Questo file ZIP è illeggibile grazie alla crittografia. Per evitare che i file selezionati vengano raggruppati in un unico file ZIP crittografato, è necessario selezionare l'opzione "**Recursively**", in modo da avere tanti file crittografati quanti sono i file da crittografare.



Per accedere ai nostri dati, dobbiamo decifrarli utilizzando Picocrypt.



![Image](assets/fr/023.webp)



Prima di parlare della decodifica dei dati, ecco alcune informazioni su alcune delle opzioni disponibili:





- Modalità paranoica**: utilizza il livello di sicurezza più elevato offerto da Picocrypt. Lo strumento utilizzerà diversi algoritmi di crittografia a cascata (XChaCha20 e Serpent) e HMAC-SHA3 invece di BLAKE2b per l'autenticazione dei dati.
- Reed-Solomon**: implementa i codici di correzione degli errori *Reed-Solomon* per facilitare la correzione degli errori sui dati corrotti. Ciò consente di supportare un livello di corruzione di circa il 3% del file.
- Dividere in pezzi** o **dividere in più parti**: se state criptando un file di grandi dimensioni, potete chiedere a Picocrypt di dividerlo in più parti. Questo può rendere il file più facile da trasferire.
- Compress Files** o **Compress files**: comprime i file per ridurre le dimensioni dei file criptati.
- File eliminati** o **Fichiers supprimés**: eliminare i file sorgente per mantenere solo la versione criptata



### B. Decrittazione dei dati con Picocrypt



Se è necessario decriptare i dati, non è più complicato che criptarli. È sufficiente aprire Picocrypt e **trascinare il file PCV da decifrare**. Quindi inserire la password e/o selezionare il file chiave prima di fare clic su "**Decrypt**".



![Image](assets/fr/021.webp)



La versione non cifrata dell'archivio ZIP "Encrypted.zip" mi permette ora di recuperare i miei due file in chiaro!



![Image](assets/fr/022.webp)



## IV. Conclusione



**Siete stati avvertiti: Picocrypt è molto facile da usare e funziona! Sebbene il Interface sia minimalista, incorpora alcune opzioni molto utili per personalizzare la crittografia! E poiché è disponibile in versione portatile, potete portarlo con voi ovunque andiate, in modo da poter decifrare i vostri dati in tutta tranquillità**



Assicuratevi di usare password forti per proteggere i dati e, se usate un file chiave, ricordatevi di farne il backup, altrimenti non sarete più in grado di decriptare il contenitore PCV generato da Picocrypt. Infine, è bene sapere che esiste anche [una versione CLI](https://github.com/Picocrypt/CLI) (con meno funzioni) che consente di eseguire Picocrypt dalla riga di comando: anche in questo caso, Picocrypt apre le porte a nuove possibilità.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5