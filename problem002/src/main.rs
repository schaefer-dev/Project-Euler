fn main() {
    let limit:u64 = 4_000_000;

    println!("the result is {}", fibonacci_sequence_even_sum(&limit));
}

fn fibonacci_sequence_even_sum(limit: &u64) -> u64{
    let mut result:u64 = 0;

    let mut fib = Fibonacci {fib1: 1, fib2: 2};

    while fib.smaller_than(&limit) {
        if fib.is_even() {
            result += fib.fib2;
        }
        fib.next();
    }

    result
}

struct Fibonacci {
    fib1: u64,
    fib2: u64,
}

impl Fibonacci {

    // calculate next fibonacci number
    fn next(&mut self) -> () {
        let help = self.fib2;
        self.fib2 = self.fib2 + self.fib1;
        self.fib1 = help;
    }

    fn smaller_than(&self, limit: &u64) -> bool {
        if self.fib1 < *limit {
            return true;
        }
        false
    }

    fn is_even(&self) -> bool {
        if self.fib2 % 2 == 0 {
            return true;
        }
        false
    }
}