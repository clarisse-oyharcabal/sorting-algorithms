import pygame

BAR_COLOR = (100, 200, 255)
COMPARE_COLOR = (255, 100, 100)
SWAP_COLOR = (100, 255, 100)

class VisualSort:
    def __init__(self, win, data, top_margin=0):
        self.win = win
        self.data = data
        self.top_margin = top_margin
        self.width = win.get_width()
        self.height = win.get_height()

    def draw_list(self, highlight=None):
        bar_width = self.width // len(self.data)

        for i, val in enumerate(self.data):
            x = i * bar_width
            y = self.height - val
            y = max(y, self.top_margin + 1)  # Respecte la marge haute
            color = BAR_COLOR
            if highlight and i in highlight:
                color = COMPARE_COLOR if highlight[i] == "compare" else SWAP_COLOR
            pygame.draw.rect(self.win, color, (x, y, bar_width, val))

        pygame.display.update()
