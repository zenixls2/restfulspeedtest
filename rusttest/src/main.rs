extern crate iron;
use iron::prelude::*;
use iron::status;

fn main() {
    Iron::new(|_: &mut Request| {
        Ok(Response::with((status::Ok, "Hello")))
    }).http("0.0.0.0:8080").unwrap();
}
