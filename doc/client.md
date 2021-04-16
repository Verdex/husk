
# design

## messages

```
Messenger { 

}

```

## surfaces

```
type surface = SingleSurface surface | Aggregate [surface]

type surface = { 
    pygame_surface,
    location,
    size,
    priority
}

Aggregate {
    add(surface)
    remove(surface)
    update(surface)
}

```

## loop

```
    foreach event in pygame.event.get()
        process

    server_messages = get messages from server
    // messages should just give high level commands and the client can decide how that is executed
    // example spawn monster with id=blah gets translated into multiple low level details


    // create object (sound, animation, image)
    // delete object
    // move visible object
    // console text

    // animations are definitely managed over time and sounds are potentially managed over time

    // TODO need resource lookup
    // TODO need live object manager
    // TODO animation manager?

    top_level_aggregate.update()

```
