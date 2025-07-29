from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        visited_routes = set()
        visited_stops = set()
        queue = deque()
        
        for route in stop_to_routes[source]:
            queue.append((route, 1))  
            visited_routes.add(route)
        while queue:
            route_index, buses = queue.popleft()
            if target in routes[route_index]:
                return buses

            for stop in routes[route_index]:
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)
                for neighbor_route in stop_to_routes[stop]:
                    if neighbor_route not in visited_routes:
                        visited_routes.add(neighbor_route)
                        queue.append((neighbor_route, buses + 1))
        
        return -1  

        

        

                
        
                
        