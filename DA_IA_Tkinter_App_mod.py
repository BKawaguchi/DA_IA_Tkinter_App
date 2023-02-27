#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tkinter import *
from tkinter import ttk

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        master.geometry('880x850')
        master.title('DA方式とボストン方式によるマッチングアプリ')
        master.resizable(True, True)
        
        canvas = Canvas(master)
        
        bar = Scrollbar(self.master, orient=VERTICAL)
        bar.pack(side=RIGHT, fill=Y)
        bar.config(command=canvas.yview)
        
        canvas.config(yscrollcommand=bar.set)
        canvas.config(scrollregion=(0, 0, 0, 25000))
        canvas.bind_all('<MouseWheel>', lambda eve: canvas.yview_scroll(int(-eve.delta/120), 'units'))
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        self.frame = Frame(canvas)
        self.frame2 = Frame(canvas)
        
        canvas.create_window((0,0), window=self.frame, anchor=NW)
        canvas.create_window((0,0), window=self.frame2, anchor=NW)
        
        self.label_lst = []
        self.entry_lst = []
        self.button_lst = []
        self.s_prefs = []
        self.c_prefs = []
        
        Label(self.frame2, text='学生の人数を入力 >>').grid(row=0, column=0, pady=5)
        self.f1 = IntVar(value='')
        Entry1 = Entry(self.frame2, textvariable=self.f1, width=5).grid(row=0, column=1, pady=5)
        
        Label(self.frame2, text='研究室の数を入力 >>').grid(row=0, column=2, pady=5)
        self.f2 = IntVar(value='')
        Entry2 = Entry(self.frame2, textvariable=self.f2, width=5).grid(row=0, column=3, pady=5)
        
        Button1 = Button(self.frame2, text='OK', command=self.btn1_clicked, width=5).grid(row=0, column=6, pady=5)
        
    def btn1_clicked(self):
        S = self.f1.get()
        
        emp_label = Label(self.frame, text='').grid(row=0, column=0, pady=5)
        self.label_lst.append(emp_label)
        
        for i in range(S):
            label = Label(self.frame, text=['学生',i+1,'の希望順に研究室の番号をスペース区切りで入力　>>']).grid(row=1+i, column=0, pady=5)
            self.f_s_pref = StringVar(value='')
            self.s_prefs.append(self.f_s_pref)
            entry = Entry(self.frame, textvariable=self.f_s_pref, width=38).grid(row=1+i, column=1, pady=5)
            
        label = Label(self.frame, text='学生が実際に応募可能な研究室の数を入力 >>').grid(row=S+1, column=0, pady=5)
        self.f3 = IntVar(value='')
        entry = Entry(self.frame, textvariable=self.f3, width=5).grid(row=S+1, column=1, pady=5)
            
        button = Button(self.frame, text='OK', command=self.btn2_clicked, width=5).grid(row=S+1, column=2, pady=5)
    
        self.label_lst.append(label)
        self.entry_lst.append(entry)
        self.button_lst.append(button)
        
    def btn2_clicked(self):
        S = self.f1.get()
        C = self.f2.get()
        
        for i in range(C):
            label = Label(self.frame, text=['研究室',i+1,'の希望順に学生の番号をスペース区切りで入力　>>']).grid(row=S+2+i, column=0, pady=5)
            self.f_c_pref = StringVar(value='')
            self.c_prefs.append(self.f_c_pref)
            entry = Entry(self.frame, textvariable=self.f_c_pref, width=38).grid(row=S+2+i, column=1, pady=5)
            
        button = Button(self.frame, text='OK', command=self.btn3_clicked, width=5).grid(row=S+C+1, column=2, pady=5)
        
    def btn3_clicked(self):
        S = self.f1.get()
        C = self.f2.get()
     
        label = Label(self.frame, text=['研究室1から順に定員をスペース区切りで入力　>>']).grid(row=S+C+3, column=0, pady=5)
        self.c_capa = StringVar(value='')
        entry = Entry(self.frame, textvariable=self.c_capa, width=15).grid(row=S+C+3, column=1, pady=5)
     
        fonts = ('',12,'bold')
        
        button = Button(self.frame, text='DA方式でマッチング', command=self.DA_matching, width=10, font=fonts).grid(row=S+C+3, column=2, pady=5)
        button = Button(self.frame, text='ボストン方式でマッチング', command=self.IA_matching, width=13, font=fonts).grid(row=S+C+4, column=2, pady=5)
        
    def DA_matching(self):
        S = self.f1.get()
        C = self.f2.get()
        apply_num = self.f3.get()
        
        err_label = Label(self.frame, text='※ 選好が無効と表示される場合は、入力した値の数が誤っているか、値が範囲外または重複しています。修正後、もう一度マッチングボタンを押してください。', 
                          wraplength=290).grid(row=S+C+4, column=0, pady=5)
        self.label_lst.append(err_label)

        fonts=('',12,'bold')
        
        s_prefs = [i.get().split() for i in self.s_prefs]
        for i in range(S):
            if len(s_prefs[i])!=C:
                s_err_label = Label(self.frame, text=['学生',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=i+1, column=2, pady=2)
                self.label_lst.append(s_err_label)
            else:
                for j in range(C):
                    s_prefs[i][j] = int(s_prefs[i][j])
                
        c_prefs = [i.get().split() for i in self.c_prefs]
        for i in range(C):
            if len(c_prefs[i])!=S:
                c_err_label = Label(self.frame, text=['研究室',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=S+2+i, column=2, pady=2)
                self.label_lst.append(c_err_label)
            else:
                for j in range(S):
                    c_prefs[i][j] = int(c_prefs[i][j])

        m = list(range(1,C+1))
        n = list(range(1,S+1))
        
        for i in range(S):
            for j in range(C):
                if m[j] not in s_prefs[i]:
                    s_err_label = Label(self.frame, text=['学生',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=i+1, column=2, pady=2)
        
        for i in range(C):
            for j in range(S):
                if n[j] not in c_prefs[i]:
                    c_err_label = Label(self.frame, text=['研究室',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=S+2+i, column=2, pady=2)
        
        capacity = [int(s) for s in self.c_capa.get().split()]
        if len(capacity)!=C:
            capa_err_label = Label(self.frame, text='定員数が研究室数と一致しません', font=fonts, foreground='#ff0000').grid(row=S+C+4, column=1, pady=2)
   
        for i in range(S):
            del s_prefs[i][apply_num:C]
    
        c_rank = [[0]*S for i in range(C)]
        for i in range(C):
            for j in range(S):
                k=c_prefs[i][j]
                c_rank[i][k-1]=j+1

        s_matched = [0]*(S+1)
        c_matched = [[0]*(S+1) for i in range(C)]
        num_match = 0
        s_filled = [0]*(S+1)
        c_filled = [0]*C
        position = [0]*(S+1)
      
        while num_match < S:
            for i in range(S):
                if s_filled[i]==0:
                    j = s_prefs[i][position[i]]-1
                    if c_filled[j]<capacity[j]:
                        c_matched[j][i] = 1
                        s_matched[i] = j
                        s_filled[i] = 1
                        c_filled[j] += 1
                        num_match += 1
                    else:
                        n = -1
                        rejected = S
                        for k in range(S):
                            if c_matched[j][k]==1:
                                if c_rank[j][i]<c_rank[j][k] and c_rank[j][k]>n:
                                    s_filled[rejected] = 1
                                    position[rejected] -= 1
                                    c_matched[j][rejected] = 1
                                    s_matched[rejected] = j
                                    s_filled[k] = 0
                                    position[k] += 1
                                    rejected = k
                                    c_matched[j][k] = 0
                                    n = c_rank[j][k]
                        if n != -1:
                            c_matched[j][i] = 1
                            s_matched[i] = j
                            s_filled[i] = 1
                            if position[rejected]==apply_num:
                                s_matched[rejected] = -1
                                s_filled[rejected] = 1
                                num_match += 1
                        else:
                            position[i] += 1
                            if position[i]==apply_num:
                                s_matched[i] = -1
                                s_filled[i] = 1
                                num_match += 1
        
        result_win = Toplevel()
        result_win.geometry('200x300')
        result_win.title('DA')
        
        tree = ttk.Treeview(result_win, height=15, show='headings', columns=[1])
        tree.pack()
        
        for i in range(S):
            if s_matched[i]==-1:
                tree.insert('', END, values=('学生{}:'.format(i+1)))
            else:
                tree.insert('', END, values=('学生{}:研究室{}'.format(i+1, s_matched[i]+1)))
                
        for i in range(C):
            if c_filled[j]==0:
                tree.insert('', END, values=(':研究室{}'.format(j+1)))
                
    def IA_matching(self):
        S = self.f1.get()
        C = self.f2.get()
        apply_num = self.f3.get()
        
        err_label = Label(self.frame, text='※ 選好が無効と表示される場合は、入力した値の数が誤っているか、値が範囲外または重複しています。修正後、もう一度マッチングボタンを押してください。', 
                          wraplength=290).grid(row=S+C+4, column=0, pady=5)
        
        fonts=('',12,'bold')
            
        s_prefs = [i.get().split() for i in self.s_prefs]
        
        for i in range(S):
            if len(s_prefs[i])!=C:
                s_err_label = Label(self.frame, text=['学生',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=i+1, column=2, pady=2)
            else:
                for j in range(C):
                    s_prefs[i][j] = int(s_prefs[i][j])
                    
        c_prefs = [i.get().split() for i in self.c_prefs]
        
        for i in range(C):
            if len(c_prefs[i])!=S:
                c_err_label = Label(self.frame, text=['研究室',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=S+2+i, column=2, pady=2)
            else:
                for j in range(S):
                    c_prefs[i][j] = int(c_prefs[i][j])
                    
        m = list(range(1,C+1))
        n = list(range(1,S+1))
        
        for i in range(S):
            for j in range(C):
                if m[j] not in s_prefs[i]:
                    s_err_label = Label(self.frame, text=['学生',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=i+1, column=2, pady=2)
                    
        for i in range(C):
            for j in range(S):
                if n[j] not in c_prefs[i]:
                    c_err_label = Label(self.frame, text=['研究室',i+1,'の選好が無効です'], font=fonts, foreground='#ff0000').grid(row=S+2+i, column=2, pady=2)
                    
        capacity = [int(s) for s in self.c_capa.get().split()]
        if len(capacity)!=C:
            capa_err_label = Label(self.frame, text='定員数が研究室数と一致しません', font=fonts, foreground='#ff0000').grid(row=S+C+4, column=1, pady=2)
        
        for i in range(S):
            del s_prefs[i][apply_num:C]
        
        c_rank = [[0]*S for i in range(C)]
        for i in range(C):
            for j in range(S):
                k=c_prefs[i][j]
                c_rank[i][k-1]=j+1
        
        s_matched = [0]*(S+1)
        c_matched = [[0]*(S+1) for i in range(C)]
        num_match = 0
        s_filled = [0]*(S+1)
        c_filled = [0]*C
        position = [0]*(S+1)
        step = [0]*(S+1)
            
        t = 1
        while num_match < S:
            for i in range(S):
                if s_filled[i]==0:
                    j = s_prefs[i][position[i]]-1
                    if c_filled[j]<capacity[j]:
                        c_matched[j][i] = 1
                        s_matched[i] = j
                        s_filled[i] = 1
                        step[i] = t
                        c_filled[j] += 1
                        num_match += 1
                    else:
                        n = -1
                        rejected = S
                        for k in range(S):
                            if c_matched[j][k]==1 and step[k]==t:
                                if c_rank[j][i]<c_rank[j][k] and c_rank[j][k]>n:
                                    s_filled[rejected] = 1
                                    position[rejected] -= 1
                                    c_matched[j][rejected] = 1
                                    s_matched[rejected] = j
                                    step[rejected] = t
                                    s_filled[k] = 0
                                    position[k] += 1
                                    rejected = k
                                    c_matched[j][k] = 0
                                    step[k] = 0
                                    n = c_rank[j][k]
                        if n != -1:
                            c_matched[j][i] = 1
                            s_matched[i] = j
                            s_filled[i] = 1
                            step[i] = t
                            if position[rejected]==apply_num:
                                s_matched[rejected] = -1
                                s_filled[rejected] = 1
                                num_match += 1
                        else:
                            position[i] += 1
                            step[i] = 0
                            if position[i]==apply_num:
                                s_matched[i] = -1
                                s_filled[i] = 1
                                num_match += 1
            t += 1
                
        result_win = Toplevel()
        result_win.geometry('200x300')
        result_win.title('ボストン')
            
        tree = ttk.Treeview(result_win, height=15, show='headings', columns=[1])
        tree.pack()
            
        for i in range(S):
            if s_matched[i]==-1:
                tree.insert('', END, values=('学生{}:'.format(i+1)))
            else:
                tree.insert('', END, values=('学生{}:研究室{}'.format(i+1, s_matched[i]+1)))
                    
        for i in range(C):
            if c_filled[j]==0:
                tree.insert('', END, values=('研究室{}'.format(j+1)))

def main():
    root = Tk()
    app = Application(master = root)
    app.mainloop()
    
if __name__ == '__main__':
    main()


# In[ ]:




