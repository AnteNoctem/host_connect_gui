# -*- coding: utf-8 -*-
'''Программа автоматизации работы с удалёнными серверами.
Данная часть кода предназначена для создания графического интерфейса для подключения к ограниченному числу узлов и вводу наиболее часто используемых команд.
Оставлен только шаблон (с ip адресами 0.0.0.0, без описания самих команд и названий кнопок).
Размер окон фиксирован, т.к. предполагается работа на определённых ПК
с мониторами 1920x1080. При желании можно исправить.
'''
import tkinter as tk
import paramiko as pm
from tkinter import filedialog as fd
import time

client = None

window = tk.Tk()
window.title('Автоматизатор удалённого соединения')
frm_comlist = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
frm_txt = tk.Frame(master=window)
frm_enter = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
cnv_canvas = tk.Canvas(master=window, relief=tk.RIDGE, borderwidth=5, width=300)
#В изображении - подсказки с минимальной справочной информацией
#(не прилогается к файлу).
img = tk.PhotoImage(master=cnv_canvas, file='img.png')
image = cnv_canvas.create_image(0, 0, anchor='nw',image=img)

frm_enter_01 = tk.Frame(master=frm_enter)
lbl_enter_01 = tk.Label(master=frm_enter_01, text='Адрес узла')
ent_enter_01 = tk.Entry(master=frm_enter_01)
h_name = ent_enter_01.get()

def open_file():
    '''Вызывает меню для загрузки файла с ключом SSH'''
    file_name = fd.askopenfilename()
    if file_name is not None:
        ent_enter_02.insert(0, file_name)
        
frm_enter_02 = tk.Frame(master=frm_enter)
lbl_enter_02 = tk.Label(master=frm_enter_02, text='Файл с ключом')
ent_enter_02 = tk.Entry(master=frm_enter_02)
btn_enter_02 = tk.Button(master=frm_enter_02, text='Загрузить',
                         command=open_file)
filename = ent_enter_02.get()

frm_enter_03 = tk.Frame(master=frm_enter)
lbl_enter_03 = tk.Label(master=frm_enter_03, text='Пароль от файла')
ent_enter_03 = tk.Entry(master=frm_enter_03, show='*')
passwd = ent_enter_03.get()

frm_enter_04 = tk.Frame(master=frm_enter)
lbl_enter_04 = tk.Label(master=frm_enter_04, text='Имя пользователя')
ent_enter_04 = tk.Entry(master=frm_enter_04)
usr = ent_enter_04.get()

frm_enter_05 = tk.Frame(master=frm_enter)
lbl_enter_05 = tk.Label(master=frm_enter_05, text='Пароль пользователя')
ent_enter_05 = tk.Entry(master=frm_enter_05, show='*')
su_pass = ent_enter_05.get()

lbl_enter_empt_01 = tk.Label(master=frm_enter)
lbl_enter_empt_02 = tk.Label(master=frm_enter)

#Кнопки ниже задают адрес узла, к которому осуществляется подключение.

def host_numb_01():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_01 = tk.Button(master=frm_enter, text='01', width=20,
                             height=1, command=host_numb_01)
def host_numb_02():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_02 = tk.Button(master=frm_enter, text='02', width=20,
                             height=1, command=host_numb_02)
def host_numb_03():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_03 = tk.Button(master=frm_enter, text='03', width=20,
                             height=1, command=host_numb_03)
def host_numb_04():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_04 = tk.Button(master=frm_enter, text='04', width=20,
                             height=1, command=host_numb_04)
def host_numb_05():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_05 = tk.Button(master=frm_enter, text='05', width=20,
                             height=1, command=host_numb_05)
def host_numb_06():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_06 = tk.Button(master=frm_enter, text='06', width=20,
                             height=1, command=host_numb_06)
def host_numb_07():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_07 = tk.Button(master=frm_enter, text='07', width=20,
                             height=1, command=host_numb_07)
def host_numb_08():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_08 = tk.Button(master=frm_enter, text='08', width=20,
                             height=1, command=host_numb_08)
def host_numb_09():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_09 = tk.Button(master=frm_enter, text='09', width=20,
                             height=1, command=host_numb_09)
