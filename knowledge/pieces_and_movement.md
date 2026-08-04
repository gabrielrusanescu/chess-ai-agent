# Chess Pieces and Movement Mechanics

Each player starts the game with 16 pieces: 1 King, 1 Queen, 2 Rooks, 2 Bishops, 2 Knights, and 8 Pawns.

---

## Standard Piece Values

While piece values are dynamic depending on the exact position, standard point values provide a useful baseline:

| Piece | Symbol | Point Value | Relative Strength |
| :--- | :---: | :---: | :--- |
| **Pawn** | P | 1 | Base unit of value; controls key squares and structure |
| **Knight** | N | 3 | Minor piece; unique jumping ability, effective in closed positions |
| **Bishop** | B | 3 | Minor piece; long-range diagonal sniper, strong in open positions |
| **Rook** | R | 5 | Major piece; powerful on open files and 7th/8th ranks |
| **Queen** | Q | 9 | Major piece; most versatile and powerful attacking unit |
| **King** | K | Infinite | Game-critical; must be defended in middle game, active attacker in endgame |

---

## Detailed Piece Movement and Characteristics

### 1. Pawn (P)
- **Movement**: Advances forward one square per turn. On its initial move from the 2nd (or 7th) rank, it can advance one or two squares forward.
- **Capture**: Captures diagonally forward one square (left or right).
- **Special Moves**: En passant capture and promotion upon reaching the final rank.
- **Strategic Note**: Pawns cannot move backward. Pawn pushes create permanent weaknesses or outposts on the board.

### 2. Knight (N)
- **Movement**: Moves in an "L-shape": two squares vertically and one horizontally, or two squares horizontally and one vertically.
- **Jumping Ability**: The Knight is the **only piece** that can leap over other pieces (both friendly and opponent).
- **Control**: Controls up to 8 squares when centralized, but only 2 squares from a corner ("A knight on the rim is dim").
- **Strategic Note**: Excels in closed positions with locked pawns and on central outpost squares.

### 3. Bishop (B)
- **Movement**: Moves any number of vacant squares diagonally.
- **Color Bound**: Each player starts with one Light-Squared Bishop and one Dark-Squared Bishop. A Bishop can never change square colors throughout the game.
- **Bishop Pair**: Having both bishops in an open position is a substantial positional advantage.

### 4. Rook (R)
- **Movement**: Moves any number of vacant squares horizontally or vertically along ranks and files.
- **Deployment**: Rooks excel when placed on **open files** (files with no pawns) or **semi-open files** (files with only enemy pawns).
- **7th Rank Penetration**: Placing a Rook on the 7th rank (2nd rank for Black) cuts off the enemy King and attacks opponent pawns from behind.

### 5. Queen (Q)
- **Movement**: Combines the power of a Rook and a Bishop. Moves any number of vacant squares horizontally, vertically, or diagonally.
- **Usage**: Outstanding at coordinating attacks, delivering tactical combinations, and creating double attacks.
- **Caution**: Avoid bringing the Queen out too early in the opening, as opponent minor pieces can attack it while developing their own forces.

### 6. King (K)
- **Movement**: Moves one square in any direction (horizontally, vertically, or diagonally).
- **Safety**: In the opening and middlegame, King safety is paramount (typically secured via castling behind a pawn shield).
- **Endgame Role**: In the endgame when major attacking threats are off the board, the King becomes an active, offensive piece vital for supporting pawn pushes and controlling key squares.
