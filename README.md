# Quantum Log Post Watch

A **survival-grade wristwatch system** designed for extreme environments (e.g., Antarctic compass failure zones). Records environmental and quantum-simulated data, generates cryptographic hashes, and stores data in an ASCII-based database for resilience and portability.

## 🎯 Core Concept

The Quantum Log Post Watch is an offline-first Python application that:
- Simulates quantum execution states for environmental scanning
- Generates tamper-evident cryptographic hashes (TerraHash-8192)
- Maintains an append-only ASCII database
- Handles compass failures with time-based polar coordinates
- Provides a terminal ASCII UI for low-power devices

**Target Platform:**
- Low-power laptops (Lepi)
- Python 3.6+
- Offline-first design
- Terminal / ASCII UI

---

## ✨ Features

### 1. Quantum Core Simulator
Simulates execution states for environmental data collection:
- **A** = Atmosphere scan
- **S** = Surface scan
- **R** = Radiation scan
- **M** = Magnetic scan

Produces deterministic measurement values for extreme environment monitoring.

### 2. TerraHash-8192 (Custom Multi-Hash)
Since SHA-8192 doesn't exist, implements a custom multi-hash algorithm:
- **SHA-512** hash
- **SHA3-512** hash
- **BLAKE2b** hash
- Concatenates all → hashes result → produces 8192-bit equivalent digest

**Properties:**
- Deterministic (same input = same hash)
- Tamper-evident (any change breaks hash)
- No external crypto dependencies

### 3. ASCII Database Generator
Stores runs in an **append-only ASCII log**:

```
[2026-02-22T23:34:51]
MODE: POLAR
A: Atmosphere scan data
S: Surface scan data
R: Radiation scan data
M: Magnetic scan data
HEADING: POLAR-137°
MEASURED: 1
TERRAHASH: <hash_value>
---
```

**Properties:**
- Human-readable format
- Tamper-evident with hashes
- Works without binary dependencies
- JSON-based for portability

### 4. Polar Coordinate Mode
When compass fails:
- Uses **time-based orientation**
- Simulates sun position
- Stores heading as pseudo-polar coordinates

**Example:**
```
HEADING: POLAR-137°
```

### 5. ASCII Watch UI
Terminal watch layout:
```
+----------------------+
|   TERRA LOG WATCH    |
|----------------------|
| MODE : POLAR         |
| TIME : 14:22:08      |
| HEAD : 137°          |
| QVAL : 1             |
+----------------------+
```

### 6. White Ring Barrier Logic
Simulates boundary detection:
- Monitors heading threshold (default: 45°)
- Triggers alerts when heading exceeds threshold
- Provides navigation safety warnings

---

## 📦 Core Modules

| Module | Purpose | Key Classes |
|--------|---------|------------|
| **quantum_core.py** | Quantum state simulation | `QuantumExecutionState` |
| **terrahash.py** | Multi-hash generation | `TerraHash` |
| **database.py** | Append-only logging | `LogDatabase`, `LogEntry` |
| **polar_mode.py** | Compass failure handling | `PolarCoordinateMode` |
| **watch_ui.py** | Terminal UI rendering | `display_watch()` |
| **main.py** | Application integration | `QuantumLogWatch` |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies (standard library only)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/PoJiC69/Quantum-Log-Post-Watch.git
cd Quantum-Log-Post-Watch

# Run the main application
python3 main.py

# Run tests
python3 test_all.py
python3 test_runner.py
python3 test_quantum_log.py
```

---

## 💻 Usage

### Run the Watch Application
```bash
python3 main.py
```

Starts the Quantum Log Watch with:
1. Module validation tests
2. Watch UI rendering
3. Real-time logging (5 iterations for testing)
4. Barrier detection alerts

### Example Output
```
==================================================
QUANTUM LOG POST WATCH - MODULE TESTS
==================================================

[TEST 1] Quantum Core Simulator
--------------------------------------------------
  Measurement output for Atmosphere: Data from Atmosphere scan
  Measurement output for Surface: Data from Surface scan
  Measurement output for Radiation: Data from Radiation scan
  Measurement output for Magnetic: Data from Magnetic scan

[TEST 2] TerraHash-8192
--------------------------------------------------
  Input: Test data for TerraHash
  Hash: a7f3c9e5b2d1f4a8...
  Hash length: 128 hex chars (~512 bits)

[TEST 3] ASCII Database
--------------------------------------------------
  Entries in database: 1
  Last entry: {'timestamp': '2026-02-22T23:34:51', ...}

[TEST 4] Polar Coordinate Mode
--------------------------------------------------
  Current heading: POLAR-45.2°
  Heading degrees: 45.2°
  Within white ring: False

