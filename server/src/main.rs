
use std::net::TcpListener;
use std::sync::mpsc;

extern crate byteorder; 

mod data;
mod comms;
mod processing;
mod network;

use processing::process;
use data::ProcComm;

use network::listening;

fn main() -> std::io::Result<()> {

    let (process_sender, process_receiver) = mpsc::channel();

    let process_socket_thread = process::start(process_receiver);
    let listener_thread = listening::start(process_sender)?;


    Ok(())
}
