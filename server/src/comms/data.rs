
#[derive(Debug)]
pub enum Direction {
    North,
    East,
    South,
    West,
}

#[derive(Debug)]
pub enum Request {
    Move(Direction),
    RequestPlayerId,
}

#[derive(Debug)]
pub struct UserRequests {
    pub id : u32,
    pub requests : Vec<Request>,
}