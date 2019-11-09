/**
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 *
 * I've taken my solution from this page: https://www.mathsisfun.com/prime-factorization.html
 * I'm basically generating a factor tree from the bottom up. Starting with
 * the smallest factor (which will always be prime) and working my way
 * up the tree.
 */

fn main() {
    let input:u64 = 600_851_475_143;
    println!("result is: {}", is_prime(&input));
}

// naive prime check implementation
fn is_prime(number: &u64) -> bool {
    for dividor in 2..(*number/2) {
        if *number % dividor == 0 {
            // found a valid dividor
            return false;
        }
    }
    return true;
}