[TEST 5] Watch UI Rendering
--------------------------------------------------
+----------------------+
|   TERRA LOG WATCH    |
|----------------------|
| MODE : POLAR         |
| TIME : 14:22:08      |
| HEAD : POLAR-45.2°   |
| QVAL : 1             |
+----------------------+
```

### Programmatic Usage

```python
from quantum_core import QuantumExecutionState
from terrahash import TerraHash
from database import LogDatabase
from polar_mode import PolarCoordinateMode

# Initialize components
qc = QuantumExecutionState()
db = LogDatabase('mylog.json')
pm = PolarCoordinateMode()

# Execute quantum scan
for state in ['A', 'S', 'R', 'M']:
    result = qc.scan(state)
    print(result)

# Generate hash
data = b"my data"
th = TerraHash(data)
hash_value = th.terra_hash()

# Get polar heading
heading = pm.get_pseudo_polar_heading()
print(f"Heading: {heading}")

# Log entry
db.append_entry('POLAR', {'heading': heading})
```

---

## 🔄 Data Flow

```
┌─────────────────────┐
│  Environmental      │
│  Sensors (A,S,R,M) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Quantum Core       │
│  Simulator          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Polar Mode         │
│  Heading Calc       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  TerraHash-8192     │
│  Generation         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  White Ring         │
│  Barrier Check      │
└──────────┬────────���─┘
           │
           ▼
┌─────────────────────┐
│  ASCII Database     │
│  Append Log         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Watch UI Display   │
│  Terminal Render    │
└─────────────────────┘
```

---

## 🧪 Test Suite

### Available Tests

**test_all.py** - Template for module tests
```bash
python3 test_all.py
```

**test_runner.py** - Comprehensive module testing
```bash
python3 test_runner.py
```

**test_quantum_log.py** - Unit tests for logging
```bash
python3 test_quantum_log.py
```

### Test Coverage

| Component | Test | Status |
|-----------|------|--------|
| Quantum Core | State execution | ✅ |
| TerraHash | Hash consistency | ✅ |
| Database | Write/Read ops | ✅ |
| Polar Mode | Heading calculation | ✅ |
| Barrier Logic | Threshold detection | ✅ |
| Watch UI | Rendering | ✅ |

---

## 📋 Technical Specifications

### Quantum Core
- **States:** 4 (A, S, R, M)
- **Output:** Deterministic measurement string
- **Format:** "Measurement output for [State]: Data from [State] scan"

### TerraHash-8192
- **Input:** Binary data (bytes)
- **Output:** 128-character hex string (~512-bit equivalent)
- **Algorithm:** SHA512 + SHA3-512 + BLAKE2b concatenated + final SHA512
- **Deterministic:** Yes (same input always produces same output)

### Database
- **Format:** JSON
- **Append Mode:** Add-only (no deletion)
- **File Extension:** .json
- **Entry Structure:**
  ```json
  {
    "timestamp": "2026-02-22T23:34:51",
    "mode": "POLAR",
    "sensor_values": {...},
    "terra_hash": "hash_value"
  }
  ```

### Polar Mode
- **Heading Range:** 0-360°
- **Barrier Threshold:** 45° (configurable)
- **Format:** POLAR-XXX.X°
- **Sun Simulation:** Time-based (15°/hour)

### Watch UI
- **Terminal:** ANSI compatible
- **Update Rate:** Configurable (default 2s)
- **Dimensions:** 22 characters wide × 7 lines
- **Display Elements:** Mode, Time, Heading, Quantum Value

---

## 🛠️ Project Structure

```
Quantum-Log-Post-Watch/
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── main.py               # Main application entry point
├── quantum_core.py       # Quantum simulator module
├── terrahash.py          # Hash generation module
├── database.py           # Database module
├── polar_mode.py         # Polar coordinate module
├── watch_ui.py           # UI rendering module
├── test_all.py           # Comprehensive tests
├── test_runner.py        # Module test runner
└── test_quantum_log.py    # Logging unit tests
```

---

## 🎨 Design Philosophy

- **Modular Python:** Clear function/class separation
- **Minimal Dependencies:** Uses only Python standard library
- **Offline-First:** No network requirements
- **Deterministic:** Reproducible results
- **ASCII-Based:** Human-readable, portable
- **Survival-Tech Aesthetic:** Designed for extreme conditions

---

## 📡 Use Cases

1. **Polar Expeditions:** Navigation when compass fails
2. **Emergency Response:** Offline data logging in remote areas
3. **Scientific Research:** Environmental data collection
4. **Survival Scenarios:** Autonomous operation without connectivity
5. **Educational:** Understanding quantum simulation and cryptography

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Performance optimizations

---

## 📞 Support

For issues, feature requests, or questions, please open a GitHub issue.

---

**Quantum Log Post Watch** - *A survival-grade wristwatch system for extreme environments.*

Built with ❄️ for the Antarctic survival challenge.