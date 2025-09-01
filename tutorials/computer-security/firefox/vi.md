---
name: Firefox
description: Làm thế nào để cấu hình Firefox để bảo vệ quyền riêng tư của bạn?
---

![cover](assets/cover.webp)



## Giới thiệu



Tất cả chúng ta đều dành hàng giờ trực tuyến, thường không nhận ra trình duyệt đang tiết lộ những gì về mình. Mỗi cú nhấp chuột, mỗi tìm kiếm, mỗi trang web chúng ta truy cập đều nuôi dưỡng một ngành công nghiệp khổng lồ thu thập dữ liệu cá nhân.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Thị phần trình duyệt web: Chrome chiếm ưu thế với 65% thị phần, tiếp theo là Safari và Edge. Nguồn: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Như biểu đồ này cho thấy, Google Chrome đang chiếm ưu thế áp đảo, với hơn 65% thị phần sử dụng trên toàn thế giới. Sự thống trị này đồng nghĩa với việc phần lớn người dùng Internet giao phó dữ liệu duyệt web của họ cho Google, một công ty có mô hình kinh doanh dựa trên quảng cáo nhắm mục tiêu. Firefox, chỉ chiếm 3% thị phần, là một lựa chọn thay thế do Mozilla, một tổ chức phi lợi nhuận không có lợi ích thương mại trong việc khai thác dữ liệu của bạn, phát triển.



Nhưng việc chọn Firefox chỉ là bước đầu tiên. Theo mặc định, ngay cả Firefox cũng cần được điều chỉnh để tối ưu hóa khả năng bảo vệ. Hướng dẫn này sẽ hướng dẫn bạn từng bước, từ đơn giản nhất đến nâng cao nhất, để biến Firefox thành một lá chắn thực sự chống lại việc theo dõi mà vẫn duy trì trải nghiệm duyệt web dễ chịu.



### Tại sao lại là Firefox?





- Mã nguồn mở và miễn phí** (Gecko engine): mã có thể kiểm tra, minh bạch
- Tổ chức phi lợi nhuận**: Mozilla Foundation, sứ mệnh vì lợi ích chung
- Các biện pháp bảo vệ gốc tích hợp**: Bảo vệ theo dõi nâng cao (ETP), Bảo vệ cookie toàn diện (TCP), Phân vùng trạng thái, chế độ chỉ HTTPS, DNS qua HTTPS (DoH)
- Tùy chỉnh nâng cao**: không giống như Chrome, Firefox cho phép bạn sửa đổi hành vi của nó một cách sâu sắc



### Những nguyên tắc quan trọng trước khi bạn bắt đầu





- Không có công thức chung nào cả**: bạn càng sửa đổi nhiều, bạn càng có nguy cơ bị lộ (dấu vân tay). Mục đích là để được bảo vệ tốt hơn mà không bị nổi bật giữa đám đông.
- Tiến trình từng bước**: Thay đổi cài đặt, kiểm tra các trang web bạn thường dùng, sau đó tiếp tục. Không cần phải thay đổi mọi thứ cùng một lúc.
- Cân bằng cá nhân**: Tìm ra sự thỏa hiệp CỦA BẠN giữa quyền riêng tư và tính dễ sử dụng.



## Cài đặt nhanh chóng



![Téléchargement Firefox](assets/fr/02.webp)



