use std::env;
use std::process;



mod b64 {
	macro_rules! BYTE_TO_B64CHAR {
		($expression:expr) => {
			POOL[($expression) as usize] as char
		};
	}

	fn b64char_to_bytes(c: u8) -> u32 {
		let mut i:usize = 0;
		loop {
			if i >= POOL.len(){ return 0; }
			if POOL[i] == c{
				return i as u32;
			}
			i += 1 ;
		}
	}

	static POOL: &[u8] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".as_bytes() ;

	pub fn decode(input: &str) -> String { //Will panic if string is invalid length
		let s = input.as_bytes();
		if s.len() % 4 != 0 {
			eprintln!("Invalid Base 64 encoded string - wrong length");
			std::process::exit(1);
		}
	    let mut out_string = String::new();

		let mut i: usize = 0;
		loop {
			if i >= s.len(){ break;	}
			
			let x : u32 = b64char_to_bytes(s[i ]).wrapping_shl(18)
							| ( b64char_to_bytes(s[i + 1]) << 12 )
							| ( b64char_to_bytes(s[i + 2]) << 6)
							| ( b64char_to_bytes(s[i + 3]) << 0);
			
			for j in 0..3 {
				if s[i+j+1] == ('=' as u8) { break };
				out_string.push((x >> (16-(j*8))) as u8 as char);
			}
			
			i += 4;
		}
		return out_string;		
	}

	pub fn encode(input: &str) -> String {
		let s = input.as_bytes();
	    let mut out_string = String::new();

		let mut i = 0;
		loop {
			if i >= s.len() { break; }
			// Fill in zeros if string is short
			let si1 = if i+1 < s.len() { s[i+1] } else { 0 };
			let si2 = if i+2 < s.len() { s[i+2] } else { 0 };
			
			let x: u32 = ((s[i] as u32) << 16) | ((si1 as u32) << 8) | (si2 as u32);

			
			for j in 0..4 {
				if i+j > s.len(){ out_string.push('=') } //put in '=' if string is short
				else {
					out_string.push( BYTE_TO_B64CHAR!(
					((x >> (6*(3-j))) & 0b111111)
					));
				}
			}
			i += 3;
		}
		return out_string;
	}
}

fn main() {
    let args: Vec<String> = env::args().collect();
	if args.len() < 3 {
		eprintln!("Not enough arguments provided");
		process::exit(1);
	}
	let action : &str = &args[1];
	let s: &str = &args[2];
	
	match action {
        "encode" | "e" => println!("{}", b64::encode(s)),
        "decode" | "d" => println!("{}", b64::decode(s)),
		_ => { eprintln!("Command \"{}\" not recognized", action); process::exit(1); },
    }
}
