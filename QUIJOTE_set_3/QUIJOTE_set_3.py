'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return 'friends'
    elif to_member in social_graph[from_member]['following']:
        return 'follower'
    elif from_member in social_graph[to_member]['following']:
        return 'followed by'
    else:
        return 'no relationship'

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board_size = len(board)
    vertical = []
    cross_one = []
    cross_two = []

    for row in range(0, board_size):
        symbol = board[row][0]
        if board[row] == [symbol] * board_size and symbol != '':
            return symbol

        cross_one.append(board[row][row])
        cross_two.append(board[row][board_size - (row + 1)])

    for position in range(0, board_size):
        for row in range(0, board_size):
            vertical.append(board[row][position])

        symbol = board[0][position]
        if vertical == [symbol] * board_size and symbol != '':
            return symbol
        vertical = []
    symbol = board[0][0]
    if cross_one == [symbol] * board_size and symbol != '':
        return symbol
    symbol = board[0][board_size -1]
    if cross_two == [symbol] * board_size and symbol != '':
        return symbol

    return 'NO WINNER'
    
def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    total_routes = len(route_map)*2
    routes_list = list(route_map.keys())*2
    times_list = list(route_map.values())*2
    start = first_stop
    time = 0

    for index in range(0, total_routes):
        if routes_list[index][0] == start:
            time += times_list[index]['travel_time_mins']
            start = routes_list[index][1]
            if routes_list[index][1] == second_stop:
                break
    return time

