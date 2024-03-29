#Quiz 6 - Forward Pass and Backpropagation

def sigmoid(x):
    return 1.0 / (1 + e ** (-1 *x))

# for function f(x, y) = (x + sigmoid(y)) / (sigmoid(x) + (x + y) ** 2)
def f(x, y):
    s0 = sigmoid(y)
    s1 = x + s0
    s2 = sigmoid(x)
    s3 = x + y
    s4 = s3 ** 2
    s5 = s2 + s4
    s6 = 1.0 / s5
    L = s1 * s6

    grad_L = 1.0
    grad_s6 = grad_L * s1
    grad_s1 = grad_L * s6
    grad_x = grad_s1
    grad_s0 = grad_s1
    grad_y = grad_s0 * (1 - y) * y
    grad_s5 = -1/ (s5 ** 2) * grad_s6
    grad_s2 = grad_s5
    grad_s4 = grad_s5
    grad_s3 = 2 * s3 * grad_s4
    grad_x += grad_s3
    grad_y += grad_s3