def host_numb_10():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_10 = tk.Button(master=frm_enter, text='10', width=20,
                             height=1, command=host_numb_10)
def host_numb_11():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_11 = tk.Button(master=frm_enter, text='11', width=20,
                             height=1, command=host_numb_11)
def host_numb_12():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_12 = tk.Button(master=frm_enter, text='12', width=20,
                             height=1, command=host_numb_12)
def host_numb_13():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_13 = tk.Button(master=frm_enter, text='13', width=20,
                             height=1, command=host_numb_13)
def host_numb_14():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_14 = tk.Button(master=frm_enter, text='14', width=20,
                             height=1, command=host_numb_14)
def host_numb_15():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_15 = tk.Button(master=frm_enter, text='15', width=20,
                             height=1, command=host_numb_15)
def host_numb_16():
    ent_enter_01.delete(0, tk.END)
    ent_enter_01.insert(0, '0.0.0.0')
btn_enter_host_16 = tk.Button(master=frm_enter, text='16', width=20,
                             height=1, command=host_numb_16)

#Основные поля ввода и вывода
txt_box = tk.Text(master=frm_txt, bg='black', fg='green')
lbl_manual_in = tk.Label(master=frm_txt, text='Ввести команду вручную')
ent_manual_in = tk.Entry(master=frm_txt, width=80)
lbl_manual_in2 = tk.Label(master=frm_txt)

def manual():
    '''Ввод однострочных команд вручную с автоматической подстановкой пароля, там где это необходимо. Программа устанавливает соединение и исполняет команду. После выполнения команды сеас закрывается.
    '''
    com = ent_manual_in.get()
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    su_pass = ent_enter_05.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    ssh = client.invoke_shell()
    ssh.send('{}'.format(com) + '\n')
    time.sleep(5)
    if com[0:5] == 'sudo ':
        ssh.send('{}'.format(su_pass) + '\n')
        time.sleep(5)
    output = ssh.recv(2000)
    txt_box.insert(1.0, output)
    ssh.close()
    client.close()    
    
btn_ent_com = tk.Button(master=frm_txt, text='Ввод', width=10, height=1, command=manual)
lbl_manual_in3 = tk.Label(master=frm_txt)

#Ниже расположены кнопки и функции, которые они выполняют.
#Кнопка отправляет команды bash на сервер.


def audio_stat():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    stdin, stdout, stderr = client.exec_command('текст команды')
    txt_box.insert(1.0, stdout.read())
    client.close()
btn_audio_status = tk.Button(master=frm_comlist, text='название кнопки',
                             width=20, height=1, command=audio_stat)
def audio_restart():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    su_pass = ent_enter_05.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    ssh = client.invoke_shell()
    ssh.send('текст команды\n')
    time.sleep(5)
    ssh.send('{}'.format(su_pass) + '\n')
    time.sleep(5)
    ssh.close()
    client.close()
btn_audio_restart = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=1, command=audio_restart)

def docker():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    su_pass = ent_enter_05.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    ssh = client.invoke_shell()
    ssh.send('текст команды\n')
    time.sleep(5)
    ssh.send('{}'.format(su_pass) + '\n')
    time.sleep(40) 
    ssh.close()                                        
    client.close()
btn_docker = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=2, command=docker)

def docker_stat():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    su_pass = ent_enter_05.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    ssh = client.invoke_shell()
    ssh.send('sudo su\n')
    time.sleep(5)
    ssh.send('{}'.format(su_pass) + '\n')
    time.sleep(5)
    ssh.send("текст команды\n")
    time.sleep(5)
    output = ssh.recv(2000)
    txt_box.insert(1.0, output)
    ssh.close()                                        
    client.close()
btn_docker_stat = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=2, command=docker_stat)

def vaccept():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    mac = ent_manual_in.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    stdin, stdout, stderr = client.exec_command('текст коанды'.format(mac=mac))
    txt_box.insert(1.0, stdout.read())
    client.close()
btn_vaccept = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=2, command=vaccept)


def deny():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    mac = ent_manual_in.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    stdin, stdout, stderr = client.exec_command('текст команды'.format(mac=mac))
    txt_box.insert(1.0, stdout.read())
    client.close()
btn_vdeny = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=2, command=deny)

