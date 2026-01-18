# 🚀 Deployment Guide: Catherine Ge's Academic Portfolio

This guide explains how to host your new "Digital Scholar" website for free using **GitHub Pages** and link it to your custom domain.

## 1. Prerequisites

* A GitHub account.
* Your domain name provider login (e.g., GoDaddy, Namecheap, Aliyun).

## 2. Uploading the Code

1. Log in to GitHub and create a **New Repository**.
    * Repository Name: `catherine-ge-portfolio` (or similar).
    * Public: **Yes**.
    * Initialize with README: **No**.
2. Upload the files from the `personal_website` folder (`index.html`, `assets/`, `CNAME`) to this repository.
    * *Option A (Command Line)*:

        ```bash
        cd /Users/catherineger/Antigravity/personal_website
        git init
        git add .
        git commit -m "Initial commit"
        git branch -M main
        git remote add origin https://github.com/YOUR_USERNAME/catherine-ge-portfolio.git
        git push -u origin main
        ```

    * *Option B (Web Upload)*: Just drag and drop the files into the GitHub website interface.

## 3. Activating GitHub Pages

1. Go to your Repository **Settings**.
2. Click **Pages** (in the left sidebar).
3. Under **Branch**, select `main` and save.
4. Under **Custom domain**, enter your domain (e.g., `www.yourdomain.com`) and click **Save**.
5. Check the box **Enforce HTTPS** (Crucial for security).

## 4. Configuring Your Domain (DNS)

Log in to your domain provider (where you bought the domain) and update the DNS records:

* **A Record**:
  * Host: `@`
  * Value: `185.199.108.153`
* **A Record** (Add 3 more):
  * `185.199.109.153`
  * `185.199.110.153`
  * `185.199.111.153`
* **CNAME Record**:
  * Host: `www`
  * Value: `YOUR_USERNAME.github.io`

*Wait up to 24 hours for global propagation (usually 30 mins).*

## 5. Adding Your Research One-Pager

1. Convert your `AU_Research_One_Pager.md` to a **PDF**.
    * *Tip*: Use a Markdown-to-PDF converter or copy the text into Word/Canva and export as PDF.
2. Name it `one_pager.pdf`.
3. Place it in the `assets/` folder.
4. The website is already coded to link to it!

---
**Why this helps:**
When Tracy McCaffrey clicks your email link, she sees a **Professional Lab Website**, not a generic LinkedIn page. It visually proves the "300k Infrastructure" existed before she even reads the email.
