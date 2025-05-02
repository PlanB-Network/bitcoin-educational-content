---
name: Zeus

description: Мульти-нодовый кошелек с самохранением
---

![Zeus](assets/zeus_intro.webp)

ZEUS — это мобильный кошелек Bitcoin и приложение для управления нодами с полным функционалом кошелька Bitcoin Lightning, который упрощает платежи в биткоинах, предоставляет пользователям полный контроль над их финансами и позволяет более продвинутым пользователям управлять их Lightning нодами прямо с мобильного устройства.

## Для кого ZEUS?
На данный момент ZEUS предназначен для людей, которые управляют своими домашними или бизнес нодами [Lightning Network Daemon (LND)](https://lightning.engineering/) или [Core Lightning (CLN)](https://blockstream.com/lightning/) и управляют ими через Zeus удаленно.

Торговцы, использующие [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) или [Alby](https://getalby.com/) (или любой другой аккаунт LNDhub), также могут подключаться, использовать и управлять своими нодами / аккаунтами через ZEUS.

[Начиная с версии 0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS начнет обслуживать обычных пользователей, которые просто хотят легкий способ совершать быстрые и дешевые платежи в биткоинах с их мобильного устройства, имея [встроенную мобильную ноду Lightning](https://docs.zeusln.app/category/embedded-node) с интегрированным [Провайдером Услуг Lightning (LSP)](https://docs.zeusln.app/lsp/intro).

## Важные ресурсы Zeus:
- Официальная веб-страница Zeus - [https://zeusln.app/](https://zeusln.app/)
- Документация Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Репозиторий Zeus на Github](https://github.com/ZeusLN/zeus)
- [Группа поддержки Zeus в Telegram](https://t.me/ZeusLN)
- [Zeus на NOSTR](https://iris.to/zeus@zeusln.app)
- [Анонсы блога Zeus](https://blog.zeusln.com)

## Функции Zeus
### Общие функции:
- Кошелек только для Bitcoin и Lightning с самохранением
- Без комиссий за обработку, без KYC
- Полностью открытый исходный код (APGLv3)
- Поддержка множества нод / аккаунтов (вы можете управлять своими домашними нодами, запускать встроенную ноду LND, подключаться к нескольким аккаунтам LNDhub)
- Простое в использовании меню активности
- Шифрование PIN-кодом или парольной фразой, Режим конфиденциальности - скрыть ваши конфиденциальные данные
- Контактная книга, множество тем, многоязычность

### Технические функции
- Подключение через Tor
- Полная поддержка LNURL (оплата, вывод средств, авторизация, каналы), отправка на Lightning адреса
- Подробное управление каналами Lightning, поддержка MPP/AMP, Keysend, управление комиссиями за маршрутизацию
- Поддержка Replace-by-fee (RBF) и Child-pays-for-parent (CPFP)
- NFC платежи и запросы, подпись и проверка сообщений
- Поддержка Segwit и Taproot
- Простые Taproot каналы
- Самохраняемые lightning адреса (@zeuspay.com)
- Точка продаж от Square (скоро открытая PoS)

## Руководства и видеоуроки
Чтобы иметь возможность использовать Zeus и управлять каналами Lightning, ликвидностью, комиссиями и т.д., лучше всего сначала ознакомиться с некоторыми важными руководствами о Lightning Network.

### Руководства:
- [Документация LND - Lightning Network Daemon](https://docs.lightning.engineering/)
- [Документация CLN - Core Lightning](https://lightning.readthedocs.io/index.html)
- [Начальное руководство по Lightning](https://bitcoiner.guide/lightning/) – от Bitcoin Q&A
- [Управление узлом Lightning](https://www.lightningnode.info/) – от openoms
- [Сеть Lightning и аналогия с аэропортом](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Управление ликвидностью узла Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Обслуживание узла Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)

### Видеоурок от BTC Sessions

![Кошелек Zeus Bitcoin Lightning - Управление мобильным узлом](https://youtu.be/hmmehTnV3ys)