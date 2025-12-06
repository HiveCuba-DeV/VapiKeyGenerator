from py_vapid import Vapid01

# Generar par de claves VAPID
vapid = Vapid01()
vapid.generate_keys()

print("Public Key:", vapid.public_key)
print("Private Key:", vapid.private_key)
