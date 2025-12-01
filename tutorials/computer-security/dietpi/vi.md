---
name: DietPi
description: Hệ điều hành nhẹ được tối ưu hóa cho các máy tính có hiệu suất thấp. Ưu tiên tự lưu trữ
---

![cover](assets/cover.webp)



Trong giới không chuyên về kỹ thuật, các thương hiệu như `Odroid`, `Raspberry Pi`, `Orange Pi` hay `Radxa` ít được biết đến. Nhưng chỉ cần nhìn vào giới công nghệ, người ta sẽ thấy rằng máy tính **SBC** - được xây dựng trên một bo mạch chủ duy nhất, thường có kích thước siêu nhỏ so với máy tính thông thường - đã trở nên không thể thiếu, hỗ trợ cho bất kỳ dự án cá nhân nào.



Đây là những máy tính được sản xuất với nhiều mẫu mã khác nhau. Chúng thường được cài đặt các bản phân phối Linux, thường được điều chỉnh để chạy mượt mà trên những máy tính có cấu hình yếu này.



**DietPi cũng không ngoại lệ**: đây là hệ điều hành dựa trên Debian, được tối ưu hóa để nhẹ nhất có thể và giúp ngay cả những `SBC` kém hiệu năng nhất cũng trở nên cực kỳ nhanh chóng. Được chuyển từ Debian12 Bookworm sang Debian13 Trixie ngay khi bài hướng dẫn này được viết, giờ đây nó cũng hỗ trợ SBC dựa trên bộ xử lý `RISC-V` mã nguồn mở. DietPi là một khám phá thú vị đáng được nghiên cứu thêm.



## Điểm mạnh



Đây không phải là "bản sao thông thường" của Debian dành cho các bo mạch nhỏ kiểu Raspberry. DietPi là:




