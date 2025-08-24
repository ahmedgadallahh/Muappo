[app]
title = MyApp
package.name = myapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# سيبهم فاضيين علشان ما يسببوش خطأ
icon.filename = 
presplash.filename = 

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# نسخة API للـ Android (مهم تبقى متوافقة مع البيئة)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = arm64-v8a
