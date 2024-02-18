import tkinter as tk
from PIL import Image, ImageTk

# Function to update values when the button is clicked
def on_button_click():
    try:
        voltage_value = float(voltage_entry.get())
        resistance_value = float(resistance_entry.get())
        
        # Calculate current
        current_value = voltage_value / resistance_value

        # Update the current label
        current_label.config(text=f"Current: {current_value:.2f} A")

    except ValueError:
        print("Please enter valid numerical values.")

# Create the main application window
app = tk.Tk()
app.title("Kei's Circuit Simulator")

# Load the image
image_path = "C:/Circuit_Simulator_feb24/Resistor_circuit_image.png"
img = Image.open(image_path)
img = img.resize((300, 200))
photo = ImageTk.PhotoImage(img)

# Create a label widget to display the image
image_label = tk.Label(app, image=photo)
image_label.grid(row=0, column=1, padx=10, pady=10)  # Adjust pady as needed

# Create entry widgets for voltage and resistance with smaller width
voltage_label = tk.Label(app, text="Voltage (V) :")
voltage_label.grid(row=0, column=0, pady=5)  # Adjust pady as needed

voltage_entry = tk.Entry(app, width=8)  # Adjust the width as needed
voltage_entry.grid(row=1, column=0, pady=5)  # Adjust pady as needed

resistance_label = tk.Label(app, text="Resistance (Ohms):")
resistance_label.grid(row=0, column=2, pady=5)  # Adjust pady as needed

resistance_entry = tk.Entry(app, width=8)  # Adjust the width as needed
resistance_entry.grid(row=1, column=2, pady=5)  # Adjust pady as needed

# Create a button widget to trigger the update function
button = tk.Button(app, text="Update Values", command=on_button_click)
button.grid(row=3, column=1, pady=5)  # Adjust pady as needed

# Create a label for displaying current
current_label = tk.Label(app, text="Current: N/A A")
current_label.grid(row=4, column=1, pady=5)  # Adjust pady as needed

# Start the main event loop
app.mainloop()
