
use std::net::TcpListener;
use std::sync::mpsc;

extern crate byteorder; 

mod data;
mod comms;
mod processing;

use processing::process;
use data::ProcComm;

fn main() -> std::io::Result<()> {

    let (process_sender, process_receiver) = mpsc::channel();

    let process_socket_thread = process::start(process_receiver);

    let listener = TcpListener::bind("127.0.0.1:0")?;

    let addr = TcpListener::local_addr(&listener)?;

    println!("port {}", addr.port());

    loop {
        let (sock, addr) = listener.accept()?;

        process_sender.send(ProcComm::Message(sock)).expect("Failed Send attempt to Process socket");
    }

    Ok(())
}
