import base64

from Crypto.Util.number import long_to_bytes


# from hex
print(bytes.fromhex("666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"))

# base party: https://cyberchef.org/


base64_str = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
base_10_str = 664813035583918006462745898431981286737635929725

print(base64.b64decode(base64_str)) # from base64
print(long_to_bytes(base_10_str)) # from base10

