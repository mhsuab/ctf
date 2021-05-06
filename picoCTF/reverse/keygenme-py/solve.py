import hashlib

bUsername_trial = b"SCHOFIELD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

hash_key = hashlib.sha256(bUsername_trial).hexdigest()

key = key_part_static1_trial
key += hash_key[4]
key += hash_key[5]
key += hash_key[3]
key += hash_key[6]
key += hash_key[2]
key += hash_key[7]
key += hash_key[1]
key += hash_key[8]
key += key_part_static2_trial

print (key_full_template_trial)
print (key)