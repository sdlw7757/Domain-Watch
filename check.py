import json
import datetime
import smtplib
from email.mime.text import MIMEText
import os

# 发送邮件
def send_email(subject, content):
    sender = os.environ.get("MAIL_SENDER")
    password = os.environ.get("MAIL_PASS")
    receiver = os.environ.get("MAIL_RECEIVER")
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.qq.com")
    smtp_port = int(os.environ.get("SMTP_PORT", 465))

    if not all([sender, password, receiver]):
        print("未配置邮箱")
        return

    try:
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, [receiver], msg.as_string())
        print("✅ 邮件发送成功")
    except Exception as e:
        print("❌ 邮件失败:", e)

# 计算剩余天数
def get_days_left(expire_str):
    try:
        now = datetime.datetime.now()
        expire = datetime.datetime.strptime(expire_str, "%Y-%m-%d")
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        expire = expire.replace(hour=0, minute=0, second=0, microsecond=0)
        return (expire - now).days
    except:
        return -999

# 主程序
def main():
    print("=== 域名到期自动检测 ===")
    with open("domains.json", "r", encoding="utf-8") as f:
        domains = json.load(f)

    warn_list = []
    for item in domains:
        domain = item.get("domain")
        expire = item.get("expire")
        warn_days = int(item.get("warnDays", 180))
        left = get_days_left(expire)

        print(f"域名: {domain:20} 剩余: {left:3}天 提醒: ≤{warn_days}天")

        if 0 <= left <= warn_days:
            warn_list.append((domain, expire, left))

    if warn_list:
        msg = ["⚠️ 域名到期提醒\n"]
        for d, e, l in warn_list:
            msg.append(f"• {d}\n  到期: {e} | 剩余: {l}天\n")
        send_email(f"【域名监控】{len(warn_list)}个域名即将到期", "\n".join(msg))
    else:
        print("✅ 所有域名正常")

if __name__ == "__main__":
    main()