**Tải xuống chính thức:** Truy cập [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Trên trang này, hãy chọn hệ điều hành của bạn (Windows, macOS, Linux) để truy cập trang tải xuống phù hợp với hướng dẫn cài đặt cụ thể.





- Windows**: tải xuống trình cài đặt `.exe`, nhấp đúp và làm theo trình hướng dẫn cài đặt
- macOS**: tải xuống tệp `.dmg`, mở tệp đó và kéo Firefox vào thư mục Ứng dụng
- Linux**: có nhiều tùy chọn - gói `.deb`/`.rpm`, Flatpak (Flathub), Snap hoặc thông qua trình quản lý gói (apt, dnf, pacman). Ưu tiên các nguồn chính thức của Mozilla.



**Mẹo:** Sau khi cài đặt, hãy kiểm tra bản cập nhật thông qua Trợ giúp → **Giới thiệu về Firefox** (quan trọng đối với các bản vá bảo mật).



![Configuration initiale Firefox](assets/fr/03.webp)


*Màn hình đầu tiên khi khởi chạy Firefox: đặt Firefox làm trình duyệt mặc định, thêm vào phím tắt, sau đó nhấp vào "Lưu và tiếp tục"*



![Création compte Firefox](assets/fr/04.webp)


*Bước tùy chọn: tạo hoặc đăng nhập vào tài khoản Firefox. Bạn có thể bỏ qua bước này bằng cách nhấp vào "Không phải bây giờ" ở góc dưới bên phải*



![Page d'accueil Firefox](assets/fr/05.webp)


*Màn hình chính Firefox sau khi cấu hình xong. Lưu ý menu ☰ ở góc trên bên phải, cho phép truy cập Cài đặt và Tiện ích mở rộng để tùy chỉnh Firefox*



## Các biện pháp bảo vệ đã được kích hoạt theo mặc định (an tâm)





- Cô lập trang web (Fission)**: đang trong giai đoạn triển khai. Tính năng này chạy từng trang web trong một quy trình riêng biệt để ngăn chặn một tab độc hại truy cập dữ liệu của tab khác. Kiểm tra trạng thái của nó qua `about:support` (tìm kiếm "Fission"). Nếu chưa được bật, bạn có thể kích hoạt thủ công trong `about:config` với `fission.autostart = true`.
- Bảo vệ Cookie Toàn diện (TCP)**: được kích hoạt theo mặc định. Cookie và các lưu trữ khác được giới hạn trong trang web của bên thứ nhất (mỗi trang web một "jar"), giúp vô hiệu hóa việc theo dõi chéo trang web. Các ngoại lệ tạm thời được tạo thông qua API Truy cập Lưu trữ khi cần thiết (các nút đăng nhập tích hợp).
- Bảo vệ theo dõi trang web bị trả lại/chuyển hướng**: Firefox tự động phát hiện và dọn dẹp các cookie do các trang web bị trả lại (các liên kết chuyển hướng bạn qua trình theo dõi trước khi đến đích), giúp giảm kênh theo dõi này mà không cần bạn phải thực hiện bất kỳ hành động nào.



## Mức 1 - Cần thiết (≤ 10 phút)



Mục tiêu: tăng cường đáng kể quyền riêng tư mà không làm gián đoạn web. Dành cho 90% người dùng.



Để truy cập cài đặt, hãy nhấp vào menu ☰ ở trên cùng bên phải, sau đó nhấp vào **"Cài đặt"**:



![Paramètres généraux](assets/fr/07.webp)


*Trang cài đặt Firefox - tab "Chung". Đây là nơi bạn cấu hình hầu hết các tùy chọn riêng tư của mình*



**Bảo vệ theo dõi (ETP)**




- Chuyển **ETP** sang **Strict**. Bạn sẽ chặn được nhiều trình theo dõi hơn (cookie chéo trang, dấu vân tay, khai thác tiền điện tử, tiện ích mạng xã hội...).
- Nếu một trang web bị lỗi (video, nút đăng nhập...), hãy tắt chế độ bảo vệ chỉ dành cho trang web đó thông qua lá chắn 🛡️, sau đó làm mới tab.



Sau đây là các cấp độ bảo mật ETP khác nhau:




- Tiêu chuẩn** (cân bằng, khả năng tương thích tối đa)
  - Khối: trình theo dõi mạng xã hội, cookie liên trang web (tất cả các cửa sổ), theo dõi nội dung khi duyệt web riêng tư, trình khai thác tiền điện tử, trình phát hiện dấu vân tay.
  - Bao gồm **Bảo vệ cookie toàn diện** (TCP): một jar cho mỗi trang web.
- Nghiêm ngặt** (khuyến nghị vì lý do bảo mật)
  - Ngoài ra còn chặn nội dung theo dõi trong mọi cửa sổ + dấu vân tay đã biết và nghi ngờ.
  - Có thể làm hỏng một số trang web; hãy sử dụng lá chắn 🛡️ để có ngoại lệ cục bộ.
- Tùy chỉnh** (nâng cao)
  - Tinh chỉnh: cookie, theo dõi nội dung, trẻ vị thành niên, dấu vân tay (đã biết/nghi ngờ).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookie và dữ liệu trang web




- Bật **"Xóa cookie và dữ liệu trang web khi đóng"** để khởi động lại sạch sẽ mỗi khi bạn khởi động lại.
- Thêm **Ngoại lệ** cho 2-3 trang web quan trọng nếu bạn muốn (email, ngân hàng).


**Nhập dữ liệu tự động, gợi ý và trang chủ**




- Tắt tính năng **tự động điền** (ID, địa chỉ, thẻ). Thay vào đó, hãy sử dụng trình quản lý mật khẩu.
- Tìm kiếm**: tắt **"Hiển thị gợi ý tìm kiếm"**.
- Thanh Address**: cắt **"Gợi ý được tài trợ "** và **"Gợi ý theo ngữ cảnh "**.
- Trang chủ**: tắt **Pocket** và **nội dung được tài trợ**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Chỉ HTTPS**




- Kích hoạt **"Chỉ chế độ HTTPS trong tất cả các cửa sổ"**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Đo lường từ xa và quảng cáo




- Trong "Thu thập dữ liệu bởi Firefox", **bỏ chọn tất cả**.
- Vô hiệu hóa **"Biện pháp quảng cáo thân thiện với quyền riêng tư"** (PPA).
- Duyệt web an toàn**: hãy bật tính năng này (khuyến nghị). Firefox kiểm tra các trang web dựa trên danh sách mối đe dọa thông qua các truy vấn băm và kiểm tra cục bộ, bảo vệ chống lừa đảo và phần mềm độc hại với tác động tối thiểu đến quyền riêng tư.



**Kiểm soát quyền riêng tư toàn cầu (tùy chọn)**




- Kích hoạt **GPC** để thông báo bạn từ chối bán/chia sẻ dữ liệu.



**Công cụ tìm kiếm




- Chuyển sang **DuckDuckGo**, **Startpage**, **Qwant** hoặc **Brave Search** (Cài đặt → Tìm kiếm).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Điều hướng riêng tư**




- Cửa sổ riêng tư (Ctrl/Cmd+Shift+P) cho các phiên làm việc một lần (quà tặng, tài khoản phụ...). Tránh chế độ "luôn riêng tư": tiện ích mở rộng có thể không hoạt động và ngoại lệ cookie ít hữu ích hơn.



**Các tiện ích mở rộng cần thiết** (cài đặt từ danh mục chính thức)




- uBlock Origin**: chặn quảng cáo và theo dõi hiện tại, nhẹ.
- Privacy Badger**: học cách chặn những thứ theo dõi bạn; gửi thông báo Không theo dõi / GPC.
- ClearURLs** (tùy chọn): Firefox (ETP Strict) và uBO đã dọn dẹp rất nhiều; hãy giữ nguyên nếu bạn vẫn thấy các URL "bẩn" (utm, fbclid).
- Firefox Multi-Account Containers**: **phân tách cookie/phiên và dung lượng lưu trữ cho mỗi container; nhiều tài khoản song song; ít theo dõi chéo trang web hơn**. Tiện ích mở rộng chính thức: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Mật khẩu và 2FA**




- Sử dụng trình quản lý mật khẩu chuyên dụng** (Bitwarden, KeePassXC). **Tránh** lưu trữ mật khẩu trong trình duyệt. **Bật xác thực hai yếu tố (2FA)** bất cứ khi nào có thể.



## Cấp độ 2 - Được củng cố (Phân chia và Mạng lưới)



Mục tiêu: phân chia các hoạt động và giảm rò rỉ mạng.



**DNS qua HTTPS (DoH)**




- Trạng thái mặc định**: Tự động kích hoạt ở một số khu vực (Hoa Kỳ, Canada, Nga, Ukraine). Các khu vực khác, cần phải kích hoạt thủ công.
- Cấu hình**: Cài đặt → Cài đặt chung → Cài đặt mạng → **Bật DoH** → **Cloudflare** hoặc **Quad9** → **Bảo vệ tối đa**.
- Bảo vệ tối đa = Chỉ TRR** (không chuyển sang DNS hệ thống). Nếu mạng công ty/khách sạn bị chặn, hãy chuyển về **Tiêu chuẩn** hoặc tắt DoH.
- Dự phòng**: Nếu bạn đang sử dụng VPN đáng tin cậy có DNS bảo mật riêng, DoH có thể trở nên dự phòng.
- Kiểm tra xác minh**: `https://www.dnsleaktest.com/` chỉ hiển thị nhà cung cấp DoH đã chọn.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Phân chia ngăn bằng thùng chứa và hồ sơ




- Container Đa Tài Khoản**: tạo không gian (Cá Nhân, Công Việc, Tài Chính, Mạng Xã Hội, Mua Sắm, Dùng Một Lần). Cấu hình **"Luôn mở trong container này"** cho các trang web định kỳ của bạn. Tiện ích mở rộng chính thức: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Tại sao lại sử dụng chúng?
  - Phân tách chặt chẽ** cookie/phiên/lưu trữ theo không gian.
  - Ít theo dõi chéo trang web hơn**: hạn chế các công ty lớn (Facebook, Google).
  - Nhiều tài khoản cùng lúc** trên cùng một dịch vụ.
  - Ít rủi ro CSRF/XSS** hơn giữa các danh tính được phân đoạn.
  - Mẹo: ít nhất, hãy tạo các vùng chứa chuyên dụng cho Mạng xã hội/Google, Công việc, Tài chính.
- Facebook Container** (tùy chọn): phiên bản đơn giản dành riêng cho FB/Instagram.
- Hồ sơ riêng biệt**: thông qua `about:profiles` (hồ sơ chính, hồ sơ "siêu bảo mật" tối thiểu, hồ sơ thử nghiệm). Phân chia toàn bộ dữ liệu và phần mở rộng.



**Phần mở rộng nâng cao** (sẽ được đặt trước)




- Tự động xóa cookie**: xóa cookie của trang web ngay khi tab được đóng (hữu ích nếu Firefox mở trong thời gian dài).
- LocalCDN**: phục vụ các thư viện hiện tại cục bộ (giảm số lần gọi đến Google/Microsoft). Khả năng tương thích một phần.



**Di động (Android)**




- Firefox Android + uBlock Origin**: khả năng bảo vệ tương tự khi di chuyển.



## Cấp độ 3 - Chuyên gia (about:config & Arkenfox)



Mục tiêu: tăng cường bảo mật nâng cao với các thỏa hiệp được chấp nhận. Khuyến nghị sử dụng **hồ sơ riêng**.



Chỉ chọn một trong hai cách tiếp cận sau:



**Cách tiếp cận A - Sửa đổi thủ công**: Một vài điều chỉnh có mục tiêu thông qua `about:config` (kiểm soát đơn giản hơn, chính xác hơn)


**Cách tiếp cận B - Arkenfox user.js**: Cấu hình hoàn toàn tự động (phức tạp hơn, bảo vệ tối đa)



➡️ **Arkenfox đã bao gồm TẤT CẢ các thay đổi about:config được đề cập bên dưới** + hàng trăm thay đổi khác. Nếu bạn chọn Arkenfox, hãy bỏ qua phần about:config.



### Cách tiếp cận A: Sửa đổi thủ công thông qua about:config



Nhập `about:config` vào thanh Address → Chấp nhận rủi ro.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Khả năng chống lại dấu vân tay (thừa hưởng từ Tor Browser)


```text
privacy.resistFingerprinting = true
```


Hiệu ứng: Múi giờ UTC, **hộp thư** (kích thước cửa sổ chuẩn), User-Agent/chính sách được chuẩn hóa, các hạn chế của Canvas/WebGL/AudioContext. Đồng bộ hơn, nhưng có một vài "điểm kỳ lạ" (thời gian lệch, đôi khi hơi giống tiếng Anh).





- Vô hiệu hóa WebRTC (tránh rò rỉ IP; phá vỡ Web Visio)


```text
media.peerconnection.enabled = false
```





- Referer plus tương thích (mặc định)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Tùy chọn nghiêm ngặt (có thể phá vỡ thanh toán/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Hạn chế các API tán gẫu và suy đoán


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Nguyên tắc vàng: nếu có gì đó hỏng, hãy quay lại thay đổi cuối cùng.



### Cách tiếp cận B: Arkenfox user.js (Cấu hình hoàn toàn tự động)



Dự án Arkenfox cung cấp tệp `user.js` do cộng đồng quản lý, tự động áp dụng hàng trăm tùy chọn bảo mật và riêng tư của Firefox. Khi khởi động lại, Firefox sẽ đọc tệp này từ hồ sơ của bạn và áp dụng các cài đặt này.





- Mục đích là gì? Hãy bắt đầu từ một **nền móng vững chắc** mà không "lệch pha"; giảm thiểu sai sót; tiết kiệm thời gian.
- Những thay đổi (ví dụ): cắt bỏ dữ liệu đo từ xa, tăng cường cookie/bộ nhớ đệm/người giới thiệu/HTTPS, **RFP** + hộp thư, **WebRTC bị vô hiệu hóa**, điều chỉnh DoH/TLS, hạn chế API trò chuyện.
- Khi nào nên sử dụng: nếu bạn muốn Firefox được bảo mật trong 10 phút và chấp nhận một số ngoại lệ (DRM/phát trực tuyến, Web visio, SSO/thanh toán).
- Ưu điểm: nhanh, nhất quán, **được cập nhật** (phù hợp với ESR), **được ghi chép** rất đầy đủ (wiki + bình luận), **có thể tùy chỉnh** thông qua ghi đè.
- Hạn chế: khả năng tương thích (một số ứng dụng web), sự thoải mái (UTC, kích thước cửa sổ) và lời nhắc nhở: **đây không phải là Tor** (không ẩn danh trên mạng).



Cài đặt (tốt nhất là trên **cấu hình chuyên dụng**)


1. Lưu hồ sơ/mục ưa thích và liệt kê các trang web của bạn có ngoại lệ về cookie.


2. Tải xuống `user.js` từ `https://github.com/arkenfox/user.js` (phiên bản ESR/ổn định).


3. Tìm thư mục hồ sơ của bạn thông qua `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Thư viện/Hỗ trợ ứng dụng/Firefox/Hồ sơ/...`


4. Đóng Firefox và di chuyển `user.js` vào thư mục gốc của hồ sơ.


5. Khởi chạy lại; tùy chỉnh thông qua `about:config` hoặc tệp ghi đè.



Cập nhật




- Thực hiện theo bản phát hành Arkenfox (tương thích với ESR), thay thế `user.js`, khởi chạy lại Firefox; đọc ghi chú phát hành.



**Tùy chỉnh thông qua Ghi đè**



Arkenfox mặc định có những hạn chế nhất định. Để điều chỉnh một số cài đặt cho phù hợp với nhu cầu của bạn (phát trực tuyến, xem, các trang web cụ thể), bạn có thể tạo tệp `user-overrides.js` trong cùng thư mục với `user.js`. Tệp này cho phép bạn "ghi đè" một số tùy chọn của Arkenfox mà không cần sửa đổi tệp chính.



Tạo `user-overrides.js` và thêm các tùy chỉnh của bạn:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Thực hành tốt nhất




- Sử dụng hồ sơ **"Arkenfox"** riêng biệt và giữ nguyên hồ sơ "bình thường" để thoải mái hơn.
- Giảm thiểu tiện ích mở rộng (uBlock Origin OK) để hạn chế bề mặt tấn công và tính duy nhất.
- Thêm các ngoại lệ cho từng trang web (shield 🛡️, uBO, NoScript nếu sử dụng) khi cần thiết.
- Kiểm tra sau mỗi lần thay đổi: Rò rỉ WebRTC/DNS, Che giấu dấu vết, CreepJS.



## Thực hành tốt nhất





- Cập nhật**: Firefox và các tiện ích mở rộng đã được cập nhật.
- Tiện ích mở rộng**: hợp lý và đáng tin cậy; hãy cẩn thận với các khoản đổi thưởng "đáng ngờ".
- Tải xuống**: thận trọng; kiểm tra các tệp nhạy cảm trên VirusTotal.
- Mật khẩu**: **trình quản lý chuyên dụng** (Bitwarden, KeePassXC); **2FA** được bật; tránh lưu trữ trong trình duyệt.
- Vệ sinh**: giới hạn Google/Facebook trong các vùng chứa; đóng/mở thường xuyên để "thiết lập lại" ngữ cảnh.



## Giới hạn & Giải pháp thay thế





- Trình duyệt được tăng cường ≠ ẩn danh mạng: không có **VPN**, IP của bạn vẫn hiển thị; ngay cả khi có VPN, vẫn có thể có mối tương quan.
- Việc thay đổi quá nhiều có thể khiến bạn trở nên **độc đáo**. **RFP** chuẩn hóa; các công cụ ngẫu nhiên hóa (ví dụ: Chameleon) có thể... khiến bạn trở nên khác biệt. Hãy thử nghiệm, so sánh và điều chỉnh.
- Các lựa chọn thay thế/bổ sung:
 - Trình duyệt Tor: ẩn danh mạng qua Tor; chậm hơn. Xem hướng dẫn cài đặt và cấu hình đầy đủ của chúng tôi**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Trình duyệt Mullvad: "Tor không cần Tor", được tích hợp với VPN; dung lượng chuẩn. Tìm hiểu cách cài đặt trong hướng dẫn chuyên dụng của chúng tôi**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Các kết hợp được đề xuất: Firefox (Cấp độ 2) + VPN cho mục đích sử dụng hàng ngày; Tor/Mullvad cho các hoạt động nhạy cảm; hồ sơ riêng biệt để phân loại.



## Phần kết luận



Bằng cách làm theo hướng dẫn từng bước này, bạn đã biến Firefox thành một bức tường thành vững chắc chống lại sự giám sát kỹ thuật số. Từ các thiết lập Cấp độ 1 thiết yếu đến các cấu hình Arkenfox nâng cao, mọi thay đổi đều tăng cường quyền riêng tư của bạn mà không ảnh hưởng đến trải nghiệm duyệt web.



**Quyền riêng tư của bạn giờ đây được bảo vệ tốt hơn**: trình theo dõi quảng cáo bị chặn, cookie được phân vùng, rò rỉ IP Address được vô hiệu hóa, dữ liệu từ xa bị vô hiệu hóa. Firefox không còn chỉ là một trình duyệt, mà là một công cụ kháng cự kỹ thuật số được thiết kế riêng cho nhu cầu của bạn.



**Hãy nhớ: bảo mật không bao giờ là điều hiển nhiên. Hãy thường xuyên kiểm tra khả năng bảo vệ, cập nhật cài đặt và đừng ngần ngại điều chỉnh cấu hình khi thói quen của bạn thay đổi. Tính ẩn danh trực tuyến của bạn phụ thuộc vào công cụ cũng như cách thức hoạt động của bạn.



## Tài nguyên



### Plan ₿ Network




- SCU 202 - Cải thiện bảo mật kỹ thuật số cá nhân của bạn: Để tìm hiểu thêm về các khái niệm bảo mật kỹ thuật số được đề cập trong hướng dẫn này**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Tài liệu Mozilla




- [Bảo vệ theo dõi nâng cao](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Hướng dẫn chính thức về bảo vệ theo dõi nâng cao
- [Phân vùng trạng thái](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Tài liệu kỹ thuật về phân vùng trạng thái
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Tài liệu tham khảo đầy đủ về bảo mật web



### Arkenfox




- [Wiki và hướng dẫn cài đặt](https://github.com/arkenfox/user.js/wiki): Tài liệu đầy đủ về dự án Arkenfox
- [Gửi tiền và phát hành](https://github.com/arkenfox/user.js): Tải xuống tệp user.js và theo dõi các bản cập nhật



### Hướng dẫn & cộng đồng




- [PrivacyGuides - Trình duyệt máy tính để bàn](https://www.privacyguides.org/en/desktop-browsers/): Đề xuất và so sánh trình duyệt
- Reddit**: r/firefox, r/privacy để nhận phản hồi và hỗ trợ
- Diễn đàn PrivacyGuides**: thảo luận chuyên sâu về kỹ thuật



### Công cụ kiểm tra




- [Che giấu dấu vết (EFF)](https://coveryourtracks.eff.org/): Hiệu quả của dấu vân tay kỹ thuật số và chống theo dõi
- [Kiểm tra rò rỉ DNS](https://www.dnsleaktest.com/): Kiểm tra rò rỉ DNS và hiệu quả DoH
- [BrowserLeaks](https://browserleaks.com/): Bộ kiểm tra hoàn chỉnh (WebRTC, Canvas, Phông chữ, v.v.)
- [BadSSL](https://badssl.com/): Kiểm tra xác thực chứng chỉ SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Phân tích nâng cao hơn 50 vectơ dấu vân tay
- [Kiểm tra DNS Cloudflare](https://1.1.1.1/help): Kiểm tra xem Cloudflare DoH có hoạt động bình thường không