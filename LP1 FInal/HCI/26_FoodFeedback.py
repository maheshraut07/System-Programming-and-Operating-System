import tkinter as tk
from tkinter import ttk

def submit_feedback():
    customer_name = name_entry.get()
    feedback_text = feedback_textbox.get("1.0", "end-1c")
    food_quality = food_quality_var.get()
    service_quality = service_quality_var.get()
    cleanliness = cleanliness_var.get()

    # You can process and store the feedback in a database or file here.
    # For this example, we'll just display the feedback.
    result_label.config(
        text=f"Thank you, {customer_name} for your feedback!\n"
        f"Feedback: {feedback_text}\n"
        f"Food Quality: {food_quality}/5\n"
        f"Service Quality: {service_quality}/5\n"
        f"Cleanliness: {cleanliness}/5"
    )

root = tk.Tk()
root.title("Customer Feedback Form")

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

# Customer Name
name_label = ttk.Label(frame, text="Your Name:")
name_label.grid(column=0, row=0)
name_entry = ttk.Entry(frame)
name_entry.grid(column=1, row=0)

# Food Quality
food_quality_label = ttk.Label(frame, text="Food Quality:")
food_quality_label.grid(column=0, row=1)
food_quality_var = tk.IntVar()
food_quality_scale = ttk.Scale(frame, from_=1, to=5, variable=food_quality_var, orient="horizontal")
food_quality_scale.grid(column=1, row=1)

# Service Quality
service_quality_label = ttk.Label(frame, text="Service Quality:")
service_quality_label.grid(column=0, row=2)
service_quality_var = tk.IntVar()
service_quality_scale = ttk.Scale(frame, from_=1, to=5, variable=service_quality_var, orient="horizontal")
service_quality_scale.grid(column=1, row=2)

# Cleanliness
cleanliness_label = ttk.Label(frame, text="Cleanliness:")
cleanliness_label.grid(column=0, row=3)
cleanliness_var = tk.IntVar()
cleanliness_scale = ttk.Scale(frame, from_=1, to=5, variable=cleanliness_var, orient="horizontal")
cleanliness_scale.grid(column=1, row=3)

# Feedback Text
feedback_label = ttk.Label(frame, text="Feedback:")
feedback_label.grid(column=0, row=4, columnspan=2)
feedback_textbox = tk.Text(frame, height=5, width=40)
feedback_textbox.grid(column=1, row=4, columnspan=2)

# Submit Button
submit_button = ttk.Button(frame, text="Submit", command=submit_feedback)
submit_button.grid(column=0, row=5, columnspan=3, pady=10)

# Result Label
result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=6, columnspan=3, pady=10)

root.mainloop()
