
from database import LocalDatabase, LocalId
from engine.resources import ResourceId
from engine.render import Renderers

class EngineManager:

    def __init__(self, local_database):
        assert type(local_database) == LocalDatabase

        self.local_database = local_database
        self.active = True

    def move(self, local_id):
        assert type(local_id) == LocalId
        mob = self.local_database.get(local_id)

    def spawn(self, resource_id, game_surface):
        assert type(resource_id) == ResourceId
        # TODO add the renderer to some list?
    
    def despawn(self, local_id):
        assert type(local_id) == LocalId
        self.local_database.remove(local_id)
