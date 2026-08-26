# GenTech Project Deployment & Workflow Protocol

## 1. Workflow Protocol (Staging -> Production)
1. **Aşama 1 (Staging / Önizleme):** 
   - İstenen tüm kod, tasarım ve 3D düzenlemeleri öncelikle `/Users/ramay/gentech3-app` dizininde yapılır.
   - Değişiklikler test edilip doğrudan GitHub `main` branch'ine pushlanır (`serhatramay/gentech3-preview`).
   - Kullanıcıya test için önizleme linki sunulur: `https://serhatramay.github.io/gentech3-preview/`

2. **Aşama 2 (Canlı Onay & Production):**
   - Kullanıcı önizlemeden onay verdiğinde veya canlıya al dediğinde, otomatik FTP scripti ile doğrudan `gentech.ae` sunucusuna yükleme yapılır.

## 2. Canlı Sunucu (gentech.ae) FTP Bilgileri
- **Host / IP:** `178.210.173.34` (veya `ftp.gentech.ae`)
- **Kullanıcı Adı:** `gentech1`
- **Şifre:** `PAnda1881`
- **Uzak Dizin:** `/gentech.ae/wwwroot`
- **Önbellek Kuralı:** Canlıya her dağıtımda CSS ve JS versiyonları (`?v=X.X`) otomatik güncellenir.
