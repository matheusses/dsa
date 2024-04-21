def call_a():
    print('call a')
    call_b()
    print('pop a')

def call_b():
    print('call b')
    call_c()
    print('pop b')

def call_c():
    print('call c')
    print('pop c')

call_a()