# Incident Response Report

## Incident Summary

**Incident Name:** Unauthorized MQTT Client Connection Attempt

**Date:** May 31, 2026

**Severity:** Medium

**Status:** Resolved

---

# Executive Summary

During routine monitoring of the Secure IoT Monitoring System, an unauthorized MQTT client attempted to connect to the Mosquitto broker. The connection was rejected because the client did not present a valid TLS certificate.

No sensor data was accessed, modified, or disrupted. Existing security controls functioned as designed and prevented unauthorized access.

---

# Detection

## Initial Alert

The incident was detected through broker logs indicating a failed client authentication attempt.

Example log entry:

```text
TLS Error: Certificate verification failed
Client connection rejected
```

## Detection Method

* TLS certificate validation
* Broker authentication controls
* Dashboard monitoring logs

---

# Analysis

## Affected Systems

* Mosquitto Broker
* Dashboard Subscriber

## Systems Not Affected

* Pool Sensor
* Kitchen Sensor
* Spa Sensor

## Investigation Findings

The connecting device:

* Did not possess a valid client certificate
* Failed TLS verification
* Was denied access before any MQTT topics were accessed

No evidence of:

* Data theft
* Message tampering
* Service interruption

was identified.

---

# Containment

## Actions Taken

1. Verified that the connection attempt was blocked.
2. Reviewed broker logs.
3. Confirmed legitimate sensors remained connected.
4. Monitored for additional connection attempts.

## Result

The threat was contained automatically by existing security controls.

---

# Eradication

## Actions Taken

* Reviewed TLS configuration.
* Verified certificate trust chain.
* Confirmed broker authentication settings.

No malicious software or compromised devices were identified.

No eradication actions were required.

---

# Recovery

## Validation Steps

* Verified broker functionality.
* Confirmed sensor communications.
* Confirmed dashboard updates.
* Verified alert generation.

## Recovery Status

System fully operational.

No downtime occurred.

---

# Timeline

| Time     | Event                                    |
| -------- | ---------------------------------------- |
| 10:15 AM | Unauthorized client attempted connection |
| 10:15 AM | TLS validation failed                    |
| 10:16 AM | Broker rejected connection               |
| 10:20 AM | Logs reviewed                            |
| 10:30 AM | Investigation completed                  |
| 10:35 AM | Incident closed                          |

---

# Lessons Learned

## What Worked Well

* TLS certificates prevented unauthorized access.
* Logging provided clear evidence of the event.
* Monitoring quickly identified the issue.

## Areas for Improvement

* Implement automated alert notifications.
* Add IP address tracking for failed connections.
* Create recurring security review procedures.

---

# Recommendations

### Short-Term

* Enable separate security alert logs.
* Increase monitoring visibility.

### Long-Term

* Implement centralized logging.
* Add certificate expiration monitoring.
* Develop formal incident response playbooks.

---

# Conclusion

The unauthorized connection attempt was successfully prevented through TLS certificate authentication and broker security controls. The incident demonstrated the effectiveness of the system's security architecture and highlighted opportunities for improving monitoring and alerting capabilities.
