from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

def to_base64url(data: bytes) -> str:
    """Convierte bytes a Base64 URL-safe sin padding."""
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")

# Generar clave privada EC (SECP256R1)
private_key = ec.generate_private_key(ec.SECP256R1())

# Serializar clave privada en formato DER
private_bytes = private_key.private_numbers().private_value.to_bytes(32, "big")
private_b64 = to_base64url(private_bytes)

# Obtener clave pública
public_key = private_key.public_key()
public_numbers = public_key.public_numbers()

x_bytes = public_numbers.x.to_bytes(32, "big")
y_bytes = public_numbers.y.to_bytes(32, "big")
public_bytes = b"\x04" + x_bytes + y_bytes  # formato uncompressed point
public_b64 = to_base64url(public_bytes)

print("VAPID_PUBLIC_KEY =", public_b64)
print("VAPID_PRIVATE_KEY =", private_b64)

