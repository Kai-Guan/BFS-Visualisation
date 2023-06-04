import pygame, pyghelpfuls, sys, numpy

inputs = []
links = []

with open("testcase.txt") as file:
    for line in file:
        a,b = line.split(":")
        b = b.rstrip('\n')
        links.append([a,b])
print(links)

letters = [i[0] for i in links]


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.neighbours = []

#print(letters)

nodes = {}
for letter in letters:
    newNode = Node(letter=letter)
    nodes[letter] = newNode

for n,node in enumerate(nodes):
    connections = links[n][1]
    for connection in connections:
        nodes[node].neighbours.append(nodes[connection])

def BFS(start,end):
    queue = []
    visited = []
    paths = []
    visited.append(start)
    queue.append(start)
    while queue:
        #print(nodes[queue[0]].letter,[n.letter for n in nodes[queue[0]].neighbours])
        if queue[0] != end:
            for neighbour in nodes[queue[0]].neighbours:
                if neighbour.letter not in visited:
                    queue.append(neighbour.letter)
                    paths.append([nodes[queue[0]].letter,neighbour.letter])
            visited.append(queue[0])
            queue.pop(0)
        else:
            break
    #print(paths)
    path = [end]
    x = end
    while True:
        for item in paths:
            if item[1] == x:
                x = item[0]
                path.append(x)
                break
        if x == start:
            path.reverse()
            break
    return(path)

#print(BFS("A","G"))

screen_width = 500
screen_height = 500


circle_radius = 20
circle_color = (0,0,0)

num_circles = len(links)

circleCoords = pyghelpfuls.polygon_corners(num_circles,screen_width,screen_height,50)
print(circleCoords)

def distance(start,end):
    deltaX = end[0]-start[0]
    deltaY = end[1]-start[1]
    return(abs(numpy.sqrt((deltaX**2)+(deltaY**2))))

def find(x):
    return(circleCoords[letters.index(x)])

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Graph")

font = pygame.font.SysFont('Arial', 20)

start,end = letters[0],letters[0]

text = ""
text_surf = font.render(text, True, (0, 0, 0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(text) == 2:
                    if text[0] in letters and text[1] in letters:
                        if nodes[text[0]].neighbours != [] and nodes[text[1]].neighbours != []:
                            start,end = text[0],text[1]
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
            if event.key == pygame.K_RETURN:
                text = str()


    window_center = screen_width/2,15

    screen.fill((255, 255, 255))

    text_surf = font.render(text, True, (0, 0, 0))
    screen.blit(text_surf, text_surf.get_rect(center = window_center))

    for group in links:
        if group[1] != "":
            for point in group[1]:
                startPos = circleCoords[letters.index(group[0])]
                endPos = circleCoords[letters.index(point)]
                pygame.draw.line(screen, (0,0,0), startPos, endPos, width=5)

    path = BFS(start,end)
    for i in range(len(path)-1):
        pygame.draw.line(screen, (255,255,0), find(path[i]), find(path[i+1]), width=7)

    for i,coord, in enumerate(circleCoords):
        pygame.draw.circle(screen, circle_color, coord, circle_radius)
        pyghelpfuls.draw_text(screen, links[i][0], font, (255,255,255), coord[0], coord[1])

    pygame.display.flip()
 
