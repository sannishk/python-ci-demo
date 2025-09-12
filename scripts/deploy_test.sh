#!/usr/bin/env bash
# This script simulates deploying to a TEST environment by packaging the app.
set -euo pipefail
echo "[TEST DEPLOY] Packaging app for test environment..."
rm -rf build_test && mkdir -p build_test/app
cp -R app/*.py build_test/app/
echo "[TEST DEPLOY] Done. (Simulated test deploy output in build_test/)"
