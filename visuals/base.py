import pygame

# 🎨 Couleurs antiques
BAR_COLOR = (193, 154, 107)        # bronze
COMPARE_COLOR = (100, 149, 237)    # bleu ancien
SWAP_COLOR = (255, 215, 0)         # or

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
            x = i * bar_width + bar_width // 2  # ligne centrée dans sa colonne
            y = self.height - val
            y = max(y, self.top_margin + 1)

            color = BAR_COLOR
            if highlight and i in highlight:
                color = COMPARE_COLOR if highlight[i] == "compare" else SWAP_COLOR

            # Ligne verticale au lieu de rectangle
            pygame.draw.line(self.win, color, (x, y), (x, self.height), width=2)
