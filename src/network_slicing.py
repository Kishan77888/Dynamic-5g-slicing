#!/usr/bin/env python3
import json
import os
from datetime import datetime

class Slice:
    def __init__(self, name, stype, bw, lat):
        self.name = name
        self.type = stype
        self.bandwidth = bw
        self.latency = lat
        self.allocated = 0
        self.users = []
    
    def allocate(self, amount):
        self.allocated = amount
        return f"Allocated {amount}Mbps to {self.name}"
    
    def add_user(self, user_id):
        self.users.append(user_id)
        return f"User {user_id} connected to {self.name}"

def main():
    print("\n" + "="*70)
    print(" 🚀 DYNAMIC 5G NETWORK SLICING PROJECT")
    print("="*70 + "\n")
    
    slices = {
        "eMBB": Slice("Enhanced Mobile Broadband", "eMBB", "1000Mbps", "10ms"),
        "URLLC": Slice("Ultra-Reliable Low Latency", "URLLC", "100Mbps", "1ms"),
        "mMTC": Slice("Massive Machine Type Comm", "mMTC", "50Mbps", "100ms")
    }
    
    slices["eMBB"].allocate(800)
    slices["URLLC"].allocate(80)
    slices["mMTC"].allocate(40)
    
    slices["eMBB"].add_user("UE_001")
    slices["eMBB"].add_user("UE_002")
    slices["URLLC"].add_user("UE_003")
    
    for name, s in slices.items():
        print(f"🔹 {s.name}")
        print(f"   Type: {s.type}")
        print(f"   Max Bandwidth: {s.bandwidth}")
        print(f"   Latency: {s.latency}")
        print(f"   Allocated: {s.allocated}Mbps")
        print(f"   Active Users: {len(s.users)}")
        print()
    
    print("="*70)
    print("✅ Network Slicing Active!")
    print("🌐 WebUI: http://localhost:9999 (admin/1423)")
    print("="*70 + "\n")
    
    log_dir = os.path.expanduser("~/5g-slicing-project/logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "slice_data.json")
    
    with open(log_file, "w") as f:
        data = {name: {
            "type": s.type,
            "bandwidth": s.bandwidth,
            "latency": s.latency,
            "allocated": s.allocated,
            "users": len(s.users),
            "timestamp": datetime.now().isoformat()
        } for name, s in slices.items()}
        json.dump(data, f, indent=2)
    
    print(f"📁 Data saved to: {log_file}\n")

if __name__ == "__main__":
    main()
