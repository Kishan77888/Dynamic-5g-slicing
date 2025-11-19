#!/bin/bash
clear
echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo "  🎓 5G NETWORK SLICING - TEACHER DEMONSTRATION"
echo "════════════════════════════════════════════════════════════════════════════"
echo ""
read -p "Press Enter to begin..."
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  📡 PART 1: Network Slice Types"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "🔹 eMBB (Enhanced Mobile Broadband)"
echo "   Use Case: 4K/8K Streaming, VR, AR Gaming"
echo "   Bandwidth: 1000 Mbps | Latency: 10ms"
echo ""
sleep 3
echo "🔹 URLLC (Ultra-Reliable Low Latency)"
echo "   Use Case: Autonomous Vehicles, Remote Surgery"
echo "   Bandwidth: 100 Mbps | Latency: 1ms"
echo ""
sleep 3
echo "🔹 mMTC (Massive Machine Type Communications)"
echo "   Use Case: IoT Sensors, Smart City"
echo "   Bandwidth: 50 Mbps | Latency: 100ms"
echo ""
sleep 3
read -p "Press Enter for LIVE VISUAL SIMULATION..."
python3 ~/5g-slicing-project/src/visual_demo.py
read -p "Press Enter for DETAILED SIMULATION..."
python3 ~/5g-slicing-project/src/advanced_slicing.py
read -p "Press Enter to view JSON DATA..."
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  📊 Network State Data (JSON)"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
if [ -f ~/5g-slicing-project/logs/network_state_final.json ]; then
    python3 -m json.tool ~/5g-slicing-project/logs/network_state_final.json
fi
echo ""
read -p "Press Enter for WEBUI GUIDE..."
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  🌐 WebUI Management Interface"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "  URL: http://localhost:9999"
echo "  Username: admin | Password: 1423"
echo ""
echo "  What to Demonstrate:"
echo "  1️⃣  Add Subscriber (IMSI: 999700000000001)"
echo "  2️⃣  Network Slicing (SST 1=eMBB, 2=URLLC, 3=mMTC)"
echo "  3️⃣  QoS Policies"
echo "  4️⃣  Real-time Database"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  ✅ DEMONSTRATION COMPLETE!"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
