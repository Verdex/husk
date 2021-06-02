
use std::io::Write;
use std::thread::{self, JoinHandle};
use std::sync::mpsc::{Sender, Receiver, SendError};
use std::sync::atomic::{AtomicU16, Ordering};
use std::net::{TcpStream, TcpListener};
use std::time::Duration;

use crate::data::{ProcComm, Stop};

static PORT : AtomicU16 = AtomicU16::new(0);

pub fn start( process_sender : Sender<ProcComm<TcpStream>>
            , listen_receiver : Receiver<Stop> ) -> std::io::Result<JoinHandle<()>> {

    let listener = TcpListener::bind("127.0.0.1:0")?;

    let addr = TcpListener::local_addr(&listener)?;

    println!("port {}", addr.port());

    PORT.store(addr.port(), Ordering::Relaxed);

    let handle = thread::spawn( move || {
        loop {
            let accept_result = listener.accept();

            match accept_result {
                Err(e) => println!("Encountered error while trying to accept: {}", e),
                Ok((sock, _addr)) => {
                    log_failure(process_sender.send(ProcComm::Message(sock)));
                },
            }

            let result = listen_receiver.recv_timeout(Duration::from_millis(10));

            match result {
                Ok(_) => break,
                _ => {},
            }

        }
    });

    Ok(handle)
}

pub fn stop( listen_sender : Sender<Stop> ) {

    let socket_result = TcpStream::connect(format!("127.0.0.1:{}", PORT.load(Ordering::Relaxed)));

    match socket_result {
        Err(_) => panic!("Failed stopping the listen thread"),
        Ok(mut socket) => { 
            log_failure(listen_sender.send(Stop { }));
            socket.write(&[0xFF, 0xFF, 0xFF, 0xFF]).expect("Failed contacting listen thread"); 
        },
    }

}

fn log_failure<T>(x : Result<(), SendError<T>>) {
    match x { 
        Err(e) => println!("Sending in listening failed: {}", e),
        _ => { },
    }
}