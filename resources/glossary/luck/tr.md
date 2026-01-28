---
term: Şans (Luck)
definition: Bir madencilik havuzunun performansını teorik beklentilere kıyasla ölçen gösterge.
---

Mining havuzlarında bir havuzun teorik beklentilerine göre performansını ölçmek için kullanılan bir gösterge. Adından da anlaşılacağı üzere, havuzun blok bulma şansını değerlendirir. Şans, Bitcoin'ın mevcut zorluğuna dayalı olarak geçerli bir blok bulmak için teorik olarak gereken hisse sayısı ile bu bloğu bulmak için üretilen gerçek hisse sayısı karşılaştırılarak hesaplanır. Beklenenden daha düşük bir hisse sayısı iyi şansı gösterirken, daha yüksek bir sayı kötü şansı gösterir.


Bitcoin'deki zorluğu her saniye üretilen hisse sayısı ve her bir hissenin zorluğu ile ilişkilendirerek, havuz geçerli bir blok bulmak için teorik olarak gerekli olan hisse sayısını hesaplayabilir. Örneğin, teorik olarak bir havuzun bir blok bulması için 100.000 hisse gerektiğini varsayalım. Havuz bir blok bulmadan önce gerçekten 200.000 üretiyorsa, şansı %50'dir:


```text
100,000 / 200,000 = 0.5 = 50%
```


Tersine, bu havuz yalnızca 50.000 hisse ürettikten sonra geçerli bir blok bulduysa, şansı %200'dür:


```text
100,000 / 50,000 = 2 = 200%
```


Şans, yalnızca bir blok havuz tarafından keşfedildikten sonra güncellenebilen bir göstergedir, bu da onu periyodik olarak güncellenen statik bir gösterge haline getirir.