#!/usr/bin/env python3
import time
import os
import random

class VisualSliceDemo:
    def __init__(self):
        self.slices = {
            "eMBB": {
                "name": "Enhanced Mobile Broadband",
                "use_case": "4K Streaming, VR Gaming",
                "max_bw": 1000,
                "current_bw": 800,
                "latency": 10,
                "users": 2,
                "color": "\033[94m",
                "bar_char": "█"
            },
            "URLLC": {
                "name": "Ultra-Reliable Low Latency",
                "use_case": "Autonomous Cars, Surgery",
                "max_bw": 100,
                "current_bw": 80,
                "latency": 1,
                "users": 1,
                "color": "\033[91m",
                "bar_char": "█"
            },
            "mMTC": {
                "name": "Massive Machine Type Comm",
                "use_case": "IoT Sensors, Smart City",
                "max_bw": 50,
                "current_bw": 40,
                "latency": 100,
                "users": 0,
                "color": "\033[92m",
                "bar_char": "█"
            }
        }
        self.reset = "\033[0m"
    
    def clear_screen(self):
        os.system('clear')
    
    def draw_bar(self, current, maximum, width=50, color="", char="█"):
        filled = int((current / maximum) * width)
        bar = color + char * filled + self.reset + "░" * (width - filled)
        percentage = (current / maximum) * 100
        return f"{bar} {percentage:.1f}%"
    
    def display_slice(self, slice_type, data):
        print(f"\n{data['color']}{'─' * 80}{self.reset}")
        print(f"{data['color']}🔹 {slice_type}: {data['name']}{self.reset}")
        print(f"{data['color']}{'─' * 80}{self.reset}")
        print(f"   📱 Use Case: {data['use_case']}")
        print(f"   📊 Bandwidth: {data['current_bw']}/{data['max_bw']} Mbps")
        print(f"   {self.draw_bar(data['current_bw'], data['max_bw'], 50, data['color'], data['bar_char'])}")
        print(f"   ⏱️  Latency: {data['latency']}ms")
        print(f"   👥 Active Users: {data['users']}")
    
    def simulate_traffic(self, duration=15):
        for second in range(1, duration + 1):
            self.clear_screen()
            print("\n" + "═" * 80)
            print(f"🚀 5G NETWORK SLICING - LIVE MONITORING (Second {second}/{duration})")
            print("═" * 80)
            
            for slice_type, data in self.slices.items():
                variation = random.randint(-20, 30)
                new_bw = max(10, min(data['max_bw'], data['current_bw'] + variation))
                data['current_bw'] = new_bw
                if random.random() > 0.8:
                    data['users'] = max(0, data['users'] + random.choice([-1, 0, 1]))
                self.display_slice(slice_type, data)
            
            total_allocated = sum(s['current_bw'] for s in self.slices.values())
            total_users = sum(s['users'] for s in self.slices.values())
            print(f"\n{'─' * 80}")
            print(f"📊 SYSTEM STATS | Total: {total_allocated}/1150 Mbps | Users: {total_users}")
            print(f"{'─' * 80}\n")
            time.sleep(1)
        print("\n✅ Simulation Complete!\n")

def main():
    demo = VisualSliceDemo()
    print("\n" + "═" * 80)
    print("🎓 5G DYNAMIC NETWORK SLICING DEMONSTRATION")
    print("═" * 80)
    print("\nReal-time resource allocation across 3 network slices:")
    print("  • eMBB  - High-speed mobile broadband")
    print("  • URLLC - Ultra-low latency applications")
    print("  • mMTC  - Massive IoT connectivity")
    print()
    input("Press Enter to start...")
    demo.simulate_traffic(duration=15)
    print("═" * 80)
    print("📊 WebUI: http://localhost:9999 (admin/1423)")
    print("═" * 80 + "\n")

if __name__ == "__main__":
    main()
