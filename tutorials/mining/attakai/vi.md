---
name: Attakaï

description: biến đổi một S9 thành hệ thống sưởi ấm gia đình
---

![cover](assets/cover.webp)

# Attakai - làm cho việc đào coin tại nhà trở nên khả thi và dễ tiếp cận!

Sáng kiến "Attakaï" khám phá việc đào Bitcoin sử dụng nhiệt lượng sinh ra. Hướng dẫn này đề xuất các giải pháp để biến máy đào trở nên phù hợp sử dụng như các bộ tản nhiệt trong nhà, mang lại sự thoải mái và tiết kiệm năng lượng hơn. Bitcoin tự động điều chỉnh độ khó của việc đào và thưởng cho các thợ mỏ vì công việc của họ. Tuy nhiên, sự tập trung của hashrate có thể đặt ra rủi ro cho tính trung lập của mạng. "Attakaï" cung cấp một hướng dẫn thực tế để nâng cấp máy đào một cách kinh tế, cho phép người tham gia giảm hóa đơn tiền điện và được thưởng bằng sats mà không cần KYC.

## Giới thiệu

"Attakaï," có nghĩa là "nhiệt độ lý tưởng" trong tiếng Nhật, là tên của sáng kiến nhằm khám phá việc đào bitcoin thông qua việc tái sử dụng nhiệt lượng phát ra, được khởi xướng bởi @ajelexBTC và @BlobOnChain cùng với Découvre Bitcoin. Hướng dẫn nâng cấp ASIC này sẽ là cơ sở để tìm hiểu thêm về việc đào, cách hoạt động, lịch sử gần đây, và nền kinh tế cơ bản.

### Tại sao tái sử dụng nhiệt từ một ASIC?

Quan trọng là phải hiểu mối quan hệ giữa năng lượng và sản xuất nhiệt trong một hệ thống điện.

Với một khoản đầu tư 1 kW năng lượng điện, một bộ tản nhiệt điện sản xuất ra 1 kW nhiệt, không hơn không kém. Các bộ tản nhiệt mới không hiệu quả hơn các bộ tản nhiệt truyền thống. Ưu điểm của chúng nằm ở khả năng phân phối nhiệt liên tục và đều đặn trong một phòng, mang lại sự thoải mái hơn so với các bộ tản nhiệt truyền thống thay đổi giữa công suất sưởi cao và không sưởi, do đó tạo ra sự biến đổi nhiệt độ thường xuyên và sự không thoải mái.

Một máy tính, hay rộng hơn là một bảng điện tử, không tiêu thụ năng lượng để thực hiện các phép tính; nó đơn giản chỉ cần năng lượng chảy qua các thành phần của nó để hoạt động. Việc tiêu thụ năng lượng là do điện trở của các thành phần, tạo ra tổn thất và do đó sinh ra nhiệt, được biết đến là hiệu ứng Joule.
Một số công ty đã nghĩ ra ý tưởng kết hợp nhu cầu về sức mạnh tính toán và nhu cầu sưởi ấm thông qua bộ tản nhiệt/máy chủ. Ý tưởng là phân phối máy chủ của một công ty thành các đơn vị nhỏ có thể được đặt trong nhà hoặc văn phòng. Tuy nhiên, ý tưởng này gặp phải một số vấn đề. Nhu cầu về máy chủ không liên quan đến nhu cầu sưởi ấm, và các công ty không thể sử dụng linh hoạt công suất tính toán của máy chủ của họ. Cũng có giới hạn về băng thông mà cá nhân có thể sở hữu. Tất cả những ràng buộc này ngăn cản công ty làm cho những lắp đặt đắt đỏ này trở nên có lợi nhuận hoặc cung cấp một dịch vụ máy chủ trực tuyến ổn định mà không cần đến các trung tâm dữ liệu có khả năng tiếp quản khi không cần sưởi ấm.

> "Nhiệt từ máy tính của bạn không phải là lãng phí nếu bạn cần sưởi ấm nhà bạn. Nếu bạn sử dụng hệ thống sưởi điện nơi bạn sống, thì nhiệt từ máy tính của bạn không phải là lãng phí. Nó có cùng chi phí nếu bạn tạo ra nhiệt này với máy tính của bạn. Nếu bạn có hệ thống sưởi rẻ hơn hệ thống điện, thì sự lãng phí chỉ nằm ở sự chênh lệch chi phí. Nếu là mùa hè và bạn sử dụng điều hòa, thì đó là gấp đôi.
> Việc đào Bitcoin nên diễn ra ở nơi rẻ hơn. Có thể đó sẽ là nơi có khí hậu lạnh và nơi sưởi ấm bằng điện, nơi mà việc đào sẽ trở nên miễn phí."
> Satoshi Nakamoto - Ngày 8 tháng 8 năm 2010
Bitcoin và hệ thống chứng minh công việc của nó nổi bật vì chúng tự động điều chỉnh độ khó của việc đào dựa trên lượng tính toán được thực hiện bởi toàn bộ mạng, lượng này được gọi là hashrate và được biểu thị bằng số hash mỗi giây. Hiện nay, nó được ước tính ở mức 280 Exahash mỗi giây, hay 280 tỷ tỷ hash mỗi giây. Hashrate này đại diện cho công việc và do đó là một lượng năng lượng đã tiêu thụ. Hashrate càng cao thì độ khó tăng lên càng nhiều, và ngược lại. Do đó, một máy đào Bitcoin có thể được kích hoạt hoặc ngừng hoạt động bất cứ lúc nào mà không ảnh hưởng gì đến mạng, không giống như máy chủ/radiator cần phải ổn định để cung cấp dịch vụ của mình. Người đào được thưởng cho công việc đã thực hiện so với công việc của người khác, bất kể sự tham gia này có thể nhỏ như thế nào.

Tóm lại, một bộ sưởi điện và một máy đào Bitcoin đều sản xuất ra 1 kW nhiệt từ 1 kW điện tiêu thụ. Tuy nhiên, người đào còn nhận được bitcoin như một phần thưởng. Bất kể giá điện, giá bitcoin, hay sự cạnh tranh của hoạt động đào trên mạng Bitcoin, việc sưởi ấm bằng máy đào là có lợi ích kinh tế hơn so với sử dụng bộ sưởi điện.

