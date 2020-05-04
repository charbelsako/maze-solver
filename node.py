class Node(object):
    def __init__(self, title, i, j):
        self.title = title
        self.i = str(i)
        self.j = str(j)
        # no neighbors at first
        # TODO: use the efficient neighbor lookup?
        self.neighbors = []

    def __str__(self):
        return '<' + self.title + '>'

    def __repr__(self):
        character = 'W' if self.title is '#' else 'O'
        return '<' + self.i + ' ' + self.j + ' ' + self.title + ', ' + str(len(self.neighbors))+'>'
