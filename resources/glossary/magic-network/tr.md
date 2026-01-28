---
term: Magic network
definition: Düğümler arasındaki mesajlarda ağı (mainnet, testnet, regtest) tanımlayan 4 baytlık sabitler.
---

Bitcoin protokolünde düğümler arasında değiş tokuş edilen bir mesajın belirli ağını (Mainnet, Testnet, regtest...) tanımlamak için kullanılan sabitler. Bu değerler, veri akışında tanımlanmalarını kolaylaştırmak için her mesajın başına yazılır. Sihirli Ağlar sıradan iletişim verilerinde nadiren bulunacak şekilde tasarlanmıştır. Gerçekten de, bu 4 bayt ASCII'de seyrektir, UTF-8'de geçersizdir ve veri depolama formatından bağımsız olarak generate çok büyük bir 32 bit tamsayıdır. Sihirli Ağlar (little-endian formatında):


- Mainnet:


```text
f9beb4d9
```



- Testnet:


```text
0b110907
```



- Regtest:


```text
fabfb5da
```


> ► *Bu 4 bayt bazen "Sihirli Sayı", "Sihirli Bayt" veya "Başlangıç Dizesi" olarak da adlandırılır*