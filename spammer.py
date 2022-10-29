from genericpath import samefile
import pyautogui as py
import time



def header():
    print("------------------------")


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        
    
    print("00:00")
    print("Done...")


def countdown_input():
    time_in = input("Hitung mundur [in sec]: ")
    
    mulai = ''
    while mulai != 'y' or mulai != 'n':
        mulai = input("Mulai [y/n]: ")
        if mulai == 'y':
            break
        elif mulai == 'n':
            exit()
        
        print("Pilihan tidak ada!")

    
    return int(time_in)


def spammer( jumlahSpam, mulaiSpam ):
    for i in range( jumlahSpam ):
        py.write( "Ini pesan ke-" + str(i+mulaiSpam) )
        # py.write( str(i+mulaiSpam) + ". Ayaang" )
        py.press( 'Enter' )

def spammerFromFile(jumlahSpam):
    # change 'assets/coba.txt' to use custom file
    spamFile = open('assets/try.txt', 'r')
    index = 1

    for i in spamFile:
        py.write(i)
        py.press('Enter')

        if index == jumlahSpam:
            break

        index += 1


def setStart():
    timeStart = input("Mulai dari [1 - @]: ")
    return int(timeStart)


def setSpam():
    spamText = input("Jumlah pesan [ex.120]: ")
    return int(spamText)

def pilih():
    pilihan = input("Gunakan file [y/n]?: ")
    if pilihan == 'y':
        return True
    else:
        return False


def runSpammer():
    # main program
    # input pilihan apakah menggunakan file
    inputPilih = pilih()

    if inputPilih == True:
        header()
        jumlahSpam = setSpam()
        time_in = countdown_input()
        header()
        countdown( time_in )
        spammerFromFile( jumlahSpam )
    else:
        header()
        time_start = setStart()
        jumlahSpam = setSpam()
        header()
        time_in = countdown_input()
        countdown( time_in )
        header()
        spammer(jumlahSpam, time_start )


# run spammer
runSpammer()