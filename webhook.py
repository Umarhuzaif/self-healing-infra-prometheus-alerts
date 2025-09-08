from flask import Flask, request
import os, logging, json

LOGFILE="/var/log/webhook.log"
logging.basicConfig(filename=LOGFILE, level=logging.INFO, format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook server is running ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    logging.info("Alert received: %s", json.dumps(data))
    # call ansible playbook that restarts nginx container
    rc = os.system("ansible-playbook /home/umarkolhar/prometheus/restart_nginx.yml > /var/log/webhook_ansible.log 2>&1")
    logging.info("Ansible return code: %s", rc)
    return "Webhook received and action executed!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
