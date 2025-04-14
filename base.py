import pygame

class VisualSort:
    def __init__(self, surface, data, bar_color=(193, 154, 107), top_margin=120):
        self.surface = surface
        self.data = data
        self.bar_color = bar_color
        self.top_margin = top_margin
        self.width = surface.get_width()
        self.height = surface.get_height()
        self.font = pygame.font.SysFont("georgia", 12)

    def draw_list(self, highlight_indices=None):
        bar_width = self.width / len(self.data)
        self.surface.fill((245, 222, 179), (0, self.top_margin, self.width, self.height - self.top_margin))

        for i, val in enumerate(self.data):
            x = i * bar_width
            y = self.height - val
            color = self.bar_color

            if highlight_indices and i in highlight_indices:
                color = (255, 100, 100)  # Couleur de surbrillance

            pygame.draw.rect(self.surface, color, (x, y, bar_width, val))

            # Afficher la valeur au-dessus de chaque barre (peu lisible si data > 200)
            label = self.font.render(str(int(val)), True, (0, 0, 0))
            label_rect = label.get_rect(center=(x + bar_width // 2, y - 10))
            self.surface.blit(label, label_rect)

        pygame.display.update()