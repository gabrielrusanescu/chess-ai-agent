# Chess Rules and Board Setup

## Board Setup

Chess is played on an 8x8 grid consisting of 64 squares of alternating colors (light and dark).

- **Files**: The eight vertical columns, labeled **a** through **h** (from White's left to right).
- **Ranks**: The eight horizontal rows, labeled **1** through **8** (Rank 1 and 2 for White, Rank 7 and 8 for Black).
- **Board Orientation**: The board is set up so that each player has a light-colored square on their bottom-right corner ("White on right").

### Initial Setup

- **Rank 1 (White)**: Rook (a1), Knight (b1), Bishop (c1), Queen (d1), King (e1), Bishop (f1), Knight (g1), Rook (h1).
- **Rank 2 (White)**: Eight pawns (a2 through h2).
- **Rank 7 (Black)**: Eight pawns (a7 through h7).
- **Rank 8 (Black)**: Rook (a8), Knight (b8), Bishop (c8), Queen (d8), King (e8), Bishop (f8), Knight (g8), Rook (h8).
- **Rule of Thumb**: White Queen starts on a light square (d1); Black Queen starts on a dark square (d8).

---

## Objective of the Game

The main goal in chess is to **checkmate** the opponent's King.

- **Check**: When a King is under direct attack by one or more enemy pieces. A player must immediately move out of check, block the attack, or capture the attacking piece.
- **Checkmate**: When a King is in check and there are no legal moves available to escape check. The game ends immediately in a win for the attacking player.

---

## Special Moves

### 1. Castling

Castling is a simultaneous move involving the King and one Rook. It helps safeguard the King and activate a Rook.

- **Kingside Castling (Short, notation `O-O`)**: The King moves two squares toward the h-file (e1 to g1 for White, e8 to g8 for Black), and the h-rook moves to the square the King crossed (f1 for White, f8 for Black).
- **Queenside Castling (Long, notation `O-O-O`)**: The King moves two squares toward the a-file (e1 to c1 for White, e8 to c8 for Black), and the a-rook moves to the square the King crossed (d1 for White, d8 for Black).

**Requirements for Castling**:
1. Neither the King nor the chosen Rook has moved prior in the game.
2. All squares between the King and the Rook must be empty.
3. The King must not currently be in check.
4. The King cannot pass through or land on any square that is under attack by an enemy piece.

### 2. En Passant

En passant (French for "in passing") is a special pawn capture rule:

- When a pawn moves two squares forward from its starting square and lands directly adjacent (side-by-side) to an enemy pawn.
- The enemy pawn has the option to capture the moving pawn diagonally as if it had only advanced one square.
- **Crucial Condition**: The en passant capture must be made on the very next turn. If not exercised immediately, the right to capture en passant is lost for that specific move.

### 3. Pawn Promotion

When a pawn reaches the opposite end of the board (the 8th rank for White, 1st rank for Black), it must be promoted to a piece of the player's choice: Queen, Rook, Bishop, or Knight.

- Most promotions are to a Queen ("queening").
- Underpromotion to a Knight, Rook, or Bishop can be tactically advantageous (e.g., to deliver a checkmate fork or avoid stalemate).

---

## Game Termination & Draws

A game can end in a draw (tie) through several conditions:

1. **Stalemate**: The player whose turn it is has no legal move available, but their King is **not** in check. The game ends in an immediate draw.
2. **Threefold Repetition**: The exact same position on the board occurs three times during a game (with the same player to move and identical legal moves available). Either player can claim a draw.
3. **50-Move Rule**: No pawn move has been made and no piece has been captured within the last 50 consecutive moves by each player.
4. **Insufficient Material**: Neither player has enough pieces to force a checkmate (e.g., King vs King, King & Knight vs King, King & Bishop vs King).
5. **Mutual Agreement**: Both players agree to end the game in a draw at any point during play.
