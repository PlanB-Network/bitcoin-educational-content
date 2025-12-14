---
term: SIKIŞTIRILMIŞ AÇIK ANAHTAR
---

Bir açık anahtar, bitcoinleri almak ve güvence altına almak için komut dosyalarında (ya doğrudan bir açık anahtar biçiminde ya da bir Address olarak) kullanılır. Ham bir açık anahtar, her biri 256 bitlik iki koordinattan (`x, y`) oluşan eliptik bir eğri üzerindeki bir nokta ile temsil edilir. Dolayısıyla ham formatta bir açık anahtar, formatı tanımlamak için kullanılan ek baytı saymazsak 512 bittir. Öte yandan sıkıştırılmış bir açık anahtar, açık anahtar gösteriminin daha kompakt bir şeklidir. Yalnızca `x` koordinatını ve `y` koordinatının paritesini (çift veya tek) belirten bir önek (`02` veya `03`) kullanır.


Bunu reel sayılar alanına indirgersek, eliptik eğrinin x eksenine göre simetrik olduğu göz önüne alındığında, eğri üzerindeki herhangi bir $P$ (`x, y`) noktası için, aynı eğri üzerinde olacak bir $P'$ (`x, -y`) noktası vardır. Bu, her `x` için `y`nin pozitif ve negatif olmak üzere yalnızca iki olası değeri olduğu anlamına gelir. Örneğin, belirli bir `x` apsisi için, eliptik eğri üzerinde aynı apsisi paylaşan ancak zıt ordinatlara sahip iki $P1$ ve $P2$ noktası olacaktır:


![](../../dictionnaire/assets/29.webp)

Eğri üzerindeki iki potansiyel nokta arasında seçim yapmak için, hangi `y`nin seçileceğini belirten bir önek `x`e eklenir. Bu yöntem açık anahtarın boyutunu 520 bitten sadece 264 bite (8 bit önek + 256 bit `x` için) düşürmeyi sağlar. Bu gösterim açık anahtarın sıkıştırılmış biçimi olarak bilinir.


Ancak, eliptik eğri kriptografisi bağlamında, reel sayıları değil, `p` mertebesinde (bir asal sayı) sonlu bir alanı kullanırız. Bu bağlamda, `y`nin "işareti" paritesine, yani `y`nin çift mi yoksa tek mi olduğuna göre belirlenir. O halde `0x02` öneki çift bir `y`yi gösterirken, `0x03` tek bir `y`yi gösterir.


Aşağıdaki ham açık anahtar örneğini (eliptik eğri üzerinde bir nokta) onaltılık olarak düşünün:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Önek, `x` ve `y`'yi izole edebiliriz:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Taban 16 (onaltılık): f

Taban 10 (ondalık): 15

y tektir

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```