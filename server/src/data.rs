
#[derive(Copy, Clone)]
pub enum ProcComm<T> {
    Message(T),
    Stop,
}

#[derive(Copy, Clone)]
pub struct Stop { }