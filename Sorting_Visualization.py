import random
import pygame

# Create the array with random numbers
def load_array(array):
    for i in range(size):
        x=random.randint(1,page_depth)
        if x not in array:
            array.append(x)
    return array

# Load Coordinates in the Window
def load_item_coordinates(array,print_start_index,gap_between_lines):
    size = len(array)
    for a in range(print_start_index, size):
        A_X.append(gap_between_lines)
        A_Y.append(page_depth)
        B_X.append(gap_between_lines)
        B_Y.append(page_depth - array[a])

        gap_between_lines += gap_between_lines_increase

# Window
def view_sorting(array,max_pass):
    pygame.init()
    size=len(array)
    screen = pygame.display.set_mode((page_width, page_depth))

    print_index_start=0
    print_index_end=size
    pass_print_count=0
    r,g,b=250,250,0

    clock = pygame.time.Clock()

    running = True

    while(running):
        clock.tick(10)
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # pygame.draw.line(screen,(0,255,0),(400,0),(400,600))
        for k in range(print_index_start,print_index_end):
            pygame.draw.line(screen, (r,g,b), (A_X[k],A_Y[k]), (B_X[k],B_Y[k]))
           
        if pass_print_count <= max_pass:
            print_index_start=print_index_end
            print_index_end = print_index_end + size
        else:
            k=print_index_start
            r,g,b=0,255,0

        pass_print_count += 1
        pygame.display.flip()

    pygame.display.update()

# Bubble sort algorithm
def bubble_sort(array):
    global max_pass
    size=len(array)
    for i in range(size-1):
        for j in range(i+1,size):
            if array[j] < array[i]:
                array[i],array[j]=array[j],array[i]
        load_item_coordinates(array,print_start_index,gap_between_lines)
        max_pass+=1

    return array

def insertion_sort(array):
    global max_pass
    n=len(array)

    for i in range(1,n):
        j=i
        while(j>0 and array[j]<array[j-1]):
            array[j],array[j-1]=array[j-1],array[j]
            j-=1
        load_item_coordinates(array,print_start_index,gap_between_lines)
        max_pass+=1

    return array

# Driver code goes here
def driver():
    array=[]
    # array = [102,57,380,408,109,78,203]
    unsorted_array = load_array(array)
    print(unsorted_array)

    load_item_coordinates(array,print_start_index,gap_between_lines)

    # bubble_sort(array)

    insertion_sort(array)

    view_sorting(array,max_pass-1)

if __name__=="__main__":
    A_X, A_Y, B_X, B_Y = [], [], [], []
    page_width, page_depth = 800, 600
    gap_between_lines = 0
    gap_between_lines_increase = 5
    print_start_index = 0
    size= page_width//gap_between_lines_increase
    max_pass=0
    driver()
