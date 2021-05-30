
pub enum ProcComm<T> {
    Message(T),
    Stop,
}