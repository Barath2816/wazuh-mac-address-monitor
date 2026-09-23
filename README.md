# Wazuh MAC Address Change Detection

## Overview
This project is a Security Information and Event Management (SIEM) solution developed using Wazuh to detect unauthorized MAC address changes in real time. It monitors network interfaces, generates structured JSON logs, detects MAC spoofing through custom Wazuh rules, executes active responses, sends email notifications, and visualizes alerts on the Wazuh Dashboard.

---

## Features

- Real-time MAC address monitoring
- Detects MAC address spoofing
- Generates JSON security events
- Custom Wazuh detection rules
- Active Response to restore original MAC address
- Email notifications using Postfix
- Dashboard visualization
- MITRE ATT&CK mapping
- Investigation report generation

---

## Architecture

```
Attacker
    │
    ▼
Kali Linux (Agent)
    │
mac_monitor.py
    │
JSON Log
    │
Wazuh Agent
    │
Ubuntu Wazuh Manager
    │
Custom Rules
    │
 ┌──────────────┬──────────────┐
 ▼              ▼              ▼
Dashboard   Email Alert   Active Response
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Wazuh 4.14 | SIEM Platform |
| Ubuntu Server | Wazuh Manager |
| Kali Linux | Monitoring Agent |
| Python 3 | MAC Monitoring Script |
| Bash | Active Response Scripts |
| Postfix | Email Notifications |
| OpenSearch Dashboard | Visualization |
| macchanger | MAC Address Spoofing Test |

---

## Project Structure

```
Wazuh-MAC-Address-Change-Detection/
│
├── docs/
├── diagrams/
├── screenshots/
├── scripts/
├── sample_logs/
├── wazuh/
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Detection Workflow

1. Read the current MAC address.
2. Compare it with the previous MAC address.
3. Detect unauthorized MAC address changes.
4. Generate a JSON investigation log.
5. Wazuh Agent collects the log.
6. Wazuh Manager applies custom rules.
7. Alert is displayed on the dashboard.
8. Email notification is sent.
9. Active Response restores the original MAC address.

---

## Screenshots

### Dashboard
<img width="1852" height="776" alt="Screenshot 2026-09-19 175850" src="https://github.com/user-attachments/assets/30764d7f-2d1c-4d07-b0cd-f34a2f6ffdf0" />

### Discover
(Add screenshot)

### Email Alert
(Add screenshot)

### Architecture
(Add screenshot)

---

## Future Enhancements

- Device profiling
- Vendor lookup API
- Threat intelligence integration
- Slack/Teams notifications
- Multi-agent monitoring
- Machine learning anomaly detection

---

## Author

Barath P


Cyber Security Enthusiast

---

## License

This project is licensed under the MIT License.
