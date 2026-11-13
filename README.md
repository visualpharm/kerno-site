# kerno-site

Company page of Kerno S.A.S. — https://kerno.com.ar

- `site/` — static page (nginx in Docker, `Dockerfile`).
- `scripts/shots.py` — re-captures live desktop/phone screenshots of the projects into `site/shots/`.
- Hosting: Coolify on Hetzner (coolify.brieflysites.com), app `kerno-site`; deploy = push to `main` + `scripts/deploy.sh`.
- DNS: Hetzner DNS zone `kerno.com.ar` (A @, www → 159.69.191.160). Domain registered at NIC.ar to Ivan Boyko until the SAS has its own CUIT.
