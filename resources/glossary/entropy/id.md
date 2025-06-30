---
term: ENTROPY

---
Entropi, dalam konteks kriptografi dan informasi, adalah sebuah ukuran kuantitatif dari ketidakpastian atau ketidakpastian yang terkait dengan sumber data atau proses acak. Entropi memainkan peran penting dalam keamanan sistem kriptografi, terutama dalam pembuatan kunci dan angka acak. Entropi yang tinggi memastikan bahwa kunci yang dihasilkan tidak dapat diprediksi dan tahan terhadap serangan brute force, di mana penyerang mencoba semua kombinasi yang mungkin untuk menebak kunci.

Dalam konteks Bitcoin, entropi digunakan untuk menghasilkan kunci privat atau _seed_. Ketika membuat sebuah dompet yang deterministik dan hirarkis (HD _Wallet_), konstruksi frasa mnemonik dilakukan dari sebuah angka acak, yang berasal dari sumber entropi. Frasa ini kemudian digunakan untuk menghasilkan beberapa private key, secara deterministik dan hirarkis, untuk menciptakan kondisi pembelanjaan pada UTXO.

Sangatlah penting untuk memiliki entropi yang baik untuk memastikan keamanan sistem kriptografi. Sumber entropi dapat berupa proses fisik, seperti derau elektronik atau variasi termal, atau proses perangkat lunak, seperti _generator_ bilangan acak semu.
