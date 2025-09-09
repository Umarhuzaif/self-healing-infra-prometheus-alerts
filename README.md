# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

This project demonstrates a **self-healing infrastructure** using **Prometheus, Alertmanager, Docker, Flask, and Ansible**.  
It automatically detects service failures (e.g., an Nginx web server going down) and triggers an automated recovery process, restoring the service without human intervention.

---

## 🚀 Project Overview

Modern systems must be **resilient and highly available**. Instead of requiring manual intervention when a service fails, a **self-healing system** detects the failure and repairs it automatically.

This project shows how to:
- Monitor a running service with **Prometheus**.
- Define alerting rules to detect failures (service down, high CPU, etc.).
- Send alerts to **Alertmanager**, which routes them to a **Flask-based webhook**.
- The webhook triggers an **Ansible playbook** to automatically restart the failed service.
- Demonstrate end-to-end recovery for an Nginx container.

---

## 🛠️ Tools & Technologies

- **Prometheus** → Metrics collection & alerting engine  
- **Alertmanager** → Alert routing & delivery  
- **Node Exporter** → Host-level metrics (CPU, memory, disk)  
- **Docker & Docker Compose** → Container orchestration  
- **NGINX** → Sample web service being monitored  
- **Flask (Python)** → Webhook receiver for Alertmanager  
- **Ansible** → Automation tool to restart failed services  
- **Ubuntu VM (VirtualBox/WSL)** → Development & deployment environment  

---

## 📂 Project Structure

prometheus/
│
├── docker-compose.yml # Defines services (Prometheus, Alertmanager, Node Exporter, Nginx)
│
├── prometheus/
│ ├── prometheus.yml # Prometheus scrape configuration
│ ├── alert.rules.yml # Alert rules (service down, etc.)
│
├── alertmanager/
│ └── alertmanager.yml # Alertmanager config (routes to webhook)
│
├── www/
│ └── index.html # Custom demo page served by Nginx
│
├── webhook.py # Flask app to receive alerts and trigger Ansible
├── restart_nginx.yml # Ansible playbook to restart webserver container
└── README.md # Documentation (this file)

yaml
Copy code

---

## ⚙️ How It Works

1. **Nginx** runs in a Docker container, serving a demo page:
Self-Healing Demo — Your Name
This server will be auto-restarted by the webhook on failure.

markdown
Copy code

2. **Prometheus** scrapes metrics (including Nginx availability) every 15 seconds.  
If the service is down (`up == 0`), it fires an alert `InstanceDown`.

3. **Alertmanager** receives the alert and forwards it via a webhook to the Flask server.

4. **Flask Webhook (`webhook.py`)** logs the alert and runs the Ansible playbook.

5. **Ansible Playbook** (`restart_nginx.yml`) executes a Docker restart for the Nginx container.

6. The service comes back up. Prometheus sees `up == 1` and the alert is resolved.

---

## 📊 System Architecture

```mermaid
flowchart LR
 subgraph Monitoring Stack
 P[Prometheus] --> A[Alertmanager]
 end

 subgraph Webhook & Automation
 A --> W[Flask Webhook]
 W --> Y[Ansible Playbook]
 end

 subgraph Services
 Y --> N[NGINX Container]
 P --> N
 end
🔧 Setup & Installation
Prerequisites
Ubuntu VM (VirtualBox / WSL2)

Docker & Docker Compose

Python 3.12+

Ansible

Git

Install essentials:

bash
Copy code
sudo apt update
sudo apt install -y docker.io docker-compose python3-pip ansible git
Clone the Repository
bash
Copy code
git clone https://github.com/Umarhuzaif/self-healing-infra-prometheus-alerts.git
cd self-healing-infra-prometheus-alerts
Start Monitoring Stack
bash
Copy code
docker compose up -d
This launches:

Prometheus (9090)

Alertmanager (9093)

Node Exporter (9100)

Nginx webserver (8080)

Run the Webhook Service
Create a systemd service (optional for auto-start):

bash
Copy code
sudo nano /etc/systemd/system/webhook.service
Paste:

ini
Copy code
[Unit]
Description=Alertmanager Webhook (Flask)
After=network.target docker.service

[Service]
User=umarkolhar
WorkingDirectory=/home/umarkolhar/prometheus
ExecStart=/usr/bin/python3 /home/umarkolhar/prometheus/webhook.py
Restart=always

[Install]
WantedBy=multi-user.target
Enable it:

bash
Copy code
sudo systemctl daemon-reload
sudo systemctl enable --now webhook.service
Verify Services
Prometheus UI → http://localhost:9090

Prometheus Alerts → http://localhost:9090/alerts

Alertmanager UI → http://localhost:9093

Nginx Demo Page → http://localhost:8080

Webhook Health → http://localhost:5001

🧪 Testing Self-Healing
Stop the Nginx container:

bash
Copy code
docker stop webserver
Wait ~30s.

Prometheus marks it as down.

InstanceDown alert fires.

Alertmanager routes to webhook.

Webhook triggers Ansible → restarts Nginx.

Verify recovery:

bash
Copy code
docker ps | grep webserver
curl http://localhost:8080
The page should be available again ✅.

📸 Deliverables
Configuration files (prometheus.yml, alert.rules.yml, alertmanager.yml)

Webhook script (webhook.py)

Ansible playbook (restart_nginx.yml)

Docker Compose file (docker-compose.yml)

Demo HTML page (index.html)

Logs/Screenshots of alerts firing, Alertmanager UI, webhook logs, auto-restart proof

🌟 Key Features
Automated monitoring with Prometheus

Real-time alerting with Alertmanager

Flask-based webhook integration

Service recovery via Ansible automation

Demonstration of self-healing infrastructure

📚 Future Improvements
Add Slack/Email notification channels in Alertmanager

Extend playbooks for multi-service recovery

Integrate Grafana for dashboards

Support scaling across multiple nodes

👤 Author
Umar Huzaif Kolhar

GitHub: @Umarhuzaif

Project Repo: Self-Healing Infra

yaml
Copy code

---

✅ This `README.md` is **professional, clear, and complete** — good for academic submission, GitHub portfolio, or DevOps interview prep.

Do you want me to also draft a **2-page PDF-style project report** (with
