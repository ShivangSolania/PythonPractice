def timeConversion(s):
    if s[-2:]=='AM':
        if s[:2]=='12':
            return f'00:{s[2:8]}'
        else:
            return s[:8]
    else:
        if s[:2]!='12':
            return f'{int(s[:2])+12}{s[2:8]}'
        else:
            return s[:8]
u=input()
print(timeConversion(u))