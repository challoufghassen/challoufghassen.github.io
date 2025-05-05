import tkinter as tk
from tkinter import ttk

# Function to load valid terms from the text file
def load_valid_terms_from_file(filename="valid_terms.txt"):
    valid_terms = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("#") or not line.strip():
                    continue
                category, terms = line.split(":")
                valid_terms[category.strip()] = [term.strip().lower() for term in terms.split(",")]
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please ensure it exists in the directory.")
        return {}
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return {}
    return valid_terms

# Function to calculate score based on valid input
def calculate_score(input_text, category, valid_terms):
    if not input_text or not category:
        return 0
    input_text = input_text.lower().strip()
    valid_list = valid_terms.get(category, [])
    # Check if input matches any valid term
    if any(term in input_text for term in valid_list):
        # Simple scoring: 10% per valid match
        return 10
    return 0

# GUI setup with Tkinter
class WhiteBoxTerminal:
    def __init__(self, root):
        self.root = root
        self.root.title("White Box Terminal v1.0")
        self.root.configure(bg="black")
        self.root.geometry("800x400")  # Set window size similar to your screenshot

        # Load valid terms from the file
        self.valid_terms = load_valid_terms_from_file("valid_terms.txt")
        if not self.valid_terms:
            print("No valid terms loaded. Please check valid_terms.txt.")
            self.valid_terms = {}

        # For demo purposes, hardcode the category; you can make this dynamic later
        self.current_category = "Static Code Analysis"

        # Title label
        self.title_label = tk.Label(root, text="WHITE_BOX_TERMINAL v1.0", bg="black", fg="white", font=("Courier", 14, "bold"))
        self.title_label.pack(pady=10)

        # Input box
        self.input_box = tk.Text(root, height=2, width=50, bg="black", fg="white", insertbackground="white", font=("Courier", 12))
        self.input_box.pack(pady=10)

        # Frame for buttons
        self.button_frame = tk.Frame(root, bg="black")
        self.button_frame.pack(pady=10)

        # Valid button
        self.valid_button = tk.Button(self.button_frame, text="Valid", command=self.validate_input, bg="black", fg="green", font=("Courier", 12))
        self.valid_button.pack(side=tk.LEFT, padx=5)

        # Back button (placeholder)
        self.back_button = tk.Button(self.button_frame, text="Back", command=self.go_back, bg="black", fg="green", font=("Courier", 12))
        self.back_button.pack(side=tk.LEFT, padx=5)

        # Score label (bottom right)
        self.score_var = tk.StringVar()
        self.score_var.set("Score: 0%")
        self.score_label = tk.Label(root, textvariable=self.score_var, bg="black", fg="green", font=("Courier", 12))
        self.score_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)  # Bottom right

    def validate_input(self):
        user_input = self.input_box.get("1.0", tk.END).strip()
        score = calculate_score(user_input, self.current_category, self.valid_terms)
        self.score_var.set(f"Score: {score}%")
        # Clear the input box after validation
        self.input_box.delete("1.0", tk.END)

    def go_back(self):
        print("Back button clicked. Implement navigation to previous screen here.")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteBoxTerminal(root)
    root.mainloop()