
use std::net::TcpStream;
use std::sync::mpsc::{Sender, Receiver, SendError};
use std::thread::{self, JoinHandle};

use crate::comms::stream;
use crate::comms::data::UserRequests;
use crate::data::ProcComm;
use crate::game_engine::interface::Action;


pub fn start( receiver : Receiver<ProcComm<TcpStream>>
            , game_engine_sender : Sender<ProcComm<Action>> ) -> JoinHandle<()> {

    let handle = thread::spawn(move || {
        loop {
            let msg = receiver.recv().expect("Receive Failure in Process");

            match msg {
                ProcComm::Message(stream) => process_stream(stream, &game_engine_sender),
                ProcComm::Stop => break,
            }
        }
    });

    handle
}

fn process_stream( mut stream : TcpStream
                 , game_engine_sender : &Sender<ProcComm<Action>> ) {

    let user_requests_result = stream::read_requests(&mut stream);

    match user_requests_result {
        Ok(user_requests) => process_requests(user_requests, game_engine_sender),
        Err(e) => println!("Encountered error while parsing TCP Stream: {}", e),
    }
}

fn process_requests( user_requests : UserRequests, game_engine_sender : &Sender<ProcComm<Action>> ) {
    // TODO 
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