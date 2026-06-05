import tkinter as tk

# --- PHASE 1: BRANDING & APP COLOR MATRIX ---
# Defining the premium luxury color palette using precise Hex values
COLOR_BG = "#0D0D0D"       # Deep Cinema Matte Black
COLOR_SCREEN = "#141414"   # Sleek Dark Charcoal Screen
COLOR_TEXT = "#FFFFFF"     # High-Contrast Crisp White
COLOR_PURPLE = "#4A154B"   # Deep Royal Purple (Numeric Keys)
COLOR_RED = "#990011"      # Intense Crimson Red (Operation Keys)
COLOR_ACCENT = "#FF3344"   # Vibrant Coral Accent for special targets

class CyberCalculator:
    def __init__(self, master):
        self.master = master
        master.title("NEXUS // CORE_CALC_v2.5")
        master.configure(bg=COLOR_BG)
        master.resizable(False, False) # Keeps layout pixel-perfect
        
        # System string to track math input
        self.equation = ""
        
        # --- PHASE 2: THE SCREEN DISPLAY ---
        self.display_var = tk.StringVar(value="0")
        self.screen = tk.Label(
            master, 
            textvariable=self.display_var, 
            anchor="e", 
            bg=COLOR_SCREEN, 
            fg=COLOR_TEXT, 
            font=("Consolas", 28, "bold"), 
            padx=20, 
            pady=25,
            bd=0,
            highlightbackground=COLOR_PURPLE,
            highlightthickness=1
        )
        self.screen.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky="nsew")
        
        # --- PHASE 3: GRID LAYOUT ARCHITECTURE ---
        # Button matrix layout blueprint
        buttons = [
            ('C', 1, 0, COLOR_RED),    ('(', 1, 1, COLOR_PURPLE), (')', 1, 2, COLOR_PURPLE), ('/', 1, 3, COLOR_RED),
            ('7', 2, 0, COLOR_BG),     ('8', 2, 1, COLOR_BG),     ('9', 2, 2, COLOR_BG),     ('*', 2, 3, COLOR_RED),
            ('4', 3, 0, COLOR_BG),     ('5', 3, 1, COLOR_BG),     ('6', 3, 2, COLOR_BG),     ('-', 3, 3, COLOR_RED),
            ('1', 4, 0, COLOR_BG),     ('2', 4, 1, COLOR_BG),     ('3', 4, 2, COLOR_BG),     ('+', 4, 3, COLOR_RED),
            ('0', 5, 0, COLOR_BG),     ('.', 5, 1, COLOR_BG),     ('=', 5, 2, COLOR_ACCENT)
        ]
        
        self.build_interface(buttons)

    def build_interface(self, buttons):
        for (text, row, col, bg_color) in buttons:
            # Special formatting rule to make the '=' button span wider
            colspan = 2 if text == '=' else 1
            
            # Setting dynamic foreground text rules based on background blocks
            fg_color = COLOR_TEXT
            if bg_color == COLOR_BG:
                highlight = COLOR_PURPLE # Purple structural borders around numeric black keys
            else:
                highlight = bg_color
            
            action = lambda x=text: self.on_button_click(x)
            
            btn = tk.Button(
                self.master, 
                text=text, 
                command=action, 
                bg=bg_color, 
                fg=fg_color, 
                font=("Consolas", 14, "bold"),
                bd=0,
                highlightbackground=highlight,
                highlightthickness=1,
                activebackground=COLOR_TEXT,
                activeforeground=COLOR_BG,
                width=5,
                height=2
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=6, pady=6, sticky="nsew")

    # --- PHASE 4: MATHEMATICAL LOGIC ENGINE ---
    def on_button_click(self, char):
        if char == 'C':
            self.equation = ""
            self.display_var.set("0")
        elif char == '=':
            try:
                # Evaluating the raw math string securely
                total = str(eval(self.equation))
                self.display_var.set(total)
                self.equation = total # Allow sequential chaining math operations
            except Exception:
                self.display_var.set("SYS_ERR")
                self.equation = ""
        else:
            self.equation += str(char)
            self.display_var.set(self.equation)

# --- PHASE 5: RUNTIME INITIALIZATION ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CyberCalculator(root)
    print("[SUCCESS] Nexus Core Engine Loaded. Application Window Active.")
    root.mainloop()
