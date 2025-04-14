import pygame
import random
from visuals.selection import SelectionSortVisualizer
from visuals.quick import QuickSortVisualizer
from visuals.merge import MergeSortVisualizer
from visuals.bubble import BubbleSortVisualizer
from visuals.insertion import InsertionSortVisualizer
from visuals.heap import HeapSortVisualizer
from visuals.comb import CombSortVisualizer

class SortVisualizerApp:
    WIDTH, HEIGHT = 800, 600
    TOP_MARGIN = 120
    BAR_COLOR = (193, 154, 107)
    BG_COLOR = (245, 222, 179)
    BUTTON_COLOR = (160, 120, 60)
    HOVER_COLOR = (190, 150, 90)
    TEXT_COLOR = (20, 20, 20)

    def __init__(self):
        pygame.init()
        self.FONT = pygame.font.SysFont("georgia", 16)
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("📜 Les Papyrus de Héron")
        self.logo_img = self.load_logo()

        self.ALGORITHMS = {
            "Tri par sélection": SelectionSortVisualizer,
            "Tri rapide": QuickSortVisualizer,
            "Tri fusion": MergeSortVisualizer,
            "Tri à bulles": BubbleSortVisualizer,
            "Tri par insertion": InsertionSortVisualizer,
            "Tri par tas": HeapSortVisualizer,
            "Tri à peigne": CombSortVisualizer
        }

        self.algo_list = list(self.ALGORITHMS.keys())
        self.algo_index = 0
        self.selected_algo_name = self.algo_list[self.algo_index]

        self.list_size = 2000
        self.min_list_size = 10
        self.max_list_size = 2000
        self.data = self.generate_new_data(self.list_size)
        self.visualizer = self.ALGORITHMS[self.selected_algo_name](self.win, self.data, top_margin=self.TOP_MARGIN)

        self.delay_ms = 20
        self.min_delay = 1
        self.max_delay = 100

        self.slider_x = 520
        self.slider_y = 36
        self.slider_width = 150
        self.speed_slider_x = self.slider_x
        self.speed_slider_y = self.slider_y + 30

        self.sorting = False
        self.paused = True
        self.finished = False
        self.dragging_slider = False
        self.dragging_speed_slider = False
        self.dropdown_open = False
        self.sort_generator = None

        self.algo_btn = pygame.Rect(150, 20, 200, 32)
        self.shuffle_btn = pygame.Rect(370, 20, 60, 32)
        self.start_btn = pygame.Rect(440, 20, 60, 32)

    def load_logo(self):
        try:
            logo = pygame.image.load("logo.png")
            return pygame.transform.scale(logo, (100, 75))
        except:
            return None

    def generate_new_data(self, size):
        return [random.randint(20, self.HEIGHT - self.TOP_MARGIN - 10) for _ in range(size)]

    def draw_button(self, rect, text, hovered=False):
        color = self.HOVER_COLOR if hovered else self.BUTTON_COLOR
        pygame.draw.rect(self.win, color, rect, border_radius=6)
        label = self.FONT.render(text, True, self.TEXT_COLOR)
        self.win.blit(label, label.get_rect(center=rect.center))

    def draw_dropdown(self, rect, options, selected_index, expanded, mouse_pos):
        self.draw_button(rect, options[selected_index], rect.collidepoint(mouse_pos))
        if expanded:
            for i, option in enumerate(options):
                option_rect = pygame.Rect(rect.x, rect.y + (i + 1) * rect.height, rect.width, rect.height)
                self.draw_button(option_rect, option, option_rect.collidepoint(mouse_pos))

    def draw_slider(self, pos_x, pos_y, width, value, min_val, max_val):
        pygame.draw.line(self.win, self.BUTTON_COLOR, (pos_x, pos_y), (pos_x + width, pos_y), 4)
        knob_x = pos_x + int((value - min_val) / (max_val - min_val) * width)
        pygame.draw.circle(self.win, self.HOVER_COLOR, (knob_x, pos_y), 8)
        return pygame.Rect(knob_x - 8, pos_y - 8, 16, 16)

    def draw_labeled_slider(self, pos_x, pos_y, width, value, min_val, max_val, label_text):
        knob_rect = self.draw_slider(pos_x, pos_y, width, value, min_val, max_val)
        label = self.FONT.render(f"{label_text} : {value}", True, self.TEXT_COLOR)
        self.win.blit(label, (pos_x + width + 10, pos_y - 10))
        return knob_rect

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            self.win.fill(self.BG_COLOR)
            pygame.draw.rect(self.win, (120, 100, 70), (0, 0, self.WIDTH, self.TOP_MARGIN))
            if self.logo_img:
                self.win.blit(self.logo_img, (10, 10))

            self.draw_button(self.start_btn, "go", self.start_btn.collidepoint(mouse_pos))
            self.draw_button(self.shuffle_btn, "list", self.shuffle_btn.collidepoint(mouse_pos))
            self.draw_dropdown(self.algo_btn, self.algo_list, self.algo_index, self.dropdown_open, mouse_pos)
            slider_knob = self.draw_labeled_slider(self.slider_x, self.slider_y, self.slider_width,
                                                   self.list_size, self.min_list_size, self.max_list_size, "Taille")
            speed_slider = self.draw_labeled_slider(self.speed_slider_x, self.speed_slider_y, self.slider_width,
                                                    self.delay_ms, self.min_delay, self.max_delay, "Vitesse")

            if self.sorting and not self.finished and not self.paused:
                try:
                    next(self.sort_generator)
                    pygame.time.delay(self.delay_ms)
                    self.visualizer.draw_list()
                except StopIteration:
                    self.finished = True
            else:
                self.visualizer.draw_list()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if slider_knob.collidepoint(event.pos):
                        self.dragging_slider = True
                    elif speed_slider.collidepoint(event.pos):
                        self.dragging_speed_slider = True
                    elif self.start_btn.collidepoint(event.pos):
                        self.sort_generator = self.visualizer.sort_generator()
                        self.paused = False
                        self.sorting = True
                        self.finished = False
                    elif self.shuffle_btn.collidepoint(event.pos):
                        self.data = self.generate_new_data(self.list_size)
                        self.visualizer = self.ALGORITHMS[self.selected_algo_name](self.win, self.data, top_margin=self.TOP_MARGIN)
                        self.sorting = False
                        self.finished = False
                        self.paused = True
                    elif self.algo_btn.collidepoint(event.pos):
                        self.dropdown_open = not self.dropdown_open
                    elif self.dropdown_open:
                        for i, option in enumerate(self.algo_list):
                            option_rect = pygame.Rect(self.algo_btn.x, self.algo_btn.y + (i + 1) * self.algo_btn.height,
                                                      self.algo_btn.width, self.algo_btn.height)
                            if option_rect.collidepoint(event.pos):
                                self.algo_index = i
                                self.selected_algo_name = self.algo_list[self.algo_index]
                                self.visualizer = self.ALGORITHMS[self.selected_algo_name](self.win, self.data, top_margin=self.TOP_MARGIN)
                                self.sorting = False
                                self.finished = False
                                self.paused = True
                                self.dropdown_open = False

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging_slider = False
                    self.dragging_speed_slider = False

                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging_slider:
                        rel_x = max(0, min(event.pos[0] - self.slider_x, self.slider_width))
                        self.list_size = self.min_list_size + int((rel_x / self.slider_width) * (self.max_list_size - self.min_list_size))
                        self.data = self.generate_new_data(self.list_size)
                        self.visualizer = self.ALGORITHMS[self.selected_algo_name](self.win, self.data, top_margin=self.TOP_MARGIN)
                        self.sorting = False
                        self.finished = False
                        self.paused = True
                    elif self.dragging_speed_slider:
                        rel_x = max(0, min(event.pos[0] - self.speed_slider_x, self.slider_width))
                        self.delay_ms = self.min_delay + int((rel_x / self.slider_width) * (self.max_delay - self.min_delay))

        pygame.quit()


def main():
    app = SortVisualizerApp()
    app.run()