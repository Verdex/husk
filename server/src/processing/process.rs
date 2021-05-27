
use std::net::TcpStream;
use std::mpsc::Receiver;
use std::thread;

use comms::stream::{read_requests};

//stream : &mut TcpStream

pub fn start(receiver : Receiver<TcpStream>) { // TODO receiver should be Receiver<TcpStream | Stop>

    thread::spawn(move || {
        loop {

        }
    });
    let user_requests = read_requests(stream)?;

}