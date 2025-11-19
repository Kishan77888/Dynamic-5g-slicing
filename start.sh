#!/bin/bash
echo "🚀 Starting 5G Environment..."
sudo systemctl start mongodb
cd ~/open5gs/webui
npm run dev > /dev/null 2>&1 &
sleep 5
echo "✅ Started!"
echo "🌐 WebUI: http://localhost:3000"
echo "   Login: admin / 1423"
