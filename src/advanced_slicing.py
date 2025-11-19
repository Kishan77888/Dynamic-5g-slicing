#!/usr/bin/env python3
import json
import os
import time
import random
from datetime import datetime
from typing import Dict

class NetworkSlice:
    def __init__(self, name: str, slice_type: str, max_bandwidth: int, latency: int):
        self.name = name
        self.type = slice_type
        self.max_bandwidth = max_bandwidth
        self.latency = latency
        self.allocated_bandwidth = 0
        self.users = []
        self.created_at = datetime.now()
    
    def allocate(self, bandwidth: int) -> bool:
        if bandwidth <= self.max_bandwidth:
            self.allocated_bandwidth = bandwidth
            return True
        return False
    
    def add_user(self, user_id: str):
        if user_id not in self.users:
            self.users.append(user_id)
            return True
        return False
    
    def get_utilization(self) -> float:
        if self.max_bandwidth > 0:
            return (self.allocated_bandwidth / self.max_bandwidth) * 100
        return 0.0
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'type': self.type,
            'max_bandwidth': f"{self.max_bandwidth}Mbps",
            'allocated_bandwidth': f"{self.allocated_bandwidth}Mbps",
            'latency': f"{self.latency}ms",
            'users': len(self.users),
            'utilization': f"{self.get_utilization():.1f}%",
            'active_users': self.users
        }

class SliceOrchestrator:
    def __init__(self, total_bandwidth: int = 1150):
        self.total_bandwidth = total_bandwidth
        self.slices: Dict[str, NetworkSlice] = {}
        self.available_bandwidth = total_bandwidth
    
    def create_slice(self, slice_id: str, name: str, slice_type: str, 
                     max_bandwidth: int, latency: int) -> bool:
        if slice_id in self.slices:
            return False
        slice_obj = NetworkSlice(name, slice_type, max_bandwidth, latency)
        self.slices[slice_id] = slice_obj
        print(f"✅ Created slice: {name} ({slice_type})")
        return True
    
    def allocate_dynamic(self, slice_id: str, demand: int) -> bool:
        if slice_id not in self.slices:
            return False
        slice_obj = self.slices[slice_id]
        old_alloc = slice_obj.allocated_bandwidth
        if slice_obj.allocate(demand):
            bandwidth_change = demand - old_alloc
            self.available_bandwidth -= bandwidth_change
            print(f"🔄 Dynamic allocation: {slice_id} -> {demand}Mbps")
            return True
        return False
    
    def get_stats(self) -> Dict:
        total_allocated = sum(s.allocated_bandwidth for s in self.slices.values())
        total_users = sum(len(s.users) for s in self.slices.values())
        return {
            'total_bandwidth': self.total_bandwidth,
            'allocated_bandwidth': total_allocated,
            'available_bandwidth': self.available_bandwidth,
            'total_slices': len(self.slices),
            'total_users': total_users,
            'timestamp': datetime.now().isoformat()
        }
    
    def save_state(self, filename: str):
        log_dir = os.path.expanduser("~/5g-slicing-project/logs")
        os.makedirs(log_dir, exist_ok=True)
        filepath = os.path.join(log_dir, filename)
        data = {
            'stats': self.get_stats(),
            'slices': {sid: s.to_dict() for sid, s in self.slices.items()}
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return filepath

def simulate_traffic(orchestrator: SliceOrchestrator, duration: int = 10):
    print(f"\n🔄 Simulating dynamic traffic for {duration} seconds...\n")
    for i in range(duration):
        print(f"⏱️  Second {i+1}/{duration}")
        for slice_id, slice_obj in orchestrator.slices.items():
            base = slice_obj.allocated_bandwidth
            variation = random.randint(-20, 50)
            new_demand = max(0, min(slice_obj.max_bandwidth, base + variation))
            if new_demand != base:
                orchestrator.allocate_dynamic(slice_id, new_demand)
        time.sleep(1)
    print("\n✅ Simulation complete!\n")

def main():
    print("\n" + "="*80)
    print(" 🚀 ADVANCED DYNAMIC 5G NETWORK SLICING SYSTEM")
    print("="*80 + "\n")
    
    orchestrator = SliceOrchestrator(total_bandwidth=1150)
    
    print("📡 Creating Network Slices...\n")
    orchestrator.create_slice("embb_1", "Enhanced Mobile Broadband", "eMBB", 1000, 10)
    orchestrator.create_slice("urllc_1", "Ultra-Reliable Low Latency", "URLLC", 100, 1)
    orchestrator.create_slice("mmtc_1", "Massive Machine Type Communications", "mMTC", 50, 100)
    
    print("\n💾 Initial Resource Allocation...\n")
    orchestrator.allocate_dynamic("embb_1", 800)
    orchestrator.allocate_dynamic("urllc_1", 80)
    orchestrator.allocate_dynamic("mmtc_1", 40)
    
    print("\n👥 Adding Users...\n")
    orchestrator.slices["embb_1"].add_user("UE_001")
    orchestrator.slices["embb_1"].add_user("UE_002")
    orchestrator.slices["urllc_1"].add_user("UE_003")
    print("✅ Users added\n")
    
    print("="*80)
    print("📊 CURRENT NETWORK STATE")
    print("="*80 + "\n")
    
    for slice_id, slice_obj in orchestrator.slices.items():
        print(f"🔹 {slice_obj.name}")
        print(f"   Type: {slice_obj.type}")
        print(f"   Max Bandwidth: {slice_obj.max_bandwidth}Mbps")
        print(f"   Allocated: {slice_obj.allocated_bandwidth}Mbps ({slice_obj.get_utilization():.1f}%)")
        print(f"   Latency: {slice_obj.latency}ms")
        print(f"   Active Users: {len(slice_obj.users)}")
        print()
    
    stats = orchestrator.get_stats()
    print("="*80)
    print("📈 SYSTEM STATISTICS")
    print("="*80)
    print(f"Total Bandwidth: {stats['total_bandwidth']}Mbps")
    print(f"Allocated: {stats['allocated_bandwidth']}Mbps")
    print(f"Available: {stats['available_bandwidth']}Mbps")
    print(f"Active Slices: {stats['total_slices']}")
    print(f"Connected Users: {stats['total_users']}")
    print("="*80 + "\n")
    
    filepath = orchestrator.save_state("network_state.json")
    print(f"💾 State saved to: {filepath}\n")
    
    simulate_traffic(orchestrator, duration=10)
    
    filepath = orchestrator.save_state("network_state_final.json")
    print(f"💾 Final state saved to: {filepath}\n")
    
    print("="*80)
    print("✅ 5G Network Slicing System Running Successfully!")
    print("🌐 WebUI: http://localhost:9999 (admin/1423)")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
