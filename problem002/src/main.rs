fn main() {
    let limit:u64 = 4_000_000;

    println!("the result is {}", fibonacci_sequence_even_sum(&limit));
}

fn fibonacci_sequence_even_sum(limit: &u64) -> u64{
    let mut result:u64 = 0;

    let mut fib = Fibonacci {fib1: 1, fib2: 2};
    let mut help:u64;

    while fib.fib2 < *limit {
        if fib.fib2 % 2 == 0 {
            result += fib.fib2;
        }

        help = fib.fib2;
        // calculate next fibunaci number
        fib.fib2 = fib.fib2 + fib.fib1;
        fib.fib1 = help;
    }

    result
}

struct Fibonacci {
    fib1: u64,
    fib2: u64,
}

