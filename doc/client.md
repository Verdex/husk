
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

    // some are going to be moving existing objects
    // some are going to be deleting existing objects
    // some are going to be creating some object
    // some are going to be activiting animations

    // TODO need resource lookup
    // TODO need live object manager
    // TODO animation manager?


```