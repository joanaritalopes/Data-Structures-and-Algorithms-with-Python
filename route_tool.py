from data_structures.graph_search import bfs, dfs
from route_tool_support import vc_metro, vc_landmarks, landmark_choices


# Build program below:
landmark_string = ''
stations_under_construction = ['Lincoln', 'Rupert', 'Waterfront', 'Burrard']
for letter, landmark in landmark_choices.items():
    landmark_string += letter + ' - ' + landmark + '\n'

def greet():
    print("Hi, we'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def goodbye():
    print("Thanks for using our tool!")

def skyroute():
    greet()
    new_route()
    goodbye()

def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
    else:
        print("Sorry, that's not a landmark we have data on. Try again...")
        get_start()
  
    return start_point

def get_end():
    end_point_letter = input("Where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
    else:
        print("Sorry, that's not a landmark we have data on. Try again...")
        get_end()
    
    return end_point

def set_start_and_end(start_point, end_point):
    if start_point != None:
        change_point = input("What would you like to change? You can enter 'o' for 'Origin', 'd' for 'Destination', or 'b' for 'Both': ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print("Invalid input. Please select again")
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == 'y':
        print(landmark_string)

def new_route(start_point= None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point) 
    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, due to maintenance, there is currently no path between {0} and {1}".format(start_point, end_point))

    again = input("Would you like to see another route? Enter y/n: ")
    if again == 'y':
        show_landmarks()
        new_route(start_point, end_point)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            
            if len(stations_under_construction) > 0:
                possible_route = dfs(metro_system, start_station, end_station) 
                if possible_route is None:
                    continue
      
            route = bfs(metro_system, start_station, end_station)
            if route is not None:
                routes.append(route)
                
    if routes:
        shortest_route = min(routes, key = len)
        return shortest_route

def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_station in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])

    return updated_metro
  