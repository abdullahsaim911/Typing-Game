import tkinter as tk
from tkinter import messagebox
import random
import time

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game - Python GUI")
        self.root.geometry("600x700")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)
        
        # Game variables
        self.width = 20
        self.height = 20
        self.cell_size = 25
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = "Right"
        self.food = self.generate_food()
        self.score = 0
        self.game_running = False
        self.speed = 150
        
        # Colors
        self.bg_color = '#2C3E50'
        self.snake_color = '#27AE60'
        self.food_color = '#E74C3C'
        self.grid_color = '#34495E'
        
        self.setup_ui()
        self.bind_keys()
        
    def setup_ui(self):
        # Title
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=10)
        
        title_label = tk.Label(title_frame, text="🐍 SNAKE GAME", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ECF0F1', bg=self.bg_color)
        title_label.pack()
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg=self.bg_color)
        self.score_frame.pack(pady=5)
        
        self.score_label = tk.Label(self.score_frame, text="Score: 0", 
                                   font=('Arial', 16), 
                                   fg='#F39C12', bg=self.bg_color)
        self.score_label.pack()
        
        # Game canvas
        canvas_width = self.width * self.cell_size
        canvas_height = self.height * self.cell_size
        
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height,
                               bg=self.grid_color, highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(button_frame, text="Start Game", 
                                     command=self.start_game,
                                     font=('Arial', 12, 'bold'),
                                     bg='#27AE60', fg='white',
                                     relief='flat', padx=20, pady=5)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = tk.Button(button_frame, text="Pause", 
                                     command=self.pause_game,
                                     font=('Arial', 12, 'bold'),
                                     bg='#F39C12', fg='white',
                                     relief='flat', padx=20, pady=5,
                                     state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(button_frame, text="Reset", 
                                     command=self.reset_game,
                                     font=('Arial', 12, 'bold'),
                                     bg='#E74C3C', fg='white',
                                     relief='flat', padx=20, pady=5)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Instructions
        instructions_frame = tk.Frame(self.root, bg=self.bg_color)
        instructions_frame.pack(pady=10)
        
        instructions_text = """Use Arrow Keys or WASD to control the snake
Eat the red food to grow and increase your score
Avoid hitting the walls or yourself!"""
        
        instructions_label = tk.Label(instructions_frame, text=instructions_text,
                                     font=('Arial', 10), 
                                     fg='#BDC3C7', bg=self.bg_color,
                                     justify=tk.CENTER)
        instructions_label.pack()
        
        self.draw_grid()
        self.draw_snake()
        self.draw_food()
        
    def draw_grid(self):
        """Draw the game grid"""
        for i in range(self.width + 1):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.height * self.cell_size, 
                                   fill='#34495E', width=1)
        
        for i in range(self.height + 1):
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.width * self.cell_size, y, 
                                   fill='#34495E', width=1)
    
    def draw_snake(self):
        """Draw the snake on the canvas"""
        self.canvas.delete("snake")
        for i, (x, y) in enumerate(self.snake):
            x1 = x * self.cell_size
            y1 = y * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            
            # Head is darker
            color = '#1E8449' if i == 0 else self.snake_color
            self.canvas.create_rectangle(x1, y1, x2, y2, 
                                       fill=color, outline='#2ECC71', 
                                       tags="snake", width=2)
    
    def draw_food(self):
        """Draw the food on the canvas"""
        self.canvas.delete("food")
        x, y = self.food
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        
        self.canvas.create_oval(x1, y1, x2, y2, 
                               fill=self.food_color, outline='#C0392B',
                               tags="food", width=2)
    
    def generate_food(self):
        """Generate food at random position"""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def move_snake(self):
        """Move the snake in the current direction"""
        if not self.game_running:
            return
        
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)
        
        # Check collision with walls
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.game_over()
            return
        
        # Check collision with self
        if new_head in self.snake:
            self.game_over()
            return
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.generate_food()
            self.draw_food()
            # Increase speed slightly
            if self.speed > 50:
                self.speed -= 2
        else:
            self.snake.pop()
        
        self.draw_snake()
        self.root.after(self.speed, self.move_snake)
    
    def bind_keys(self):
        """Bind keyboard controls"""
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.focus_set()
    
    def on_key_press(self, event):
        """Handle key press events"""
        key = event.keysym.lower()
        
        if key in ['up', 'w'] and self.direction != "Down":
            self.direction = "Up"
        elif key in ['down', 's'] and self.direction != "Up":
            self.direction = "Down"
        elif key in ['left', 'a'] and self.direction != "Right":
            self.direction = "Left"
        elif key in ['right', 'd'] and self.direction != "Left":
            self.direction = "Right"
        elif key == 'space':
            if self.game_running:
                self.pause_game()
            else:
                self.start_game()
    
    def start_game(self):
        """Start the game"""
        if not self.game_running:
            self.game_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.move_snake()
    
    def pause_game(self):
        """Pause the game"""
        self.game_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
    
    def reset_game(self):
        """Reset the game"""
        self.game_running = False
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = "Right"
        self.food = self.generate_food()
        self.score = 0
        self.speed = 150
        
        self.score_label.config(text="Score: 0")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        
        self.draw_snake()
        self.draw_food()
    
    def game_over(self):
        """Handle game over"""
        self.game_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        
        # Show game over message
        result = messagebox.askyesno("Game Over!", 
                                   f"Game Over!\nFinal Score: {self.score}\n\nWould you like to play again?")
        if result:
            self.reset_game()
        else:
            self.root.quit()

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
