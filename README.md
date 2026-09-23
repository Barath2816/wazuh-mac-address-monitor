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
<img width="1853" height="802" alt="Screenshot 2026-09-19 175900" src="https://github.com/user-attachments/assets/94c56cd6-3464-40cc-87fc-766d73a6f0f5" />

### Endpoint
<img width="1846" height="660" alt="Screenshot 2026-09-19 175615" src="https://github.com/user-attachments/assets/d1e075e4-d11c-4934-99eb-775d674a5623" />


### Email Alert
<img width="1506" height="642" alt="Screenshot 2026-09-19 180122" src="https://github.com/user-attachments/assets/fd97174d-75fa-4364-99b1-35098dd7ef6f" />


### Architecture
<img width="940" height="1015" alt="image" src="https://github.com/user-attachments/assets/79257675-78a4-40e5-98ad-57465185e2bb" />


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
