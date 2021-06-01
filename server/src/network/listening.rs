
use std::thread::{self, JoinHandle};
use std::net::{TcpStream, TcpListener};
use std::sync::mpsc::{Sender, Receiver};

use crate::data::ProcComm;

pub fn start(process_sender : Sender<ProcComm<TcpStream>>) -> std::io::Result<JoinHandle<()>> {

    let listener = TcpListener::bind("127.0.0.1:0")?;

    let addr = TcpListener::local_addr(&listener)?;

    println!("port {}", addr.port());

    let handle = thread::spawn( move || {
        loop {
            let (sock, addr) = listener.accept()?;

            process_sender.send(ProcComm::Message(sock)).expect("Failed Send attempt to Process socket");
        }
    });


    Ok(handle)
}