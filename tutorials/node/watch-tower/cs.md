---
name: Watch Tower
description: Porozumění a používání strážní věže
---

## Jak fungují strážní věže?

Jako nezbytná součást ekosystému Lightning Network poskytují strážní věže uživatelům lightning kanálů další stupeň ochrany. Jejich hlavní odpovědností je sledovat zdraví kanálů a zasáhnout, pokud se jedna ze stran kanálu pokusí podvést druhou.

Jak tedy strážní věž určí, že byl kanál kompromitován? Strážní věž obdrží potřebné informace od klienta, jedné ze stran kanálu, aby správně identifikovala a reagovala na jakékoli porušení. Tyto informace často zahrnují nejnovější detaily transakce, aktuální stav kanálu a informace potřebné k vytvoření trestných transakcí. Před odesláním dat strážní věži je klient může zašifrovat, aby ochránil soukromí a tajemství. To brání strážní věži v dešifrování zašifrovaných dat, pokud nedošlo skutečně k porušení, i když data obdrží. Tento šifrovací systém chrání soukromí klienta a zároveň brání strážní věži v přístupu k soukromým datům bez oprávnění.

## Jak si nastavit vlastní Oko Satoshiho a začít přispívat

Oko Satoshiho ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) je nevlastnická Lightning strážní věž v souladu s [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Má dva hlavní komponenty:

1. teos: zahrnuje CLI a serverovou základní funkcionalitu věže. Při sestavení tohoto balíčku budou vytvořeny dva binární soubory—teosd a teos-cli.

2. teos-common: Zahrnuje sdílenou serverovou a klientskou funkcionalitu (užitečné pro vytvoření klienta).

Pro úspěšný běh věže budete potřebovat, aby bitcoind běžel před spuštěním věže s příkazem teosd. Před spuštěním obou těchto příkazů musíte nastavit soubor bitcoin.conf. Zde jsou kroky, jak to udělat:-

1. Nainstalujte bitcoin core ze zdroje nebo ho stáhněte. Po stažení umístěte soubor bitcoin.conf do uživatelského adresáře Bitcoin core. Pro více informací, kde soubor umístit, v závislosti na operačním systému, který používáte, navštivte tento odkaz.

2. Po identifikaci místa, kde má být soubor vytvořen, přidejte tyto možnosti:-

'''
#RPC
server=1
rpcuser=<váš-uživatel>
rpcpassword=<vaše-heslo>

#chain
regtest=1
'''

- server: Pro RPC požadavky
- rpcuser a rpcpassword: RPC klienti se mohou autentizovat se serverem
- regtest: Není nutné, ale užitečné, pokud plánujete vývoj.

rpcuser a rpcpassword si musíte vybrat sami. Musí být napsány bez uvozovek. Například:-

'''
rpcuser=aniketh
rpcpassword=strongpassword
'''

Nyní, pokud spustíte bitcoind, měl by začít běžet uzel.

1. Pro část věže nejprve musíte nainstalovat teos ze zdroje. Postupujte podle pokynů uvedených v tomto odkazu.

2. Po úspěšné instalaci teos ve vašem systému a spuštění testů můžete pokračovat posledním krokem, kterým je nastavení souboru teos.toml v uživatelském adresáři teos. Soubor musí být umístěn ve složce nazvané .teos (všimněte si tečky) ve vaší domovské složce. To znamená například /home/<vaše-uživatelské-jméno>/.teos pro Linux. Jakmile najdete místo, vytvořte soubor teos.toml a nastavte tyto možnosti odpovídající změnám, které jsme provedli na bitcoind.
#bitcoindbtc_network = "regtest"
btc_rpc_user = <vaše-uživatelské-jméno>
btc_rpc_password = <vaše-heslo>
'''

Všimněte si, že zde musí být uživatelské jméno a heslo uvedeny v uvozovkách, tedy pro stejný příklad jako předtím:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "silnéheslo"
'''

Až to uděláte, měli byste být připraveni spustit věž. Vzhledem k tomu, že běžíme na regtest, je pravděpodobné, že v naší bitcoinové testovací síti nebudou při prvním připojení věže vytěženy žádné bloky (pokud ano, něco je určitě špatně). Věž si vytváří interní mezipaměť posledních 100 bloků z bitcoind, takže při prvním spuštění můžeme dostat následující chybu:

> CHYBA [teosd] Nedostatek bloků pro spuštění věže (požadováno: 100). Vytěžte alespoň 100 dalších

Vzhledem k tomu, že běžíme na regtest, můžeme bloky těžit vydáním RPC příkazu, bez nutnosti čekat na 10minutový průměrný čas, který obvykle vidíme v jiných sítích (jako mainnet nebo testnet). Podívejte se na nápovědu bitcoin-cli a hledejte, jak těžit bloky. Pokud potřebujete pomoc, můžete se podívat na tento článek.

![obrázek](assets/2.webp)

To je vše, úspěšně jste spustili věž. Gratulujeme. 🎉