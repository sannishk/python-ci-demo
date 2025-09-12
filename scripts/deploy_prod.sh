#!/usr/bin/env bash
# This script simulates deploying to a PRODUCTION environment by packaging the app.
set -euo pipefail
echo "[PROD DEPLOY] Packaging app for production..."
rm -rf build_prod && mkdir -p build_prod/app
cp -R app/*.py build_prod/app/
echo "[PROD DEPLOY] Done. (Simulated prod deploy output in build_prod/)"
