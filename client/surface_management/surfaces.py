
from id import LocalId

class SingleSurface:

    def __init__(self, id, surface, location, size, priority):
        assert type(id) == LocalId, "id is not a local id"

        self.id = id
        self.surface = surface
        self.location = location
        self.size = size
        self.priority = priority


class AggregateSurface:

    def __init__(self, id, surface, location, size, priority):
        assert type(id) == LocalId, "id is not a local id"

        self.id = id
        self.surface = surface
        self.location = location
        self.size = size
        self.priority = priority
        self.surfaces = {} 
    
    def add(self, surface):
        self.surfaces[surface.id.value] = surface
    
    def remove(self, id):
        if self.surfaces[id.value]:
            del self.surfaces[id.value]

    def update(self):
        for surface in sorted( self.surfaces.values(), lambda s: s.priority ):
            if type(surface) == AggregateSurface: 
                surface.update()
            else if type(surface) == SingleSurface:
                self.surface.blit(surface.surface, surface.location)
            else:
                raise SystemError(f"Encountered unknown surface type: {type(surface)}")
