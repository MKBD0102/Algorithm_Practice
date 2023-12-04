def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    codes = letter.split(" ")
    # return ''.join([morse.get(k) for k in codes])
    # 리스트 컴프리헨션 대신 제너레이터 표현식 사용
    morse_generator = (morse.get(k) for k in codes)
    return ''.join(morse_generator)