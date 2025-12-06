# VapiKeyGenerator

Generator of VAPI Key Pairs for Push Notification

## Overview

**VapiKeyGenerator** is a simple Python utility that generates VAPID (Voluntary Application Server Identification) key pairs.  
These keys are required to authenticate your server when sending Web Push notifications to browsers.

The tool is based on the [`py-vapid`](https://github.com/web-push-libs/py-vapid) library and outputs both the **public** and **private** keys.

- The **public key** is shared with your client-side application (e.g., React PWA).
- The **private key** is kept securely on your backend (e.g., Flask) to sign push requests.

---

## Features

- Generate new VAPID key pairs quickly.
- Print keys directly to the console.
- Easy integration with Flask or any backend using `pywebpush`.
- Lightweight and minimal code (`pyVapiGenerator.py`).

---

## Requirements

- Python 3.7+
- Dependencies:

  ```bash
  pip install py-vapid
  ```

---

## Usage

Run the script directly:

```bash
python pyVapiGenerator.py
```

Example output:

```text
Public Key: BExAMPLEPuBLicKey...
Private Key: 1aExAMPLePrIVateKey...
```

---

## Integration

1. **Frontend (React PWA)**

   - Use the **public key** in your `pushManager.subscribe` call:

     ```typescript
     registration.pushManager.subscribe({
       userVisibleOnly: true,
       applicationServerKey: vapidPublicKey,
     });
     ```

2. **Backend (Flask + pywebpush)**

   - Use the **private key** to sign push requests:

     ```python
     from pywebpush import webpush

     webpush(
       subscription_info=subscription,
       data="Hello from HiveP2P!",
       vapid_private_key=VAPID_PRIVATE_KEY,
       vapid_claims={"sub": "mailto:admin@yourdomain.com"}
     )
     ```

---

## Security Notes

- **Never expose the private key** in your frontend code or repository.
- Store the private key in environment variables or a secure secrets manager.
- Rotate keys periodically if required by your security policy.

---

## License

This project is released under the MIT License.  
See [LICENSE](LICENSE) for details.
