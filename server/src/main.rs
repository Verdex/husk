
use std::net::TcpListener;
use std::sync::mpsc;

extern crate byteorder; 

mod comms;
mod processing;

use comms::stream::{read_requests};

fn main() -> std::io::Result<()> {

    let (sender, receiver) = mpsc::channel();

    let listener = TcpListener::bind("127.0.0.1:0")?;

    let addr = TcpListener::local_addr(&listener)?;

    println!("port {}", addr.port());

    loop {
        let (mut sock, addr) = listener.accept()?;

        let user_requests = read_requests(&mut sock)?;

        println!("requets = {:?}", user_requests);
    }

    Ok(())
}
