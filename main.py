import tkinter as tk
import game as game

def create_board(grid):
    for row in range(3):
		for col in range(3):
            button = tk.Button(root, text="", width=10, height=3, command=lambda r=row, c=col: game.on_click(r, c, grid))
            button.grid(row=row, column=col)

def main():
	grid = [[0 for i in range(3)] for i in range(3)]
	root = tk.Tk()
	create_board(grid)
	root.mainloop()

if __name__ == "__main__":
	main()
