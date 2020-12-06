def timeConverter(seconds):
    """
    Fungsi timeConverter dibuat dengan melakukan perhitungan standar secara matematik menggunakan
    fungsi math.floor untuk melakukan pembulatan hasil bagi ke bawah. Fungsi logika if else digunakan
    untuk mengatur agar tampilan output akan memunculkan 01, 02, 03 , dst... ketika variabel bernilai satuan
    (1-9). Fungsi try except digunakan sebagai error handling jika input yang dimasukkan tidak sesuai
    """
    try:
        if int(seconds) > 359999 or int(seconds) < 0 or '.' in str(seconds):
            output = 'Invalid input!'
        else:
            import math

            sec_hours = 3600
            sec_mins = 60

            hours = math.floor(seconds/sec_hours)
            mins = math.floor((seconds - hours*sec_hours)/sec_mins)
            seconds_left = seconds - hours*sec_hours - mins*sec_mins

            if len(str(hours)) == 1:
                hours = f'0{hours}'
            else:
                hours = hours

            if len(str(mins)) == 1:
                mins = f'0{mins}'
            else:
                mins = mins

            if len(str(seconds_left)) == 1:
                seconds_left = f'0{seconds_left}'
            else:
                seconds_left = seconds_left

            output = f'{hours}:{mins}:{seconds_left}'
    except ValueError:
        output = 'Invalid input!'
        
    return output

print(timeConverter(-1))
print(timeConverter('Jam'))
print(timeConverter(100.5))
print(timeConverter(360000))
print(timeConverter(3677))
print(timeConverter(359999))