![Video presentation](https://youtu.be/gKoh44UCSnE)

### Giá trị gia tăng cho Bitcoin

Chúng tôi sẽ không đi vào chi tiết của hoạt động đào ở đây (có nguồn lực sẵn có trên học viện nếu cần). Điều quan trọng cần hiểu là việc đào góp phần như thế nào vào việc phân quyền cho Bitcoin. Một số công nghệ hiện có đã được kết hợp một cách tài tình để đưa sự đồng thuận của Nakamoto vào cuộc sống. Sự đồng thuận này kinh tế thưởng cho những người chơi trung thực vì sự tham gia của họ vào việc vận hành mạng Bitcoin, đồng thời làm giảm khả năng của những người chơi không trung thực. Đây là một trong những điểm chính cho phép mạng lưới tồn tại bền vững.

Những người chơi trung thực, những người đào theo quy tắc, đều cạnh tranh với nhau để nhận được phần thưởng lớn nhất có thể cho việc sản xuất các khối mới. Động lực kinh tế này tự nhiên dẫn đến một hình thức tập trung hóa khi các công ty chọn chuyên môn hóa vào hoạt động sinh lợi này bằng cách giảm chi phí thông qua quy mô kinh tế. Những người chơi công nghiệp này có vị trí thuận lợi để mua và bảo trì máy móc, cũng như thương lượng mức giá điện hàng loạt.

> "Ban đầu, hầu hết người dùng sẽ chạy các nút mạng, nhưng khi mạng phát triển vượt qua một điểm nhất định, nó sẽ càng ngày càng được để lại cho các chuyên gia với các trang trại máy chủ của phần cứng chuyên dụng. Một trang trại máy chủ chỉ cần chạy một nút trên mạng và phần còn lại của LAN kết nối với nút đó." - Satoshi Nakamoto - Ngày 2 tháng 11 năm 2008

Một số thực thể nắm giữ một tỷ lệ đáng kể của tổng hashrate trong các trang trại đào lớn. Chúng ta có thể quan sát đợt sóng lạnh gần đây ở Hoa Kỳ nơi một phần lớn hashrate đã bị ngừng trực tuyến để chuyển hướng năng lượng cho các hộ gia đình có nhu cầu điện đặc biệt. Trong vài ngày, các thợ đào được kích thích kinh tế để tắt các trang trại của họ, và do đó chúng ta có thể thấy điều kiện thời tiết ngoại lệ này trên đường cong hashrate của Bitcoin.

Vấn đề này có thể trở nên phức tạp và đặt ra một rủi ro đáng kể đối với tính trung lập của mạng. Một người chơi sở hữu hơn 51% hashrate có thể dễ dàng kiểm duyệt các giao dịch nếu họ muốn. Đó là lý do tại sao việc phân phối hashrate giữa nhiều người chơi thay vì các thực thể tập trung có thể dễ dàng bị một chính phủ chiếm đoạt, chẳng hạn, là quan trọng.

**Nếu các thợ đào được phân tán khắp hàng nghìn, thậm chí hàng triệu, hộ gia đình trên khắp thế giới, việc cho một quốc gia kiểm soát họ trở nên rất phức tạp.**
Tại nhà máy, một máy đào không phù hợp để sử dụng như một bộ tản nhiệt trong nhà ở, do hai vấn đề chính: tiếng ồn quá mức và thiếu khả năng điều chỉnh. Tuy nhiên, những vấn đề này có thể được giải quyết một cách dễ dàng thông qua những thay đổi đơn giản được thực hiện trên phần cứng và phần mềm, cho phép có một máy đào yên tĩnh hơn nhiều có thể được cấu hình và tự động hóa giống như các loại máy sưởi điện hiện đại.
**Attakaï là một sáng kiến giáo dục dạy bạn cách nâng cấp Antminer S9 một cách tiết kiệm chi phí nhất có thể.**

Đây là một cơ hội tuyệt vời để học bằng cách thực hành. Ngoài việc giảm hóa đơn điện của bạn, bạn còn được thưởng cho sự tham gia của mình bằng KYC sats miễn phí.

## Chương 1: Hướng dẫn Mua Máy ASIC Cũ

Trong phần này, chúng tôi sẽ thảo luận về các phương pháp tốt nhất khi mua một Bitmain Antminer S9 đã qua sử dụng, máy mà hướng dẫn nâng cấp bộ tản nhiệt này sẽ dựa trên. Hướng dẫn này cũng áp dụng cho các mô hình ASIC khác vì đây là một hướng dẫn mua hàng cũ chung cho phần cứng đào mỏ.

Antminer S9 là thiết bị được Bitmain cung cấp từ tháng 5 năm 2016. Nó tiêu thụ 1323W điện và sản xuất 13.5 TH/s. Mặc dù được coi là cũ, nó vẫn là một lựa chọn xuất sắc để bắt đầu đào. Vì nó đã được sản xuất với số lượng lớn, nên rất dễ tìm kiếm phụ tùng thay thế phong phú ở nhiều khu vực trên thế giới. Nói chung, nó có thể được mua từ người dùng sang người dùng trên các trang web như Ebay hoặc LeBonCoin, vì các nhà bán lẻ chuyên nghiệp không còn cung cấp nó do tính cạnh tranh thấp hơn so với các máy mới hơn. Nó kém hiệu quả hơn so với ASIC như Antminer S19, được giới thiệu từ tháng 3 năm 2020, nhưng điều này làm cho nó trở thành phần cứng cũ giá cả phải chăng và phù hợp hơn cho các sửa đổi mà chúng tôi sẽ thực hiện.

Antminer S9 có một số biến thể (i, j) mang lại những thay đổi nhỏ cho phần cứng thế hệ đầu tiên. Chúng tôi không tin rằng điều này nên ảnh hưởng đến quyết định mua của bạn, và hướng dẫn này sẽ áp dụng cho tất cả các biến thể này.

Giá của ASIC thay đổi tùy thuộc vào nhiều yếu tố như giá bitcoin, độ khó của mạng, hiệu quả máy móc, và chi phí điện. Do đó, khó có thể đưa ra một ước lượng chính xác cho việc mua một máy cũ. Vào tháng 2 năm 2023, giá dự kiến ở Pháp nói chung dao động từ €100 đến €200, nhưng những giá này có thể thay đổi nhanh chóng.

![image](assets/guide-achat/1.webp)

Antminer S9 bao gồm các bộ phận sau:

- 3 bảng hash nơi các chip sản xuất sức mạnh băm được đặt

![image](assets/guide-achat/2.webp)

- Một bảng điều khiển bao gồm một khe cắm cho thẻ SD, cổng Ethernet, và các kết nối cho bảng hash và quạt. Đây là bộ não của ASIC của bạn.
  ![image](assets/guide-achat/3.webp)

- 3 cáp dữ liệu kết nối các bảng hash với bảng điều khiển.

![image](assets/guide-achat/4.webp)

- Nguồn cung cấp điện hoạt động trên 220V và có thể được cắm như một thiết bị gia dụng thông thường.

![image](assets/guide-achat/5.webp)

- 2 quạt 120mm.

![image](assets/guide-achat/6.webp)

- Một cáp nam C13.

![image](assets/guide-achat/7.webp)
Khi mua một máy móc đã qua sử dụng, điều quan trọng là phải kiểm tra xem tất cả các bộ phận có đầy đủ và hoạt động không. Trong quá trình giao dịch, bạn nên yêu cầu người bán bật máy để xác minh sự hoạt động đúng đắn của nó. Quan trọng là phải kiểm tra xem thiết bị có khởi động đúng cách không, sau đó kiểm tra kết nối internet bằng cách kết nối cáp Ethernet và truy cập giao diện kết nối Bitmain thông qua một trình duyệt web trên cùng một mạng cục bộ. Bạn có thể tìm thấy địa chỉ IP này bằng cách kết nối với giao diện router internet của bạn và tìm kiếm các thiết bị đã kết nối. Địa chỉ này nên có định dạng sau: 192.168.x.x
![image](assets/guide-achat/8.webp)

Ngoài ra, kiểm tra xem thông tin đăng nhập mặc định có hoạt động không (tên đăng nhập: root, mật khẩu: root). Nếu thông tin đăng nhập mặc định không hoạt động, bạn sẽ cần thực hiện việc đặt lại máy.

![image](assets/guide-achat/9.webp)

Một khi đã kết nối, bạn nên có thể xem trạng thái của từng bảng hash trên bảng điều khiển. Nếu máy đào được kết nối với một pool, bạn nên thấy tất cả các bảng hash đang hoạt động. Quan trọng là phải lưu ý rằng máy đào tạo ra rất nhiều tiếng ồn, điều này là bình thường. Cũng, hãy chắc chắn rằng quạt đang hoạt động đúng cách.

Sau đó, bạn có thể loại bỏ pool đào của chủ sở hữu trước để thiết lập pool của riêng bạn sau này. Nếu muốn, bạn cũng có thể kiểm tra các bảng hash bằng cách tháo máy. Tuy nhiên, bước này phức tạp hơn và đòi hỏi nhiều thời gian và một số công cụ nhất định. Nếu bạn muốn tiến hành việc tháo này, bạn có thể tham khảo phần tiếp theo của hướng dẫn này chi tiết cách làm điều đó. Quan trọng là phải lưu ý rằng máy đào thu thập rất nhiều bụi và đòi hỏi bảo dưỡng định kỳ. Bạn có thể quan sát sự tích tụ bụi và chất lượng bảo dưỡng bằng cách tháo máy.
Sau khi xem xét tất cả những điểm này, bạn có thể mua máy của mình với một mức độ tự tin cao. Nếu có nghi ngờ, hãy liên hệ với cộng đồng, và nếu bạn cần thiết bị để hoàn thành hướng dẫn này, đừng ngần ngại gửi cho chúng tôi một tin nhắn.
Tóm tắt hướng dẫn này trong một câu: **"Đừng tin, hãy kiểm chứng."**

## Chương 2: Hướng dẫn Mua Sắm Phụ Tùng Điều Chỉnh

![image](assets/piece/1.webp)

### Làm thế nào để biến Antminer S9 của bạn thành một máy sưởi yên tĩnh và kết nối?

Nếu bạn sở hữu một Antminer S9, có lẽ bạn đã biết nó có thể ồn ào và cồng kềnh như thế nào. Tuy nhiên, có thể biến nó thành một máy sưởi yên tĩnh và kết nối bằng cách theo dõi một số bước đơn giản. Trong bài viết này, chúng tôi sẽ trình bày thiết bị cần thiết để thực hiện các sửa đổi, trong khi một bài viết sau sẽ giải thích chi tiết các bước cần theo dõi để thực hiện những thay đổi này.

### 1. Thay thế quạt

Quạt gốc của Antminer S9 quá ồn để sử dụng nó như một máy sưởi. Giải pháp là thay thế chúng bằng quạt yên tĩnh hơn. Đội ngũ của chúng tôi đã thử nghiệm một số mô hình từ thương hiệu Noctua và chọn Noctua NF-A14 iPPC-2000 PWM là sự thỏa hiệp tốt nhất. Hãy chắc chắn chọn phiên bản 12V của quạt. Quạt 140mm này có thể tạo ra tới 1300W nhiệt trong khi duy trì mức độ ồn lý thuyết là 31 dB. Để lắp đặt những quạt 140mm này, bạn sẽ cần một bộ chuyển đổi từ 140mm sang 120mm, mà bạn có thể tìm thấy tại cửa hàng DécouvreBitcoin. Chúng tôi cũng sẽ thêm lưới bảo vệ 140mm.

![image](assets/piece/1.webp)
![image](assets/piece/2.webp)
![image](assets/piece/3.webp)
Quạt nguồn cung cấp cũng khá ồn và cần được thay thế. Chúng tôi khuyến nghị sử dụng quạt Noctua NF-A6x25 PWM. Lưu ý rằng các đầu nối của quạt Noctua không giống với đầu nối gốc, vì vậy bạn sẽ cần một bộ chuyển đổi đầu nối để kết nối chúng. Hai cái là đủ. Lại một lần nữa, hãy chắc chắn chọn phiên bản 12V của quạt.
![image](assets/piece/4.webp)
![image](assets/piece/5.webp)

### 2. Thêm cầu nối WIFI/Ethernet

Thay vì sử dụng cáp Ethernet, bạn có thể kết nối Antminer của mình với WIFI bằng cách thêm một cầu nối WIFI/Ethernet. Chúng tôi đã chọn vonets vap11g-300 vì nó dễ dàng cho phép bạn thu tín hiệu WIFI từ hộp Internet của mình và truyền nó đến Antminer qua Ethernet mà không tạo ra một subnet. Nếu bạn có kỹ năng về điện, bạn có thể cung cấp điện trực tiếp cho nó bằng nguồn cung cấp điện của Antminer mà không cần thêm bộ sạc USB. Đối với điều này, bạn sẽ cần một jack nữ 5.5mmx2.1mm.

![image](assets/piece/6.webp)
![image](assets/piece/7.webp)

### 3. Tùy chọn: Thêm ổ cắm thông minh

Nếu bạn muốn bật/tắt Antminer của mình từ điện thoại thông minh và theo dõi mức tiêu thụ điện năng của nó, bạn có thể thêm một ổ cắm thông minh. Chúng tôi đã thử nghiệm ổ cắm ANTELA phiên bản 16A, tương thích với ứng dụng smartlife. Ổ cắm thông minh này cho phép bạn kiểm tra mức tiêu thụ điện năng hàng ngày và hàng tháng và kết nối trực tiếp với hộp Internet của bạn qua WIFI.
![image](assets/piece/8.webp)

> Danh sách thiết bị và liên kết
>
> - 2X miếng chuyển đổi 3D từ 140mm sang 120mm
> - 2X NF-A14 iPPC-2000 PWM [link](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - 2X lưới quạt 140mm [link](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - Noctua NF-A6x25 PWM [link](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
- Đường dây điện 2.5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- Vonets VAP11G-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
- Tùy chọn: Ổ cắm thông minh ANTELA https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

## Chương 3 - HƯỚNG DẪN: Làm thế nào để biến một máy đào thành một bộ sưởi?

![image](assets/hardware/0.webp)

Nếu bạn là một người yêu thích tự làm và muốn biến một máy đào thành bộ sưởi, hướng dẫn này dành cho bạn. Chúng tôi muốn cảnh báo bạn rằng việc chỉnh sửa một thiết bị điện tử có thể gây ra nguy cơ về điện và hỏa. Việc lấy tất cả các biện pháp phòng ngừa cần thiết để tránh bất kỳ thiệt hại hoặc chấn thương nào là rất quan trọng.
Ngay từ nhà máy, một máy đào không thực sự có thể sử dụng như một bộ tản nhiệt trong nhà vì nó quá ồn và không thể điều chỉnh. Tuy nhiên, có thể thực hiện một số chỉnh sửa đơn giản để giải quyết những vấn đề này.

> CẢNH BÁO: Điều cần thiết là phải đã cài đặt trước Braiins OS+ trên máy đào của bạn hoặc bất kỳ phần mềm nào khác có thể giảm hiệu suất của máy. Biện pháp này rất quan trọng bởi vì, để giảm tiếng ồn, chúng tôi sẽ lắp đặt quạt ít mạnh mẽ hơn có thể tản nhiệt ít hơn.

### Vật liệu cần thiết

- 2 bộ chuyển đổi 3D từ 140mm sang 120mm
- 2 quạt Noctua NF-A14 iPPC-2000 PWM
- 2 lưới bảo vệ quạt 140mm
- 1 quạt Noctua NF-A6x25 PWM
- Đường dây điện 2.5mm2
- Vonets VAP11G-300
- Tùy chọn: Ổ cắm thông minh ANTELA

### Thay thế quạt

Chúng tôi sẽ bắt đầu bằng việc thay thế quạt của nguồn cung cấp.

> CẢNH BÁO: Trước hết và quan trọng nhất, trước khi bắt đầu, hãy chắc chắn rằng bạn đã rút phích cắm của máy đào để tránh bất kỳ nguy cơ điện giật nào.

![image](assets/hardware/1.webp)

Chúng tôi sẽ bắt đầu bằng việc thay thế quạt của nguồn cung cấp.

Đầu tiên, tháo 6 ốc vít ở bên cạnh thùng máy giữ nó đóng lại. Sau khi các ốc vít được tháo ra, nhẹ nhàng mở thùng máy để lấy bỏ vỏ nhựa bảo vệ các linh kiện bên trong.

![image](assets/hardware/2.webp)
![image](assets/hardware/3.webp)
Tiếp theo, đã đến lúc tháo quạt gốc, lưu ý không làm hỏng các linh kiện khác. Để làm điều này, hãy tháo các ốc giữ nó và nhẹ nhàng gỡ bỏ keo trắng xung quanh đầu nối. Quan trọng là phải tiến hành một cách cẩn thận để tránh làm hỏng dây hoặc đầu nối. ![image](assets/hardware/4.webp)

Khi quạt gốc đã được tháo ra, bạn sẽ nhận thấy rằng đầu nối của quạt Noctua mới không khớp với quạt gốc. Thực tế, quạt mới có 3 dây, bao gồm một dây màu vàng cho phép điều khiển tốc độ. Tuy nhiên, dây này sẽ không được sử dụng trong trường hợp cụ thể này. Để kết nối quạt mới, khuyến nghị sử dụng một bộ chuyển đổi đặc biệt. Tuy nhiên, quan trọng là phải lưu ý rằng bộ chuyển đổi này đôi khi có thể khó tìm.

![image](assets/hardware/5.webp)

Nếu bạn không có bộ chuyển đổi này, bạn vẫn có thể tiếp tục kết nối quạt mới bằng cách sử dụng một nút nối dây. Để làm điều này, bạn sẽ cần cắt các dây của quạt cũ và quạt mới.

![image](assets/hardware/6.webp)
![image](assets/hardware/7.webp)

Trên quạt mới, sử dụng dao cắt và cẩn thận cắt đường viền của vỏ chính ở 1cm mà không cắt vỏ của các dây bên dưới.

![image](assets/hardware/8.webp)

Sau đó, kéo vỏ chính xuống dưới, cắt vỏ của dây đỏ và dây đen theo cách tương tự như trước. Và cắt dây vàng ngang.

![image](assets/hardware/9.webp)

Trên quạt cũ, việc cắt vỏ chính mà không làm hỏng vỏ của dây đỏ và dây đen là khó khăn hơn. Để làm điều này, chúng tôi đã sử dụng một cây kim mà chúng tôi luồn giữa vỏ chính và dây đỏ và dây đen.

![image](assets/hardware/10.webp)
![image](assets/hardware/11.webp)

Một khi dây đỏ và dây đen đã lộ ra, cắt vỏ một cách cẩn thận để tránh làm hỏng dây điện.

![image](assets/hardware/12.webp)

Sau đó, kết nối các dây bằng nút nối dây, dây đen với dây đen và dây đỏ với dây đỏ. Bạn cũng có thể thêm băng điện.

![image](assets/hardware/13.webp)
![image](assets/hardware/14.webp)

Một khi kết nối đã được thực hiện, đã đến lúc lắp quạt Noctua mới với lưới và các ốc cũ, các ốc mới trong hộp sẽ được sử dụng lại sau. Đảm bảo đặt nó với hướng đúng. Bạn sẽ nhận thấy một mũi tên trên một bên của quạt, chỉ hướng luồng khí. Quan trọng là phải đặt quạt sao cho mũi tên này hướng vào bên trong của thùng máy. Sau đó, kết nối lại quạt.
![image](assets/hardware/15.webp)![image](assets/hardware/16.webp)

> Tùy chọn: Nếu bạn có kỹ năng về điện, bạn có thể trực tiếp thêm một đầu nối jack nữ 5.5mm vào nguồn điện 12V, điều này sẽ cho phép bạn cung cấp điện trực tiếp cho cầu Wi-Fi Vonet. Tuy nhiên, nếu bạn không chắc về kỹ năng điện của mình, tốt nhất là sử dụng đầu nối USB với bộ sạc điện thoại để tránh bất kỳ rủi ro nào về mạch ngắn hoặc hỏng hóc điện.

![image](assets/hardware/17.webp)

Một khi các kết nối đã được thực hiện, hãy chắc chắn đặt nắp nhựa lên trên vỏ nhựa và không phải bên trong.

![image](assets/hardware/18.webp)
Cuối cùng, đặt lại nắp vỏ và vặn 6 ốc ở các cạnh để giữ mọi thứ cố định an toàn. Và bạn đã hoàn thành, vỏ nguồn của bạn giờ đã được trang bị quạt mới.
### Thay thế 2 quạt chính

1. Đầu tiên, ngắt kết nối quạt và tháo ốc.
   ![image](assets/hardware/19.webp)

2. Các đầu nối của quạt Noctua mới không khớp với đầu nối gốc, nhưng đừng hoảng sợ! Lấy dao cắt ra và cẩn thận cắt bỏ các thanh nhựa nhỏ để các đầu nối vừa khít với máy đào của bạn.

![image](assets/hardware/20.webp)
![image](assets/hardware/21.webp)

3. Đã đến lúc lắp đặt các bộ phận 3D!
   Gắn chúng vào cả hai bên của máy đào sử dụng các ốc bạn đã tháo ra từ quạt. Vặn cho đến khi đầu ốc chìm vào bộ phận 3D và được giữ chắc chắn. Hãy cẩn thận không vặn quá chặt, vì bạn có thể làm biến dạng bộ phận và một trong các ốc có thể chạm vào tụ điện! Sau đó cắt cẩn thận các thanh nhựa nhỏ để các đầu nối vừa khít với máy đào của bạn.

![image](assets/hardware/22.webp)

4. Bây giờ chúng ta chuyển sang quạt.
   Gắn chúng vào các bộ phận 3D sử dụng các ốc được cung cấp trong hộp. Chú ý đến hướng luồng khí, các mũi tên trên cạnh của quạt sẽ chỉ hướng bạn cần theo. Di chuyển từ phía cổng Ethernet sang phía bên kia. Xem hình dưới đây.

![image](assets/hardware/23.webp)
![image](assets/hardware/24.webp)
![image](assets/hardware/25.webp)

5. Bước cuối cùng: cắm quạt và gắn lưới bảo vệ phía trên với các ốc không sử dụng từ hộp quạt. Bạn chỉ có 4, nhưng 2 ốc cho mỗi lưới ở các góc đối diện sẽ đủ. Bạn cũng có thể tìm các ốc tương tự khác tại cửa hàng phần cứng nếu cần.

![image](assets/hardware/26.webp)
'![image](assets/hardware/27.webp)

Trong khi chờ đợi có thể cung cấp một vỏ bọc đẹp hơn cho bộ sưởi mới của bạn, bạn có thể gắn vỏ và nguồn cùng nhau bằng dây buộc điện.

![image](assets/hardware/28.webp)

Và cho bước hoàn thiện, kết nối cầu nối Vonet vào cổng Ethernet trên nguồn của nó. Nếu bạn chưa thực hiện, bạn có thể theo dõi hướng dẫn này để thiết lập cầu nối của mình.

![image](assets/hardware/29.webp)

Và đó là, xin chúc mừng! Bạn vừa thay thế toàn bộ phần cơ khí của máy đào của mình. Bây giờ bạn nên nghe thấy tiếng ồn ít hơn nhiều.

## Chương 4 - Sửa đổi Phần mềm - Đặt lại Antminer S9

**Loạt bài viết được đề xuất bởi BlobOnChain & Ajelex - 15/02/2023**

### Đặt lại qua nút "Reset"

Phương pháp này có thể được áp dụng trong vòng 10 phút sau khi khởi động máy đào.

Sau khi bật máy đào trong 2 phút, hãy nhấn nút "Reset" trong 5 giây, sau đó thả ra. Máy đào sẽ được khôi phục về cài đặt gốc trong vòng 4 phút và sẽ tự động khởi động lại (không cần phải tắt máy).

![image](assets/software/1.webp)

Khôi phục qua web

Đăng nhập vào giao diện người dùng của máy đào của bạn, nhấp vào "Upgrade" >> "Perform a reset", sau đó nhấp "OK" trong cửa sổ pop-up.

### Hệ điều hành gốc
Trong phần này, chúng ta sẽ giả định rằng máy đang hoạt động, chạy và hệ điều hành gốc của nó đã được cài đặt. Chúng ta sẽ nhanh chóng xem qua giao diện của hệ điều hành gốc do Bitmain cung cấp.
Đầu tiên, kết nối với máy của bạn thông qua mạng nội bộ:

![hình ảnh](assets/software/2.webp)

Khi bạn đến trang đăng nhập, bạn sẽ cần đăng nhập vào ASIC sử dụng thông tin đăng nhập mặc định:

- tên người dùng: root
- mật khẩu: root

(Làm thế nào để đặt lại nếu mật khẩu mặc định không hoạt động?)

Hệ điều hành chính tương đối cơ bản. Với 4 tab: Hệ Thống, Cấu Hình Miner, Trạng Thái Miner, Mạng. Trong tab Cấu Hình Miner, bạn có thể cấu hình tối đa 3 nhóm đào.

![hình ảnh](assets/software/3.webp)

Trong tab Trạng Thái Miner, bạn có thể quan sát các thông tin khác nhau về hoạt động trực tiếp của ASIC. Tốc độ băm được biểu thị bằng GH/s, thông tin chi tiết hơn về nhóm, cũng như chi tiết về trạng thái của từng bảng băm và tốc độ quạt tính bằng vòng/phút.

![hình ảnh](assets/software/4.webp)

### Braiins OS+

Bây giờ, chúng ta sẽ nghiên cứu phần mềm cho ASIC Braiins OS+ (https://braiins.com/os/plus). Phần mềm được phát triển bởi công ty Braiins (https://braiins.com/), là công ty mẹ của nhóm đào Braiins Pool (https://braiins.com/pool). Nhóm đào này hiện có 4.39% tổng tốc độ băm toàn cầu (https://mempool.space/fr/mining/pool/slushpool) tại thời điểm viết những dòng này. Công ty có trụ sở tại Prague trước đây được biết đến với tên là Slushpool và là nhóm đào đầu tiên bắt đầu vào tháng 11 năm 2010. Ngày nay, công ty, với các hoạt động khác nhau của mình, cung cấp công cụ nghiên cứu lợi nhuận cho việc đào (https://insights.braiins.com/en), giải pháp quản lý trang trại đào song song với hoạt động nhóm của mình, và phần mềm tối ưu hóa cho ASIC. Nó cũng cung cấp việc đào sử dụng giao thức Stratum V2 mới (https://braiins.com/bitcoin-mining-stack-upgrade).

Chúng ta sẽ do đó nghiên cứu chi tiết hơn về hoạt động của các thiết bị Bitmain, hiện là các mô hình duy nhất tương thích:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Phần mềm Braiins OS có thể dễ dàng được cài đặt trên tất cả các máy nêu trên. Nó sẽ cho phép kiểm soát chính xác hơn của một máy bằng cách cho phép tăng tốc hoặc giảm tốc. Nó cũng cho phép điều chỉnh tinh tế tần số của từng chip thông qua tính năng tối ưu hóa tự động gọi là autotuning. Vì mỗi chip băm hơi khác nhau do quá trình sản xuất của nó, phần mềm kiểm tra tần số tối ưu cho mỗi chip để đạt được hiệu suất tối đa (W/THs). Phần mềm tuyên bố đạt được hiệu suất có thể cao hơn 25% so với bản gốc. Theo các phép đo của chúng tôi, có thể đạt được những con số này.

## Cài đặt Braiins OS+

Có một số cách để cài đặt Braiins OS+ trên một ASIC. Bạn có thể tham khảo hướng dẫn này cũng như tài liệu chính thức từ Braiins và các video hướng dẫn.
Cài đặt Braiins OS+ trực tiếp trên bộ nhớ của Antminer

Học cách dễ dàng cài đặt Braiins OS+ trực tiếp trên bộ nhớ của Antminer của bạn sử dụng BOS toolbox, thay thế hệ điều hành gốc, thông qua các bước chi tiết dưới đây. Nếu bạn muốn giữ hệ điều hành gốc song song, bạn có thể cài đặt Braiins OS+ trên một thẻ SD.
1. Bật Antminer của bạn và kết nối nó với hộp internet của bạn.
2. Tải xuống BOS toolbox cho Windows / Linux.
3. Giải nén tệp đã tải và mở tệp bos-toolbox.bat, chọn ngôn ngữ, và sau một lúc bạn sẽ thấy cửa sổ này:
   ![image](assets/software/5.webp)

4. BOS toolbox sẽ giúp bạn dễ dàng tìm địa chỉ IP của Antminer và cài đặt Braiins OS+. Nếu bạn đã biết địa chỉ IP của máy, bạn có thể bỏ qua đến bước 8. Nếu không, hãy chuyển đến tab quét.

![image](assets/software/6.webp)

5. Thông thường, trên các mạng gia đình, phạm vi địa chỉ IP nằm giữa 192.168.1.1 và 192.168.1.255, vì vậy nhập "192.168.1.0/24" vào trường phạm vi IP. Nếu mạng của bạn khác, vui lòng thay đổi các địa chỉ này. Sau đó nhấn vào "Bắt đầu".

6. Chú ý, nếu Antminer có mật khẩu, việc phát hiện sẽ không hoạt động. Nếu đó là trường hợp, giải pháp đơn giản nhất là thực hiện cài đặt lại cài đặt gốc.

7. Bạn sẽ thấy tất cả các Antminer trên mạng của mình, ở đây địa chỉ IP là 192.168.1.37.

![image](assets/software/7.webp)

8. Nhấn vào Quay lại, sau đó chuyển đến tab cài đặt, nhập địa chỉ IP đã tìm thấy trước đó vào trường Miner(s) và "admin" (hoặc "root") vào trường Mật khẩu, đó là mật khẩu mặc định, sau đó nhấn vào "Bắt đầu".
   Nếu việc cài đặt không hoạt động với "admin" hoặc "root" làm mật khẩu, có thể cần thực hiện cài đặt lại cài đặt gốc và thử lại.

![image](assets/software/8.webp)

9. Sau vài phút, Antminer của bạn sẽ khởi động lại và bạn sẽ có thể truy cập giao diện Braiins OS+ tại địa chỉ IP đó, ở đây là 192.168.1.37, trực tiếp trong thanh địa chỉ của trình duyệt của bạn. Tên người dùng mặc định là "root" và không có mật khẩu mặc định.
   Cài đặt Braiins OS+ trên thẻ SD

![image](assets/software/9.webp)

![image](assets/software/10.webp)

Phương pháp thứ hai sử dụng giao diện gốc của Antminer của bạn. Phương pháp này hoạt động cho các máy có hệ điều hành từ trước năm 2019.

### Giao Diện Antminer

1. Tải xuống hệ điều hành mới để cài đặt tại đây.
2. Như trong phần trước, kết nối với máy của bạn qua mạng địa phương.
3. Chuyển đến tab Hệ thống và sau đó Nâng cấp.
4. Tải tệp bạn đã tải xuống và flash hình ảnh.

![image](assets/software/11.webp)

### Thẻ Micro SD

Một phương pháp thứ hai cho phép bạn sử dụng thẻ micro SD. Phương pháp này chỉ hoạt động với các máy có hệ điều hành từ sau năm 2019.

1. Tải xuống hệ điều hành mới để cài đặt tại đây.

2. Flash hình ảnh đã tải xuống vào thẻ micro SD. Để làm điều này, bạn có thể sử dụng Etcher. Chỉ đơn giản sao chép tệp vào thẻ micro SD sẽ không hoạt động.
3. Nếu bạn sở hữu một Antminer S9 và các biến thể của nó (S9i, S9j), bạn sẽ cần phải điều chỉnh các jumper để buộc ASIC của bạn khởi động từ tệp trên thẻ micro SD thay vì NAND. Nếu bạn có một mẫu khác, bạn có thể bỏ qua và chuyển đến phần 4. Các jumper nằm trên bảng điều khiển ở phần trên của ASIC, gần cổng Ethernet. Bạn sẽ cần phải tháo nó ra bằng cách trượt nó về phía sau. Một khi vị trí jumper được chỉnh sửa như hình dưới đây KHỞI ĐỘNG TỪ SD, bạn có thể lắp lại bảng điều khiển và kết nối lại S9.
![image](assets/software/12.webp)

![image](assets/software/13.webp)

4. Chèn thẻ micro SD vào ASIC.
5. Khởi động ASIC. Nếu phiên bản cài đặt tự động được sử dụng, hệ điều hành mới sẽ được cài đặt tự động. Việc cài đặt hoàn tất khi cả hai đèn LED sáng cùng một lúc. Bạn có thể khởi động lại ASIC và loại bỏ thẻ micro SD. Nếu phiên bản khác được tải về, bạn sẽ cần phải để thẻ micro SD bên trong ASIC.

Để biết thêm thông tin về cài đặt, bạn có thể truy cập phần này trên trang web của Braiins.

## Giao Diện

Bạn sẽ cần kết nối với ASIC của mình một cách tương tự. Sử dụng địa chỉ IP cục bộ của thiết bị trên mạng của bạn thông qua trình duyệt.

Thông tin đăng nhập mặc định giống như hệ điều hành gốc.

- tên đăng nhập: root
- mật khẩu: root

Sau đó, bạn sẽ được chào đón bởi Bảng Điều Khiển của Brains OS+.

### Bảng Điều Khiển

![image](assets/software/14.webp)

Trên trang đầu tiên này, bạn có thể quan sát hiệu suất thực tế của máy của mình.

- Ba biểu đồ thời gian thực hiển thị nhiệt độ, hashrate, và tình trạng tổng thể của máy.
- Bên phải, hashrate thực tế, nhiệt độ chip trung bình, hiệu quả ước tính theo W/THs, và mức tiêu thụ điện năng.
- Bên dưới, tốc độ quạt tính theo phần trăm tốc độ tối đa và số vòng quay mỗi phút.

![image](assets/software/15.webp)

- Phía dưới, bạn sẽ tìm thấy một cái nhìn chi tiết về từng hashboard. Nhiệt độ trung bình của bảng và các chip bên trong nó, điện áp, và tần số.
- Chi tiết về các hồ bơi khai thác hoạt động trong Pools.
- Tình trạng của autotuning trong Tuner Status.
- Bên phải, chi tiết về các share được truyền đến hồ bơi.

### Cấu Hình

![image](assets/software/16.webp)

### Hệ Thống

![image](assets/software/17.webp)

### Hành Động Nhanh

![image](assets/software/18.webp)

Cấu hình một hồ bơi khai thác
Người ta có thể hình dung một hồ bơi khai thác (mining pool) như một hợp tác xã nông nghiệp. Các nông dân gộp sản xuất của họ lại với nhau để giảm biến động của cung và cầu và do đó, có được thu nhập ổn định hơn cho hoạt động của họ. Một hồ bơi khai thác hoạt động theo cùng một cách, và nguyên liệu được gộp lại là các hash. Thực tế, việc phát hiện ra một hash hợp lệ duy nhất cho phép tạo ra một khối và do đó giành được coinbase hoặc phần thưởng, hiện tại là 6.25 BTC cộng với các phí giao dịch được bao gồm trong khối. Nếu bạn khai thác một mình, bạn chỉ được thưởng khi tìm thấy một khối. Khi cạnh tranh với tất cả các thợ mỏ khác trên hành tinh, bạn sẽ có rất ít cơ hội giành chiến thắng trong xổ số lớn này và bạn vẫn phải trả các phí liên quan đến việc sử dụng máy đào của mình mà không có bất kỳ bảo đảm nào về thành công. Các hồ bơi khai thác giải quyết vấn đề này bằng cách gộp công suất tính toán của nhiều (hàng nghìn) thợ mỏ và chia sẻ phần thưởng của họ dựa trên tỷ lệ phần trăm tham gia vào hashrate của hồ khi một khối được tìm thấy. Để hình dung cơ hội của bạn trong việc khai thác một khối một mình, bạn có thể sử dụng công cụ này. Bằng cách nhập thông tin của một Antminer S9, chúng ta có thể thấy rằng cơ hội tìm thấy một hash cho phép tạo ra một khối là 1 trong 24,777,849 cho mỗi khối hoặc 1 trong 172,068 mỗi ngày. Trung bình (với hashrate và độ khó không đổi), nó sẽ mất 471 năm để tìm thấy một khối.
Tuy nhiên, vì mọi thứ trong Bitcoin đều là xác suất, đôi khi các thợ mỏ solo được thưởng cho việc chấp nhận rủi ro này: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Nếu bạn thích cờ bạc, bạn có thể thử, nhưng hướng dẫn của chúng tôi sẽ không tập trung vào hướng đó. Thay vào đó, chúng tôi sẽ tập trung vào hồ bơi khai thác phù hợp nhất với nhu cầu của chúng tôi để tạo ra một hệ thống sưởi.
Những điều cần xem xét khi chọn một hồ bơi khai thác là hoạt động của hệ thống phần thưởng của hồ, có thể khác nhau, cũng như số lượng tối thiểu trước khi có thể rút phần thưởng về một địa chỉ. Ví dụ, Braiins, cung cấp phần mềm mà chúng tôi đang nói ở đây, cũng cung cấp một hồ bơi. Hồ bơi này có một hệ thống phần thưởng gọi là "Score" khuyến khích thợ mỏ khai thác trong thời gian dài. Sự tham gia bao gồm một yếu tố thời gian hoạt động được biểu thị bằng "scoring hashrate". Trong trường hợp của chúng tôi, nơi chúng tôi muốn một hệ thống sưởi có thể được bật chỉ trong vài phút, đây không phải là hệ thống phần thưởng lý tưởng. Chúng tôi ưu tiên một hệ thống phần thưởng cho chúng tôi một phần thưởng bằng nhau cho mỗi lần tham gia. Ngoài ra, số lượng rút tối thiểu cho Braiins Pool là 100,000 sats và On-Chain. Vì vậy, chúng tôi mất một số sats trong phí giao dịch và một phần của phần thưởng của chúng tôi có thể bị khóa nếu chúng tôi không khai thác đủ trong mùa đông.

Mô hình phần thưởng mà chúng tôi quan tâm là PPS, có nghĩa là "trả tiền theo mỗi cổ phần". Điều này có nghĩa là thợ mỏ sẽ nhận được phần thưởng cho mỗi cổ phần hợp lệ. Cũng có một biến thể của hệ thống này, FPPS (Full Pay Per Share), không chỉ chia sẻ phần thưởng coinbase, mà còn cả các phí giao dịch được bao gồm trong khối. Các hồ bơi khai thác mà chúng tôi khuyên dùng để kết nối hệ thống khai thác/sưởi của bạn là Linecoin Pool (FPPS) và Nicehash (PPS).

- Nicehash: Lợi ích của Nicehash là việc rút tiền có thể được thực hiện bằng Lightning với phí tối thiểu. Ngoài ra, số lượng rút tối thiểu là 2000 sats. Nhược điểm là Nicehash sử dụng hashrate của mình cho blockchain có lợi nhuận cao nhất, mà không thực sự cho phép người dùng kiểm soát, vì vậy nó có thể không nhất thiết tham gia vào hashrate của Bitcoin.
- Linecoin: Ưu điểm của Linecoin là số lượng tính năng được cung cấp, như bảng điều khiển chi tiết, khả năng thực hiện rút tiền với Paynym (BIP 47) để bảo vệ quyền riêng tư tốt hơn, và việc tích hợp bot Telegram cũng như tự động hóa có thể cấu hình trực tiếp trong ứng dụng di động. Pool này chỉ đào các khối Bitcoin, nhưng số lượng tối thiểu để rút tiền vẫn cao, ở mức 100,000 sats. Chúng tôi sẽ xem xét giao diện của một trong những pool này một cách chi tiết hơn trong một bài viết tương lai.
Để cấu hình một pool trong Braiins OS+, bạn sẽ cần tạo một tài khoản trong một trong những pool của sự lựa chọn của bạn. Ở đây chúng tôi sẽ lấy ví dụ về Linecoin:

![hình ảnh](assets/software/19.webp)

Sau khi tài khoản của bạn được tạo, nhấp vào Connect To Pool

Sau đó sao chép địa chỉ Stratum cũng như tên người dùng của bạn:

![hình ảnh](assets/software/20.webp)

Bây giờ bạn có thể quay trở lại giao diện Braiins OS+ để nhập những thông tin đăng nhập này. Đối với mật khẩu, bạn có thể để trống.

![hình ảnh](assets/software/21.webp)

### Tăng tốc và Giảm tốc

Tăng tốc và tự điều chỉnh đều liên quan đến việc điều chỉnh tần số trên các thẻ băm để cải thiện hiệu suất ASIC. Sự khác biệt giữa hai phương pháp này nằm ở độ phức tạp của các cài đặt tần số này.

**Tăng tốc** là một điều chỉnh đơn giản bao gồm việc tăng tần số trên các thẻ băm để tăng tốc độ băm của máy. Ngược lại, giảm tốc bao gồm việc giảm tần số đồng hồ của một mạch tích hợp dưới tần số danh nghĩa của nó. Bằng cách giảm tần số đồng hồ của một ASIC thông qua giảm tốc, nhiệt độ sinh ra bởi phần cứng cũng được giảm. Điều này cho phép giảm tốc độ của quạt cần thiết để làm mát ASIC, vì chúng không cần phải làm việc chăm chỉ để duy trì nhiệt độ phù hợp. Bằng cách giảm tốc độ quạt, tiếng ồn sinh ra bởi ASIC cũng được giảm. Điều này có thể đặc biệt hữu ích cho những người dùng ASIC tại nhà và muốn giảm thiểu sự quấy rầy do tiếng ồn từ phần cứng đào.

Quan trọng là phải lưu ý rằng giảm tốc có thể dẫn đến giảm hiệu suất của ASIC, vì vậy việc tìm một sự cân bằng tốt giữa hiệu suất và tiếng ồn là quan trọng.

Braiins OS+ hỗ trợ tăng tốc, giảm tốc của ASICs, và tự điều chỉnh. Nó cho phép người dùng điều chỉnh linh hoạt tần số đồng hồ của phần cứng của họ để tối đa hóa hiệu suất hoặc tiết kiệm năng lượng theo sở thích của họ.

### Tự Điều Chỉnh

Trước năm 2018, thợ mỏ có hai cách để có được lợi thế trong hoạt động của mình: tìm điện với giá cả hợp lý và mua phần cứng hiệu quả hơn. Tuy nhiên, vào năm 2018, một tiến bộ mới được phát hiện trong lĩnh vực phần mềm và firmware đào, được gọi là AsicBoost. Kỹ thuật này cho phép thợ mỏ giảm chi phí khoảng 13% bằng cách sửa đổi firmware chạy trên thiết bị của họ.
Ngày nay, có một tiến bộ mới trong lĩnh vực phần mềm và firmware đào gọi là tự điều chỉnh, mang lại lợi thế lớn hơn so với AsicBoost. ASIC được cấu thành từ nhiều chip máy tính nhỏ thực hiện băm. Những chip này được làm từ silicon, cùng một nguyên tố được sử dụng rộng rãi trong bán dẫn và các thành phần vi điện tử khác. Điều quan trọng ở đây là không phải tất cả các chip silicon đều giống nhau - mỗi chip có thể có sự khác biệt nhỏ về tính chất điện. Các nhà sản xuất phần cứng biết điều này và công bố thông số hiệu suất của máy đào của họ dựa trên giới hạn thấp nhất của khoảng chịu đựng của họ. Nói cách khác, các nhà sản xuất biết tần số hoạt động tốt nhất cho các chip trung bình và họ sử dụng tần số này một cách đồng nhất cho tất cả các chip trong máy.
Điều này đặt ra một giới hạn trên cho tốc độ hash mà một máy có thể có. Autotuning là quá trình mà trong đó các thuật toán đánh giá các tần số tối ưu cho việc hash từng chip một, thay vì xử lý toàn bộ máy như một đơn vị duy nhất. Điều này có nghĩa là một chip chất lượng cao có thể thực hiện nhiều hash mỗi giây sẽ nhận được tần số cao hơn, và một chip chất lượng thấp hơn có thể thực hiện ít hash hơn sẽ nhận được tần số thấp hơn. Autotuning ở cấp độ chip về cơ bản là một cách để tối ưu hóa hiệu suất của một ASIC thông qua phần mềm và firmware chạy trên nó.

Kết quả cuối cùng là tốc độ hash cao hơn mỗi watt điện năng, điều này có nghĩa là lợi nhuận lớn hơn cho các thợ mỏ. Lý do tại sao các máy không được phân phối với loại phần mềm này là vì sự biến động của máy là không mong muốn, vì khách hàng muốn biết chính xác họ đang nhận được cái gì, và do đó, việc bán một sản phẩm không có hiệu suất nhất quán và dự đoán được từ máy này sang máy khác là một ý tưởng tồi cho các nhà sản xuất. Ngoài ra, autotuning ở cấp độ chip đòi hỏi nguồn lực phát triển đáng kể, vì nó phức tạp để triển khai. Các nhà sản xuất đã chi rất nhiều nguồn lực để phát triển firmware của riêng họ. Có các giải pháp phần mềm cho phép autotuning, như Braiins OS+. Ngoài ra còn cải thiện hiệu suất ASIC lên đến 20%.

> Hướng dẫn được tạo bởi DecouvreBitcoin, thêm thông tin về MINAGE 201 - tín dụng Jim và Ajelex'