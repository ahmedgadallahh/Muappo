[app]
title = tictactoeapp
package.name = tictactoeapk
package.domain = org.tictactoeapp
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
# Consider specifying source.include_patterns or source.exclude_patterns if needed
version = 0.1
requirements = python3,kivy==2.1.0,kivymd==0.104.2,pillow==8.3.1
presplash.filename = %(source.dir)s/image/presplash.png
icon.filename = %(source.dir)s/image/presplash.png
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0
android.presplash_color = black
#android.presplash_lottie = "path/to/lottie/file.json" # Uncomment if you want to use Lottie animations
#android.permissions = android.permission.INTERNET # Add permissions as needed
android.archs = arm64-v8a
android.allow_backup = True
#android.manifest.* = # Uncomment and adjust as per your app's requirements

[buildozer]
log_level = 2
warn_on_root = 1
# Additional buildozer settings...

# iOS configuration (not used in this case)
#ios.kivy_ios_dir =../kivy-ios
#ios.ios_deploy_dir =../ios_deploy
