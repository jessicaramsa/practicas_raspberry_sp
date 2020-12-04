import json

class Image:
    id: int
    url: str
    extension: str

    def __init__(self, url, extension):
        self.url = url
        self.extension = extension
    
    def __repr__(self):
        return { 'id': self.id, 'url': self.url, 'extension': self.extension }
