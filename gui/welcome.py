import tkinter as tk
import resources.style as font
from PIL import Image, ImageTk

class WelcomeFrame(tk.Frame):
    """
    Frame with a greeting label and an image.
    """

    welcome_label: tk.Label
    image_label: tk.Label

    __y_label_padding: int
    __original_image: Image

    def __init__(self, root: tk.Frame | tk.Tk, translations: dict, row: int = 0, column: int = 0, columnspan: int = 2,
                 padx: int = 20, pady: int = 20):
        """
        Initialize the WelcomeFrame.

        Args:
            root (Frame | Tk): Frame parent. A Tkinter frame or the root Tkinter window.
            translations (dict): A dictionary of translations for UI text.
            row (int): The row position of the frame in the grid.
            column (int): The column position of the frame in the grid.
            columnspan (int): The number of columns the frame spans in the grid.
            padx (int): The horizontal padding around the frame.
            pady (int): The vertical padding around the frame.
        """
        super().__init__(root)
        self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=tk.N)

        self.__y_label_padding = 50

        # welcome label
        self.welcome_label = tk.Label(self, font=font.welcome_font, text=translations["greeting"])
        self.welcome_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=20, pady=self.__y_label_padding)
        self.welcome_label.bind("<Configure>", self.update_image_label_height)

        # image label
        self.__original_image = Image.open("resources/image/Forkium-Logo.png")
        photo: ImageTk.PhotoImage = ImageTk.PhotoImage(self.__original_image)
        self.image_label = tk.Label(self, image=photo)
        self.image_label.grid(row=0, column=1, padx=10, pady=10)

    def update_image_label_height(self, event: tk.Event):
        """
        Update the height of the image label based on the height of the welcome label.

        Args:
            event (tk.Event): The event that triggered the update.
        """
        # Calculate the height of the welcome label
        label_height: int = self.welcome_label.winfo_height() + self.__y_label_padding

        # Scale the image to the new height
        scaled_image: Image = self.__original_image.resize(
            (int(self.__original_image.width * label_height / self.__original_image.height), label_height),
            Image.Resampling.LANCZOS)
        photo: ImageTk.PhotoImage = ImageTk.PhotoImage(scaled_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
