# Threat Model

## Threats

### Eavesdropping
Attackers intercept MQTT traffic.

Mitigation:
TLS encryption.

### Device Spoofing
Attacker pretends to be a sensor.

Mitigation:
Client certificates.

### Data Tampering
Attacker modifies messages.

Mitigation:
TLS integrity protection.

### Denial of Service
Flooding broker with requests.

Mitigation:
Broker access controls.
