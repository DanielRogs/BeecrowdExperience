n = int(input())



for j in range(1,n+1):
    LED = 0
    x = input()
    for a in range(0,len(x)):
        if x[a] == '1':
            LED = LED + 2
        if x[a] == '2':
            LED = LED + 5
        if x[a] == '3':
            LED = LED + 5
        if x[a] == '4':
            LED = LED + 4
        if x[a] == '5':
            LED = LED + 5
        if x[a] == '6':
            LED = LED + 6
        if x[a] == '7':
            LED = LED + 3
        if x[a] == '8':
            LED = LED + 7
        if x[a] == '9':
            LED = LED + 6
        if x[a] == '0':
            LED = LED + 6
    print('{} leds'.format(LED))
