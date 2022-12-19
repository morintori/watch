# This is a sample Python script.
import time
import tkinter as tk

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# r_list=reading.split('\n')
# print(r_list[1][0])
#
# print(reading)
# print(watch)

def numtoascii(num): # this translates numbers into ascii
    match num:
        case 0:
            toprow = ' _ '
            midrow = '| |'
            botrow = '|_|'
        case 1:
            toprow = '   '
            midrow = '  |'
            botrow = '  |'
        case 2:
            toprow = ' _ '
            midrow = ' _|'
            botrow = '|_ '
        case 3:
            toprow = ' _ '
            midrow = ' _|'
            botrow = ' _|'
        case 4:
            toprow = '   '
            midrow = '|_|'
            botrow = '  |'
        case 5:
            toprow = ' _ '
            midrow = '|_ '
            botrow = ' _|'
        case 6:
            toprow = ' _ '
            midrow = '|_ '
            botrow = '|_|'
        case 7:
            toprow = ' _ '
            midrow = '  |'
            botrow = '  |'
        case 8:
            toprow = ' _ '
            midrow = '|_|'
            botrow = '|_|'
        case 9:
            toprow = ' _ '
            midrow = '|_|'
            botrow = '  |'
        case _:
            toprow = ' XD'
            midrow = ' D:'
            botrow = ':D '

    return toprow,midrow,botrow

class Watch(tk.Frame): #class that holds my watch

    global watch_tiem

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master =master
        self.label = tk.Label(text='',justify=tk.LEFT, font=('Courier',10))
        self.label.place(relx=0.5,rely=0.5,anchor='center')
        self.gib_time()

    # def default_watch():
    #     f = open('watch.txt', 'r')
    #     wt = ''
    #     rr = ''
    #     wb = ''
    #     for (ln, line) in enumerate(f):
    #         if ln < 9:
    #             wt = wt + ''.join(line)
    #         elif (ln >= 9 and ln < 12):
    #             rr = rr + ''.join(line)
    #         else:
    #             wb = wb + ''.join(line)
    #
    #     return(wt,rr,watchbot)



    def gib_time(self): # get the time and change the number from the watch in the template
        f = open('watch.txt', 'r')
        wt = ''
        rr = ''
        wb = ''
        #watch is divided into three, top and bottom parts does not change but the middle contains the digits
        # so that will have to be changed
        for (ln, line) in enumerate(f):
            if ln < 9:
                wt = wt + ''.join(line)
            elif (ln >= 9 and ln < 12):
                rr = rr + ''.join(line)
            else:
                wb = wb + ''.join(line)

        hr = time.localtime().tm_hour
        h1 = hr//10
        h2 = hr%10
        m = time.localtime().tm_min
        m1 = m//10
        m2 = m%10
        h1tr,h1mr,h1br = numtoascii(h1)
        ind11 = 5
        ind12 = 7
        ind21 = 33
        ind22=35
        ind31 = 63
        ind32=65
        # rr[ind11:ind12] = h1tr
        # rr[ind21:ind22]=h1mr
        # rr[ind31:ind32] = h1br
        h2tr,h2mr,h2br = numtoascii(h2)#translating time to ascii
        # rr[ind11+3:ind12+3] = h2tr
        # rr[ind21+3:ind22+3] = h2mr
        # rr[ind31+3:ind32+3] = h2br
        m1tr, m1mr, m1br = numtoascii(m1)
        # rr[ind11 + 9:ind12 + 9] = m1tr
        # rr[ind21 + 9:ind22 + 9] = m1mr
        # rr[ind31 + 9:ind32 + 9] = m1br
        m2tr, m2mr, m2br = numtoascii(m2)
        # rr[ind11 + 13:ind12 + 13] = m2tr
        # rr[ind21 + 13:ind22 + 13] = m2mr
        # rr[ind31 + 13:ind32 + 13] = m2br
        # the indexing of the original ascii art combined with the new readout
        nrr = (rr[0:ind11]+h1tr+h2tr +"   "+m1tr+ " " + m2tr +rr[ind12+14:ind21] + h1mr + h2mr + " . " + m1mr +" "
            + m2mr + rr[ind22 + 14:ind31] + h1br + h2br + " . " + m1br + " " + m2br + rr[ind32 + 14:])

        watch_tiem = wt + nrr + wb #add the pieces of the watch togther
        self.label.configure(text=watch_tiem)
        self.after(1000,self.make_dots_beep)
        self.after(60000,self.gib_time) #checks every 30 seconds but really could be a minute

    def make_dots_beep(self):
        #dots located 252,282
        curr_tiem=self.label['text']
        if '.' in curr_tiem[252]:
            new_tiem = curr_tiem[0:252] +' ' + curr_tiem[253:282] + ' ' +curr_tiem[283:]
        else:
            new_tiem = curr_tiem[0:252] +'.' + curr_tiem[253:282] + '.' +curr_tiem[283:]

        self.label.configure(text=new_tiem)
        self.after(1000, self.make_dots_beep)




# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




window=tk.Tk()
watch = Watch(window)
window.wm_title('Casio Watch')
window.geometry("500x500")
window.after(60000,watch.gib_time)
#window.after(1000,watch.make_dots_beep)
window.mainloop()
# label=tk.Label(text=watch,justify=tk.LEFT,font=("Courier",10))
#
# label.pack()
#
#
# window.mainloop()

# import sched,time
# s= sched.scheduler(time.time,time.sleep)
# def gib_time(s):
#     hr = time.localtime().tm_hour
#     m =  time.localtime().tm_min
#     if m <10:
#         m ='0'+str(m)
#     print(str(hr) +':'+ str(m) )
#     s.enter(60,1,gib_time, (s,))
#
# s.enter(60,1,gib_time,(s,))
# s.run()