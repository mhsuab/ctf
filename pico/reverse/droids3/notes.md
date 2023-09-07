1. `apktool d three.apk`
2. modify `nope` to `yep`
3. `apktool b three -o three_mod.apk`
4. sign
   1. `keytool -genkey -v -keystore my-release-key.keystore -alias AliasName -keyalg RSA -keysize 2048 -validity 10000`
   2. `jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore three_mod.apk AliasName`