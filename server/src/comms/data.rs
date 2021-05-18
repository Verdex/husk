
#[derive(Debug)]
pub enum Direction {
    North,
    East,
    South,
    West,
}

#[derive(Debug)]
pub enum Request {
    Move(Direction) 
}

#[derive(Debug)]
pub struct UserRequests {
    id : u32,

}