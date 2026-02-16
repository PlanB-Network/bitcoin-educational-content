---
term: Address spoofing
definition: Útok, při kterém škodlivý aktér vytvoří adresu velmi podobnou adrese oběti, aby ji oklamal a přesměroval její platby.
---

Útok, při kterém záškodník vytvoří identifikátor Address (nebo jiný platební identifikátor) velmi podobný identifikátoru oběti. Cílem je oklamat uživatele, aby během transakce opsal tento nesprávný Address, což vede k tomu, že bitcoiny jsou místo zamýšlenému cíli odeslány útočníkovi.



Útočník využije spěchu uživatele a zkopíruje nesprávný kód Address, pokud provede transakci, aniž by zkontroloval její správnost. Obecně platí, že k provedení tohoto útoku útočník provádí platby malými částkami na Wallet oběti, aby do její transakční historie začlenil falešný Address. Tento útok bývá používán u altcoinů, kde je běžnou praxí opakované používání stejných přijímacích adres, na rozdíl od Bitcoin, kde je používání prázdných adres pro každou transakci rozšířenější praxí. Uživatelé Bitcoin však nejsou vůči tomuto útoku imunní.



Další metodou, jak předložit oběti nesprávnou adresu, je použití podvodného softwaru pro správu peněženek, který napodobuje legitimní software, nebo změna adresy v případě kompromitace zařízení mezi okamžikem, kdy je zkopírována, a okamžikem, kdy je transakce sestavena. Někdy se tomu říká '"*address swapping*"'.



Abyste se ochránili před těmito různými způsoby útoku, je důležité před podpisem transakce zkontrolovat na obrazovce podepisovacího zařízení několik znaků kódu Address, zejména jeho kontrolní součet (na konci).



Tento útok se někdy také označuje jako '"*address poisoning*"'.