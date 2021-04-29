
from database import MobFieldObjects
from resources import ResourceId
from engine.render import Renderers
from engine.game_field import FieldObject, Field

class EngineManager:

    def __init__(self, game_field):
        assert type(game_field) == Field

        self.game_field = game_field
        self.active = True

    def move(self, value, location):
        id = MobFieldObjects.int_to_id(value)
        fo = MobFieldObjects.get(id)
        if fo:
            fo.location = location 
            return True
        else:
            return False

    def spawn(self, resource_id, location):
        assert type(resource_id) == ResourceId
        if resource_id.value in Renderers:
            renderer = Renderers[resource_id.value]
            fo = FieldObject(location, renderer)
            id = MobFieldObjects.add(fo)
            return id
        else:
            return False
    
    def despawn(self, value):
        id = MobFieldObjects.int_to_id(value)
        MobFieldObjects.remove(id)
