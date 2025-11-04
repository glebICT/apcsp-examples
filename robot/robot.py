import turtle
import time
import json


CELL_SIZE = 40
WALL_COLOR = "#1e3a8a"
PATH_COLOR = "#dbeafe"
TURTLE_COLOR = "#059669"
GOAL_COLOR = "#fbbf24"


class MazeGame:
    def __init__(self, levels_file):
        self.screen = turtle.Screen()
        self.screen.title("🐢 Turtle Maze Game - Learn Programming!")
        self.screen.setup(width=800, height=700)
        self.screen.bgcolor("#f0f9ff")
        self.screen.tracer(0)

        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(0)

        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.color(TURTLE_COLOR)
        self.player.penup()
        self.player.speed(0)

        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

        self.commands = []
        self.current_pos = None
        self.running = True

        self.load_levels(levels_file)
        self.level = 1
        self.setup_level()
        self.draw_instructions()

    def load_levels(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.levels = json.load(f)

    def setup_level(self):
        """Initialize a level"""
        level_data = self.levels[str(self.level)]
        self.maze = level_data['maze']
        self.start_pos = level_data['start']
        self.end_pos = level_data['end']
        self.current_pos = list(self.start_pos)
        self.commands = []

        self.maze_width = len(self.maze[0])
        self.maze_height = len(self.maze)

        self.draw_maze()
        self.position_player()
        self.player.showturtle()   # Make sure turtle is visible here
        self.draw_ui()
        
        self.screen.update()       # Refresh screen to show changes immediately


    def draw_maze(self):
        self.drawer.clear()
        offset_x = -self.maze_width * CELL_SIZE // 2
        offset_y = self.maze_height * CELL_SIZE // 2

        for y in range(self.maze_height):
            for x in range(self.maze_width):
                cell_x = offset_x + x * CELL_SIZE
                cell_y = offset_y - y * CELL_SIZE

                self.drawer.penup()
                self.drawer.goto(cell_x, cell_y)
                self.drawer.pendown()

                if self.maze[y][x] == 1:
                    self.drawer.fillcolor(WALL_COLOR)
                else:
                    self.drawer.fillcolor(PATH_COLOR)

                self.drawer.begin_fill()
                for _ in range(4):
                    self.drawer.forward(CELL_SIZE)
                    self.drawer.right(90)
                self.drawer.end_fill()

        goal_x = offset_x + self.end_pos[0] * CELL_SIZE + CELL_SIZE // 2
        goal_y = offset_y - self.end_pos[1] * CELL_SIZE - CELL_SIZE // 2
        self.drawer.penup()
        self.drawer.goto(goal_x, goal_y)
        self.drawer.color(GOAL_COLOR)
        self.drawer.dot(CELL_SIZE - 10)
        self.drawer.goto(goal_x, goal_y - 8)
        self.drawer.color("black")
        self.drawer.write("🏆", align="center", font=("Arial", 16, "normal"))

    def position_player(self):
        offset_x = -self.maze_width * CELL_SIZE // 2
        offset_y = self.maze_height * CELL_SIZE // 2

        x = offset_x + self.current_pos[0] * CELL_SIZE + CELL_SIZE // 2
        y = offset_y - self.current_pos[1] * CELL_SIZE - CELL_SIZE // 2

        self.player.goto(x, y)
        self.player.setheading(90)

    def draw_ui(self):
        self.writer.clear()

        self.writer.goto(0, self.maze_height * CELL_SIZE // 2 + 40)
        self.writer.color("#1e3a8a")
        self.writer.write(f"Level {self.level}",
                          align="center", font=("Arial", 20, "bold"))

        level_data = self.levels[str(self.level)]
        self.writer.goto(0, self.maze_height * CELL_SIZE // 2 + 15)
        self.writer.write(level_data.get('concept', ''),
                          align="center", font=("Arial", 12, "normal"))

        self.writer.goto(0, -self.maze_height * CELL_SIZE // 2 - 40)
        cmd_text = f"Commands: {' → '.join(self.commands) if self.commands else 'None yet'}"
        self.writer.write(cmd_text, align="center", font=("Arial", 14, "normal"))

    def draw_instructions(self):
        instructions = [
            "KEYBOARD CONTROLS:",
            "Arrow keys: Add movement command",
            "'r': Run commands",
            "'c': Reset commands",
            "'h': Show hint",
            "'n': Next level",
            "'q': Quit game"
        ]

        self.writer.goto(-380, 200)
        self.writer.color("#6b7280")
        for i, line in enumerate(instructions):
            self.writer.goto(-380, 200 - i * 20)
            self.writer.write(line, font=("Arial", 9, "normal"))

    def add_command(self, direction):
        self.commands.append(direction)
        self.draw_ui()
        self.screen.update()
        print(f"✓ Added command: {direction}")
        print(f"Current sequence: {' -> '.join(self.commands)}")

    def run_commands(self):
        if not self.commands:
            print("⚠️ No commands to run! Add some commands first.")
            return

        print("\n🚀 Executing commands...")
        print(f"Sequence: {' -> '.join(self.commands)}")
        print()

        self.current_pos = list(self.start_pos)
        self.position_player()
        self.screen.update()
        time.sleep(0.3)

        for i, cmd in enumerate(self.commands, 1):
            print(f"Step {i}: {cmd}")
            success = self.move_turtle(cmd)
            self.screen.update()
            time.sleep(0.4)

            if not success:
                return

            if self.current_pos == list(self.end_pos):
                self.win_level()
                return

        print("\n❌ Not quite there! Try adding more commands or reset and try again.\n")

    def move_turtle(self, direction):
        next_pos = self.current_pos.copy()

        if direction == "up":
            next_pos[1] -= 1
            self.player.setheading(90)
        elif direction == "down":
            next_pos[1] += 1
            self.player.setheading(270)
        elif direction == "left":
            next_pos[0] -= 1
            self.player.setheading(180)
        elif direction == "right":
            next_pos[0] += 1
            self.player.setheading(0)

        if (0 <= next_pos[1] < self.maze_height and
            0 <= next_pos[0] < self.maze_width and
            self.maze[next_pos[1]][next_pos[0]] == 0):
            self.current_pos = next_pos
            self.position_player()
            return True
        else:
            print(f"\n💥 CRASH! Hit a wall while moving {direction}!")
            print("Try a different sequence of commands.\n")

            for _ in range(3):
                self.player.goto(self.player.xcor() + 5, self.player.ycor())
                self.screen.update()
                time.sleep(0.05)
                self.player.goto(self.player.xcor() - 5, self.player.ycor())
                self.screen.update()
                time.sleep(0.05)

            self.reset_level()
            return False

    def win_level(self):
        print("\n" + "="*50)
        print(f"🎉 LEVEL {self.level} COMPLETE! 🎉")
        print(f"Commands used: {len(self.commands)}")
        print("="*50 + "\n")

        for _ in range(3):
            self.player.right(120)
            self.screen.update()
            time.sleep(0.1)

        if self.level < len(self.levels):
            print(f"Press 'n' to go to Level {self.level + 1}!\n")
        else:
            print("🏆 YOU BEAT ALL LEVELS! CONGRATULATIONS! 🏆\n")

    def reset_level(self):
        self.current_pos = list(self.start_pos)
        self.commands = []
        self.position_player()
        self.draw_ui()
        self.screen.update()
        print("🔄 Level reset! Commands cleared.\n")

    def next_level(self):
        if self.level < len(self.levels):
            self.level += 1
            self.setup_level()
            self.screen.update()
            print(f"\n📈 Welcome to Level {self.level}!")
            print(f"Concept: {self.levels[str(self.level)].get('concept', '')}")
            print()
        else:
            print("🏆 You've completed all levels! Amazing work!\n")

    def show_hint(self):
        level_data = self.levels[str(self.level)]
        print("\n💡 HINT:")
        print(f"   {level_data.get('hint', 'No hint available.')}")
        print()

    # Keyboard event handlers
    def key_up(self):
        self.add_command('up')

    def key_down(self):
        self.add_command('down')

    def key_left(self):
        self.add_command('left')

    def key_right(self):
        self.add_command('right')

    def key_run(self):
        self.run_commands()

    def key_reset(self):
        self.reset_level()

    def key_hint(self):
        self.show_hint()

    def key_next(self):
        self.next_level()

    def key_quit(self):
        print("\n👋 Thanks for playing! Goodbye!\n")
        self.running = False
        self.screen.bye()

    def run(self):
        self.screen.listen()

        self.screen.onkey(self.key_up, "Up")
        self.screen.onkey(self.key_down, "Down")
        self.screen.onkey(self.key_left, "Left")
        self.screen.onkey(self.key_right, "Right")

        self.screen.onkey(self.key_run, "r")
        self.screen.onkey(self.key_reset, "c")
        self.screen.onkey(self.key_hint, "h")
        self.screen.onkey(self.key_next, "n")
        self.screen.onkey(self.key_quit, "q")

        print("\n🐢 Turtle Maze Game - Use arrow keys to add commands.")
        print("r=run, c=reset, h=hint, n=next, q=quit\n")

        self.screen.mainloop()


if __name__ == "__main__":
    game = MazeGame("levels.json")
    game.run()