def hosts():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    ssh = client.invoke_shell()
    ssh.send('текст команды\n')
    time.sleep(1)
    output = ssh.recv(2000)
    txt_box.insert(1.0, output)
    ssh.close() 
    client.close()
btn_hosts = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=1, command=hosts)

def coord():
    h_name = ent_enter_01.get()
    filename = ent_enter_02.get()
    passwd = ent_enter_03.get()
    usr = ent_enter_04.get()
    key = pm.RSAKey.from_private_key_file('{}'.format(filename), password='{}'.format(passwd))
    client = pm.SSHClient()
    client.set_missing_host_key_policy(pm.AutoAddPolicy())
    txt_box.delete(1.0, tk.END)
    client.connect(h_name, username=usr, pkey=key)
    if h_name == '0.0.0.0':
        stdin, stdout, stderr = client.exec_command('текст команды')
    else:
        stdin, stdout, stderr = client.exec_command("текст команды")
    txt_box.insert(1.0, stdout.read())
    client.close()
btn_coord = tk.Button(master=frm_comlist, text='название кнопки',
                              width=20, height=1, command=coord)


cnv_canvas.pack(fill=tk.BOTH, side=tk.RIGHT)
frm_txt.pack(fill=tk.BOTH, side=tk.RIGHT)
frm_enter.pack(fill=tk.BOTH, side=tk.RIGHT)
frm_comlist.pack(fill=tk.BOTH, side=tk.RIGHT)
frm_enter_01.pack()
lbl_enter_01.pack()
ent_enter_01.pack()
frm_enter_04.pack()
lbl_enter_04.pack()
ent_enter_04.pack()
frm_enter_05.pack()
lbl_enter_05.pack()
ent_enter_05.pack()
frm_enter_02.pack()
lbl_enter_02.pack()
ent_enter_02.pack()
btn_enter_02.pack()
frm_enter_03.pack()
lbl_enter_03.pack()
ent_enter_03.pack()
lbl_enter_empt_01.pack()
btn_enter_host_01.pack()
btn_enter_host_02.pack()
btn_enter_host_03.pack()
btn_enter_host_04.pack()
btn_enter_host_05.pack()
btn_enter_host_06.pack()
btn_enter_host_07.pack()
btn_enter_host_08.pack()
btn_enter_host_09.pack()
btn_enter_host_10.pack()
btn_enter_host_11.pack()
btn_enter_host_12.pack()
btn_enter_host_13.pack()
btn_enter_host_14.pack()
btn_enter_host_15.pack()
btn_enter_host_16.pack()
txt_box.pack()
lbl_manual_in.pack()
ent_manual_in.pack()
lbl_manual_in2.pack()
btn_ent_com.pack()
lbl_manual_in3.pack()
btn_audio_status.pack()
btn_audio_restart.pack()
btn_docker.pack()
btn_docker_stat.pack()
btn_vaccept.pack()
btn_vdeny.pack()
btn_hosts.pack()
btn_coord.pack()

#Изначально разрабатывалось для другого механизма соединения.
#Использовалось для закрытия соединений при выходе в случае,
#если они не были по какой-то причине закрыты на момент выхода.
#Оставлено на случай дальнейших доработок.
try:
    window.mainloop()
finally:
    end_w = tk.Tk()
    end_w.title('Выход')
    w = end_w.winfo_screenwidth()
    h = end_w.winfo_screenheight()
    w = w//2
    h = h//2 
    w = w - 250
    h = h - 100
    end_w.geometry('250x100+{}+{}'.format(w, h))
    end_w.columnconfigure(0, minsize=250)
    end_w.rowconfigure(0, minsize=100)
    frm_end = tk.Frame(master=end_w)
    lbl_end = tk.Label(master=frm_end, text='АКТИВНЫЕ СОЕДИНЕНИЯ БУДУТ ЗАКРЫТЫ')
    lbl_end_emp = tk.Label(master=frm_end)
    btn_end = tk.Button(master=frm_end, text='OK', width=20, height=1, command=end_w.destroy)
    lbl_end.pack()
    lbl_end_emp.pack()
    btn_end.pack()
    frm_end.grid()
    if isinstance(client, pm.client.SSHClient):
        client.close()
    end_w.mainloop()
