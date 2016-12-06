extern crate mioco;
extern crate httparse;

use std::io::{self, Write, Read};
use mioco::tcp::TcpListener;
use std::str::FromStr;

const RESPONSE: &'static str = "HTTP/1.1 200 OK\r
Content-Length: 8\r
\r
Hello\r
\r";

fn main() {
    let addr = FromStr::from_str("0.0.0.0:8080").unwrap();
    let listener = TcpListener::bind(&addr).unwrap();
    mioco::start(move || {
        for _ in 0..mioco::thread_num() {
            let listener = listener.try_clone().unwrap();
            mioco::spawn(move || -> io::Result<()> {
                loop {
                    let conn = try!(listener.accept());
                    mioco::spawn(move || -> io::Result<()> {
                        let mut buf_i = 0;
                        let mut buf = [0u8; 1024];
                        let mut headers = [httparse::EMPTY_HEADER; 16];
                        let mut conn = conn;
                        loop {
                            let len = try!(conn.read(&mut buf[buf_i ..]));
                            if len == 0 {
                                return Ok(());
                            }
                            buf_i += len;
                            let mut req = httparse::Request::new(&mut headers);
                            let res = req.parse(&buf[0..buf_i]).unwrap();
                            if res.is_complete() {
                                match req.path {
                                    Some("/") => {
                                        let _ = try!(conn.write_all(&RESPONSE.as_bytes()));
                                        buf_i = 0
                                    }
                                    Some(&_) => {
                                    }
                                    None => {
                                    }
                                }
                            }
                        }
                    });
                }
            });
        }
    }).unwrap();
}
