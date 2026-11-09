# Plugin Hành chính – Nhân sự (HCNS) cho doanh nghiệp Việt Nam 2026

Plugin trọn bộ cho **nhân viên và trưởng phòng Hành chính – Nhân sự** ở doanh nghiệp vừa và nhỏ (một người làm cả hai mảng, đúng thực tế phổ biến ở Việt Nam). Gồm **16 skill**, **6 lệnh quy trình**, **1 agent thẩm định**, **connector khai báo sẵn** (Gmail, Google Calendar, Google Drive, Microsoft 365, Zoom, Slack) và 20 công cụ tính toán theo pháp luật hiện hành đi kèm từng skill:

- Văn bản đúng thể thức **Nghị định 30/2020/NĐ-CP**, xuất file Word chuẩn; kiểm tra thể thức tự động.
- Lao động theo **Bộ luật Lao động 2019**, **NĐ 145/2020**, **Luật BHXH 2024**, **Luật Việc làm 2025**; lương tối thiểu vùng **NĐ 293/2025**; giảm trừ gia cảnh **NQ 110/2025**; biểu thuế TNCN 5 bậc 2026.
- Lịch âm, ngày lễ Tết, nghỉ bù, ngày làm việc; sổ văn bản đi/đến; trợ cấp thôi việc; phép năm; thời hạn báo trước; thời hiệu kỷ luật; lương net ↔ gross.

Nguyên tắc: **không bịa** (thiếu thì `[CẦN BỔ SUNG]`), **tính bằng công cụ**, **viện dẫn có số hiệu và nhãn tin cậy** ([Chắc chắn] / [Cần kiểm tra]), **soạn nháp – con người quyết định** (không tự gửi, ký, nộp; xem [POLICY.md](POLICY.md)).

## Thành phần

### Skill – nhóm Hành chính (7)

| Skill | Làm gì |
|---|---|
| `soan-van-ban-hanh-chinh` | Công văn, quyết định, tờ trình, thông báo, kế hoạch, báo cáo đúng NĐ 30; xuất .docx |
| `giay-to-hanh-chinh` | Giấy mời, giới thiệu, ủy quyền, cử đi công tác, xác nhận việc làm/thu nhập, đơn nội bộ |
| `kiem-tra-truoc-trinh-ky` | Rà thể thức bằng công cụ + soát nội dung; lỗi 3 mức CHẶN / CẦN SỬA / GỢI Ý |
| `so-van-ban-di-den` | Cấp số văn bản đi, đăng ký văn bản đến, hạn xử lý theo ngày làm việc, nhắc quá hạn |
| `luu-tru-ho-so` | Danh mục hồ sơ, thời hạn bảo quản, cây thư mục, đặt tên file, số hóa, tiêu hủy |
| `quy-che-noi-bo` | Quy chế văn thư – con dấu, chi tiêu – công tác phí, tài sản, làm việc từ xa, bảo mật, sử dụng AI |
| `hoi-hop-su-kien` | Lịch họp, chương trình, biên bản (không bịa kết luận), theo dõi kết luận; tất niên, du lịch, sự kiện |

### Skill – nhóm Nhân sự (9)

| Skill | Làm gì |
|---|---|
| `tuyen-dung` | JD, tin tuyển dụng không phân biệt đối xử, sàng lọc CV, phỏng vấn STAR, offer gross/net, thư từ chối |
| `hop-dong-lao-dong` | HĐLĐ, thử việc, phụ lục; nhận diện "CTV" là HĐLĐ; rà điều khoản trái luật |
| `onboarding-offboarding` | Checklist vào – ra, lịch hội nhập, 30-60-90, bàn giao, thanh toán 14 ngày làm việc |
| `noi-quy-thoa-uoc` | Nội quy đủ 9 nhóm nội dung + đăng ký Sở Nội vụ; thỏa ước; dân chủ cơ sở, đối thoại |
| `danh-gia-luong-thuong` | KPI, đánh giá, PIP, quy chế đánh giá (căn cứ chấm dứt), thang bảng lương, quy chế thưởng |
| `ky-luat-lao-dong` | Sàng lọc điều kiện, thời hiệu, thông báo họp 5 ngày làm việc, biên bản, quyết định, bồi thường |
| `cham-dut-hop-dong` | Căn cứ chấm dứt, Điều 37, báo trước, trợ cấp, hậu quả trái luật, cắt giảm nhân sự |
| `bhxh-che-do` | Đối tượng, mức đóng, báo tăng/giảm, ốm đau, thai sản, TNLĐ, thất nghiệp |
| `lich-tuan-thu-hcns` | Lịch nghĩa vụ cả năm (báo cáo 05/6, 05/12...), mốc HĐLĐ theo danh sách nhân viên, xuất .ics |

