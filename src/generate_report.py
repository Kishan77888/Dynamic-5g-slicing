#!/usr/bin/env python3
import json
import os
from datetime import datetime

# Read the simulation data
log_file = os.path.expanduser("~/5g-slicing-project/logs/network_state_final.json")

if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        data = json.load(f)
    
    print("\n" + "="*80)
    print(" PROJECT REPORT: Dynamic 5G Network Slicing")
    print("="*80)
    
    print("\n📊 EXECUTIVE SUMMARY")
    print("-" * 80)
    stats = data['stats']
    print(f"Total System Bandwidth: {stats['total_bandwidth']} Mbps")
    print(f"Allocated Bandwidth: {stats['allocated_bandwidth']} Mbps")
    print(f"Utilization: {(stats['allocated_bandwidth']/stats['total_bandwidth']*100):.1f}%")
    print(f"Active Slices: {stats['total_slices']}")
    print(f"Connected Users: {stats['total_users']}")
    
    print("\n📡 NETWORK SLICE DETAILS")
    print("-" * 80)
    for slice_name, slice_data in data['slices'].items():
        print(f"\n{slice_name}:")
        print(f"  Type: {slice_data['type']}")
        print(f"  Bandwidth: {slice_data['allocated_bandwidth']}")
        print(f"  Latency: {slice_data['latency']}")
        print(f"  Users: {slice_data['users']}")
        print(f"  Utilization: {slice_data['utilization']}")
    
    print("\n" + "="*80 + "\n")
else:
    print("❌ No simulation data found. Run the simulation first!")
