def square_and_filter(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)


square_and_filter(1, 10)