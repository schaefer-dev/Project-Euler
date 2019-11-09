// Helper function to update x and y values to the following fibunacci pair
func fib(x: inout Int, y: inout Int) {
    let fib_sum = x + y
    x = y
    y = fib_sum
}

var fib1 = 0
var fib2 = 1

var even_fib_sum = 0

while (fib2 <= 4000000) {
    if (fib2 % 2 == 0) {
        even_fib_sum += fib2
    }
    
    // Caculate next fib numbers
    fib(x: &fib1, y: &fib2)
}

print(even_fib_sum)
