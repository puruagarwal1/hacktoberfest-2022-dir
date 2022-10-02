import tkinter as tk
from tkinter import ttk,filedialog
from tkinter import messagebox as m_box
import os,shutil
win=tk.Tk()
win.geometry("1200x800")
win.configure(background='#00eeff')
win.title("File")
url=""
label_frame=ttk.Labelframe(win)
label_frame.pack(pady=300)
file_name_label=ttk.Label(label_frame,text="Entre File Path")
file_name_label.grid(row=2,column=0,pady=10,padx=10)
file_name_var=tk.StringVar()
file_name_box=ttk.Entry(label_frame,textvariable=file_name_var,width=30)
file_name_box.focus()
file_name_box.grid(row=2,column=1)
file_path=""
folderpath=""
def open(event=None):
    global url,file_path
    url=filedialog.askdirectory(initialdir=os.getcwd(),title="Select Folder")
    file_name_box.delete(0,tk.END)
    try:
        file_path=url
        file_name_box.configure(textvariable=file_path)
    except :
        pass

def entre(event=None):
    
    global file_name_var,file_path,folderpath
    dict_extention={
        'audio_extenstion':('.M4V', '.MP3', '.wav', '.mp3', '.MPEG', '.MOV', '.M4P', '.WEBM.MPG', '.flac',
    '.MPE', '.OGG', '.WMV', '.QT', '.AVI', '.MP2', '.m4a', '.FLV', '.SWFAVCHD', '.MPV',"mp.3"),
    'videos_extentions':(
        'WAV', 'm4r', 'QuickTime*', 'asf*', 'webm', 'MPEG-2 PS', 'ogg', 'AVI*', 'OP1a', '.MKV', 'HDV*', '3gpp', 'LXF',
            '.mppeg', 'OP-Atom', 'ogx', 'wmv', 'wma', '.mkv', 'f4b', '.mp4', '3g2', 'GXF*',
            'mp4', 'm4b', 'ogv', 'f4v', 'VOB*', 'mov', 'Broadcast WAV*', 'ts', '3gp2', 'm4v', '3gpp2', 'MPEG-2 TS*', 
            '.flv', '3gp', 'f4a', 'm4a', 'oga', 'flv'
    ),
    "document_extention":(
    '.PSD', '.EXE', '.AVI', '.MAP', '.JPG', '.DBF', '.CLASS ', '.MTW', '.AIF', 'JPEG', '.MIDI.MOV', '.WKS', 'WPD', '.MDB',
    '.EPS', '.AIFF', '.ZIP', '.HTML', '.WK3', '.T65', '.CSV', '.MID', '.PSP', '.HQX', '.TIF', '.DOCX', '.XLS', '.CVS', '.BAT',
    '.BMP', '.pdf', '.TXT', '.SIT', '.RA', '.TAR', '.RTF', '.PDF', '.PNG', '.FM3',
    '.P65', '.PPT', '.JAVA', '.QXD', '.WP5', '.DIF', '.GIF', '.WAV', '.HTM', '.AU', '.MTB', '.QT', '.DOC', '.XLSX', '.MAC'
    ),
    }
    if len(file_name_var.get())==0:
        folderpath=file_path
        print("aaa")
    else:
        folderpath=file_name_var.get()
    print(folderpath)
    if len(folderpath)!=0:
        def file_finder(folderpaths,file_extention):
            return [i for i in os.listdir(folderpaths) for ext in file_extention if i.endswith(ext)]
    try:
        for extention_type,extention_tuple in dict_extention.items():
            folder_name=extention_type.split("_")[0]+'Files'
            folder_path=os.path.join(folderpath,folder_name)
            if folder_name not in os.listdir(folderpath) and len(file_finder(folderpath,extention_tuple))!=0:
                os.mkdir(folder_path)
                for item in (file_finder(folderpath,extention_tuple)):
                    item_path=os.path.join(folderpath+'\\'+item)
                    new_item_path=os.path.join(folder_path,item)
                    shutil.move(item_path,new_item_path)
    except FileNotFoundError:
        m_box.showerror("Error","Enter valid path")
    except:
         m_box.showerror("Error","Enter valid path")
brouse_btn=tk.Button(label_frame,text="Open",command=open)
brouse_btn.grid(row=2,column=2,padx=10)
entre_btn=tk.Button(label_frame,text="Entre",command=entre)
entre_btn.grid(row=3,column=1,pady=15,padx=15)

win.mainloop()
