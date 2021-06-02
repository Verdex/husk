
use std::net::TcpStream;
use std::sync::mpsc::{Sender, Receiver, SendError};
use std::thread::{self, JoinHandle};

use crate::comms::stream::{read_requests};
use crate::data::ProcComm;


pub fn start(receiver : Receiver<ProcComm<TcpStream>>) -> JoinHandle<()> {

    let handle = thread::spawn(move || {
        loop {
            let msg = receiver.recv().expect("Receive Failure in Process");

            match msg {
                ProcComm::Message(stream) => process_stream(stream),
                ProcComm::Stop => break,
            }
        }
    });

    handle
}

fn process_stream(mut stream : TcpStream) {
    let user_requests_result = read_requests(&mut stream);

    match user_requests_result {
        Ok(user_requests) => println!("USER REQUESTS"),
        Err(e) => println!("Encountered error while parsing TCP Stream: {}", e),
    }
}

pub fn stop(process_sender : Sender<ProcComm<TcpStream>> ) {
    log_failure(process_sender.send(ProcComm::Stop));
}


fn log_failure<T>(x : Result<(), SendError<T>>) {
    match x { 
        Err(e) => println!("Sending in listening failed: {}", e),
        _ => { },
    }
}