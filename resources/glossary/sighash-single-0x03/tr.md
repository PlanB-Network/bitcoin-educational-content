---
term: SIGHASH_SINGLE (0X03)
definition: İmzalanan her girdiyi aynı dizindeki karşılık gelen çıktıya bağlayan SigHash bayrağı.
---

Bitcoin işlem imzalarında, imzanın işlemin tüm girdilerine ve imzalanan aynı girdinin indeksine karşılık gelen yalnızca bir çıktıya uygulandığını belirtmek için kullanılan SigHash Bayrağı türü. Böylece, `SIGHASH_SINGLE` ile imzalanan her girdi özellikle belirli bir çıktıya bağlanır. Diğer çıktılar imza tarafından taahhüt edilmez ve bu nedenle daha sonra değiştirilebilir. Bu imza türü, katılımcıların belirli girdileri belirli çıktılara bağlamak istedikleri karmaşık işlemlerde kullanışlıdır, ancak işlemin diğer çıktıları için esneklik bırakır.