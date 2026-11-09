# Hành chính – Nhân sự VN – gói cho ChatGPT / Codex

Thư mục này được sinh tự động bởi `scripts/build_openai.py` – không sửa tay.

16 skill cho nhân viên và trưởng phòng Hành chính – Nhân sự doanh nghiệp vừa và nhỏ Việt Nam: văn bản đúng thể thức Nghị định 30/2020, giấy tờ hành chính, kiểm tra trước trình ký, sổ văn bản đi/đến, lưu trữ, quy chế nội bộ, hội họp – sự kiện; tuyển dụng, hợp đồng lao động, onboarding/offboarding, nội quy – thỏa ước, đánh giá – lương thưởng, kỷ luật, chấm dứt HĐLĐ, BHXH, lịch tuân thủ. Kèm quy trình trọn gói (nhân viên mới, nghỉ việc, kỷ luật, trình ký, văn bản đến, lịch tháng) và công cụ tính theo Bộ luật Lao động 2019.

## Skill (23)

- `bhxh-che-do`
- `cham-dut-hop-dong`
- `danh-gia-luong-thuong`
- `giay-to-hanh-chinh`
- `hoi-hop-su-kien`
- `hop-dong-lao-dong`
- `kiem-tra-truoc-trinh-ky`
- `ky-luat-lao-dong`
- `lich-thang`
- `lich-tuan-thu-hcns`
- `luu-tru-ho-so`
- `nghi-viec`
- `nhan-vien-moi`
- `noi-quy-thoa-uoc`
- `onboarding-offboarding`
- `quy-che-noi-bo`
- `so-van-ban-di-den`
- `soan-van-ban-hanh-chinh`
- `tham-dinh-hcns`
- `trinh-ky`
- `tuyen-dung`
- `van-ban-den`
- `xu-ly-ky-luat`

Chuyển từ lệnh/agent của bản Claude:

- commands/lich-thang.md → skills/lich-thang
- commands/nghi-viec.md → skills/nghi-viec
- commands/nhan-vien-moi.md → skills/nhan-vien-moi
- commands/trinh-ky.md → skills/trinh-ky
- commands/van-ban-den.md → skills/van-ban-den
- commands/xu-ly-ky-luat.md → skills/xu-ly-ky-luat
- agents/tham-dinh-hcns.md → skills/tham-dinh-hcns

## Cài đặt

Xem README ở gốc repo, mục **ChatGPT / Codex**.

## Connector khai báo sẵn (`.app.json`)

Khi cài plugin, ChatGPT đề nghị kết nối các ứng dụng: `gmail`, `google-calendar`, `google-drive`, `outlook-email`, `outlook-calendar`, `sharepoint`, `teams`, `zoom`, `slack`. Mỗi người đăng nhập một lần bằng tài khoản của mình. Chưa kết nối thì skill vẫn chạy, chỉ không tự lấy dữ liệu hoặc tạo nháp được.
