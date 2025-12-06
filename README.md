# VapiKeyGenerator

Generator of VAPI Key Pairs for Push Notification

## Overview

**VapiKeyGenerator** is a simple Python utility that generates VAPID (Voluntary Application Server Identification) key pairs.  
These keys are required to authenticate your server when sending Web Push notifications to browsers.

The tool is based on the [`cryptography`](https://github.com/pyca/cryptography/) library and outputs both the **public** and **private** keys.

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
  pip install cryptography
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

    export function urlBase64ToUint8Array(base64String: string):Uint8Array {
        const padding = "=".repeat((4 - (base64String.length % 4)) % 4);
        const base64 = (base64String + padding)
        .replace(/-/g, "+")
        .replace(/_/g, "/");

        const rawData = window.atob(base64);
        const outputArray = new Uint8Array(rawData.length);

        for (let i = 0; i < rawData.length; ++i) {
          outputArray[i] = rawData.charCodeAt(i);
        }
        return outputArray;
    }


    const VAPID_PUBLIC_KEY = "BExAMPLEPuBLicKeyBase64Url";
    registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY),
    });

    ```

2. **Backend (Flask + pywebpush)**

   - Use the **private key** to sign push requests:

    ```python
    from pywebpush import webpush

    VAPID_PRIVATE_KEY = "1aExAMPLePrIVateKeyBase64Url"
    VAPID_PUBLIC_KEY = "BExAMPLEPuBLicKeyBase64Url"

    VAPID_CLAIMS = {
      "sub": "mailto:admin@hivep2p.com"
    }

    webpush(
    subscription_info=subscription,
    data=json.dumps({"title": "HiveP2P", "body": "New message"}),
    vapid_private_key=VAPID_PRIVATE_KEY,
    vapid_claims=VAPID_CLAIMS
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
