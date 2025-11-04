import turtle
import tkinter as tk
from tkinter import ttk

# Create main tkinter window
root = tk.Tk()
root.title("Star Animation Control Panel")
root.geometry("300x200")

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Zoom In and Out Star Animation")
screen.tracer(0, 0)  # Turn off automatic screen updates

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.color("yellow")
t.hideturtle()

# Global variables for animation control
animating = False
current_size = 20
zoom_direction = 1  # 1 for zoom in, -1 for zoom out

# Function to draw a star
def draw_star(size):
    t.clear()
    t.penup()
    t.goto(-size/2, size/4)  # Position to center the star
    t.pendown()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    screen.update()

# Animation function using tkinter's after method
def animate():
    global animating, current_size, zoom_direction
    
    if not animating:
        return
    
    # Update size based on direction
    current_size += 2 * zoom_direction
    
    # Change direction at boundaries
    if current_size >= 200:
        zoom_direction = -1
    elif current_size <= 20:
        zoom_direction = 1
    
    # Draw the star with current size
    draw_star(current_size)
    
    # Schedule next animation frame
    root.after(50, animate)  # 50ms delay for ~20 FPS

# Start/Stop animation functions
def toggle_animation():
    global animating
    if not animating:
        animating = True
        start_button.config(text="Stop Animation")
        animate()  # Start the animation
    else:
        animating = False
        start_button.config(text="Start Animation")

def close_application():
    global animating
    animating = False
    screen.bye()
    root.destroy()

# Create UI controls
control_frame = ttk.Frame(root)
control_frame.pack(pady=20)

start_button = ttk.Button(control_frame, text="Start Animation", command=toggle_animation)
start_button.pack(pady=10)

close_button = ttk.Button(control_frame, text="Close", command=close_application)
close_button.pack(pady=10)

# Status label
status_label = ttk.Label(root, text="Click 'Start Animation' to begin")
status_label.pack(pady=10)

# Draw initial star
draw_star(current_size)

# Start the tkinter main loop
root.protocol("WM_DELETE_WINDOW", close_application)
root.mainloop()