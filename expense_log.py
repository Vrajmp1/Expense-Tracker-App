#expense log entry

import csv, os, sys
sys.path.insert(0,'C:\\Users\\Patel\\OneDrive\\Desktop\\Python_Files')
import date_checker as dc
import tkinter as tk
from datetime import date

class App(tk.Tk):
    def make_num(self,num):
        new = ''
        for i in num:
            if i=='$' or i==' ' or i.isalpha() == True:
                pass
            else:
                new+=i
        if len(new)==0:
            return 0
        else:
            return float(new)
    
    def initial(self):
        try:
            self.contain_d.destroy()
            self.geometry('700x400')
            self.limit = self.max
        except:
            pass

        try:
            self.contain_s.destroy()
        except:
            pass
        
        self.columnconfigure(index=0,weight=1)
        self.columnconfigure(index=1,weight=3)
        self.columnconfigure(index=2,weight=1)
        self.rowconfigure(index=0,weight=1)
        self.rowconfigure(index=1,weight=1)
        self.rowconfigure(index=2,weight=1)
        self.rowconfigure(index=3,weight=1)
        self.rowconfigure(index=4,weight=1)

        self.header = tk.Label(self,text='Expense Log',font='Arial 50')
        self.header.grid(row=0,column=0,columnspan=2, sticky='N',pady=20)

        self.enter = tk.Label(self,text="Name of Expense:",font="Arial 20")
        self.enter.grid(row=1,column=0,sticky="NE",padx="20")

        self.expense = tk.StringVar(self)
        self.entry = tk.Entry(self,textvariable = self.expense,font="Arial 20")
        self.entry.grid(row=1,column=1,sticky="NW")

        self.amount_label = tk.Label(self,text="Amount:",font="Arial 20")
        self.amount_label.grid(row=2,column=0,sticky="NE",padx="20")

        self.amount = tk.StringVar(self)
        self.entry_amount = tk.Entry(self,textvariable = self.amount,font="Arial 20")
        self.entry_amount.grid(row=2,column=1,sticky="NW")

        self.submit = tk.Button(self,text="Submit",font='Arial 20',command=self.append)
        self.submit.grid(row=3,column=1,sticky="NW")

        self.save_but = tk.Button(self,text="Save",font='Arial 10',command=self.save)
        self.save_but.grid(row=4,column=2,sticky="SE")

        self.display_t = tk.Button(self,text="Display Transactions",font='Arial 10',command= lambda: self.clear('t'))
        self.display_t.grid(row=4,column=1,sticky="SW")

        self.display_s = tk.Button(self,text="Statistics",font='Arial 10',command= lambda: self.clear('s'))
        self.display_s.grid(row=4,column=0,sticky="SW")
    #Statistics Screen----------------------------------------------------------------------------------------------------------------
    def sum_it(self):
        self.tmp = []
        total = 0
        choice = self.per_var.get()
        category = self.type_var.get()
        if category == 'Other':
            category = self.other1.get()
        if choice == 'All':
            for i in range(0,len(self.data)):
                if self.data[i][2]==category or category=='All':
                    val = self.make_num(self.data[i][3])
                    total += val
        num = 0
        for i in dc.month_to_digit:
            if choice == i:
                num = int(dc.month_to_digit[i])
                break
        print(num)
        if num != 0:
            for i in range(0,len(self.data)):
                date = self.data[i][1].split('-')
                if len(date)==1:
                    date = self.data[i][1].split('/')
                    m,d,y = int(date[0]),int(date[1]),int(date[2])
                else:
                    y,m,d = int(date[0]),int(date[1]),int(date[2])
                    
                if dc.check_between(num,1,2022,num,31,2022,m,d,y) == True:
                    if self.data[i][2] == category or category=='All':
                        val = self.make_num(self.data[i][3])
                        total += val
                        
        elif choice == 'Custom':
            #----------------------Input Validation for dates-------------------------#
            wrong = 0
            try:
                date1 = self.date1.get().split('/')
                m1,d1,y1 = int(date1[0]),int(date1[1]),int(date1[2])
                if m1<1 or m1>12:
                    wrong = 1
                    self.date1.set('month value invalid')
                elif d1<1 or d1>dc.days_in_months[m1]:
                    wrong = 1
                    self.date1.set('day value invalid')       
            except:
                self.date1.set('Enter in form MM/DD/YYYY')
                wrong = 1
            try:
                date2 = self.date2.get().split('/')
                m2,d2,y2 = int(date2[0]),int(date2[1]),int(date2[2])
                if m2<1 or m2>12:
                    wrong = 1
                    self.date2.set('month value invalid')
                elif d2<1 or d2>dc.days_in_months[m2]:
                    wrong = 1
                    self.date2.set('day value invalid')
            except:
                self.date2.set('Enter in form MM/DD/YYYY')
                wrong = 1
            if wrong==1:
                print('Error in reading dates')
                return
            #-------------------------------------------------------------------------#
                

            for i in range(0,len(self.data)):
                date = self.data[i][1].split('-')
                if len(date)==1:
                    date = self.data[i][1].split('/')
                    m,d,y = int(date[0]),int(date[1]),int(date[2])
                else:
                    y,m,d = int(date[0]),int(date[1]),int(date[2])
                    
                if dc.check_between(m1,d1,y1,m2,d2,y2,m,d,y) == True:
                    if self.data[i][2] == category or category=='All':
                        val = self.make_num(self.data[i][3])
                        total += val
            
        print(total)
        self.sum.set('$'+format(total,',.2f'))
        return '$'+format(total,',.2f')
    
    def custom_entry(self,*args):
        self.sum.set('$__.__')
        if self.per_var.get() == 'Custom':
            BG = '#B787BF'
            self.custom_frame = tk.Frame(self.contain_s,bg=BG)
            self.custom_frame.grid(row=3,column=0)
            
            self.custom_frame.rowconfigure(index=0,weight=1)
            self.custom_frame.rowconfigure(index=1,weight=1)
            self.custom_frame.rowconfigure(index=2,weight=1)
            self.custom_frame.rowconfigure(index=3,weight=1)
            self.custom_frame.columnconfigure(index=0,weight=1)
            
            self.date1_label = tk.Label(self.custom_frame,text='Enter Start Date (MM/DD/YYYY):',font='Arial 8',bg = BG)
            self.date1_label.grid(row=0,column=0,pady=(0,5),columnspan=3)

            self.date2_label = tk.Label(self.custom_frame,text='Enter End Date (MM/DD/YYYY):',font='Arial 8',bg = BG)
            self.date2_label.grid(row=2,column=0,pady=(5,5),columnspan=3)
            
            #------------------Entry Widgets for Date1------------------------#
            months_options = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

            self.date1 = tk.StringVar(self.custom_frame)
            self.date1_enter = tk.Entry(self.custom_frame,textvariable=self.date1,width=20,font='Arial 8')
            self.date1_enter.grid(row=1,column=0)

            #------------------Entry Widgets for Date1------------------------#
            self.date2 = tk.StringVar(self.custom_frame)
            self.date2_enter = tk.Entry(self.custom_frame,textvariable=self.date2,width=20,font='Arial 8')
            self.date2_enter.grid(row=3,column=0)
            
        else:
            try:
                self.custom_frame.destroy()
            except:
                pass

            
                                 
    def other_entry(self,*args):
        self.sum.set('$__.__')
        if self.type_var.get() == 'Other':
            BG = '#B787BF'
            self.other_frame = tk.Frame(self.contain_s,bg=BG)
            self.other_frame.grid(row=3,column=1)
            
            self.other_frame.rowconfigure(index=0,weight=1)
            self.other_frame.columnconfigure(index=0,weight=1)
            self.other_frame.columnconfigure(index=1,weight=2)
            
            self.other_label = tk.Label(self.other_frame,text='Enter type: ',font='Arial 8',bg = BG)
            self.other_label.grid(row=0,column=0,pady=(0,5),columnspan=1)
            
            #------------------Entry For Type Filter------------------------#
            self.other1 = tk.StringVar(self.other_frame)
            self.other1_enter = tk.Entry(self.other_frame,textvariable=self.other1,width=20,font='Arial 8')
            self.other1_enter.grid(row=0,column=1)
            
        else:
            try:
                self.other_frame.destroy()
            except:
                pass
    
    def display_stats(self):
        BG = '#B787BF'
        self.geometry('700x400')
        
        self.contain_s = tk.Frame(self,bg=BG,width=700,height=400)
        self.contain_s.pack()
        self.contain_s.grid_propagate(False)

        self.contain_s.columnconfigure(index=0,weight=1)
        self.contain_s.columnconfigure(index=1,weight=1)
        self.contain_s.columnconfigure(index=2,weight=1)
        
        self.contain_s.rowconfigure(index=0,weight=1)
        self.contain_s.rowconfigure(index=1,weight=1)
        self.contain_s.rowconfigure(index=2,weight=1)
        self.contain_s.rowconfigure(index=3,weight=1)
        self.contain_s.rowconfigure(index=4,weight=1)
        self.contain_s.rowconfigure(index=5,weight=1)
        self.contain_s.rowconfigure(index=6,weight=1)

        self.header_stats = tk.Label(self.contain_s,text="Display Statistics",font="Arial 50",bg=BG)
        self.header_stats.grid(row=0,column=0,columnspan=3)

        '''self.header_sum = tk.Label(self.contain_s,text='Sum',font='Arial 25 underline',bg=BG)
        self.header_sum.grid(row=1,column=0,sticky='N')'''

        self.header_period = tk.Label(self.contain_s,text='Period',font='Arial 25 underline',bg=BG)
        self.header_period.grid(row=1,column=0,sticky='N')
        
        months = ['All','Apr','May','Jun','Jul','Aug','Sep','Oct','Custom']
        self.per_var = tk.StringVar(self.contain_s,months[0])
        self.per_var.trace('w',self.custom_entry)
        self.menu_period = tk.OptionMenu(self.contain_s,self.per_var,*months)
        self.menu_period.grid(row=2,column=0,sticky='N')
        
        self.header_classification = tk.Label(self.contain_s,text='Filter',font='Arial 25 underline',bg=BG)
        self.header_classification.grid(row=1,column=1,sticky='N')
        
        types = ['All','Gas','Milk','Grocery','Rent','Other']
        self.type_var = tk.StringVar(self.contain_s,types[0])
        self.type_var.trace('w',self.other_entry)
        self.menu_period = tk.OptionMenu(self.contain_s,self.type_var,*types)
        self.menu_period.grid(row=2,column=1,sticky='N')

        self.sum_but = tk.Button(self.contain_s,text='Sum',font='Arial 25',command=self.sum_it,bg=BG)
        self.sum_but.grid(row=2,column=2,sticky='S')

        self.sum = tk.StringVar(self.contain_s)
        self.sum_label = tk.Label(self.contain_s,textvariable=self.sum,font='Arial 25',bg=BG)
        self.sum_label.grid(row=6,column=1,sticky='S')

        self.go_back = tk.Button(self.contain_s,text="Back",command = self.initial,bg=BG)
        self.go_back.grid(row=6,column=2,sticky="SE")
    #----------------------------------------------------------------------------------------------------------------------------------
    def clear(self, option):
        self.header.destroy()

        self.enter.destroy()

        self.entry.destroy()

        self.amount_label.destroy()

        self.entry_amount.destroy()

        self.submit.destroy()

        self.save_but.destroy()

        self.display_t.destroy()

        self.display_s.destroy()

        if option=='t':
            self.create_display() #this is the display transactions screen
        else:
            self.display_stats()

    def del_entry(self,num):
        del self.data[self.limit-num]
        self.max -= 1
        self.limit=self.max
        self.contain_d.destroy()
        print(self.limit-1)
        self.create_display()
    #Scroll Up and Down functions for create_display transactions screen -------------------------------------------------------
    #needs little bit of work. Not perfect yet. Once scroll is used, delete doesn't work.
    def scroll_up(self):
        print('difference:',self.max-self.position)
        if self.max - self.position < self.max:
            self.limit = self.max - self.position
            if self.limit <= self.max:
                self.position -= 1
                self.contain_d.destroy()
                self.create_display()
        else:
            pass

    def scroll_down(self):
        if self.max - self.position > 0:
            self.limit = self.max - self.position
            if self.limit >= 10:
                self.position += 1
                self.contain_d.destroy()
                self.create_display()
        else:
            pass
            
        
    #---------------------------------------------------------------------------------------------------------------------------
        
    def create_display(self):
        self.geometry('900x430')

        if self.position == 0:
            self.max = len(self.data)
            self.limit = self.max
        print(self.limit)
        

        self.contain_d = tk.Frame(self)
        self.contain_d.pack()
        
        self.contain_d.columnconfigure(index=0,weight=1)
        self.contain_d.columnconfigure(index=1,weight=1)
        self.contain_d.columnconfigure(index=2,weight=1)
        self.contain_d.columnconfigure(index=3,weight=1)
        self.contain_d.columnconfigure(index=4,weight=1)
        self.contain_d.columnconfigure(index=5,weight=1)
        
        self.contain_d.rowconfigure(index=0,weight=1)
        self.contain_d.rowconfigure(index=1,weight=1)
        self.contain_d.rowconfigure(index=2,weight=1)
        self.contain_d.rowconfigure(index=3,weight=1)
        self.contain_d.rowconfigure(index=4,weight=1)
        self.contain_d.rowconfigure(index=5,weight=1)
        self.contain_d.rowconfigure(index=6,weight=1)
        self.contain_d.rowconfigure(index=7,weight=1)
        self.contain_d.rowconfigure(index=8,weight=1)
        self.contain_d.rowconfigure(index=9,weight=1)
        self.contain_d.rowconfigure(index=10,weight=1)
        self.contain_d.rowconfigure(index=11,weight=1)
        self.contain_d.rowconfigure(index=12,weight=1)
        self.contain_d.rowconfigure(index=13,weight=1)
        self.contain_d.rowconfigure(index=14,weight=1)
        self.contain_d.rowconfigure(index=15,weight=1)

        
        
        self.header2 = tk.Label(self.contain_d,text="Display Transactions",font="Arial 50")
        self.header2.grid(column=1,row=0,columnspan=5,rowspan=3,pady=(20,40))

        self.date_header = tk.Label(self.contain_d,text="Date",font="Arial 25 underline")
        self.date_header.grid(column=0,row=3,rowspan=2,padx=(0,25))

        self.name_header = tk.Label(self.contain_d,text="Name of Expense",font="Arial 25 underline")
        self.name_header.grid(column=1,row=3,rowspan=2,columnspan=3)

        self.amount_header = tk.Label(self.contain_d,text="Amount",font="Arial 25 underline")
        self.amount_header.grid(column=4,row=3,rowspan=2,sticky='E')

        self.delete_header = tk.Label(self.contain_d,text="Delete",font="Arial 25 underline")
        self.delete_header.grid(column=5,row=3,rowspan=2)

        self.go_back = tk.Button(self.contain_d,text="Back",command = self.initial)
        self.go_back.grid(row=15,column=6,sticky="SE")

        self.contain_d_scroll = tk.Frame(self.contain_d)
        self.contain_d_scroll.rowconfigure(index=0,weight=1)
        self.contain_d_scroll.columnconfigure(index=0,weight=1)
        self.contain_d_scroll.columnconfigure(index=1,weight=1)
        self.up = tk.Button(self.contain_d_scroll,relief='flat',text='↑',font='Arial 20',command=self.scroll_up)
        self.up.grid(row=0,column=0)
        self.down = tk.Button(self.contain_d_scroll,relief='flat',text='↓',font='Arial 20',command=self.scroll_down)
        self.down.grid(row=0,column=1)
        self.contain_d_scroll.grid(row=15,column=5)

        #display recent transactions:
        
        if self.limit>0:
            date1_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date1 = tk.Label(self.contain_d,textvariable=date1_var,font='Arial 15')
            date1.grid(row=5,column=0)

            name1_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name1 = tk.Label(self.contain_d,textvariable=name1_var,font='Arial 15')
            name1.grid(row=5,column=1,columnspan=3)

            amount1_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount1 = tk.Label(self.contain_d,textvariable=amount1_var,font='Arial 15')
            amount1.grid(row=5,column=4,sticky='E')

            del_1 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(1), relief="flat")
            del_1.grid(row=5,column=5)
            
            self.limit -= 1
            
        if self.limit>0:
            date2_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date2 = tk.Label(self.contain_d,textvariable=date2_var,font='Arial 15')
            date2.grid(row=6,column=0)

            name2_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name2 = tk.Label(self.contain_d,textvariable=name2_var,font='Arial 15')
            name2.grid(row=6,column=1,columnspan=3)

            amount2_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount2 = tk.Label(self.contain_d,textvariable=amount2_var,font='Arial 15')
            amount2.grid(row=6,column=4,sticky='E')

            del_2 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(2), relief="flat")
            del_2.grid(row=6,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date3_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date3 = tk.Label(self.contain_d,textvariable=date3_var,font='Arial 15')
            date3.grid(row=7,column=0)

            name3_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name3 = tk.Label(self.contain_d,textvariable=name3_var,font='Arial 15')
            name3.grid(row=7,column=1,columnspan=3)

            amount3_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount3 = tk.Label(self.contain_d,textvariable=amount3_var,font='Arial 15')
            amount3.grid(row=7,column=4,sticky='E')

            del_3 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(3), relief="flat")
            del_3.grid(row=7,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date4_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date4 = tk.Label(self.contain_d,textvariable=date4_var,font='Arial 15')
            date4.grid(row=8,column=0)

            name4_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name4 = tk.Label(self.contain_d,textvariable=name4_var,font='Arial 15')
            name4.grid(row=8,column=1,columnspan=3)

            amount4_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount4 = tk.Label(self.contain_d,textvariable=amount4_var,font='Arial 15')
            amount4.grid(row=8,column=4,sticky='E')

            del_4 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(4), relief="flat")
            del_4.grid(row=8,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date5_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date5 = tk.Label(self.contain_d,textvariable=date5_var,font='Arial 15')
            date5.grid(row=9,column=0)

            name5_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name5 = tk.Label(self.contain_d,textvariable=name5_var,font='Arial 15')
            name5.grid(row=9,column=1,columnspan=3)

            amount5_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount5 = tk.Label(self.contain_d,textvariable=amount5_var,font='Arial 15')
            amount5.grid(row=9,column=4,sticky='E')

            del_5 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(5), relief="flat")
            del_5.grid(row=9,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date6_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date6 = tk.Label(self.contain_d,textvariable=date6_var,font='Arial 15')
            date6.grid(row=10,column=0)

            name6_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name6 = tk.Label(self.contain_d,textvariable=name6_var,font='Arial 15')
            name6.grid(row=10,column=1,columnspan=3)

            amount6_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount6 = tk.Label(self.contain_d,textvariable=amount6_var,font='Arial 15')
            amount6.grid(row=10,column=4,sticky='E')

            del_6 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(6), relief="flat")
            del_6.grid(row=10,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date7_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date7 = tk.Label(self.contain_d,textvariable=date7_var,font='Arial 15')
            date7.grid(row=11,column=0)

            name7_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name7 = tk.Label(self.contain_d,textvariable=name7_var,font='Arial 15')
            name7.grid(row=11,column=1,columnspan=3)

            amount7_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount7 = tk.Label(self.contain_d,textvariable=amount7_var,font='Arial 15')
            amount7.grid(row=11,column=4,sticky='E')

            del_7 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(7), relief="flat")
            del_7.grid(row=11,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date8_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date8 = tk.Label(self.contain_d,textvariable=date8_var,font='Arial 15')
            date8.grid(row=12,column=0)

            name8_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name8 = tk.Label(self.contain_d,textvariable=name8_var,font='Arial 15')
            name8.grid(row=12,column=1,columnspan=3)

            amount8_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount8 = tk.Label(self.contain_d,textvariable=amount8_var,font='Arial 15')
            amount8.grid(row=12,column=4,sticky='E')

            del_8 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(8), relief="flat")
            del_8.grid(row=12,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date9_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date9 = tk.Label(self.contain_d,textvariable=date9_var,font='Arial 15')
            date9.grid(row=13,column=0)

            name9_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name9 = tk.Label(self.contain_d,textvariable=name9_var,font='Arial 15')
            name9.grid(row=13,column=1,columnspan=3)

            amount9_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount9 = tk.Label(self.contain_d,textvariable=amount9_var,font='Arial 15')
            amount9.grid(row=13,column=4,sticky='E')

            del_9 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(9), relief="flat")
            del_9.grid(row=13,column=5)
            
            self.limit -= 1

        if self.limit>0:
            date10_var = tk.StringVar(self.contain_d,self.data[self.limit-1][1])
            date10 = tk.Label(self.contain_d,textvariable=date10_var,font='Arial 15')
            date10.grid(row=14,column=0)

            name10_var = tk.StringVar(self.contain_d,self.data[self.limit-1][2])
            name10 = tk.Label(self.contain_d,textvariable=name10_var,font='Arial 15')
            name10.grid(row=14,column=1,columnspan=3)

            amount10_var = tk.StringVar(self.contain_d,self.data[self.limit-1][3])
            amount10 = tk.Label(self.contain_d,textvariable=amount10_var,font='Arial 15')
            amount10.grid(row=14,column=4,sticky='E')

            del_10 = tk.Button(self.contain_d,text="•",command= lambda: self.del_entry(10), relief="flat")
            del_10.grid(row=14,column=5)
            
            self.limit -= 1

        #self.limit = self.max - self.position ---------------- fix
        
    def save(self):
        if os.path.exists('expense_log.csv'):
            os.remove('expense_log.csv')
            
        file = open('expense_log.csv','w',newline='')
        file_writer = csv.writer(file)

        file_writer.writerow(['Number','Date','Expense','Amount'])

        for i in self.data:
            file_writer.writerow(i)

        file.close()

        print(len(self.data))

        
            
    def append(self):
        self.number += 1
        self.data.append([self.number,self.today,self.entry.get(),'$'+self.entry_amount.get()])
        print('Entry Successful')
        self.expense.set('')
        self.amount.set('')
            
        
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.today = str(date.today())
        print("Today's Date is",self.today)

        self.position = 0 #for display transaction screen scrolling

        self.data = []

        self.geometry('700x400')
        self.minsize(700,400)
        self.title('Expense Tracker')

        self.initial()

        if os.path.exists('expense_log.csv'):
            file = open('expense_log.csv','r')
            file_reader = csv.reader(file)
            self.data = list(file_reader)[1:]
            try:
                self.number = int(self.data[-1][0])
            except:
                self.number = 0
            file.close()
        else:
            self.number = 1

        
'''          
class App2(tk.Tk):
    def back(self):
        root = App()
        root.mainloop()
        self.destroy()
    def __init__(self,*args,**kwargs):
        super().__init__()

        self.geometry('700x400')
        self.minsize(700,400)
        self.title('Log')

        self.header = tk.Label(self,text="Display Transactions",font="Arial 25")
        self.header.grid(column=0,row=0,columnspan=4)

        self.columnconfigure(index=0,weight=1)
        self.columnconfigure(index=1,weight=1)
        self.columnconfigure(index=2,weight=1)
        self.columnconfigure(index=3,weight=1)
        self.rowconfigure(index=0,weight=1)
        self.rowconfigure(index=1,weight=1)
        self.rowconfigure(index=2,weight=1)
        self.rowconfigure(index=3,weight=1)
        self.rowconfigure(index=4,weight=1)

        self.go_back = tk.Button(self,text="Back",command = self.back)
        self.go_back.grid(row=0,column=0)
        
'''       
    

root = App()
root.mainloop()
