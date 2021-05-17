
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn main() -> std::io::Result<()> {

    let listener = TcpListener::bind("127.0.0.1:0")?;

    let addr = TcpListener::local_addr(&listener)?;

    println!("port {}", addr.port());

    loop {
        let (mut sock, addr) = listener.accept()?;

        blarg(&mut sock);
        println!("blarg");
    }

    Ok(())
}

fn blarg(x : &mut TcpStream) -> std::io::Result<()> {
    let mut buffer = vec![];
    println!("first");
    x.read_to_end(&mut buffer)?;
    for xlet in buffer {
        print!("{:x?} ", xlet);
    }
    println!("");
    println!("read");
    x.write(&[0, 1, 2])?;
    println!("write");
    Ok(())
}