### Lệnh quy trình (Claude Code)

`/hanhchinh-nhansu:nhan-vien-moi` · `/hanhchinh-nhansu:nghi-viec` · `/hanhchinh-nhansu:xu-ly-ky-luat` · `/hanhchinh-nhansu:trinh-ky` · `/hanhchinh-nhansu:van-ban-den` · `/hanhchinh-nhansu:lich-thang`

### Agent
`tham-dinh-hcns` – thẩm định độc lập văn bản/quyết định nhân sự trước khi ban hành (tính lại mọi con số bằng công cụ).

### Connector
<!-- KET-NOI-README:BAT-DAU (sinh tự động bởi scripts/ket_noi.py) -->
Plugin **khai báo sẵn** connector: Gmail, Google Calendar, Google Drive, Microsoft 365 (Outlook, OneDrive/SharePoint, Teams), Zoom, Slack. Cài plugin xong chỉ cần bấm kết nối và đăng nhập một lần (tab **Connectors** của plugin). Mỗi skill ghi rõ dùng connector vào việc gì; chưa kết nối thì skill vẫn chạy, chỉ không tự lấy dữ liệu hoặc tạo nháp được. Email chỉ tạo bản nháp, mọi thao tác ghi phải được bạn xác nhận. Chi tiết: [CONNECTORS.md](CONNECTORS.md).
<!-- KET-NOI-README:KET-THUC -->

Ví dụ việc skill làm qua connector: lấy CV từ hộp thư, đặt lịch phỏng vấn kèm link Zoom, tạo nháp thư mời nhận việc; nhắc hạn hết thử việc, hết hạn HĐLĐ trên lịch; lưu quyết định vào Drive.

## Cài đặt

### Claude Code – cả bộ plugin (khuyên dùng)

```
/plugin marketplace add nguyenvansuai/hanhchinh-nhansu
```

```
/plugin install hanhchinh-nhansu@hanhchinh-nhansu
```

### Claude Code – chỉ một skill

```
/plugin install ky-luat-lao-dong@hanhchinh-nhansu
```

Tên cài = tên skill trong bảng trên. Skill lẻ có sẵn công cụ `scripts/cong_cu.py` và khai báo đúng các connector nó dùng (không có lệnh, agent).

Cập nhật: `/plugin marketplace update hanhchinh-nhansu`

### Claude Desktop / Cowork
Tải [`dist/hanhchinh-nhansu.plugin`](dist/) và cài plugin từ file (gồm skill, lệnh, agent và connector khai báo sẵn), rồi mở tab **Connectors** của plugin để kết nối.

### Claude.ai (web, app) – từng skill
1. Bật **Settings → Capabilities → Code execution and file creation**.
2. **Settings → Capabilities → Skills → Upload skill** → chọn file trong [`dist/`](dist/), ví dụ `tuyen-dung.zip`.
Mỗi file zip là một skill độc lập, có sẵn công cụ tính toán. Skill tải lên kiểu này không tự khai báo connector: bật Gmail, Calendar, Drive trong **Settings → Connectors** để skill dùng được.

### ChatGPT / Codex – cả bộ plugin (OpenAI)

Gói plugin cho ChatGPT và Codex nằm ở [`openai/hanhchinh-nhansu/`](openai/hanhchinh-nhansu/), theo cấu trúc portable của OpenAI (`plugin.json`, `skills/`, `.app.json`), gồm **23 skill** (lệnh quy trình và agent của bản Claude đã được chuyển thành skill).

**ChatGPT desktop / Codex** – cài cá nhân, không cần OpenAI duyệt:

```bash
codex plugin marketplace add nguyenvansuai/hanhchinh-nhansu
```

```bash
codex plugin add hanhchinh-nhansu@hanhchinh-nhansu
```

Hoặc trong ứng dụng ChatGPT desktop: **Plugins** → chọn nguồn **Hành chính – Nhân sự VN** → **Install**. Khi dùng: mở chat chế độ **Work**, gõ `@` và chọn plugin.

Gói khai báo sẵn connector của ChatGPT trong `.app.json` (danh sách ở [CONNECTORS.md](CONNECTORS.md)): khi cài, ChatGPT đề nghị kết nối từng ứng dụng, mỗi người đăng nhập một lần. Không cần cài Python hay chạy server trên máy.

