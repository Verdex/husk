
from database import MobFieldObjects
from resources import ResourceId
from engine.render import Renderers
from engine.game_field import FieldObject, Field

class EngineManager:

    def __init__(self, game_field):
        assert type(game_field) == Field

        self.game_field = game_field
        self.active = True

    def move(self, local_id):
        assert type(local_id) == LocalId
        #mob = self.local_database.get(local_id)

    def spawn(self, resource_id, location):
        assert type(resource_id) == ResourceId
        if resource_id.value in Renderers:
            renderer = Renderers[resource_id.value]
            fo = FieldObject(location, renderer)
            id = MobFieldObjects.add(fo)
            return id
        else:
            return False
    
    def despawn(self, local_id):
        assert type(local_id) == LocalId
        self.local_database.remove(local_id)
        # TODO need to remove from game field
