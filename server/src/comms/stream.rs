
use std::io::{Read, Error, ErrorKind, Cursor};
use std::net::TcpStream;

use super::data::{Request, UserRequests};
use super::parse::{parse_request, parse_id, parse_length};

pub fn read_requests(stream : &mut TcpStream) -> std::io::Result<UserRequests> {
    let mut buffer = vec![];
    stream.read_to_end(&mut buffer)?;

    if buffer.len() < 9 {
        return e(format!("Requests wasn't long enough.  Found {} bytes.", buffer.len()));
    }

    let buffer_length : u32 = (buffer.len() as u32) - 9;

    if buffer[0] != 0 {
        return e(format!("Found unknown packet version: {}", buffer[0]));
    }

    let mut input = Cursor::new(buffer);

    let id = parse_id(&mut input)?;
    let length = parse_length(&mut input)?;

    if buffer_length != length {
        return e(format!("Expected packet length {}, but found length {}", length, buffer_length));
    }

    let requests = parse_request(&mut input)?;

    Ok(UserRequests { id, requests })
}


fn e<T>(v : String) -> std::io::Result<T> {
    Err(Error::new(ErrorKind::Other, v))
}