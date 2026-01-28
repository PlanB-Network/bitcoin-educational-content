---
term: Cookie (.cookie)
definition: Plik uwierzytelniający RPC generowany przez bitcoind w celu zabezpieczenia komunikacji z aplikacjami zewnętrznymi.
---

Plik używany do uwierzytelniania RPC (*Remote Procedure Call*) w Bitcoin Core. Po uruchomieniu bitcoind generuje unikalny plik cookie uwierzytelniania i przechowuje go w tym pliku. Klienci lub skrypty, które chcą wchodzić w interakcje z bitcoind za pośrednictwem RPC Interface, mogą używać tego pliku cookie do bezpiecznego uwierzytelniania. Mechanizm ten pozwala na bezpieczną komunikację między bitcoind i zewnętrznymi aplikacjami (takimi jak na przykład oprogramowanie Wallet), bez konieczności ręcznego zarządzania nazwami użytkowników i hasłami. Plik `.cookie` jest regenerowany przy każdym ponownym uruchomieniu bitcoind i usuwany po wyłączeniu.