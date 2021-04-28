
from database import LocalDatabase, LocalId
from engine.resources import ResourceId
from engine.render import Renderers
from engine.game_field import FieldObject, Field

class EngineManager:

    def __init__(self, local_database):
        assert type(local_database) == LocalDatabase

        self.local_database = local_database
        self.active = True

    def move(self, local_id):
        assert type(local_id) == LocalId
        mob = self.local_database.get(local_id)

    def spawn(self, resource_id, location, game_field):
        assert type(resource_id) == ResourceId
        assert type(game_field) == Field
        if resource_id.value in Renderers:
            renderer = Renderers[resource_id.value]
            fo = FieldObject(location, renderer)
            id = self.database.add(fo)
            game_field.add(id)
            return True
        else:
            return False
    
    def despawn(self, local_id):
        assert type(local_id) == LocalId
        self.local_database.remove(local_id)
