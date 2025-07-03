
<h1 align="center">🔁 Return/Exchange Cycle Detector</h1>

<p align="center">
  <b>Detect potential frauds in product return/exchange using graph cycle detection</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Graph-Theory-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Fraud--Detection-red?style=flat-square" />
</p>

---

## 🧠 Project Overview

This project helps in detecting **fraudulent return/exchange cycles** in product transactions using **graph cycle detection**. Each return or exchange is treated as a directed edge in a graph. If a cycle is found, it indicates a suspicious loop (Product A → B → C → A), suggesting potential fraud.

---

## 📌 Key Features

- ✅ Simple command-line interface
- 🔁 Detects cycles in product return/exchange data
- 🔐 Identifies potential fraud based on cyclic patterns
- 🧮 Uses DFS (Depth-First Search) for cycle detection

---

## ⚙️ How It Works

1. Each product is treated as a node.
2. Each return/exchange is treated as a directed edge.
3. The algorithm checks if there is a cycle in the graph:
   - **Cycle = Fraud**
   - **No Cycle = Safe**

---

## 🚀 Usage

### 💻 Run the Program

```bash
python return_exchange_cycle_detector.py
```

### 📝 Sample Input

```
Enter number of transactions (return/exchange records):
4
Enter each transaction in the format 'ProductA ProductB' (ProductA returned for ProductB):
A B
B C
C D
D A
```

### 📤 Sample Output

```
Cycle detected! Potential fraud in return/exchange patterns.
```

---

## 🧪 Tech Stack

| Tool      | Description                   |
|-----------|-------------------------------|
| Python 🐍 | Core Programming Language     |
| DFS       | Algorithm used for detection |
| OOP       | Object-Oriented Programming   |

---

## 📂 File Structure

```
📁 return-exchange-detector/
├── return_exchange_cycle_detector.py
└── README.md
```

---

## 🧑‍💻 Made By

**Arpan Mukherjee**

> Passionate about building intelligent systems that make real-world decisions smarter and safer.

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

⭐️ If you found this project helpful, consider starring it on GitHub!
