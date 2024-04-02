def elevator(left, right, call):
    return 'right' if abs(call-right) == abs(call-left) else 'left' if abs(call-left)<abs(call-right) else 'right'
