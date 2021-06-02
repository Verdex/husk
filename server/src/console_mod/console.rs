
use std::io;

pub fn start_blocking() {

    let stdin = io::stdin();
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