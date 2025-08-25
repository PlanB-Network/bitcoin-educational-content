---
term: DAL VE BAĞ
---

Bitcoin core Wallet'de 0.17 sürümünden beri girdileri seçmek için kullanılan ve Murch tarafından icat edilen yöntem. Branch-and-Bound (BnB), değişikliği ve ilgili ücretleri en aza indirmek için bir işlemde yerine getirilecek çıktıların tam miktarıyla eşleşen bir UTXO kümesi bulmaya yönelik bir aramadır. Amacı, hem anlık maliyeti hem de değişiklik için beklenen gelecekteki maliyetleri dikkate alan bir atık kriterini azaltmaktır. Bu yöntem, *Knapsack Solver* gibi önceki sezgisel yöntemlere kıyasla ücretler açısından daha doğrudur. Branch-and-Bound*, 1960 yılında Ailsa Land ve Alison Harcourt tarafından icat edilen aynı isimli problem çözme yönteminden esinlenmiştir.


> ► *Bu yöntem bazen mucidine atfen "Murch Algoritması" olarak da adlandırılır.*