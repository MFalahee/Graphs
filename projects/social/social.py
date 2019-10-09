import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(i)

        # Create friendships
        possible_friends = []
        for user in range(1, numUsers + 1):
            for friend in range(1, numUsers + 1):
                if user is not friend and (friend, user) not in possible_friends:
                    possible_friends.append((user, friend))

        random.shuffle(possible_friends)
        total_friendships = avgFriendships * (numUsers//2)

        for num in range(total_friendships):
            self.addFriendship(possible_friends[num][0], possible_friends[num][1])

    def bfs(self, starting_vertex, visited):
       
        qq = Queue()
        qq.enqueue([starting_vertex])

        while qq.size() > 0:
            route = qq.dequeue()
            vertex = route[-1]

            if vertex not in visited:
                visited[vertex] = route

                for friendship in self.friendships[vertex]:
                    route_copy = route.copy()
                    route_copy.append(friendship)
                    qq.enqueue(route_copy)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        self.bfs(userID, visited)
            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
