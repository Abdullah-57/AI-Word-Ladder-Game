# Word Ladder Adventure Game

This repository contains the implementation of the **Word Ladder Adventure Game**. The game is an interactive puzzle where players transform a starting word into a target word by changing one letter at a time, with AI-powered hints using search algorithms (BFS, UCS, A\*) to find the shortest path.

---

## 🌐 Project Overview

**Objective**: Create an interactive word ladder puzzle game that uses AI-driven search algorithms to provide hints, supports various difficulty modes, and ensures an engaging user experience through a console-based UI.

---

## 🎯 Game Mechanics

### Word Selection

- The game randomly selects a valid starting word based on the chosen difficulty level.
- A target word is chosen, ensuring a valid transformation path exists between the start and target.

### Gameplay Features

🔹 **Manual Changes**: Players change one letter at a time to form valid words from a predefined dictionary.\
🔹 **AI Assistance**: Hints provided via BFS, UCS, or A\* search algorithms to suggest the next word or path.\
🔹 **Challenge Mode**: Includes banned words, restricted letters, turn limits, and hint limits.\
🔹 **Graph Visualization**: Players can view the word dictionary as a graph.\
🔹 **Difficulty Levels**: Vary in word length, constraints, and limits on turns/hints.

### Scoring System

- Score calculated based on turns taken and hints used—fewer turns/hints yield higher scores.
- Real-time statistics and instructions displayed in a formatted console UI.

---

## 🔍 Comparison of Implemented Search Algorithms

### Breadth-First Search (BFS)

🔹 Explores words level by level in an unweighted graph.\
🔹 Guarantees the shortest path but may explore unnecessary branches.

### Uniform Cost Search (UCS)

🔹 Prioritizes nodes by cumulative cost, ideal for weighted transformations.\
🔹 Ensures lowest-cost path but slower for uniform costs compared to BFS.

### A\* Search

🔹 Combines UCS with a heuristic (e.g., letter differences) for efficient pathfinding.\
🔹 Most optimal for large graphs, balancing exploration and goal proximity.

---

## ⚠️ Challenges Faced During Development

### API Dependency and Performance Issues

🔹 Initial use of a dictionary API caused delays; switched to a local text file for validation.\
🔹 Managed large datasets to maintain efficient searches.

### AI Algorithm Optimization

🔹 Early versions of BFS, UCS, and A\* were slow for longer words.\
🔹 Optimized by restricting search space and refining heuristics.

### User Interface Design

🔹 Designed a clean, color-coded console UI for engagement.\
🔹 Ensured real-time updates without overwhelming the display.

### Ensuring Valid Transformation Paths

🔹 Validated word pairs to guarantee solvable puzzles.\
🔹 Implemented continuous searching for valid pairs to avoid game termination.

---

## 🏁 Conclusion

The Word Ladder Adventure Game effectively integrates graph-based AI search techniques into an educational and fun puzzle. With optimized algorithms, varied difficulty levels, and a user-friendly console interface, it provides insights into search strategies while ensuring an engaging player experience.

---

## 📁 Project Structure

```plaintext
.
├── src/                    # Source code for game logic
│   ├── main.py            # Entry point for the game
│   ├── algorithms.py      # Implementations of BFS, UCS, A*
│   ├── game.py            # Core game mechanics and UI
│   └── utils.py           # Utility functions (dictionary loading, validation)
├── data/                   # Data files
│   └── dictionary.txt     # Local word dictionary
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 🛠️ Installation

### Prerequisites

🔹 **Python**: v3.8 or later

### Setup

- **Clone the Repository**:

  ```bash
  git clone https://github.com/username/word-ladder-game.git
  cd word-ladder-game
  ```

- **Install Dependencies**:

  ```bash
  pip install -r requirements.txt
  ```

- **Run the Game**:

  ```bash
  python src/main.py
  ```

---

## 📖 Usage

- Launch the game and select a difficulty level.
- Follow console prompts to make word changes or request AI hints.
- Visualize the graph or check scores at any time.

---

## 👨‍💻 Contributors
- **Abdullah Daoud (22I-2626)**  
- **Zaid Masood (22I-8793)**  

---

## ⚖️ License
This project is for **academic and personal skill development purposes only**.  
Reuse is allowed for **learning and research** with proper credit.

---
