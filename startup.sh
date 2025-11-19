#!/bin/bash
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  🚀 Starting Complete 5G Network Slicing Environment"
echo "════════════════════════════════════════════════════════════════════"
echo ""
pkill -f "npm run dev" 2>/dev/null
pkill -f "node server" 2>/dev/null
sleep 2
echo "📦 Starting MongoDB..."
sudo systemctl start mongodb
sleep 3
if sudo systemctl is-active --quiet mongodb; then
    echo "   ✅ MongoDB is running"
else
    echo "   ❌ MongoDB failed"
    exit 1
fi
echo "🌐 Starting WebUI..."
cd ~/open5gs/webui
npm run dev > ~/5g-slicing-project/logs/webui.log 2>&1 &
WEBUI_PID=$!
echo "⏳ Waiting for WebUI..."
for i in {1..30}; do
    if grep -q "Ready on" ~/5g-slicing-project/logs/webui.log 2>/dev/null; then
        echo "   ✅ WebUI ready!"
        break
    fi
    sleep 1
    echo -n "."
done
echo ""
sleep 2
echo "🌐 Opening browser..."
if command -v firefox &> /dev/null; then
    firefox http://localhost:9999 &
else
    xdg-open http://localhost:9999 &
fi
echo ""
python3 ~/5g-slicing-project/src/network_slicing.py
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  ✅ EVERYTHING IS RUNNING!"
echo "════════════════════════════════════════════════════════════════════"
echo "  🌐 WebUI: http://localhost:9999 (admin/1423)"
echo "  🎓 Demo: demo5g"
echo "  🛑 Stop: stop5g"
echo "════════════════════════════════════════════════════════════════════"
echo ""
