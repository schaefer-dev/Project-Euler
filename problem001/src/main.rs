fn main() {
    let limit = 1000;
    let multiples = vec![3, 5];

    println!("Sum of all multiples of {:?} up to {} is: {}",
    multiples,
    limit,
    sum_of_multiples(&multiples, &limit));
}

fn sum_of_multiples(multiples: &Vec<i32>, limit: &i32) -> i32 {
    let mut result:i32 = 0;

    for x in 0..*limit {
        for dividor in multiples {
            if x % dividor == 0 {
                result += x;
                break;
            }

        }
    }
    result
}
