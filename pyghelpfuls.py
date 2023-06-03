import math 

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_width, text_height = text_surface.get_size()
    center_x = x - text_width // 2
    center_y = y - text_height // 2
    screen.blit(text_surface, (center_x, center_y))

def polygon_corners(n, x, y, z):
    radius = min(x, y) / 2 - z
    cx, cy = x / 2, y / 2
    angle = 2 * math.pi / n
    corners = []
    for i in range(n):
        x_i = cx + radius * math.cos(i * angle)
        y_i = cy + radius * math.sin(i * angle)
        corners.append((x_i, y_i))
    
    first_corner = min(corners, key=lambda c: c[1])
    
    first_corner_index = corners.index(first_corner)
    ordered_corners = corners[first_corner_index:] + corners[:first_corner_index]
    if first_corner_index != 0:
        ordered_corners.reverse()
    
    return [(round(x), round(y)) for x, y in ordered_corners]
    #return ordered_corners
