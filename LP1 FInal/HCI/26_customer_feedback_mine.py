import tkinter as tk

# Function to handle the form submission
def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c")
    selected_options = [option for var, option in checkbox_vars if var.get() == 1]
    feedback_text_label.config(text="Feedback: " + feedback)
    options_text_label.config(text="Selected Options: " + ', '.join(selected_options))

# Create the main application window
root = tk.Tk()
root.title("Customer Feedback Form")

# Set background color
root.configure(bg="cyan4")  # Use a light yellow background color

# Labels
title_label = tk.Label(root, text="Hotel Feedback Form", font=("Helvetica", 16), bg="cyan4")  # Set label background color
title_label.pack(pady=10)

feedback_label = tk.Label(root, text="Please provide your feedback:", bg="cyan4", font=("Helvetica", 12))  # Increase text size
feedback_label.pack()

# Text Entry for Feedback
feedback_text = tk.Text(root, height=8, width=40)  # Increase the height of the text entry
feedback_text.pack(pady=10)  # Add padding below the text entry

# Checkbuttons for Feedback Options
feedback_options = ["Quality", "Service", "Cleanliness", "Price"]
checkbox_vars = []

for option in feedback_options:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=option, variable=var, bg="cyan", font=("Helvetica", 12))  # Increase text size
    checkbox.pack()

# Add distance between the text entry and the list of options
distance_label = tk.Label(root, text="", bg="cyan4")  # Empty label for spacing
distance_label.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback, bg="green", font=("Helvetica", 12))  # Increase text size
submit_button.pack(pady=10)

# Labels for Displaying Feedback and Selected Options
feedback_text_label = tk.Label(root, text="Feedback: ", bg="pink", font=("Helvetica", 12))  # Increase text size
feedback_text_label.pack()
options_text_label = tk.Label(root, text="Selected Options: ", bg="pink", font=("Helvetica", 12))  # Increase text size
options_text_label.pack()

# Start the GUI main loop
root.mainloop()
