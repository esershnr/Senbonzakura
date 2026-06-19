# Senbonzakura (Özelleştirilmiş AutoHotkey v2.0.26)

Senbonzakura, oyunlardaki anti-cheat sistemlerinin (BattlEye, Easy Anti-Cheat vb.) imza ve pencere tespit engellerini aşmak amacıyla AutoHotkey v2.0.26 kaynak kodu üzerinden özelleştirilmiş, tamamen bağımsız bir makro ve otomasyon motorudur.

---

## 🚀 sakura Branch Farkları ve Yapılan Değişiklikler
Bu branch üzerinde, sistemin hiçbir şekilde "AutoHotkey" izi taşımaması için şu kritik değişiklikler yapılmıştır:

1. **Uzantı Değişikliği (`.ahk` ➔ `.sbz`):**
   * Varsayılan `.ahk` uzantısı sistemden tamamen kaldırılmış ve yerine **`.sbz`** uzantısı getirilmiştir. Yorumlayıcı artık sadece `.sbz` dosyalarını çalıştıracak ve hata ayıklama yığınlarında bu uzantıyı arayacaktır.
2. **Pencere Sınıfları (Window Classes):**
   * Arka planda tespit edilebilecek `AutoHotkey` ve `AutoHotkeyGUI` pencere sınıf isimleri sırasıyla **`Senbonzakura`** ve **`SenbonzakuraGUI`** olarak değiştirilmiştir.
3. **Sistem Mutex İsimleri:**
   * Kancalar (Hooks) tarafından oluşturulan ve anti-cheat'ler tarafından taranan `AHK Keybd` ve `AHK Mouse` mutex isimleri sırasıyla **`SBZ Keybd`** ve **`SBZ Mouse`** olarak güncellenmiştir.
4. **Metadata & Assembly Kimliği:**
   * Derlenen yürütülebilir dosyanın (`.exe`) detaylarındaki Şirket Adı (`ES Corp.`), Ürün Adı (`Senbonzakura`), Dosya Açıklaması (`Senbonzakura Sicak Tush`) ve Manifest assembly kimlik bilgileri tamamen değiştirilerek AutoHotkey izleri silinmiştir.
5. **Dahili Tanımlar & Aliaslar:**
   * Ses oynatma kütüphanesindeki `AHK_PlayMe` aliası `SBZ_PlayMe` yapılmış ve `InternetOpen` içindeki User-Agent başlığı `Senbonzakura` olarak güncellenmiştir.

---

## ⚠️ Bu Branch Kullanılırken Dikkat Edilmesi Gerekenler
* **`.ahk` Uzantısı Desteklenmez:** Yazdığınız script dosyalarını mutlaka `.sbz` uzantısıyla kaydetmelisiniz.
* **Yorumlayıcı Adı:** Derleme sonrasında exe dosyası doğrudan `Senbonzakura64.exe` (veya 32-bit ise `Senbonzakura32.exe`) olarak çıktı verir.
* **#Requires Direktifi:** Scriptlerinizin başında sürüm kontrolü yaparken `#Requires AutoHotkey` yerine `#Requires Senbonzakura` kullanmalısınız.
* **UPX Sıkıştırması:** Exe oluştururken (paketlerken) UPX sıkıştırmasını devre dışı bırakın; aksi halde anti-cheat sistemleri UPX imzasından dolayı programı engelleyebilir.

---

## 🛠️ Nasıl Derlenir?

Senbonzakura, **Visual Studio 2022** veya **Visual Studio Build Tools 2022** ile C++ araçları yüklü olarak derlenebilir.

### VS Code / Antigravity ve MSBuild ile Derleme:
MSBuild.exe yolunu kullanarak terminalden doğrudan şu komutla temiz ve sıfırdan bir derleme yapabilirsiniz:

```powershell
# Projeyi temizle ve yeniden derle (Release x64)
& "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /t:Clean /p:Configuration=Release /p:Platform=x64
& "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\MSBuild\Current\Bin\MSBuild.exe" AutoHotkeyx.sln /p:Configuration=Release /p:Platform=x64
```

Derleme çıktısı projenizin ana dizinindeki `bin\Senbonzakura64.exe` konumunda yer alacaktır.
