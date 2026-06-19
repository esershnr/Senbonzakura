# Senbonzakura Geliştirme ve Güvenlik Yapılacaklar Listesi (TODO)

## 📌 [TAMAMLANDI] Pencere Kriteri İsimlerini Özelleştirme
Standart pencere arama kriterleri (`ahk_id`, `ahk_class`, `ahk_exe`, vb.) projedeki C++ kodlarından başarıyla `sbz_` ön ekiyle değiştirilmiştir.

### Değiştirilen Kelimeler:
* `ahk_id` ➔ `sbz_id`
* `ahk_class` ➔ `sbz_class`
* `ahk_exe` ➔ `sbz_exe`
* `ahk_pid` ➔ `sbz_pid`
* `ahk_group` ➔ `sbz_group`

> ⚠️ **Not:** Artık `.sbz` uzantılı scriptlerinizi yazarken de `WinExist("sbz_exe chrome.exe")` şeklinde yazmanız gerekmektedir.

---

## 🛠️ Derleme ve Sıkıştırma Kuralları
1. **Derleme:** Her değişiklikten sonra projeyi `MSBuild` ile `x64` Release modunda derleyin:
   ```powershell
   & "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /t:Clean /p:Configuration=Release /p:Platform=x64
   & "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /p:Configuration=Release /p:Platform=x64
   ```
2. **Paketleme (Ahk2Exe):** Scriptleri derlenmiş exe haline getirirken **UPX sıkıştırmasını kesinlikle devre dışı bırakın**.
