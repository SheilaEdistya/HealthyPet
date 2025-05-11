from tkinter import*
from tkinter import ttk
import tkinter as tk
import PIL as p
from PIL import Image, ImageTk
from tkcalendar import *
# import pandas as pd


class HealthyPet:
        def __init__(self, master):
                self.master = master
                self.master.title("Healthy Pet")
                master.geometry("1937x1000")

                self.nama_petugas = tk.StringVar()
                self.nomor_petugas = tk.IntVar()
                self.nama_pengunjung = tk.StringVar()
                self.jenis_hewan = tk.StringVar()
                self.nomor_antrean = tk.IntVar()
                self.tanggal_kunjungan = tk.IntVar()
                self.jenis_penyakit = tk.StringVar()
                self.treatment = tk.StringVar()
                self.ras = tk.StringVar() 
                self.alamat = tk.StringVar()
                self.nama_hewan = tk.StringVar()
                self.warna = tk.StringVar()
                self.nama_helper = tk.StringVar()
                self.KontrolKucing = tk.IntVar()
                self.KontrolAnjing = tk.IntVar()
                self.KontrolKelinci = tk.IntVar()
                self.KontrolHamster = tk.IntVar()
                self.DaruratKucing = tk.IntVar()
                self.DaruratAnjing = tk.IntVar()
                self.DaruratKelinci = tk.IntVar()
                self.DaruratHamster = tk.IntVar()
                self.KontrolUmum = tk.IntVar()
                self.DaruratUmum = tk.IntVar()


                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.foto=Image.open("1.jpg")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.photoo=ImageTk.PhotoImage(self.foto)
                label_background = Label(master, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)
                label_background.photo=self.photoo

                self.NamaPetugasEntry = tk.Entry(master, textvariable= self.nama_petugas, bg="#FAEED1", width=40,font=("Times New Roman",23)).place(x=550, y=398)
                self.NomorPetugasEntry = tk.Entry(master, textvariable= self.nomor_petugas, bg="#FAEED1", width=40, font=("Times New Roman",24)).place(x=550, y=496)
                tk.Button(master, text="Login", bg="#FAEED1", width=30, height=1, font=("Britannic Bold", 25), command=self.SetelahLogin).place(x=400, y=600)
        
                        
        def SetelahLogin(self):
                
                new_window = tk.Toplevel(self.master)
                new_window.title("Healthy Pet")
                new_window.geometry("1937x1000")

                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.foto=Image.open("vbgpetshop.jpeg")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.photoo=ImageTk.PhotoImage(self.foto)
                label_background = Label(new_window, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)
                label_background.photo=self.photoo

                ButtonDaftar = Button(new_window, text="Daftar", bg="#FAEED1", width=30, height=1, font=("Britannic Bold", 20), command=self.SetelahDaftar)
                ButtonDaftar.place(x=650, y=430)
                ButtonRiwayat = Button(new_window, text="Riwayat", bg="#FAEED1", width=30, height=1, font=("Britannic Bold", 20),command=self.SetelahRiwayat)
                ButtonRiwayat.place(x=150, y=430)


        def SetelahDaftar(self):
                print()

        def SetelahRiwayat(self):
                new_window2 = tk.Toplevel(self.master)
                new_window2.title("Healthy Pet")
                new_window2.geometry("1937x1000")
                new_window2.state("zoomed")
                new_window2.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.fotoo=Image.open("2.jpg")
                self.fotoo=self.fotoo.resize((screen_width,screen_height))
                self.photooo=ImageTk.PhotoImage(self.fotoo)
                label_background = Label(new_window2, image=self.photooo)
                label_background.pack(fill=BOTH, expand=YES)
                label_background.photo=self.photoo

                frame=Frame(new_window2)
                frame.place(width=990, height=500 , x=100, y=100)
                self.tree = ttk.Treeview(frame, columns=("No","Tanggal", "Pengunjung", "Hewan", "Helper", "Keterangan"), show="headings")


                self.tree.heading("No", text="No")
                self.tree.heading("Tanggal", text="Tamggal")
                self.tree.heading("Pengunjung", text="Pengunjung")
                self.tree.heading("Hewan", text="Hewan")
                self.tree.heading("Helper", text="Helper")
                self.tree.heading("Keterangan", text="Keterangan")
                


                self.tree.column("No", width=50)
                self.tree.column("Tanggal", width=100)
                self.tree.column("Pengunjung", width=200)
                self.tree.column("Hewan", width=150)
                self.tree.column("Helper", width=200)
                self.tree.column("Keterangan", width=150)
                

                treescroll = tk.Scrollbar(frame, command=self.tree.yview)
                treescroll.pack(side="right", fill="y")
                self.tree.configure(yscrollcommand=treescroll.set)

                tanggal = self.EntryTanggalKunjungan.get()
                pengunjung = self.EntryNamaPengunjung.get()
                hewan = self.EntryNamaHewan.get()
                helper = self.EntryNamaHelper.get()
                ket = self.SetelahNext3.get()


                data = [["1", f"{tanggal}", f"{pengunjung}", f"{hewan}", f"{helper}", f"{ket}"],["2","Dog","Tidak ada","Sheila"]]

                for row in data:
                        self.tree.insert("", "end", values=row)


                self.tree.pack(padx=10, pady=10)


        def SetelahDaftar(self):
                new_window5 = tk.Toplevel(self.master)
                new_window5.title("Healthy Pet")
                new_window5.geometry("1937x1000")
        
                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.foto=Image.open("3.jpg")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.photoo=ImageTk.PhotoImage(self.foto)
                label_background = Label(new_window5, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)



                self.EntryTanggalKunjungan = DateEntry(new_window5, textvariable= self.tanggal_kunjungan, bg="#FAEED1", width=30,font=("Times New Roman",23)).place(x=600, y=255)
                self.EntryNamaPengunjung = tk.Entry(new_window5, textvariable= self.nama_pengunjung, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=600, y=380)
                self.EntryAlamat = tk.Entry(new_window5, textvariable= self.alamat, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=600, y=497)
                ButtonNext = Button(new_window5, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.SetelahNext).place(x=950, y=640)

        
        def SetelahNext(self):
                new_window6 = tk.Toplevel(self.master)
                new_window6.title("Healthy Pet")
                new_window6.geometry("1937x1000")
        
                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.foto=Image.open("4.jpg")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.photoo=ImageTk.PhotoImage(self.foto)
                label_background = Label(new_window6, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)


                self.EntryNamaHewan = tk.Entry(new_window6, textvariable= self.nama_hewan, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=530, y=258)
                values=["Kucing", "Anjing", "Kelinci", "Hamster", "Lainnya"]
                self.hewan = ttk.Combobox(new_window6, values=values, width=30,height=5, font=("Britannic Bold",20), background="#FAEED1")
                self.hewan.set("Jenis Hewan")
                self.hewan.place(x=530, y=355)
                # entryHewan = tk.Entry(new_window6, textvariable=self.nama_hewan, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=530, y=355)
                values=["Lokal", "Domestik"]
                self.ComboRas = ttk.Combobox(new_window6, values=values, width=30,height=5, font=("Britannic Bold",20), background="#FAEED1")
                self.ComboRas.set("Ras")
                self.ComboRas.place(x=530, y=452)
                self.EntryWarna = tk.Entry(new_window6, textvariable=self.warna, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=530, y=549)
                #ButtonNext2 = Button(new_window6, text="Next", bg="FAEED1", width=20, height=1, font=("Britannic Bold", 20), command= self.SetelahNext2)
                #ButtonNext2.place(x=900, y=600)
                ButtonNext2 = Button(new_window6, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.SetelahNext2).place(x=950, y=640)


        def SetelahNext2(self):
                new_window7 = tk.Toplevel(self.master)
                new_window7.title("Healthy Pet")
                new_window7.geometry("1937x1000")
        
                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                self.foto=Image.open("5.jpg")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.photoo=ImageTk.PhotoImage(self.foto)
                label_background = Label(new_window7, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)

                self.EntryNamaHelper = tk.Entry(new_window7, textvariable= self.nama_helper, bg="#FAEED1", width=31,font=("Times New Roman",23)).place(x=530, y=314)
                values=["Berobat", "Treatment"]
                self.ComboKeperluan = ttk.Combobox(new_window7, values=values, width=30,height=5, font=("Britannic Bold",20), background="#FAEED1")
                self.ComboKeperluan.set("Keperluan")
                self.ComboKeperluan.place(x=530, y=466)
                self.ButtonNext3= Button(new_window7, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.SetelahNext3).place(x=950, y=640)

        def SetelahNext3(self):
                jenishewan = self.hewan.get()

                if jenishewan == "Kucing":

                        new_window8 = tk.Toplevel(self.master)
                        new_window8.title("Healthy Pet")
                        new_window8.geometry("1937x1000")
                
                        self.master.state("zoomed")
                        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                        screen_width = self.master.winfo_screenwidth()
                        screen_height = self.master.winfo_screenheight()
                        self.foto=Image.open("6.jpg")
                        self.foto=self.foto.resize((screen_width,screen_height))
                        self.photoo=ImageTk.PhotoImage(self.foto)
                        label_background = Label(new_window8, image=self.photoo)
                        label_background.pack(fill=BOTH, expand=YES)

                        self.labelcekkesehatankucing = tk.Label(new_window8, text="Cek Kesehatan", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahCekKesehatanKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahCekKesehatanKucing.set(0)
                        self.JumlahCekKesehatanKucing.place(x=270, y=252)
                        
                        self.labelSterilKucing = tk.Label(new_window8, text="Steril", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSterilKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSterilKucing.set(0)
                        self.JumlahSterilKucing.place(x=270, y=310)

                        self.labelVaksinKucing = tk.Label(new_window8, text="Vaksin Kucing", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=363)
                        values=[3,4]
                        self.JumlahVaksinKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVaksinKucing.set(0)
                        self.JumlahVaksinKucing.place(x=270, y=373)

                        self.labelScallingKucing = tk.Label(new_window8, text="Scalling Kucing ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahScallingKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahScallingKucing.set(0)
                        self.JumlahScallingKucing.place(x=270, y=435)

                        self.labelUSGKucing = tk.Label(new_window8, text="USG ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahUSGKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahUSGKucing.set(0)
                        self.JumlahUSGKucing.place(x=270, y=557)

                        self.labelRInapKucing = tk.Label(new_window8, text="Rawat Inap/hari ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahRInapKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahRInapKucing.set(0)
                        self.JumlahRInapKucing.place(x=270, y=615)

                        self.labelSuntikRabies = tk.Label(new_window8, text="Suntik Rabies ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=726)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSuntikRabiesKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSuntikRabiesKucing.set(0)
                        self.JumlahSuntikRabiesKucing.place(x=270, y=736)
 ####################################################################################################################################################################################################
                        self.labelGroomingKucing = tk.Label(new_window8, text="Grooming Lengkap", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahGroomingKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahGroomingKucing.set(0)
                        self.JumlahGroomingKucing.place(x=1155, y=252)

                        self.labelMandiKucing = tk.Label(new_window8, text="Mandi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKucing.set(0)
                        self.JumlahMandiKucing.place(x=1155, y=310)

                        self.labelMandiJamurKucing = tk.Label(new_window8, text="Mandi Jamur", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiJamurKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiJamurKucing.set(0)
                        self.JumlahMandiJamurKucing.place(x=1155, y=373)

                        self.labelMandiKutuKucing = tk.Label(new_window8, text="Mandi Kutu", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKutuKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKutuKucing.set(0)
                        self.JumlahMandiKutuKucing.place(x=1155, y=435)

                        self.labelMandiKombinasiKucing = tk.Label(new_window8, text="Mandi Kombinasi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=485)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKombinasiKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKombinasiKucing.set(0)
                        self.JumlahMandiKombinasiKucing.place(x=1155, y=495)

                        self.labelPotongRambutKucing = tk.Label(new_window8, text="Potong Rambut", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPotongRambutKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPotongRambutKucing.set(0)
                        self.JumlahPotongRambutKucing.place(x=1155, y=557)
########################################################################################################################################################################################################
                        self.labelMKeringKucing = tk.Label(new_window8, text="Makanan Kering/kg ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=247)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMKeringKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMKeringKucing.set(0)
                        self.JumlahMKeringKucing.place(x=777, y=252)

                        self.labelMBasahKucing = tk.Label(new_window8, text="Makanan Basah/400g  ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=305)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMBasahKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMBasahKucing.set(0)
                        self.JumlahMBasahKucing.place(x=777, y=310)

                        self.labelVitaminKucing = tk.Label(new_window8, text="Vitamin ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=368)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVitaminKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVitaminKucing.set(0)
                        self.JumlahVitaminKucing.place(x=777, y=373)

                        self.labelShampoKucing = tk.Label(new_window8, text="Shampo ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=430)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahShampoKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahShampoKucing.set(0)
                        self.JumlahShampoKucing.place(x=777, y=435)

                        self.labelPastaGigiKucing = tk.Label(new_window8, text="Pasta Gigi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=494)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPastaGigiKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPastaGigiKucing.set(0)
                        self.JumlahPastaGigiKucing.place(x=777, y=499)

                        self.labelPawKucing = tk.Label(new_window8, text="Paw Balm", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=552)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPawKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPawKucing.set(0)
                        self.JumlahPawKucing.place(x=777, y=557)

                        self.labelParfumeKucing = tk.Label(new_window8, text="Parfume ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=610)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahParfumeKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahParfumeKucing.set(0)
                        self.JumlahParfumeKucing.place(x=777, y=615)

                        self.labelAntiKutuKucing = tk.Label(new_window8, text="Anti Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=671)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiKutuKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiKutuKucing.set(0)
                        self.JumlahAntiKutuKucing.place(x=777, y=676)

                        self.labelAntiJamurKucing = tk.Label(new_window8, text="Anti Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=732)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiJamurKucing = ttk.Combobox(new_window8, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiJamurKucing.set(0)
                        self.JumlahAntiJamurKucing.place(x=777, y=737)

                        ButtonNextKucing = Button(new_window8, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.Nota).place(x=950, y=660)

                        self.labelDaruratKucing = tk.Label(new_window8, text="Darurat ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=666)
                        self.JumlahDaruratKucing = tk.Entry(new_window8, textvariable = self.DaruratKucing, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratKucing.place(x=270, y=676)

                        self.labelKontrolKucing = tk.Label(new_window8, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahKontrolKucing = tk.Entry(new_window8, textvariable = self.KontrolKucing, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolKucing.place(x=270, y=499)


                elif jenishewan == "Anjing":
                        
                        new_window9 = tk.Toplevel(self.master)
                        new_window9.title("Healthy Pet")
                        new_window9.geometry("1937x1000")
                
                        self.master.state("zoomed")
                        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                        screen_width = self.master.winfo_screenwidth()
                        screen_height = self.master.winfo_screenheight()
                        self.foto=Image.open("7.jpg")
                        self.foto=self.foto.resize((screen_width,screen_height))
                        self.photoo=ImageTk.PhotoImage(self.foto)
                        label_background = Label(new_window9, image=self.photoo)
                        label_background.pack(fill=BOTH, expand=YES)

                        self.labelCekKesehatanKucing = tk.Label(new_window9, text="Cek Kesehatan", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahCekAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahCekAnjing.set(0)
                        self.JumlahCekAnjing.place(x=270, y=252)

                        self.labelSterilAnjing = tk.Label(new_window9, text="Steril", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSterilAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSterilAnjing.set(0)
                        self.JumlahSterilAnjing.place(x=270, y=310)

                        self.labelVaksinAnjing = tk.Label(new_window9, text="Vaksin", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=363)
                        values=[1,2,3,4]
                        self.JumlahVaksinAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVaksinAnjing.set(0)
                        self.JumlahVaksinAnjing.place(x=270, y=373)

                        self.labelScallingGigi = tk.Label(new_window9, text="Scalling Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahScallingAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahScallingAnjing.set(0)
                        self.JumlahScallingAnjing.place(x=270, y=435)

                        self.labelKontrolAnjing = tk.Label(new_window9, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahKontrolAnjing = tk.Entry(new_window9, textvariable = self.KontrolAnjing, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolAnjing.place(x=270, y=499)

                        self.labelUSGAnjing = tk.Label(new_window9, text="USG", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahUSGAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahUSGAnjing.set(0)
                        self.JumlahUSGAnjing.place(x=270, y=557)

                        self.labelRInapAnjing = tk.Label(new_window9, text="Rawat Inap/hari ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahRInapAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahRInapAnjing.set(0)
                        self.JumlahRInapAnjing.place(x=270, y=615)

                        self.labelDaruratAnjing = tk.Label(new_window9, text="Darurat ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=666)
                        self.JumlahDaruratAnjing = tk.Entry(new_window9, textvariable = self.DaruratAnjing, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratAnjing.place(x=270, y=676)

                        self.labelSuntikRabiesAnjing = tk.Label(new_window9, text="Suntik Rabies ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=726)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSuntikRabiesAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSuntikRabiesAnjing.set(0)
                        self.JumlahSuntikRabiesAnjing.place(x=270, y=736)

#################################################################################################################################################
                        self.labelGroomingAnjing = tk.Label(new_window9, text="Grooming Lengkap ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=247)
                        values=[1,2,3,4]
                        self.JumlahGroomingAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahGroomingAnjing.set(0)
                        self.JumlahGroomingAnjing.place(x=1155, y=252)

                        self.labelMandiAnjing = tk.Label(new_window9, text="Mandi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=305)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiAnjing.set(0)
                        self.JumlahMandiAnjing.place(x=1155, y=310)

                        self.labelMandiJamurAnjing = tk.Label(new_window9, text="Mandi Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=368)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiJamurAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiJamurAnjing.set(0)
                        self.JumlahMandiJamurAnjing.place(x=1155, y=373)

                        self.labelMandiKutuAnjing = tk.Label(new_window9, text="Mandi Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=430)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKutuAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKutuAnjing.set(0)
                        self.JumlahMandiKutuAnjing.place(x=1155, y=435)

                        self.labelMandiKombinasiAnjing = tk.Label(new_window9, text="Mandi Kombinasi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=490)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKombinasiAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKombinasiAnjing.set(0)
                        self.JumlahMandiKombinasiAnjing.place(x=1155, y=495)

                        self.labelPotongRambutAnjing = tk.Label(new_window9, text="Potong Rambut ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=552)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPotongRambutAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPotongRambutAnjing.set(0)
                        self.JumlahPotongRambutAnjing.place(x=1155, y=557)

############################################################################################################################################
                        self.labelMKeringAnjing = tk.Label(new_window9, text="Makanan Kering/ kg", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=247)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMKeringAnjing = ttk.Combobox(new_window9, values=values, width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMKeringAnjing.set(0)
                        self.JumlahMKeringAnjing.place(x=777, y=252)

                        self.labelMBasahAnjing = tk.Label(new_window9, text="Makanan Basah/ 400g ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=305)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMBasahAnjing = ttk.Combobox(new_window9, values=values, width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMBasahAnjing.set(0)
                        self.JumlahMBasahAnjing.place(x=777, y=310)

                        self.labelVitaminAnjing = tk.Label(new_window9, text="Vitamin ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=368)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVitaminAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVitaminAnjing.set(0)
                        self.JumlahVitaminAnjing.place(x=777, y=373)

                        self.labelShampoAnjing = tk.Label(new_window9, text="Shampo", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=430)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahShampoAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahShampoAnjing.set(0)
                        self.JumlahShampoAnjing.place(x=777, y=435)

                        self.labelPastaGigiAnjing = tk.Label(new_window9, text="Pasta Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=494)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPastaGigiAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPastaGigiAnjing.set(0)
                        self.JumlahPastaGigiAnjing.place(x=777, y=499)

                        self.labelPawAnjing = tk.Label(new_window9, text="Paw Balm", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=552)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPawAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPawAnjing.set(0)
                        self.JumlahPawAnjing.place(x=777, y=557)

                        self.labelParfumeAnjing = tk.Label(new_window9, text="Parfume ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=610)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahParfumeAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahParfumeAnjing.set(0)
                        self.JumlahParfumeAnjing.place(x=777, y=615)

                        self.labelAntiKutuAnjing = tk.Label(new_window9, text="Anti Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=671)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiKutuAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiKutuAnjing.set(0)
                        self.JumlahAntiKutuAnjing.place(x=777, y=676)

                        self.labelAntiJamurAnjing = tk.Label(new_window9, text="Anti Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=732)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiJamurAnjing = ttk.Combobox(new_window9, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiJamurAnjing.set(0)
                        self.JumlahAntiJamurAnjing.place(x=777, y=737)

                        ButtonNextAnjing = Button(new_window9, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.Nota).place(x=950, y=660)

                elif jenishewan == "Kelinci":
                        
                        new_window10 = tk.Toplevel(self.master)
                        new_window10.title("Healthy Pet")
                        new_window10.geometry("1937x1000")
                
                        self.master.state("zoomed")
                        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                        screen_width = self.master.winfo_screenwidth()
                        screen_height = self.master.winfo_screenheight()
                        self.foto=Image.open("8.jpg")
                        self.foto=self.foto.resize((screen_width,screen_height))
                        self.photoo=ImageTk.PhotoImage(self.foto)
                        label_background = Label(new_window10, image=self.photoo)
                        label_background.pack(fill=BOTH, expand=YES)

                        self.labelCekKesehatan = tk.Label(new_window10, text="Cek Kesehatan", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahCekKesehatanKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahCekKesehatanKelinci.set(0)
                        self.JumlahCekKesehatanKelinci.place(x=270, y=252)

                        self.labelSterilKelinci = tk.Label(new_window10, text="Steril", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSterilKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSterilKelinci.set(0)
                        self.JumlahSterilKelinci.place(x=270, y=310)

                        self.labelVaksinKelinci = tk.Label(new_window10, text="Vaksin", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVaksinKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVaksinKelinci.set(0)
                        self.JumlahVaksinKelinci.place(x=270, y=373)

                        self.labelScallingKelinci = tk.Label(new_window10, text="Scalling Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahScallingKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahScallingKelinci.set(0)
                        self.JumlahScallingKelinci.place(x=270, y=435)

                        self.labelKontrolKelinci = tk.Label(new_window10, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahKontrolKelinci = tk.Entry(new_window10, textvariable = self.KontrolKelinci, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolKelinci.place(x=270, y=499)

                        self.labelUSGKelinci = tk.Label(new_window10, text="USG", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahUSGKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahUSGKelinci.set(0)
                        self.JumlahUSGKelinci.place(x=270, y=557)

                        self.labelRInapKelinci = tk.Label(new_window10, text="Rawat Inap/ hari", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahRInapKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahRInapKelinci.set(0)
                        self.JumlahRInapKelinci.place(x=270, y=615)
                        
                        self.labelDaruratKelinci = tk.Label(new_window10, text="Darurat ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=666)
                        self.JumlahDaruratKelinci = tk.Entry(new_window10, textvariable = self.DaruratKelinci, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratKelinci.place(x=270, y=676)

                        self.labelSuntikScabies = tk.Label(new_window10, text="Suntik Scabies ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=726)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSuntikScabies = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSuntikScabies.set(0)
                        self.JumlahSuntikScabies.place(x=270, y=736)
################################################################################################################################################
                        self.labelGroomingKelinci = tk.Label(new_window10, text="Grooming Lengkap", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahGroomingKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahGroomingKelinci.set(0)
                        self.JumlahGroomingKelinci.place(x=1166, y=252)

                        self.labeMandiKelinci = tk.Label(new_window10, text="Mandi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKelinci.set(0)
                        self.JumlahMandiKelinci.place(x=1166, y=310)

                        self.labelMandiJamurKelinci = tk.Label(new_window10, text="Mandi Jamur", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiJamurKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiJamurKelinci.set(0)
                        self.JumlahMandiJamurKelinci.place(x=1166, y=373)

                        self.labeMandiKutuKelinci = tk.Label(new_window10, text="Mandi Kutu", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKutuKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKutuKelinci.set(0)
                        self.JumlahMandiKutuKelinci.place(x=1166, y=435)

                        self.labelMandiKombinasiKelinci = tk.Label(new_window10, text="Mandi Kombinasi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=484)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKombinasiKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKombinasiKelinci.set(0)
                        self.JumlahMandiKombinasiKelinci.place(x=1166, y=492)

                        self.labelPotongRambutKelinci = tk.Label(new_window10, text="Potong Rambut", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=545)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPotongRambutKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPotongRambutKelinci.set(0)
                        self.JumlahPotongRambutKelinci.place(x=1166, y=555)
################################################################################################################################################
                        self.labelMakananKelinci = tk.Label(new_window10, text="Rumput Thimothy ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMakananKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMakananKelinci.set(0)
                        self.JumlahMakananKelinci.place(x=730, y=252)

                        self.labelMakananBasahKelinci = tk.Label(new_window10, text="Makanan Basah ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=305)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMakananBasahKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMakananBasahKelinci.set(0)
                        self.JumlahMakananBasahKelinci.place(x=730, y=315)

                        self.labelVitaminKelinci = tk.Label(new_window10, text="Vitamin ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVitaminKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVitaminKelinci.set(0)
                        self.JumlahVitaminKelinci.place(x=730, y=373)

                        self.labelShampooKelinci = tk.Label(new_window10, text="Shampoo ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahShampoKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahShampoKelinci.set(0)
                        self.JumlahShampoKelinci.place(x=730, y=435)

                        self.labelPastaGigiKelinci = tk.Label(new_window10, text="Pasta Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=490)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPastaGigiKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPastaGigiKelinci.set(0)
                        self.JumlahPastaGigiKelinci.place(x=730, y=498)

                        self.labelParfumeKelinci = tk.Label(new_window10, text="Parfume", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahParfumeKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahParfumeKelinci.set(0)
                        self.JumlahParfumeKelinci.place(x=730, y=557)

                        self.labelAntiKutuKelinci = tk.Label(new_window10, text="Anti Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiKutuKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiKutuKelinci.set(0)
                        self.JumlahAntiKutuKelinci.place(x=730, y=615)

                        self.labelAntiJamurKelinci = tk.Label(new_window10, text="Anti Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=666)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiJamurKelinci = ttk.Combobox(new_window10, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiJamurKelinci.set(0)
                        self.JumlahAntiJamurKelinci.place(x=730, y=676)
                        
                        ButtonNextKelinci = Button(new_window10, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.Nota).place(x=950, y=660)

                elif jenishewan == "Hamster":

                        new_window11 = tk.Toplevel(self.master)
                        new_window11.title("Healthy Pet")
                        new_window11.geometry("1937x1000")
                
                        self.master.state("zoomed")
                        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                        screen_width = self.master.winfo_screenwidth()
                        screen_height = self.master.winfo_screenheight()
                        self.foto=Image.open("C:/Users/ASUS/Downloads/menu hamster.jpg")
                        self.foto=self.foto.resize((screen_width,screen_height))
                        self.photoo=ImageTk.PhotoImage(self.foto)
                        label_background = Label(new_window11, image=self.photoo)
                        label_background.pack(fill=BOTH, expand=YES)

                        self.labelCekHamster = tk.Label(new_window11, text="Cek Kesehatan", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahCekHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahCekHamster.set(0)
                        self.JumlahCekHamster.place(x=270, y=252)

                        self.labelKontrolHamster = tk.Label(new_window11, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahKontrolHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahKontrolHamster.set(0)
                        self.JumlahKontrolHamster.place(x=270, y=310)

                        self.labelUSGHamster = tk.Label(new_window11, text="USG", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahUSGHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahUSGHamster.set(0)
                        self.JumlahUSGHamster.place(x=270, y=373)

                        self.labelRInapHamster = tk.Label(new_window11, text="Rawat Inap/ hari", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahRInapHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahRInapHamster.set(0)
                        self.JumlahRInapHamster.place(x=270, y=435)

                        self.labelDaruratHamster = tk.Label(new_window11, text="Darurat", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahDaruratHamster = tk.Entry(new_window11, textvariable = self.DaruratHamster, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratHamster.place(x=270, y=555)

                        self.labelObatHamster = tk.Label(new_window11, text="Obat", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=548)
                        self.JumlahKontrolHamster = tk.Entry(new_window11, textvariable = self.KontrolHamster, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolHamster.place(x=270, y=499)

                            
###############################################################################################################################################
                        self.labelGroomingHamster = tk.Label(new_window11, text="Grooming Pasir ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahGroomingHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahGroomingHamster.set(0)
                        self.JumlahGroomingHamster.place(x=1155, y=252)

                        self.labelMandiJamurHamster = tk.Label(new_window11, text="Mandi Jamur", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiJamurHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiJamurHamster.set(0)
                        self.JumlahMandiJamurHamster.place(x=1155, y=310)

#################################################################################################################################################
                        self.MakananKeringHamster = tk.Label(new_window11, text="Makanan Kering ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=248)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMakananHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMakananHamster.set(0)
                        self.JumlahMakananHamster.place(x=720, y=252)

                        self.MakananBasahHamster = tk.Label(new_window11, text="Makanan Basah ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=310)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMakananBasahHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMakananBasahHamster.set(0)
                        self.JumlahMakananBasahHamster.place(x=720, y=310)

                        self.VitaminHamster = tk.Label(new_window11, text="MVitamin  ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=368)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVitaminHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVitaminHamster.set(0)
                        self.JumlahVitaminHamster.place(x=720, y=373)

                        self.ShampooHamster = tk.Label(new_window11, text="Shampoo ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=430)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahShampooHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahShampooHamster.set(0)
                        self.JumlahShampooHamster.place(x=720, y=435)

                        self.SerbukHamster = tk.Label(new_window11, text="Serbuk/400g ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=489)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSerbukHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSerbukHamster.set(0)
                        self.JumlahSerbukHamster.place(x=720, y=499)

                        self.PasirHamster = tk.Label(new_window11, text="Pasir Zeolit/ 25kg", font=("Britannic Bold",20),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPasirHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPasirHamster.set(0)
                        self.JumlahPasirHamster.place(x=720, y=555)

                        self.ParfumeHamster = tk.Label(new_window11, text="Parfume ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahParfumeHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahParfumeHamster.set(0)
                        self.JumlahParfumeHamster.place(x=720, y=615)

                        self.AntiKutuHamster = tk.Label(new_window11, text="Anti Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=671)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiKutuHamster = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiKutuHamster.set(0)
                        self.JumlahAntiKutuHamster.place(x=720, y=676)

                        self.AntijamurHamster = tk.Label(new_window11, text="Anti Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=478, y=731)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiJamurHams = ttk.Combobox(new_window11, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiJamurHams.set(0)
                        self.JumlahAntiJamurHams.place(x=720, y=736)

                        ButtonNextHamster = Button(new_window11, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.Nota).place(x=950, y=660)
######################################################################################################################################################################################

                elif jenishewan == "Lainnya":

                        new_window12 = tk.Toplevel(self.master)
                        new_window12.title("Healthy Pet")
                        new_window12.geometry("1937x1000")
                
                        self.master.state("zoomed")
                        self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                        screen_width = self.master.winfo_screenwidth()
                        screen_height = self.master.winfo_screenheight()
                        self.foto=Image.open("C:/Users/ASUS/Downloads/menu umum.jpg")
                        self.foto=self.foto.resize((screen_width,screen_height))
                        self.photoo=ImageTk.PhotoImage(self.foto)
                        label_background = Label(new_window12, image=self.photoo)
                        label_background.pack(fill=BOTH, expand=YES)

                        self.labelcekkesehatanUmum = tk.Label(new_window12, text="Cek Kesehatan", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahCekKesehatanUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahCekKesehatanUmum.set(0)
                        self.JumlahCekKesehatanUmum.place(x=270, y=252)
                        
                        self.labelSterilUmum = tk.Label(new_window12, text="Steril", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahSterilUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahSterilUmum.set(0)
                        self.JumlahSterilUmum.place(x=270, y=310)

                        self.labelVaksinUmum = tk.Label(new_window12, text="Vaksin", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVaksinUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVaksinUmum.set(0)
                        self.JumlahVaksinUmum.place(x=270, y=373)

                        self.labelScallingUmum = tk.Label(new_window12, text="Scalling Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahScallingUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahScallingUmum.set(0)
                        self.JumlahScallingUmum.place(x=270, y=435)

                        self.labelKontrolUmum = tk.Label(new_window12, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahKontrolUmum = tk.Entry(new_window12, textvariable = self.KontrolUmum, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolUmum.place(x=270, y=499)

                        self.labelUSGUmum = tk.Label(new_window12, text="USG", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahUSGUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahUSGUmum.set(0)
                        self.JumlahUSGUmum.place(x=270, y=557)

                        self.labelRInapUmum = tk.Label(new_window12, text="Rawat Inap/hari ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=605)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahRInapUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahRInapUmum.set(0)
                        self.JumlahRInapUmum.place(x=270, y=615)

                        self.labelDaruratUmum = tk.Label(new_window12, text="Darurat", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=666)
                        self.JumlahDaruratUmum = tk.Entry(new_window12, textvariable = self.DaruratUmum, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratUmum.place(x=270, y=676)

                        self.labelObatUmum = tk.Label(new_window12, text="Obat", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=726)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahObatUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahObatUmum.set(0)
                        self.JumlahObatUmum.place(x=270, y=736)
 ####################################################################################################################################################################################################
                        self.labelGroomingUmum = tk.Label(new_window12, text="Grooming Lengkap", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=242)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahGroomingUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahGroomingUmum.set(0)
                        self.JumlahGroomingUmum.place(x=1170, y=252)

                        self.labelMandiUmum = tk.Label(new_window12, text="Mandi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=300)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiUmum.set(0)
                        self.JumlahMandiUmum.place(x=1170, y=310)

                        self.labelMandiJamurUmum = tk.Label(new_window12, text="Mandi Jamur", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=363)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiJamurUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiJamurUmum.set(0)
                        self.JumlahMandiJamurUmum.place(x=1170, y=373)

                        self.labelMandiKutuUmum = tk.Label(new_window12, text="Mandi Kutu", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=425)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKutuUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKutuUmum.set(0)
                        self.JumlahMandiKutuUmum.place(x=1170, y=435)

                        self.labelMandiKombinasiUmum = tk.Label(new_window12, text="Mandi Kombinasi ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=485)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMandiKombinasiUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMandiKombinasiUmum.set(0)
                        self.JumlahMandiKombinasiUmum.place(x=1170, y=495)

                        self.labelPotongRambutUmum = tk.Label(new_window12, text="Potong Rambut", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=910, y=547)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPotongRambutUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPotongRambutUmum.set(0)
                        self.JumlahPotongRambutUmum.place(x=1170, y=557)
########################################################################################################################################################################################################
                        self.labelMKeringUmum = tk.Label(new_window12, text="Makanan Kering ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=247)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMKeringUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMKeringUmum.set(0)
                        self.JumlahMKeringUmum.place(x=720, y=252)

                        self.labelMBasahUmum = tk.Label(new_window12, text="Makanan Basah ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=305)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahMBasahUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahMBasahUmum.set(0)
                        self.JumlahMBasahUmum.place(x=720, y=310)

                        self.labelVitaminUmum = tk.Label(new_window12, text="Vitamin ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=368)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahVitaminUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahVitaminUmum.set(0)
                        self.JumlahVitaminUmum.place(x=720, y=373)

                        self.labelShampoUmum = tk.Label(new_window12, text="Shampoo", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=430)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahShampoUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahShampoUmum.set(0)
                        self.JumlahShampoUmum.place(x=720, y=435)

                        self.labelPastaGigiUmum = tk.Label(new_window12, text="Pasta Gigi", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=494)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPastaGigiUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPastaGigiUmum.set(0)
                        self.JumlahPastaGigiUmum.place(x=720, y=499)

                        self.labelPawUmum = tk.Label(new_window12, text="Paw Balm", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=552)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahPawUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahPawUmum.set(0)
                        self.JumlahPawUmum.place(x=720, y=557)

                        self.labelParfumeUmum = tk.Label(new_window12, text="Parfume ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=610)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahParfumeUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahParfumeUmum.set(0)
                        self.JumlahParfumeUmum.place(x=720, y=615)

                        self.labelAntiKutuUmum = tk.Label(new_window12, text="Anti Kutu ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=671)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiKutuUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiKutuUmum.set(0)
                        self.JumlahAntiKutuUmum.place(x=720, y=676)

                        self.labelAntiJamurUmum = tk.Label(new_window12, text="Anti Jamur ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=475, y=732)
                        values=[1, 2, 3, 4, 5]
                        self.JumlahAntiJamurUmum = ttk.Combobox(new_window12, values=values,width=2, font=("Britannic Bold",12), background="#FAEED1")
                        self.JumlahAntiJamurUmum.set(0)
                        self.JumlahAntiJamurUmum.place(x=720, y=737)


                        self.labelDaruratUmum = tk.Label(new_window12, text="Darurat ", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=666)
                        self.JumlahDaruratUmum = tk.Entry(new_window12, textvariable = self.DaruratUmum, width=4, font=("Britannic Bold",12))
                        self.JumlahDaruratUmum.place(x=270, y=676)

                        self.labelKontrolUmum = tk.Label(new_window12, text="Kontrol", font=("Britannic Bold",21),fg="#42291C", background="#F9F9E0", height=1).place(x=45, y=489)
                        self.JumlahKontrolUmum = tk.Entry(new_window12, textvariable = self.KontrolUmum, width=4, font=("Britannic Bold",12))
                        self.JumlahKontrolUmum.place(x=270, y=499)

                        ButtonNextUmum = Button(new_window12, text="Next", bg="#FAEED1", width=15, height=1, font=("Britannic Bold", 20), command=self.Nota).place(x=950, y=660)

        def Nota(self):
                new_window13 = tk.Toplevel(self.master)
                new_window13.title("Healthy Pet")
                new_window13.geometry("1937x1000")
                
                self.master.state("zoomed")
                self.master.resizable(width=tk.FALSE, height=tk.FALSE)
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight() 
                self.foto=Image.open("C:/Users/ASUS/Downloads/nota.png")
                self.foto=self.foto.resize((screen_width,screen_height))
                self.foto.place(x=0, y=0)
                self.photoo=ImageTk.PhotoImage(self.foto)
                
                label_background = Label(new_window13, image=self.photoo)
                label_background.pack(fill=BOTH, expand=YES)

                self.jumlahproduk = self.SetelahNext3.get()
                self.JumlahProduk = tk.Label(new_window13, text=f"{self.jumlahproduk}", width=1, height=1, font=("Times New Roman", 16), bg="#FAEED1")
                self.JumlahProduk.place(x=705, y=435)

                self.namehelper = self.EntryNamaHelper.get()
                self.NamaHelper = tk.Label(new_window13, text=f"{self.namehelper}", width=1, height=1, font=("Times New Roman", 16), bg="#FAEED1").place(x=300, y=400)
                # self.NamaHelper

                


        def TotalHarga(self):
                self.hargaCekKesKucing == self.JumlahCekKesehatanKucing.get()*120000
                self.hargaSterilKucing == self.JumlahSterilKucing.get()*300000
                if self.JumlahVaksinKucing == 3:
                        self.hargaVaksinKucing == self.JumlahVaksinKucing.get()*190000
                else:
                        self.hargaVaksinKucing == self.JumlahVaksinKucing.get()*170000
                # self.




                

                        
                


  





root = tk.Tk()
app = HealthyPet(root)
root.mainloop()