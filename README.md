# self-healing-infra-prometheus-alerts

Self-healing infrastructure demo using Prometheus + Alertmanager + Flask webhook + Ansible.
This repo contains Docker Compose files, Prometheus configs, alert rules, Alertmanager config,
a Flask webhook to receive notifications and an Ansible playbook to restart the NGINX container.

## Quick start (VM / Ubuntu)
1. cd ~/prometheus
2. docker compose up -d
3. sudo systemctl start webhook.service
4. Visit:
   - Prometheus: http://<VM_IP>:9090
   - Alertmanager: http://<VM_IP>:9093
   - App (NGINX): http://<VM_IP>:8080
   - Webhook: http://<VM_IP>:5001

See `prometheus/`, `alertmanager/`, `www/`, `webhook.py`, `restart_nginx.yml` for configs.
