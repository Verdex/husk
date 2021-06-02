
use std::sync::mpsc;

extern crate byteorder; 

mod data;
mod comms;
mod processing;
mod network;
mod console_mod;

use data::{Stop, ProcComm};
use processing::process;
use network::listening;
use console_mod::console;

fn main() -> std::io::Result<()> {

    let (process_sender, process_receiver) = mpsc::channel();
    let (listening_sender, listening_receiver) = mpsc::channel();

    let process_socket_thread = process::start(process_receiver);
    let listening_thread = listening::start(process_sender.clone(), listening_receiver)?;

    console::start_blocking();

    process::stop(process_sender);
    listening::stop(listening_sender);

    process_socket_thread.join().expect("Waiting for process socket thread to end failed");
    listening_thread.join().expect("Waiting for listening thread to end failed");


    Ok(())
}
