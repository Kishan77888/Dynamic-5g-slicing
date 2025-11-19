#!/bin/bash
echo "🛑 Stopping..."
sudo pkill -f "npm run dev"
sudo systemctl stop mongodb
echo "✅ Stopped!"
