# MQTT User Account Setup

## Overview

This document explains how to create and manage user accounts for the Mosquitto MQTT broker used by the Secure IoT Monitoring System.

The broker requires username/password authentication in addition to TLS encryption.

---

# Prerequisites

Install Mosquitto:

## Windows

Download and install Mosquitto.

Verify installation:

```bash
mosquitto -h
```

## Linux

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
```

---

# Create Password File

Create a new password file:

```bash
mosquitto_passwd -c passwords.txt sensor
```

You will be prompted to enter a password.

Example:

```text
Password:
Reenter password:
```

---

# Add Dashboard User

```bash
mosquitto_passwd passwords.txt dashboard
```

---

# Add Administrator User

```bash
mosquitto_passwd passwords.txt admin
```

---

# Verify Users

The password file should now contain encrypted password hashes.

Example:

```text
sensor:<hashed_password>
dashboard:<hashed_password>
admin:<hashed_password>
```

Passwords are stored as hashes and cannot be read in plain text.

---

# Broker Configuration

Update `mosquitto.conf`:

```text
allow_anonymous false
password_file passwords.txt
```

This forces all clients to authenticate.

---

# Client Configuration Example

Example MQTT connection:

```python
client.username_pw_set(
    username="dashboard",
    password="StrongPassword123!"
)
```

---

# Security Recommendations

## Use Strong Passwords

Recommended:

* Minimum 12 characters
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Example:

```text
M@rina2026Secure!
```

---

## Do Not Store Passwords in Source Code

Avoid:

```python
password = "admin123"
```

Instead use:

```python
import os

password = os.getenv("MQTT_PASSWORD")
```

---

## Rotate Credentials

Recommended rotation schedule:

* Every 90 days
* Immediately after a suspected compromise

---

## Remove Unused Accounts

Periodically review:

* Sensor accounts
* Dashboard accounts
* Administrative accounts

Delete accounts that are no longer needed.

---

# Troubleshooting

## Authentication Failed

Check:

* Username spelling
* Password correctness
* `password_file` location
* Broker restart status

Example restart:

```bash
mosquitto -c mosquitto.conf
```

---

# Summary

The MQTT broker uses layered security:

1. TLS encryption protects data in transit.
2. Client certificates verify device identity.
3. Username/password authentication controls access.
4. Broker logging records authentication events.

Together these controls help protect the Secure IoT Monitoring System from unauthorized access.
