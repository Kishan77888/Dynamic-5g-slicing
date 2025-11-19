#!/bin/bash

clear
echo ""
echo "════════════════════════════════════════════════════════════════════════════"
echo "  🎓 5G NETWORK SLICING DEMONSTRATION"
echo "  Dynamic Resource Allocation for eMBB, URLLC, and mMTC"
echo "════════════════════════════════════════════════════════════════════════════"
echo ""
read -p "Press Enter to start demonstration..."

# Demo 1: Show all slices
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  📡 PART 1: Network Slice Types"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "🔹 eMBB (Enhanced Mobile Broadband)"
echo "   Use Case: 4K Video Streaming, VR/AR Gaming"
echo "   Bandwidth: 1000 Mbps (High)"
echo "   Latency: 10ms (Moderate)"
echo "   Priority: Throughput"
echo ""
sleep 3

echo "🔹 URLLC (Ultra-Reliable Low Latency Communications)"
echo "   Use Case: Autonomous Vehicles, Remote Surgery, Industrial Automation"
echo "   Bandwidth: 100 Mbps (Medium)"
echo "   Latency: 1ms (Ultra-Low)"
echo "   Priority: Reliability & Low Latency"
echo ""
sleep 3

echo "🔹 mMTC (Massive Machine Type Communications)"
echo "   Use Case: IoT Sensors, Smart City, Agriculture Monitoring"
echo "   Bandwidth: 50 Mbps (Low)"
echo "   Latency: 100ms (High tolerance)"
echo "   Priority: Massive connectivity"
echo ""
sleep 3

read -p "Press Enter to see dynamic resource allocation..."

# Demo 2: Run the simulation
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  🔄 PART 2: Dynamic Resource Allocation in Action"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

python3 ~/5g-slicing-project/src/advanced_slicing.py

read -p "Press Enter to view saved data..."

# Demo 3: Show the data
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  📊 PART 3: Network State Data (JSON Format)"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

python3 -m json.tool ~/5g-slicing-project/logs/network_state_final.json

echo ""
read -p "Press Enter to see WebUI instructions..."

# Demo 4: WebUI
clear
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  🌐 PART 4: Open5GS WebUI Management"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "  Browser URL: http://localhost:9999"
echo "  Username: admin"
echo "  Password: 1423"
echo ""
echo "  📋 What to Show in WebUI:"
echo "  ✅ 1. Subscriber Management (Add/Edit/Delete UEs)"
echo "  ✅ 2. Network Slicing Configuration"
echo "  ✅ 3. QoS Policy Settings"
echo "  ✅ 4. Real-time subscriber database"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "  ✅ DEMONSTRATION COMPLETE!"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
