# Dynamic 5G Network Slicing – Simulation & Demo

This repository contains my **Dynamic 5G Network Slicing** simulation project, built and tested on **Kali Linux (VMware)**.  
The project simulates 3GPP-style slices:

- **eMBB** – Enhanced Mobile Broadband (4K/8K streaming, VR gaming)
- **URLLC** – Ultra-Reliable Low Latency (autonomous cars, remote surgery)
- **mMTC** – Massive Machine Type Communications (IoT sensors, smart city)

The system shows:

- live **terminal-based visualization** of all slices  
- **dynamic bandwidth allocation every second**  
- final **JSON state export**  
- integration with **Open5GS WebUI** (subscriber view on `http://localhost:9999`)

---

## 🔧 Project structure

Main files in this repo:

```text
5g-slicing-project/
├─ README.md                # You are here 🙂
├─ README.txt               # Text version used during development
├─ src/
│  ├─ network_slicing.py    # Basic 5G slicing logic
│  ├─ advanced_slicing.py   # Dynamic allocator + logging
│  ├─ visual_demo.py        # Live visual bar-style simulation
│  └─ generate_report.py    # Uses JSON logs to prepare reports
├─ logs/
│  ├─ network_state.json        # Live simulation intermediate state
│  ├─ network_state_final.json  # Final state after simulation
│  ├─ slice_data.json           # Slice configuration & summary
│  └─ webui.log                 # WebUI related logs
├─ start.sh                 # Start complete 5G slicing environment
├─ startup.sh               # Helper for environment startup (used by aliases)
├─ stop.sh                  # Stop services
├─ shutdown.sh              # Full shutdown helper
├─ demo.sh                  # Short demo run (10-second dynamic simulation)
└─ teacher_demo.sh          # Full presentation demo (for viva / review)
