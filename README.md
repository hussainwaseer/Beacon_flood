# Beacon Flood with Scapy

A Python script that sends fake Wi-Fi beacon frames using `scapy`, simulating multiple access points (APs) with custom SSIDs. Useful for testing, red teaming, or wireless network research.

## ⚠️ Disclaimer
This tool is for **educational and authorized testing** only. **Do not use** it on networks you don't own or have explicit permission to test.

## 🐍 Requirements
- Python 3.x  
- [`scapy`](https://pypi.org/project/scapy/)  
- A wireless adapter that supports **monitor mode**

Install dependencies:

```bash
pip install scapy
```

## 🧠 How It Works
The script crafts and sends `802.11` beacon frames with fake SSIDs to simulate access points.

## 🚀 Usage

```bash
sudo python3 beacon_flood.py <interface> <ssid-list.txt>
```

- `<interface>`: Your Wi-Fi interface in **monitor mode** (e.g., `wlan0mon`)
- `<ssid-list.txt>`: A file with one SSID per line

### Example

```bash
sudo python3 beacon_flood.py wlan0mon ssids.txt
```

## 📝 ssid-list.txt format

```
Free_WiFi
Hotel_Guest
Starbucks_AP
```

## ✍️ Author
**Coded by Kolzec,huszn**

---
> For educational use only. Use responsibly.
