import json

class Note:
    id: int
    title: str
    description: str

    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    def __repr__(self):
        return { 'id': self.id, 'title': self.title, 'description': self.description }
