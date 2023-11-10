

"""

@author: mehdi


    
"""
import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog

import Scripts.Core as Core
import Scripts.WorldSubtitleApi as worldsubtitle


class ProcessThread(QThread):
    sending_mss = QtCore.pyqtSignal(str)
    sending_bool = QtCore.pyqtSignal(bool)
    def __init__(self, UI, filename, num, pathfile=None):
        QThread.__init__(self)
        self.UI = UI
        self.FName = filename
        self.num = num
        self.pf = pathfile

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        if self.num == 1:
            self.single_movie()
        elif self.num == 2:
            self.multiy_movies()
        elif self.num == 3:
            self.folder_of_movies()

    def single_movie(self):
        b_input_name = self.FName[0]
        if b_input_name != "":
            if Core.check_internet_conntion():
                self.sending_mss.emit("بقیه ی  دکمه ها تا پایان دانلود زیرنویس /زیرنویس ها غیر فعال خواهند بود ")
               # self.UI.textBrowser.append("بقیه ی  دکمه ها تا پایان دانلود زیرنویس /زیرنویس ها غیر فعال خواهند بود ")
                self.sending_bool.emit(False)
                # self.UI.pbf.setEnabled(False)
                # self.UI.pbmul.setEnabled(False)
                # self.UI.pbpa.setEnabled(False)
                a = os.path.split(os.path.abspath(b_input_name))
                self.pf = a[0]
                input_name = os.path.basename(str(b_input_name))
                editted_name = input_name
                final_edit = Core.final_name(editted_name).lower()
                self.sending_mss.emit("فیلم های انتخاب شده ")
                self.sending_mss.emit(final_edit)
                search = worldsubtitle.WorldSubtitle(final_edit, self.pf)
                reasult = search.main_page()
                try:
                    if reasult[0]:
                        st = reasult[1]
                        set2 = reasult[2]
                        for i in set2:
                            self.sending_mss.emit("زیرنویس" + i + " موجود است")
                            
                        for i in st:
                            downloadinfo = search.resualt_page(i)
                            if downloadinfo == True:
                                self.sending_mss.emit("زیرنویس این فیلم دانلود شد : {} ".format(set2[st.index(i)]))
                                
                            elif downloadinfo == False:
                                self.sending_mss.emit(
                                        " رو فرستادم به مرورگرت {}زیرنویس ".format(set2[st.index(i)])
                                        )
                            else:
                                self.sending_mss.emit("something went wrong bro !")
                                
                    elif not reasult[0] and len(reasult) == 2:

                        for j in reasult[1]:
                            self.sending_mss.emit("زیرنویس فیلم {}موجود نبود ".format(j))
                            
                    else:
                        self.sending_mss.emit("زیرنویس فیلم موجود نبود ")
                    

                except Exception:
                    pass

                QThread.msleep(3)
            else:

                self.UI.textBrowser.append("اینترنت وصل نیست لطفا از اتصال به اینترنت مطمین شوید و دوباره امتحان کنید")
        else:
            pass
        self.sending_bool.emit(True)
        # self.UI.pbf.setEnabled(True)
        # self.UI.pbmul.setEnabled(True)
        # self.UI.pbpa.setEnabled(True)

    def multiy_movies(self):
        b_input_name = self.FName[0]
        if len(b_input_name) != 0:
            if Core.check_internet_conntion():
                self.sending_mss.emit("بقیه ی  دکمه ها تا پایان دانلود زیرنویس /زیرنویس ها غیر فعال خواهند بود ")
                self.sending_bool.emit(False)
                a = os.path.split(os.path.abspath(b_input_name[0]))
                self.pf = a[0]
                input_name = []
                for i in b_input_name:
                    input_name.append(os.path.basename(str(i)))
                    editted_name = input_name
                final_edit = []
                for i in editted_name:
                    final_edit.append(Core.final_name(i).lower())
                self.sending_mss.emit("فیلم های انتخاب شده ")
                for i in final_edit:
                    # pass
                    self.sending_mss.emit(i)
                    
                for i in final_edit:
                    search = worldsubtitle.WorldSubtitle(i, self.pf)
                    reasult = search.main_page()
                    try:
                        if reasult[0]:
                            st = reasult[1]
                            set2 = reasult[2]
                            for i in set2:
                                self.sending_mss.emit("زیرنویس" + i + " موجود است")
                                
                            for i in st:
                                downloadinfo = search.resualt_page(i)
                                if downloadinfo == True:
                                    self.sending_mss.emit("زیرنویس این فیلم دانلود شد : {} ".format(set2[st.index(i)]))
                                elif downloadinfo == False:
                                    self.sending_mss.emit(" رو فرستادم به مرورگرت {}زیرنویس ".format(set2[st.index(i)]))
                                else:
                                    self.sending_mss.emit("something went wrong bro !")
                                    
                        elif not reasult[0] and len(reasult) == 2:

                            for j in reasult[1]:
                                self.sending_mss.emit("زیرنویس فیلم {}موجود نبود ".format(j))
                                
                        else:
                            self.sending_mss.emit("زیرنویس فیلم موجود نبود ")
                            

                    except Exception :
                        pass

                
            else:
                self.sending_mss.emit("اینترنت وصل نیست لطفا از اتصال به اینترنت مطمین شوید و دوباره امتحان کنید")
            
        else:
            pass
        self.sending_bool.emit(True)


    def folder_of_movies(self):
        if len(self.FName) != 0:
            if Core.check_internet_conntion():
                self.sending_mss.emit("بقیه ی  دکمه ها تا پایان دانلود زیرنویس /زیرنویس ها غیر فعال خواهند بود ")
                input_name = []
                self.sending_bool.emit(False)
                for i in self.FName:
                    input_name.append(os.path.basename(str(i)))
                    editted_name = input_name
                final_edit = []
                for i in editted_name:
                    final_edit.append(Core.final_name(i).lower())
                self.sending_mss.emit("   فیلم های موجود در پوشه      : ")
                for i in final_edit:
                    # pass
                    self.sending_mss.emit(i)
                for i in final_edit:
                    search = worldsubtitle.WorldSubtitle(i, self.pf)
                    reasult = search.main_page()
                    try:
                        if reasult[0]:
                            st = reasult[1]
                            set2 = reasult[2]
                            for i in set2:
                                self.sending_mss.emit("زیرنویس" + i + " موجود است")
                            for i in st:
                                downloadinfo = search.resualt_page(i)
                                if downloadinfo == True:
                                    self.sending_mss.emit("زیرنویس این فیلم دانلود شد : {} ".format(set2[st.index(i)]))
                                elif downloadinfo == False:
                                    self.sending_mss.emit(" لینک دانلوداین فیلم به مرورگر فرستاده شد : {}   ".format(set2[st.index(i)]))
                                else:

                                    self.sending_mss.emit("something went wrong bro !")
                        elif not reasult[0] and len(reasult) == 2:

                            for j in reasult[1]:
                               self.sending_mss.emit("زیرنویس فیلم {}موجود نبود ".format(j))
                        else:
                            self.sending_mss.emit("زیرنویس فیلم موجود نبود ")

                    except Exception:
                        pass
                   
            else:

                self.sending_mss.emit("اینترنت وصل نیست لطفا از اتصال به اینترنت مطمین شوید و دوباره امتحان کنید")
        else:
            pass
        self.sending_bool.emit(True)