- Được tối ưu hóa về tốc độ và dung lượng**: [so sánh với các bản phân phối Debian khác dành cho SBC](https://dietpi.com/blog/?p=888), DietPi nhẹ hơn về mọi mặt. Ảnh ISO của DietPi chỉ nặng chưa đến 1 GB, nhỏ nhất trong số các ảnh dành riêng cho các mẫu Raspberry hoặc Orange PI cũ (ví dụ). Nhu cầu về tài nguyên RAM và CPU rất thấp, nhờ đó nó luôn tận dụng tối đa hiệu suất của bo mạch chủ, ngay cả những bo mạch cũ.
- Tự động hóa và trình cài đặt tích hợp**: Một bộ lệnh chuyên dụng giúp người dùng theo dõi tài nguyên hệ thống cũng như tự động hóa các tác vụ cài đặt và khởi chạy chương trình, cập nhật phiên bản, tạo bản sao lưu và kiểm tra tất cả nhật ký.
- Một cộng đồng mạnh mẽ, hướng đến thử nghiệm**: [hướng dẫn](https://dietpi.com/forum/c/community-tutorials/8) và các dự án từ cộng đồng DietPi là nơi lý tưởng để tìm cảm hứng về phần mềm mà bạn có thể cài đặt chỉ bằng một cú nhấp chuột, nhờ DietPi.



**Việc vắt kiệt từng chút một từ SBC chưa bao giờ dễ dàng đến thế**.



## Tự động hóa cho việc tự lưu trữ


Bạn muốn thử nghiệm máy chủ của riêng mình để chạy các giải pháp mạng tiên tiến, hoặc các công cụ để phát triển chuyên môn Bitcoin? DietPi có thể là giải pháp bạn đang tìm kiếm. Mặc dù nhiều người biết cách quản lý cơ sở hạ tầng của riêng mình và vận hành các máy chủ được cấu hình và bảo vệ hoàn hảo, DietPi là một bước đi phù hợp cho những ai muốn bắt đầu từ con số 0.



Thay vì phải tự tay thực hiện tất cả các tác vụ phức tạp mà một tác vụ như vậy yêu cầu, DietPi cho phép bạn xây dựng chúng bằng một `wizard` và dòng lệnh riêng. Tại đây, bạn có thể thử nghiệm với đám mây cá nhân, quản lý thiết bị _nhà thông minh_, sao lưu tự động và crontab, cũng như các giải pháp nâng cao hơn.



![img](assets/en/01.webp)



## Cài đặt



### Tải xuống



DietPi cung cấp vô số ảnh ISO để ghi hệ điều hành vào nhiều thiết bị khác nhau. Một số chỉ được hỗ trợ: ví dụ, ISO cho Raspberry PI5 vẫn đang trong quá trình thử nghiệm, nhưng bạn chắc chắn có thể tìm thấy ảnh phù hợp với bo mạch của mình.



Trong hướng dẫn này, tôi chọn cài đặt trên máy khách mỏng (thin client), vì vậy tôi chọn _PC/VM_ rồi đến _Native PC_. Có hai file ISO dành cho hai thiết bị này, khác nhau về thế hệ bootloader. Máy được sử dụng trong hướng dẫn khá cũ, vì vậy tôi chọn phiên bản _BIOS/CSM_. Nếu bạn dùng máy mới hơn, phiên bản chính xác có thể là `UEFI`.



![img](assets/en/02.webp)



Bạn sẽ đến trang chứa `hình ảnh của trình cài đặt`, `sha256` và `Chữ ký`.



![img](assets/en/03.webp)



Chuẩn bị một thư mục trong `home` của máy tính bạn sử dụng hàng ngày để bạn có thể tải xuống các tệp cần thiết bằng `wget`.



![img](assets/en/04.webp)



Khóa công khai của nhà phát triển yêu cầu phải nghiên cứu tối thiểu, nhưng bạn có thể tìm thấy nó tại liên kết này: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Kiểm tra nội dung của thư mục bằng lệnh `ls -la` và nhập khóa MichaIng vào vòng chìa khóa của bạn bằng lệnh `gpg --import`.



### Xác minh và flash



Cuối cùng, phần tôi khuyên bạn nên làm nhất: xác định tính xác thực của hệ điều hành bạn đã tải xuống và sắp cài đặt trên SBC của mình.



![img](assets/en/06.webp)



Nếu bạn cũng nhận được kết quả `Good signature` và cùng một điều khiển Hash với lệnh sha256sum, bạn có thể tiến hành flash ISO vào ổ USB. Sử dụng các ứng dụng như Whale Etcher để thực hiện việc này.



![img](assets/en/07.webp)



## Cài đặt DietPi



![img](assets/en/09.webp)



Chuyển ổ đĩa flash sang thiết bị sẽ lưu trữ DietPi và bắt đầu cài đặt hệ điều hành lime Green. Trong bài tập này, chúng tôi sử dụng một máy khách mỏng với RAM 16 GB, ổ SSD 128 GB cho hệ điều hành và một ổ dữ liệu thứ hai dung lượng 1 TB. Quá trình cài đặt mất chưa đến 30 phút, nhưng nếu bạn sử dụng Raspberry chẳng hạn, tài nguyên có thể ít hơn và mất nhiều thời gian hơn. Bạn sẽ được hiển thị tiến trình trong quá trình cài đặt.



![img](assets/en/08.webp)



Được thiết kế cho Raspberry và các hệ điều hành tương tự, bản chất thực sự của DietPi là cài đặt `headless`, không có môi trường đồ họa và có quyền truy cập `shsh'' gốc. Trong hướng dẫn, bạn sẽ thấy một môi trường đồ họa, chính xác là LXDE.



Trong bước này, bạn cũng sẽ được yêu cầu quyết định xem bạn muốn sử dụng trình duyệt web nào làm mặc định, giữa Chromium và Firefox. Cả hai đều hoạt động tốt; không có chống chỉ định cụ thể nào cho cả hai, ngoại trừ sở thích cá nhân của bạn.



Gần cuối, trình cài đặt có thể hỏi bạn có muốn cài đặt bất kỳ chương trình nào không, nhưng ở đây **tôi khuyên bạn không nên tải trước bất cứ thứ gì**. Bạn nên biết rằng sau bước này, bạn sẽ được yêu cầu thay đổi mật khẩu mặc định của hai người dùng vì lý do bảo mật. Quan trọng nhất là bạn sẽ được yêu cầu **đặt `Mật khẩu Phần mềm Toàn cầu (GSP)`**, điều này sẽ đảm bảo quyền truy cập vào các phần mềm khác nhau một cách có kiểm soát. **Nếu bạn tải xuống bất kỳ phần mềm nào trong quá trình cài đặt hệ điều hành mà không đặt `GSP`, chúng sẽ hầu như không thể truy cập được**. Bạn sẽ phải gỡ cài đặt và cài đặt lại chúng sau khi đặt `Mật khẩu Phần mềm Toàn cầu`: do đó, **không cài đặt bất cứ thứ gì để tránh làm việc trùng lặp**. (Sự bất tiện này có thể xảy ra, nhưng không chắc chắn 100%).



Quá trình cài đặt kết thúc bằng yêu cầu kích hoạt DietPi-Survey, một dịch vụ thu thập dữ liệu tự động được sử dụng để hỗ trợ phát triển hệ điều hành. Theo trang web, việc thu thập dữ liệu được kích hoạt khi bạn tải xuống bất kỳ phần mềm nào từ tính năng tự động hóa do DietPi cung cấp, hoặc khi bạn nâng cấp lên phiên bản tiếp theo. Mọi người đều có tùy chọn tham gia (_Opt IN_) hoặc không tham gia (_Opt OUT_).



![img](assets/en/23.webp)



Sau khi hoàn tất cài đặt và khởi động lại, DietPi sẽ hiển thị trên màn hình như bạn đã thiết lập. Trong phần hướng dẫn, như đã đề cập, tôi đã chọn môi trường đồ họa `LXDE`. Trên màn hình nền, tôi tìm thấy phím tắt để khởi động `htop` và mở terminal.



![img](assets/en/10.webp)



### "Công cụ" từ hệ điều hành



Hãy quên hầu hết các chương trình bạn sử dụng trên bản phân phối Linux của mình đi - DietPi được tối ưu hóa đến mức bạn đã bỏ sót khá nhiều. Về cơ bản, bạn sẽ phải cài đặt thủ công rất nhiều lệnh, nhưng nếu bạn chỉ đang dùng thử, hãy kiềm chế và thử kiểm tra tính năng tự động hóa của DietPi.



Chắc chắn terminal là công cụ hữu ích đầu tiên giúp bạn bắt đầu sử dụng hệ điều hành mới và nó sẽ tự động mở ra mỗi khi bạn bật máy.



![img](assets/en/11.webp)



Trên màn hình thiết bị đầu cuối, bạn sẽ thấy một loạt lệnh được liệt kê theo sau `dietpi-` đại diện cho [các công cụ](https://dietpi.com/docs/dietpi_tools/) của hệ điều hành này:




- `dietpi-launcher`: để truy cập hệ điều hành, trình quản lý tệp, v.v.
- `dietpi-Software`: là công cụ cho phép bạn cài đặt tất cả các phần mềm đã có sẵn trong bộ phần mềm
- `dietpi-config`: để truy cập vào cấu hình hệ thống, ngay cả những cấu hình nâng cao nhất.



![img](assets/en/14.webp)



### Hỗ trợ



Sao lưu máy chủ là một công việc thường xuyên mà người quản trị hệ thống phải thực hiện ngay từ lần khởi động đầu tiên.



Với DietPi có lệnh `dietpi-Backup`, tôi khuyên bạn nên khám phá lệnh này để tìm ra giải pháp lý tưởng: lệnh cho phép bạn thiết lập bản sao lưu thường xuyên, tăng dần hoặc không tùy thuộc vào ứng dụng được sử dụng và tất cả các tùy chọn để tùy chỉnh thói quen.



![img](assets/en/22.webp)



Chọn đích đến của bản sao lưu, ví dụ như một đĩa khác, bằng cách khởi động `dietpi-Drive_Manager` để gắn ổ đĩa đích và sử dụng ổ đĩa đó cho chức năng này.



## Cấu hình



Tự lưu trữ là một trải nghiệm đáng cân nhắc cho tất cả mọi người, dù tò mò hay chỉ đơn giản là đam mê. Tuy nhiên, việc thiết lập và cấu hình máy chủ cũng tiềm ẩn một số thách thức công nghệ không hề nhỏ. Đây chính là lúc **sự đơn giản của DietPi** phát huy tác dụng, cho phép bạn cấu hình một hệ thống phù hợp với nhu cầu của mình chỉ trong vài bước đơn giản.



![img](assets/en/24.webp)



Cài đặt cơ bản và nâng cao, tất cả đều nằm trong tầm tay bạn trong Interface có sẵn bằng lệnh:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```