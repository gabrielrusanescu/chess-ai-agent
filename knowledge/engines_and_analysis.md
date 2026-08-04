# Chess Engines and Computer Analysis

Modern chess engines are far stronger than any human player, with top engines exceeding Elo ratings of 3500+.

---

## Leading Chess Engines

1. **Stockfish**: Free, open-source, powerful engine that combines brute-force search with NNUE (Efficiently Updatable Neural Network) evaluation.
2. **Leela Chess Zero (LCZero / Lc0)**: Open-source neural network engine modeled after DeepMind's AlphaZero architecture. Uses Monte Carlo Tree Search (MCTS) and neural evaluation.
3. **Komodo Dragon**: Commercial chess engine utilizing MCTS alongside neural network evaluations.

---

## Understanding Engine Evaluations

Engines output positional evaluations using numeric scores:

### 1. Centipawn Scores
- **100 centipawns = 1 Pawn unit**.
- **`+1.00`**: White is ahead by the equivalent of one pawn.
- **`-0.50`**: Black is ahead by half a pawn equivalent.
- **`0.00`**: The position is completely balanced (equal chances).
- **`+3.00`**: White has a winning advantage (equivalent to a minor piece up).
- **`+9.00`**: White has a decisive advantage (equivalent to a Queen up).

### 2. Mate Scores
- Displayed as **`#N`** or **`M N`**.
- Example: **`#5`** means White can force checkmate in 5 moves.
- Example: **`- #3`** means Black can force checkmate in 3 moves.

---

## Engine Search Algorithms

- **Alpha-Beta Pruning**: A search algorithm that cuts off branches of the move tree that are proven inferior to previously evaluated moves, allowing deeper calculation.
- **NNUE (Efficiently Updatable Neural Network)**: Evaluates leaf nodes of a search tree rapidly on standard CPUs without requiring expensive GPU hardware.
- **Monte Carlo Tree Search (MCTS)**: Evaluates moves by simulating many probabilistic game continuations, used extensively in deep learning engines like Lc0.

---

## Best Practices for Computer Analysis

1. **Do Not Rely Solely on Engine Scores**: Try to analyze positions on your own before turning on engine evaluations.
2. **Identify Missed Tactics**: Use engines post-game to spot blunders (`??`), mistakes (`?`), or missed wins (`!`).
3. **Understand the "Why"**: If an engine recommends an unexpected move, step through the principal variation (PV) line to see what tactic or positional threat the engine is anticipating.
4. **Opening Novelties**: Engines help test opening preparation against potential opponent responses.
