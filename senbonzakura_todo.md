# Senbonzakura Geliştirme ve Güvenlik Yapılacaklar Listesi (TODO)

## 📌 Sonraki Aşama: Pencere Kriteri İsimlerini Özelleştirme
Daha ileri düzey bir gizlilik sağlamak için AHK'nin standart pencere arama kriterlerini (`ahk_id`, `ahk_class`, `ahk_exe`, vb.) projedeki C++ kodlarından tamamen değiştirebilirsiniz.

Bu sayede anti-cheat'in binary (makine kodu) taramalarında hiçbir şekilde bu kancalar geçmeyecektir.

### Değiştirilmesi Planlanan Kelimeler:
* `ahk_id` ➔ `sbz_id`
* `ahk_class` ➔ `sbz_class`
* `ahk_exe` ➔ `sbz_exe`
* `ahk_pid` ➔ `sbz_pid`
* `ahk_group` ➔ `sbz_group`

> ⚠️ **Not:** Bu değişikliği yaptıktan sonra `.sbz` uzantılı scriptlerinizi yazarken de `WinExist("sbz_exe chrome.exe")` şeklinde yazmanız gerekecektir.

---

## 🛠️ Derleme ve Sıkıştırma Kuralları
1. **Derleme:** Her değişiklikten sonra projeyi `MSBuild` ile `x64` Release modunda derleyin:
   ```powershell
   & "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /t:Clean /p:Configuration=Release /p:Platform=x64
   & "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /p:Configuration=Release /p:Platform=x64
   ```
2. **Paketleme (Ahk2Exe):** Scriptleri derlenmiş exe haline getirirken **UPX sıkıştırmasını kesinlikle devre dışı bırakın**.
