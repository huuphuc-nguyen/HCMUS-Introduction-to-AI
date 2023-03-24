from Space import *
from Constants import *
import math

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while(open_set):
        '''
        Get current node
        '''
        current_node_value = open_set.pop()
        current_node = g.get_node(current_node_value)
    
        if current_node != g.start:
            current_node.set_color(yellow)
            current_node.update_color(sc)
            pygame.time.wait(50)

        '''
        Check if current node is goal
        '''
        if current_node == g.goal:
            path = []
            while current_node != g.start:
                path.append(current_node)
                current_node = g.get_node(father[current_node.value])
            path.append(g.start)
            path.reverse

            # Draw Path
            for node in path:
                node.set_color(grey)
                node.update_color(sc)
                pygame.time.wait(50)
            
            g.start.set_color(orange)
            g.start.update_color(sc)
            g.goal.set_color(purple)
            g.goal.update_color(sc)

            return 

        '''
        Get neighbor nodes and visit
        '''
        neighbors = g.get_neighbors(current_node)

        for node in neighbors:

            if node.value in closed_set:
                continue

            if node.value not in open_set:
                open_set.append(node.value)
                father[node.value] = current_node_value

                if node != g.goal:
                    node.set_color(red)
                    node.update_color(sc)
                    pygame.time.wait(50)

        '''
        Add current set into closed_set
        '''
        closed_set.append(current_node.value)

        if current_node != g.start:
            current_node.set_color(blue)
            current_node.update_color(sc)
            pygame.time.wait(70)
        
    
    raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while(open_set):
        '''
        Get current node
        '''
        current_node_value = open_set.pop(0)
        current_node = g.get_node(current_node_value)
    
        if current_node != g.start:
            current_node.set_color(yellow)
            current_node.update_color(sc)
            pygame.time.wait(50)

        '''
        Check if current node is goal
        '''
        if current_node == g.goal:
            path = []
            while current_node != g.start:
                path.append(current_node)
                current_node = g.get_node(father[current_node.value])
            path.append(g.start)
            path.reverse

            # Draw Path
            for node in path:
                node.set_color(grey)
                node.update_color(sc)
                pygame.time.wait(50)
            
            g.start.set_color(orange)
            g.start.update_color(sc)
            g.goal.set_color(purple)
            g.goal.update_color(sc)

            return 

        '''
        Get neighbor nodes and visit
        '''
        neighbors = g.get_neighbors(current_node)

        for node in neighbors:

            if node.value in closed_set:
                continue

            if node.value not in open_set:
                open_set.append(node.value)
                father[node.value] = current_node_value

                if node != g.goal:
                    node.set_color(red)
                    node.update_color(sc)
                    pygame.time.wait(50)

        '''
        Add current set into closed_set
        '''
        closed_set.append(current_node.value)

        if current_node != g.start:
            current_node.set_color(blue)
            current_node.update_color(sc)
            pygame.time.wait(70)

    raise ValueError('No path found')

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [50_000]*g.get_len()
    cost[g.start.value] = 0

    while open_set:
        # Get node with smallest cost in open_set
        current_node_value = min(open_set, key = open_set.get)
        current_node = g.get_node(current_node_value)
        del open_set[current_node_value]

        if current_node != g.start:
            current_node.set_color(yellow)
            current_node.update_color(sc)
            pygame.time.wait(50) 

        # Check if current node is goal
        if current_node == g.goal:
            path = []
            while current_node != g.start:
                path.append(current_node)
                current_node = g.get_node(father[current_node.value])
            path.append(g.start)
            path.reverse()

            # Draw Path
            for node in path:
                node.set_color(grey)
                node.update_color(sc)
                pygame.time.wait(50)
            
            g.start.set_color(orange)
            g.start.update_color(sc)
            g.goal.set_color(purple)
            g.goal.update_color(sc)

            return 
        
        # Get neighbor nodes and visit
        neighbors = g.get_neighbors(current_node)
        
        for node in neighbors:
            if node.value in closed_set:
                continue

            if node.value not in open_set:
                father[node.value] = current_node.value
                neighbor_cost = cost[current_node.value] + distance_between(current_node,node)
                open_set[node.value] = neighbor_cost
                cost[node.value] = neighbor_cost

                if node != g.goal:
                        node.set_color(red)
                        node.update_color(sc)
                        pygame.time.wait(50)

         # Add current node to closed_set
        closed_set.append(current_node.value)

        if current_node != g.start:
            current_node.set_color(blue)
            current_node.update_color(sc)
            pygame.time.wait(70)

    raise ValueError('No path found')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0

    closed_set:list[int] = []

    father = [-1]*g.get_len()

    cost = [50_000]*g.get_len()
    cost[g.start.value] = 0

    f_cost = [50_000]*g.get_len()
    f_cost[g.start.value] = heuristic(g.start,g.goal)

    while (open_set):
        current_node_value = min(open_set, key = open_set.get)
        current_node = g.get_node(current_node_value)
        del open_set[current_node_value]

        if current_node != g.start:
            current_node.set_color(yellow)
            current_node.update_color(sc)
            pygame.time.wait(50) 
        # Check if current node is goal
        if current_node == g.goal:
            path = []
            while current_node != g.start:
                path.append(current_node)
                current_node = g.get_node(father[current_node.value])
            path.append(g.start)
            path.reverse()

            # Draw Path
            for node in path:
                node.set_color(grey)
                node.update_color(sc)
                pygame.time.wait(50)
            
            g.start.set_color(orange)
            g.start.update_color(sc)
            g.goal.set_color(purple)
            g.goal.update_color(sc)

            return 
        
        # Get neighbor nodes and visit
        neighbors = g.get_neighbors(current_node)
        
        for node in neighbors:
            if node.value in closed_set:
                continue

            if node.value not in open_set:
                father[node.value] = current_node.value

                g_cost = cost[current_node.value] + distance_between(node,current_node) 
                cost[node.value] = g_cost
                
                h_cost = heuristic(node,g.goal)

                f_cost[node.value] = cost[node.value] + h_cost

                open_set[node.value] = f_cost[node.value]

                if node != g.goal:
                        node.set_color(red)
                        node.update_color(sc)
                        pygame.time.wait(50)

         # Add current node to closed_set
        closed_set.append(current_node.value)

        if current_node != g.start:
            current_node.set_color(blue)
            current_node.update_color(sc)
            pygame.time.wait(70)

    raise ValueError('No path found')

def distance_between(a:Node, b:Node):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def heuristic (a:Node, b:Node): # Diagonal Distance
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    D = 1
    D2 = math.sqrt(2) * 30
    
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)


