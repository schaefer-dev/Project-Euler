// You should probably not execute this in playground, performance will suffer a LOT compared to regular commandline execution of compiled code

func is_palindrom_base_10(number: Int) -> Bool {
    var digit_array: [Int] = [0, 0, 0, 0, 0, 0]
    var array_length = 0
    var number_remaining = number
    
    // write number in array for single digits
    while number_remaining > 0 {
        digit_array[array_length] = (number_remaining % 10)
        
        array_length += 1
        number_remaining /= 10
    }
    
    // checking palindrom now
    var top_index = array_length - 1
    var lower_index = 0
    
    while (top_index > lower_index) {
        if (digit_array[lower_index] != digit_array[top_index]) {
            return false
        }
        lower_index += 1
        top_index -= 1
    }
    return true
}

func is_palindrom_base_2(number: Int) -> Bool {
    var digit_array = Array(repeating: false, count: 20)
    var array_length = 0
    var number_remaining = number
    
    // write number in array for single digits
    while number_remaining > 0 {
        if (number_remaining % 2) == 1 {
            digit_array[array_length] = true
        }
        
        array_length += 1
        number_remaining /= 2
    }
    
    // checking palindrom now
    var top_index = array_length - 1
    var lower_index = 0
    
    while (top_index > lower_index) {
        if (digit_array[lower_index] != digit_array[top_index]) {
            return false
        }
        lower_index += 1
        top_index -= 1
    }
    return true
}

is_palindrom_base_10(number: 585)
is_palindrom_base_2(number: 585)


var sum_solution = 0

for n in 3..<1000000 {
    if (is_palindrom_base_10(number: n) && is_palindrom_base_2(number: n)) {
        sum_solution += n
    }
}

print(sum_solution)
