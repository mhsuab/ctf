1. printout password calculated in `FlagstaffHill.java`
2. `apktool d four.apk`
3. modify `FlagstaffHill.smali`
   ```java
   if-eqz v5, :cond_0

    const-string v5, "call it"

    return-object v5

    .line 37
    :cond_0
    const-string v5, "NOPE"

    return-object v5
   ```
   to
   ```java
   if-eqz v5, :cond_0

    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    return-object v5

    .line 37
    :cond_0
    const-string v5, "NOPE"

    return-object v5
   ```
4. `apktool b four -o four_mod.apk`
5. sign
   1. `keytool -genkey -v -keystore my-release-key.keystore -alias AliasName -keyalg RSA -keysize 2048 -validity 10000`
   2. `jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore four_mod.apk AliasName`