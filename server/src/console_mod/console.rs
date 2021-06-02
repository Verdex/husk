
use std::io::{self, Read};

pub fn start_blocking() {

    let mut stdin = io::stdin();
    loop {
        let mut buffer = String::new();
        let result = stdin.read_line(&mut buffer);
        match result {
            Err(_) => println!("Failed to read from console"),
            _ => { },
        }

        let clean = buffer.trim();

        if clean == "exit" {
            break;
        }
    }

}