import flet as ft

def main(page: ft.Page):
    # Ρυθμίσεις παραθύρου
    page.title = "Μίκτης Χρωμάτων RGB"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Σύγχρονος τρόπος για μέγεθος παραθύρου
    page.window.width = 450
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Αυτή η συνάρτηση τρέχει ΚΑΘΕ ΦΟΡΑ που κουνάς μια μπάρα (slider)
    def allagi_xrwmatos(e):
        # Παίρνουμε τις τιμές (από 0 έως 255) και τις κάνουμε ακέραιους int
        r = int(red_slider.value or 0)
        g = int(green_slider.value or 0)
        b = int(blue_slider.value or 0)
        
        #Μετατρέπουμε τους αριθμούς σε κωδικό χρώματος
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        # Αλλάζουμε το χρώμα στο τετράγωνο και το κείμενο από κάτω
        color_box.bgcolor = hex_color
        hex_text.value = f"Χρώμα: {hex_color.upper()} | RGB: ({r}, {g}, {b})"
        
        page.update()

    
    # Ένα μεγάλο τετράγωνο που θα δείχνει το χρώμα Ξεκινάει με μαύρο
    color_box = ft.Container(
        width=200,
        height=200,
        bgcolor="#000000",
        border_radius=20,  # Στρογγυλεμένες γωνίες για να φαίνεται μοντέρνο!
        margin=ft.margin.only(top=20, bottom=20)
    )
    
    # Το κείμενο που θα δείχνει τους κωδικούς του χρώματος
    hex_text = ft.Text(value="Χρώμα: #000000 | RGB: (0, 0, 0)", size=18, weight=ft.FontWeight.BOLD)

    # Οι 3 μπάρες, βάζουμε on_change αντί για on_click, ώστε να αντιδρούν στο σύρσιμο
    red_slider = ft.Slider(min=0, max=255, value=0, active_color="red", on_change=allagi_xrwmatos)
    green_slider = ft.Slider(min=0, max=255, value=0, active_color="green", on_change=allagi_xrwmatos)
    blue_slider = ft.Slider(min=0, max=255, value=0, active_color="blue", on_change=allagi_xrwmatos)

    # Βάζουμε όλα τα στοιχεία στη σελίδα με τη σειρά που θέλουμε να εμφανιστούν
    page.add(
        color_box,
        hex_text,
        ft.Text("Κόκκινο (Red):", color="red"), red_slider,
        ft.Text("Πράσινο (Green):", color="green"), green_slider,
        ft.Text("Μπλε (Blue):", color="blue"), blue_slider
    )

ft.run(main)