#!/bin/bash
# Deploy kerno-site on Coolify (Hetzner brieflysites). Push to main first.
set -e
"$(dirname "$0")/coolify" GET "/deploy?uuid=m3icy3gi615sv5mij22cfnay&force=false"
