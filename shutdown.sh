#!/bin/bash
echo ""
echo "🛑 Stopping 5G Network Slicing Environment..."
echo ""
pkill -f "npm run dev"
pkill -f "node server"
sudo systemctl stop mongodb
echo ""
echo "✅ Everything stopped!"
echo ""
