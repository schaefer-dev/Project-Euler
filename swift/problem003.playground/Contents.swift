func is_prime_naive(x: Int) -> Bool {
    
    // Basic primes 2 and 3
    if (x == 2 || x == 3) {
        return true
    }
    
    // Number is even -> not prime
    if (x % 2 == 0) {
        return false
    }
    
    // all other Numbers smaller than 9 are prime
    if (x < 9) {
        return true
    }
    
    // r = square root of x
    let double_x = Double(x)
    let r = Int(double_x.squareRoot())
    var f = 5
    
    while (f <= r) {
        if (x % f == 0){
            return false
        }
        if (x % (f + 2) == 0) {
            return false
        }
        f += 6
    }
    return true
}


var input_number = 600851475143
var biggest_prime_devider = 1

for i in 2..<input_number {
    if (input_number % i == 0) {
        let possible_devider = input_number / i
        if (is_prime_naive(x: possible_devider)) {
            biggest_prime_devider = possible_devider
            break
        }
    }
}

print(biggest_prime_devider)


