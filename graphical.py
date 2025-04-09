import pygame
import random
from visuals.selection import SelectionSortVisualizer
from visuals.quick import QuickSortVisualizer
from visuals.merge import MergeSortVisualizer

WIDTH, HEIGHT = 800, 600
TOP_MARGIN = 120  # Espace réservé en haut
BUTTON_WIDTH, BUTTON_HEIGHT = 90, 40
BUTTON_COLOR = (70, 130, 180)
HOVER_COLOR = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (245, 235, 220)  # beige doux

def draw_button(win, rect, text, font, hovered=False):
    color = HOVER_COLOR if hovered else BUTTON_COLOR
    pygame.draw.rect(win, color, rect, border_radius=8)
    text_surf = font.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    win.blit(text_surf, text_rect)

def load_logo():
    try:
        logo = pygame.image.load("logo.png")
        return pygame.transform.scale(logo, (120, 90))
    except:
        return None

def display_logo(win, logo):
    if logo:
        win.blit(logo, (10, 10))

def graphical_menu():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Les Papyrus de Héron – Visualisation")
    font = pygame.font.SysFont("arial", 24)
    logo = load_logo()

    buttons = {
        "selection": pygame.Rect(WIDTH//2 - 100, 250, 200, 50),
        "quick": pygame.Rect(WIDTH//2 - 100, 320, 200, 50),
        "merge": pygame.Rect(WIDTH//2 - 100, 390, 200, 50)
    }

    while True:
        win.fill(BACKGROUND_COLOR)
        display_logo(win, logo)

        for key, rect in buttons.items():
            hovered = rect.collidepoint(pygame.mouse.get_pos())
            draw_button(win, rect, f"Tri {key}", font, hovered)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["selection"].collidepoint(event.pos):
                    launch_sort(win, SelectionSortVisualizer, logo)
                elif buttons["quick"].collidepoint(event.pos):
                    launch_sort(win, QuickSortVisualizer, logo)
                elif buttons["merge"].collidepoint(event.pos):
                    launch_sort(win, MergeSortVisualizer, logo)

def launch_sort(win, VisualizerClass, logo):
    font = pygame.font.SysFont("arial", 20)
    data = [random.randint(20, HEIGHT - TOP_MARGIN - 10) for _ in range(100)]
    visualizer = VisualizerClass(win, data, top_margin=TOP_MARGIN)
    paused = False
    finished = False

    pause_button = pygame.Rect(WIDTH - 220, 30, BUTTON_WIDTH, BUTTON_HEIGHT)
    back_button = pygame.Rect(WIDTH - 110, 30, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Dessin initial
    win.fill(BACKGROUND_COLOR)
    display_logo(win, logo)
    draw_button(win, pause_button, "Pause", font)
    draw_button(win, back_button, "Menu", font)
    visualizer.draw_list()
    pygame.display.update()

    sort_generator = visualizer.sort_generator()

    while True:
        if not paused and not finished:
            try:
                next(sort_generator)
                visualizer.draw_list()
                pygame.display.update()
            except StopIteration:
                finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(event.pos):
                    paused = not paused
                    draw_button(win, pause_button, "Pause" if not paused else "Reprendre", font)
                    draw_button(win, back_button, "Menu", font)
                    pygame.display.update()
                elif back_button.collidepoint(event.pos):
                    return
 
if __name__ == "__main__":
    graphical_menu()