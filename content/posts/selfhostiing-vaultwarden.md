---
title: "Selfhosting Vaultwarden Password Manager"
date: 2023-02-26T00:00:00+08:00  
draft: false
tags: []
---

I used 1Password as a password manager. I decided to switch to a self-hosted solution.

- 1Password provides many cool features and tweaks, but I value simplicity and minimalistic style in tooling more than an extensive list of add-ons.
- I convinced my family to start using password managers, and it began to cost twice more.
- Finally, It takes very little time - the whole setup took me one evening.

# Bitwarden Resources Requirments
My first choice was a self-hosted [Bitwarden](https://bitwarden.com/).  

Bitwarden is available for installation on your computer or VPS. You can check it here [https://bitwarden.com/help/install-on-premise-linux/](https://bitwarden.com/help/install-on-premise-linux/).

It’s pretty straightforward, but the is one downside — system requirements. Bare-bones installation of Bitwarden requires 2-3GB of Ram and 12-25GB of disk space. It’s a total overkill for a small setup and can be a significant price increase. 

For example, a DigitalOcean droplet with 4GiB of RAM costs 24$/month, negating the whole point of cheaper self-hosting.  Most of this space and memory is occupied by MSSQL storage which Bitwarden uses.  

# Vaultwarden

Luckily there is an alternative - [Vaultwarden](https://github.com/dani-garcia/vaultwarden).

It implements the Bitwarden server API and is compatible with all the official Bitwarden clients. And most importantly, it uses sqlite instead of heavy-weight MSSQL, which allows it to be installed even on the smallest and cheapest VPS.

# Vaultwarden Installation

Most up-to-date information on setup and installation is in the vaultwarden repository: [https://github.com/dani-garcia/vaultwarden#installation](https://github.com/dani-garcia/vaultwarden#installation)

Default installation of Vaultwarden is pretty straightforward and requires only running docker image on your VPS:
```
docker pull vaultwarden/server:latest
docker run -d --name vaultwarden -v /vw-data/:/data/ -p 80:80 vaultwarden/server:latest 
```

```
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}" --no-stream vaultwarden
NAME          CPU %     MEM USAGE / LIMIT   MEM %
vaultwarden   0.00%     30MiB / 473.6MiB    6.33%
```

# Reverse Proxy

Enabling HTTPS is required to access the web console and perform encryption operations.

The most straightforward approach will be to use docker-compose for Caddy image [https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)

```
version: '3'

services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: always
    environment:
      WEBSOCKET_ENABLED: "true"  # Enable WebSocket notifications.
    volumes:
      - ./vw-data:/data

  caddy:
    image: caddy:2
    container_name: caddy
    restart: always
    ports:
      - 80:80  # Needed for the ACME HTTP-01 challenge.
      - 443:443
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - ./caddy-config:/config
      - ./caddy-data:/data
    environment:
      DOMAIN: "https://vaultwarden.example.com"  # <----- Your domain to access web console 
      EMAIL: "admin@example.com"                 
      LOG_FILE: "/data/access.log"
```

Together with Caddyfile in the same directory

```
{$DOMAIN}:443 {
  log {
    level INFO
    output file {$LOG_FILE} {
      roll_size 10MB
      roll_keep 10
    }
  }

  # Use the ACME HTTP-01 challenge to get a cert for the configured domain.
  tls {$EMAIL}

  # This setting may have compatibility issues with some browsers
  # (e.g., attachment downloading on Firefox). Try disabling this
  # if you encounter issues.
  encode gzip

  # Notifications redirected to the WebSocket server
  reverse_proxy /notifications/hub vaultwarden:3012

  # Proxy everything else to Rocket
  reverse_proxy vaultwarden:80 {
       # Send the true remote IP to Rocket, so that vaultwarden can put this in the
       # log, so that fail2ban can ban the correct IP.
       header_up X-Real-IP {remote_host}
  }
}
```

Afterward, you can access the web console via the `https://vaultwarden.example.com` address, create your account there, and import all secrets from your previous password manager, for example from [1Password](https://bitwarden.com/help/import-from-1password/) or [Google Chrome](https://bitwarden.com/help/import-from-chrome/).

# Setup Backups
For global backups you can backup the whole Vaultwarden instance database and restore content from it.

It’s easy to setup using cron-jobs, rsync/rclone, or other similar tools, but if you are looking for ready-to-go solutions here are two most popular scripts repos:

- [https://github.com/ttionya/vaultwarden-backup](https://github.com/ttionya/vaultwarden-backup)
- [https://github.com/Bruceforce/vaultwarden-backup](https://github.com/Bruceforce/vaultwarden-backup)

Another option is to save your private vault backups from the web console – https://bitwarden.com/resources/guide-how-to-create-and-store-a-backup-of-your-bitwarden-vault/. 

Note that there are options to get all data in the plain text or encrypted. Prefer encrypted one if you store backups somewhere else.

# Security Measures
Hosting important services means you will be responsible for taking action to secure them. Here are steps that you can take to secure Bitwarden service
- Enable HTTPS only(enforced by default).
- Setup Two-factor authentication (2FA) – [https://bitwarden.com/help/setup-two-step-login-authenticator/](https://bitwarden.com/help/setup-two-step-login-authenticator/).
- VPN. Put your vault behind a private network only you and trusted users can access.
- Disable Admin Panel – [https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page](https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page).
- Disable remote access entirely. Make the server available only in your home network. Mobile applications and browser extensions can sync their data with the server once per day.
- Enable emergency access – [https://bitwarden.com/help/emergency-access/](https://bitwarden.com/help/emergency-access/).
- Disable password login, change default passwords, and disable password access to VPS.
