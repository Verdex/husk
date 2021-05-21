
use std::io::{Error, ErrorKind, Cursor};

use byteorder::{NetworkEndian, ReadBytesExt};

use super::data::{Request, Direction};

pub fn parse_request(input : &mut Cursor<&[u8]>) -> std::io::Result<Vec<Request>> {
    let mut requests = vec! [];
    loop {
        let maybe_opcode = input.read_u16::<NetworkEndian>();
        if matches!(maybe_opcode, Err(_)) {
            return Ok(requests);
        }

        match maybe_opcode.unwrap() {
            0x0001 => { requests.push(parse_move(input)?) }, 
            x => { return e(format!("Failed to parse Request because of unknown value: {}", x)); },
        }
    }
}

pub fn parse_id(input : &mut Cursor<&[u8]>) -> std::io::Result<u32> {
    input.read_u32::<NetworkEndian>()
}

pub fn parse_length(input : &mut Cursor<&[u8]>) -> std::io::Result<u32> {
    input.read_u32::<NetworkEndian>()
}

fn parse_move(input : &mut Cursor<&[u8]> ) -> std::io::Result<Request> {
    let w = |d| Ok(Request::Move(d));

    let direction = input.read_u8()?;
    match direction {
        0x01 => w(Direction::North), 
        0x02 => w(Direction::East), 
        0x03 => w(Direction::South), 
        0x04 => w(Direction::West),
        x => e(format!("Failed to parse move because of unknown value: {}", x)),
    }
}

fn e<T>(v : String) -> std::io::Result<T> {
    Err(Error::new(ErrorKind::Other, v))
}

#[cfg(test)]
mod test {
    use super::*;

    use byteorder::{NetworkEndian, WriteBytesExt};

    #[test]
    fn should_parse_move_request() -> std::io::Result<()> {
        let mut b = vec![];
        b.write_u16::<NetworkEndian>(0x0001)?;
        b.push(0x01);

        let rs = parse_request(b)?;
        assert_eq!( rs.len(), 1 );
        assert!(matches!(rs[0], Request::Move(Direction::North)));

        Ok(())
    }
}