---
name: luu-tru-ho-so
description: Tổ chức lưu trữ hồ sơ, tài liệu doanh nghiệp Việt Nam — lập danh mục hồ sơ năm theo phòng ban, mã hồ sơ, thời hạn bảo quản (chứng từ kế toán 5/10 năm hoặc vĩnh viễn theo Luật Kế toán, hồ sơ thuế, hồ sơ nhân sự, hợp đồng, hồ sơ pháp lý doanh nghiệp, biên bản họp HĐQT), cách đặt tên file và cây thư mục trên Google Drive/SharePoint, số hóa tài liệu giấy, lưu văn bản điện tử có chữ ký số, lập hội đồng và biên bản tiêu hủy tài liệu hết hạn, xử lý dữ liệu cá nhân khi hết mục đích (CV ứng viên, hồ sơ nhân viên đã nghỉ). Dùng khi người dùng nói "sắp xếp hồ sơ", "lưu trữ tài liệu bao lâu", "danh mục hồ sơ", "hồ sơ nào được hủy", "biên bản tiêu hủy tài liệu", "đặt tên file thống nhất", "số hóa hồ sơ", "tổ chức thư mục Drive".
---

# Lưu trữ hồ sơ

Đọc trước: `references/nguyen-tac-chung.md`, `references/thoi-han-bao-quan.md`.

## Việc người dùng hay cần

### 1. Lập danh mục hồ sơ năm
Bảng: `Mã hồ sơ | Tên hồ sơ | Đơn vị/người lập | Thời hạn bảo quản | Căn cứ thời hạn | Ghi chú`.
- Mã gợi ý: `<NĂM>.<MÃ PHÒNG>.<STT>` – ví dụ `2026.HCNS.05` = "Hồ sơ tuyển dụng năm 2026".
- Mỗi việc/một vụ việc = một hồ sơ (ví dụ: hồ sơ từng nhân viên; hồ sơ từng hợp đồng; hồ sơ từng kỳ quyết toán).
- Thời hạn lấy từ `references/thoi-han-bao-quan.md`; mục nào luật không quy định cho doanh nghiệp → ghi "Theo quy chế công ty (đề xuất ...)" và nêu lý do đề xuất (thời hiệu khởi kiện, thời hiệu thanh tra thuế...).

### 2. Cây thư mục và quy tắc đặt tên file
```
00_PHAP-LY-DOANH-NGHIEP/   (ĐKKD, điều lệ, sổ cổ đông, biên bản ĐHĐCĐ/HĐQT – vĩnh viễn)
01_VAN-BAN-DI/<năm>/       02_VAN-BAN-DEN/<năm>/
03_HOP-DONG/<năm>/<đối tác>/
04_NHAN-SU/<mã NV>_<họ tên không dấu>/
05_KE-TOAN-THUE/<năm>/<kỳ>/
06_QUY-CHE-NOI-BO/ (bản hiệu lực + thư mục _HET-HIEU-LUC)
```
Tên file: `<yyyy-mm-dd>_<loại>_<số ký hiệu>_<trích yếu ngắn không dấu>.pdf` – ví dụ `2026-03-05_QD_15-QD-ABC_bo-nhiem-truong-phong-HCNS.pdf`. Không dùng dấu cách, ký tự đặc biệt; phiên bản: `_v2`, bản ký: `_da-ky`.

### 3. Số hóa tài liệu giấy
Quét ≥ 300 dpi, PDF có lớp chữ (OCR tiếng Việt), đặt tên theo quy tắc trên, đối chiếu số trang; **bản số hóa không thay thế bản gốc giấy** trừ khi pháp luật chuyên ngành cho phép – vẫn giữ bản gốc đến hết thời hạn bảo quản.

### 4. Văn bản điện tử
Lưu bản gốc điện tử có chữ ký số (file .pdf ký số), không chỉ lưu bản in; giữ khả năng kiểm tra chữ ký (Luật Giao dịch điện tử 2023). Sao lưu định kỳ (quy tắc 3-2-1: 3 bản, 2 phương tiện, 1 bản ở nơi khác).

### 5. Tiêu hủy tài liệu hết thời hạn
1. Lập danh mục tài liệu hết hạn (tính ngày hết hạn bằng `cong_ngay_lich` từ ngày kết thúc hồ sơ + số năm).
2. Thành lập hội đồng xác định giá trị tài liệu/hội đồng tiêu hủy (quyết định của giám đốc – dùng skill `soan-van-ban-hanh-chinh`).
3. Hội đồng xem xét, đề xuất; giám đốc phê duyệt.
4. Tiêu hủy (hủy giấy bằng máy hủy/thuê đơn vị có chức năng; xóa dữ liệu điện tử không khôi phục được).
5. Lập **biên bản tiêu hủy** (mẫu trong `references/thoi-han-bao-quan.md`) + lưu danh mục tài liệu đã hủy **vĩnh viễn**.
Chứng từ kế toán: tiêu hủy theo quy định riêng của pháp luật kế toán (phối hợp kế toán).

### 6. Dữ liệu cá nhân
- CV ứng viên không trúng tuyển: chỉ giữ khi ứng viên đồng ý (ví dụ cho đợt tuyển sau); hết mục đích → xóa/hủy (Luật BVDLCN 2025).
- Hồ sơ nhân viên đã nghỉ: giữ phần cần cho nghĩa vụ pháp lý (HĐLĐ, BHXH, thuế, quyết định), hạn chế người truy cập.

## Đầu ra
Danh mục hồ sơ (bảng/Excel), cây thư mục, quy tắc đặt tên, kế hoạch số hóa, hoặc bộ hồ sơ tiêu hủy (quyết định + danh mục + biên bản) – tùy yêu cầu.