**ChatGPT web / chia sẻ rộng**: muốn plugin xuất hiện trong thư mục plugin chung của ChatGPT phải gửi OpenAI duyệt qua [cổng nộp plugin](https://platform.openai.com/plugins) (cần xác minh danh tính). File nén sẵn để nộp: [`dist/hanhchinh-nhansu-chatgpt.zip`](dist/). Quản trị viên workspace ChatGPT có thể **Publish** plugin cá nhân cho cả workspace.

Sau khi sửa skill, sinh lại gói: `python3 scripts/build_openai.py`.

### ChatGPT – từng skill (Project / Custom GPT)
Mỗi skill có hướng dẫn trong [`chatgpt/`](chatgpt/) (dán Instructions vào Custom GPT/Project, tải `references/` vào Knowledge).

## Ví dụ câu lệnh

- "Nhân viên Nguyễn Văn A vào làm 01/3/2016, nghỉ việc 15/10/2026, lương bình quân 20 triệu, đóng BHTN từ 01/2009. Tính trợ cấp thôi việc."
- "Nhân viên tự ý nghỉ 6 ngày liên tục từ 02/11. Tôi muốn sa thải, làm thế nào cho đúng?"
- "Soạn quyết định bổ nhiệm bà Trần Thị B làm Trưởng phòng Kế toán từ 01/12/2026, xuất file Word."
- "Ứng viên đòi net 25 triệu, có 1 con, làm ở Hà Nội. Gross bao nhiêu, công ty tốn bao nhiêu?"
- "Lập lịch tuân thủ HCNS năm 2027 và xuất file lịch."
- "Kiểm tra giúp file quyet-dinh.docx trước khi trình giám đốc."

## Cấu trúc repo

```
.claude-plugin/plugin.json        manifest plugin trọn bộ (+ icon.png)
.claude-plugin/marketplace.json   danh mục: gói trọn bộ + 16 skill lẻ (sinh tự động)
.mcp.json                         connector khai báo sẵn (sinh từ scripts/ket_noi.json)
skills/<skill>/                   SKILL.md + references/ + scripts/ (công cụ đi kèm)
commands/ agents/                 lệnh quy trình, agent thẩm định
tools/                            công cụ (nguồn; build chép vào skills/<x>/scripts/) (lịch, văn thư, thể thức, lao động, lịch tuân thủ) + tham_so.py
shared/                           tài liệu dùng chung (nguồn gốc, build chép vào skill)
tests/test_cong_cu.py             kiểm thử công cụ
scripts/build.py                  đồng bộ, sinh marketplace/chatgpt/dist, kiểm tra
scripts/ket_noi.py + ket_noi.json  connector: .mcp.json, mục "Kết nối ứng dụng" trong skill, CONNECTORS.md
```

## Phát triển

```bash
python3 tests/test_cong_cu.py
```

```bash
python3 scripts/build.py
```

Khi quy định thay đổi (lương tối thiểu, lương cơ sở, giảm trừ, biểu thuế): sửa `tools/tham_so.py` và `shared/quy-dinh-lao-dong-2026.md`, chạy test, build lại.

## Lưu ý pháp lý

Nội dung cập nhật đến **11/2026**. Mục gắn **[Cần kiểm tra]** chưa đối chiếu văn bản gốc hoặc dễ thay đổi. Plugin hỗ trợ soạn thảo, tính toán – **không thay thế** tư vấn của luật sư, cơ quan BHXH, cơ quan lao động. Vụ việc sa thải, cắt giảm nhân sự, tranh chấp: tham vấn chuyên gia trước khi quyết định.

## Hệ sinh thái

- Kế toán – tài chính (bảng lương, BHXH, thuế): [skill-ketoan-tai-chinh](https://github.com/nguyenvansuai/skill-ketoan-tai-chinh)
- Pháp chế – hợp đồng: [phapche-hopdong](https://github.com/nguyenvansuai/phapche-hopdong)
- Hành chính công (cơ quan nhà nước): [hanh-chinh-cong](https://github.com/nguyenvansuai/hanh-chinh-cong)
- Sales – marketing: [skill-sales-marketing](https://github.com/nguyenvansuai/skill-sales-marketing) · Hộ kinh doanh: [skill-ho-kinh-doanh](https://github.com/nguyenvansuai/skill-ho-kinh-doanh)
- Bộ văn phòng tổng hợp: [20skill-van-phong](https://github.com/nguyenvansuai/20skill-van-phong)

## Giấy phép
MIT – xem [LICENSE](LICENSE).
