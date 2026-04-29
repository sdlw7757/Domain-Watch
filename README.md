# DomainGuard — 域名到期提醒续订智能监控系统

<img width="1225" height="389" alt="DomainWatch" src="https://github.com/user-attachments/assets/8f3f49f1-18d6-48e0-b1fb-4c3faf2e011c" />
🔧一款专为域名打造的**本地可视化管理 + 云端自动提醒**工具，支持独立提醒天数、手动录入到期时间、每日自动检测。

## ✨ 核心功能

- 🌍 **纯本地可视化面板**：精美UI，双击即用，无需部署
- 📅 **手动录入到期日期**：完美支持所有域名，不依赖WHOIS
- ⚠️ **独立提醒天数**：每个域名可自定义到期提醒天数（30/60/90/180天等）
- 📊 **自动计算剩余天数**：精准计算，到期自动标红预警
- ☁️ **GitHub Actions 全自动运行**：每日定时检测，无需服务器
- 📧 **邮件实时通知**：域名即将到期自动发邮件提醒
- 💾 **一键导出/导入备份**：数据安全不丢失

## 🚀 项目结构

```
DomainGuard/
├── 域名续订提醒.html              # 本地可视化管理面板
├── domains.json              # 域名数据文件（导出自动生成）
├── check.py                  # 云端自动检测脚本
└── .github/workflows/check.yml  # 每日自动运行配置
```

## 📌 使用流程

1. 打开 `域名管理.html` 添加、编辑域名信息
2. 点击「导出备份」生成 `domains.json`
3. 上传项目到 GitHub 仓库
4. 配置邮箱密钥，开启自动监控

   进入你的仓库：
   Settings → Secrets and variables → Actions → New repository secret
   
   添加下面 5 个密钥：
   
   | 密钥名称 | 值 |
   |---------|-----|
   | `MAIL_SENDER` | 你的QQ邮箱 |
   | `MAIL_PASS` | QQ邮箱授权码 |
   | `MAIL_RECEIVER` | 你要收提醒的邮箱 |
   | `SMTP_SERVER` | smtp.qq.com |
   | `SMTP_PORT` | 465 |

5. 系统每日自动检测，到期邮件提醒

## 🔧 适用场景

- 免费本地化运行
- 多平台域名统一到期提醒日监控
- 个人/工作室域名资产维护
- 无需服务器的轻量化自动化提醒

## 🎯 项目亮点

✅ 零代码使用

✅ 零依赖运行

✅ 零成本部署

✅ 全平台兼容

✅ 全自动守护

## 📄 开源协议

本项目基于 [MIT License](https://opensource.org/licenses/MIT) 开源。


---

**DomainGuard — 让你的域名永不过期**
