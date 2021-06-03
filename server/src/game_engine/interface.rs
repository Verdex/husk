
use std::sync::mpsc::{Sender, Receiver, SendError};
use std::thread::{self, JoinHandle};

use crate::data::ProcComm;

#[derive(Clone, Copy)]
pub enum Action {

}

pub fn start(receiver : Receiver<ProcComm<Action>>) -> JoinHandle<()> {

    let handle = thread::spawn(move || {
        loop {
            let msg = receiver.recv().expect("Receive Failure in Process");

            match msg {
                ProcComm::Message(action) => handle_action(action),
                ProcComm::Stop => break,
            }
        }
    });

    handle
}

fn handle_action(action : Action) {

}

pub fn stop(process_sender : Sender<ProcComm<Action>> ) {
    log_failure(process_sender.send(ProcComm::Stop));
}

fn log_failure<T>(x : Result<(), SendError<T>>) {
    match x { 
        Err(e) => println!("Sending in listening failed: {}", e),
        _ => { },
    }
}