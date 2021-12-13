from tkinter import *

class App():


	#Attributes - Fields
	#Constructors
	def __init__(self):


			self.root = Tk()
			self.root.title("My Application")
			self.root.geometry("720x480")
			self.root.resizable(0, 0)
			
			# Scène du suivi du patient
			self.frame = Frame(self.root)
			
			self.frame1 = Frame(self.root,width =720, height =480)
			self.frame2 = Frame(self.root,width =720, height =480)
			self.frame3 = Frame(self.root,width =720, height =480)
			self.frame4 = Frame(self.root,width =720, height =480)
			self.frame5 = Frame(self.root,width =720, height =480)
			self.frame6 = Frame(self.root,width =720, height =480)

			bg = PhotoImage(file="test.png")
			my_Label = Label(self.frame, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			my_Label = Label(self.frame1, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frame1.pack_propagate(False)
			my_Label = Label(self.frame2, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frame2.pack_propagate(False)
			my_Label = Label(self.frame3, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			my_Label = Label(self.frame4, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			my_Label = Label(self.frame5, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			my_Label = Label(self.frame6, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			
			
			# Label du suivi du patient
			self.lab1f = Label(self.frame, text = "Système Expert", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f1 = Label(self.frame1, text = "Quelle est ton age ?", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f2 = Label(self.frame2, text = "Etat de la consultation ?", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f3 = Label(self.frame3, text = "Quelle est la dyoptrie ?", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f4 = Label(self.frame4, text = "Quel est le Kmean ?", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f5 = Label(self.frame5, text = "Quelle est l'opacité ( 0 ou 1)?", font=("Courrier", 30),fg='#2f61ad')
			self.lab1f6 = Label(self.frame6, text = "Quelle est la pachymétrie?", font=("Courrier", 30),fg='#2f61ad')

			# Input du suivi du patient
			self.entry1 = Entry(self.frame1, width=75)
			self.entry2 = Entry(self.frame2, width=75)
			self.entry3 = Entry(self.frame3, width=75)
			self.entry4 = Entry(self.frame4, width=75)
			self.entry5 = Entry(self.frame5, width=75)
			self.entry6 = Entry(self.frame6, width=75)

			# Bouton de la première interface
			self.btn0to1 = Button(self.frame, text = "Suivi de la maladie",font=("Courrier", 14), bg='white', fg='#2f61ad', command = self.fnc0to1)
			self.btn0 = Button(self.frame, text = "Méthode de Mazzotta",font=("Courrier", 14), bg='white', fg='#2f61ad', command = self.fm0to1)
			self.boutonsilva = Button(self.frame, text = "Méthode de Wittig-Silva",font=("Courrier", 14), bg='white', fg='#2f61ad', command = self.fs0to1)
			self.boutonquit = Button(self.frame, text="Quitter",font=("Courrier", 14), bg='white', fg='#2f61ad',command = self.root.destroy)
			self.btnkcNon = Button(self.frame, text = "Thérapeutique KC non Evolutif",font=("Courrier", 14), bg='white', fg='#2f61ad', command = self.fg0to1)
			self.btnkc = Button(self.frame, text = "Thérapeutique KC Evolutif",font=("Courrier", 14), bg='white', fg='#2f61ad', command = self.fa0to1)

			# Bouton suivant du suivi du patient
			self.btn1to2 = Button(self.frame1, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc1to2)
			self.btn2to3 = Button(self.frame2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc2to3)
			self.btn3to4 = Button(self.frame3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad',command = self.fnc3to4)
			self.btn4to5 = Button(self.frame4, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad',command = self.fnc4to5)
			self.btn5to6 = Button(self.frame5, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad',command = self.fnc5to6)
			# Bouton allant calculer la maladie
			self.btn6toresult = Button(self.frame6, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad',command = self.niveaux)

			# Bouton retour du suivi du patient
			self.btn2to1 = Button(self.frame2, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc2to1)
			self.btn3to2 = Button(self.frame3, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc3to2)
			self.btn4to3 = Button(self.frame4, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc4to3)
			self.btn5to4 = Button(self.frame5, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc5to4)
			self.btn6to5 = Button(self.frame6, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fnc6to5)

			# Scène de la méthode Mazzo
			self.frameMazzo1 = Frame(self.root,width =720, height =480)
			self.frameMazzo2 = Frame(self.root,width =720, height =480)
			self.frameMazzo3 = Frame(self.root,width =720, height =480)
			self.frameMazzo4 = Frame(self.root,width =720, height =480)
			self.frameMazzo5 = Frame(self.root,width =720, height =480)
			self.frameMazzo6 = Frame(self.root,width =720, height =480)

			my_Label = Label(self.frameMazzo1, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo1.pack_propagate(False)
			my_Label = Label(self.frameMazzo2, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo2.pack_propagate(False)
			my_Label = Label(self.frameMazzo3, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo3.pack_propagate(False)
			my_Label = Label(self.frameMazzo4, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo4.pack_propagate(False)
			my_Label = Label(self.frameMazzo5, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo5.pack_propagate(False)
			my_Label = Label(self.frameMazzo6, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameMazzo6.pack_propagate(False)
			# Scène de la méthode Silva
			self.frameSilva2 = Frame(self.root,width =720, height =480)
			self.frameSilva3 = Frame(self.root,width =720, height =480)
			self.frameSilva4 = Frame(self.root,width =720, height =480)
			self.frameSilva5 = Frame(self.root,width =720, height =480)
			self.frameSilva6 = Frame(self.root,width =720, height =480)

			my_Label = Label(self.frameSilva2, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameSilva2.pack_propagate(False)
			my_Label = Label(self.frameSilva3, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameSilva3.pack_propagate(False)
			my_Label = Label(self.frameSilva4, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameSilva4.pack_propagate(False)
			my_Label = Label(self.frameSilva5, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameSilva5.pack_propagate(False)
			my_Label = Label(self.frameSilva6, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameSilva6.pack_propagate(False)
			# Scène KC Non Evolutif
			self.frameNonEvo1 = Frame(self.root,width =720, height =480)
			self.frameNonEvo2 = Frame(self.root,width =720, height =480)
			self.frameNonEvo3 = Frame(self.root,width =720, height =480)

			my_Label = Label(self.frameNonEvo1, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameNonEvo1.pack_propagate(False)
			my_Label = Label(self.frameNonEvo2, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameNonEvo2.pack_propagate(False)
			my_Label = Label(self.frameNonEvo3, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameNonEvo3.pack_propagate(False)

			# Scène KC Evolutif
			self.frameEvo1 = Frame(self.root,width =720, height =480)
			self.frameEvo2 = Frame(self.root,width =720, height =480)
			self.frameEvo3 = Frame(self.root,width =720, height =480)
			self.frameEvo4 = Frame(self.root,width =720, height =480)
			self.frameEvo5 = Frame(self.root,width =720, height =480)
			self.frameEvo6 = Frame(self.root,width =720, height =480)
			self.frameEvo7 = Frame(self.root,width =720, height =480)
			self.frameEvo8 = Frame(self.root,width =720, height =480)

			my_Label = Label(self.frameEvo1, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo1.pack_propagate(False)
			my_Label = Label(self.frameEvo2, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo2.pack_propagate(False)
			my_Label = Label(self.frameEvo3, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo3.pack_propagate(False)
			my_Label = Label(self.frameEvo4, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo4.pack_propagate(False)
			my_Label = Label(self.frameEvo5, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo5.pack_propagate(False)
			my_Label = Label(self.frameEvo6, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo6.pack_propagate(False)
			my_Label = Label(self.frameEvo7, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo7.pack_propagate(False)
			my_Label = Label(self.frameEvo8, image=bg)
			my_Label.place(x=0,y=0,relwidth=1, relheight=1)
			self.frameEvo8.pack_propagate(False)

			# Label + Bouton +Input de la Méthode Mazzo sur l'age 
			self.labMazzo1 = Label(self.frameMazzo1, text = "Quelle est ton age ?", font=("Courrier", 30),fg='#2f61ad')
			self.entryMazzo1 = Entry(self.frameMazzo1, width=75)
			self.btn1_2 = Button(self.frameMazzo1, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm1to2)

			# Label de la méthode Silva
			self.labSilva4 = Label(self.frameSilva2, text = "Quel est l'ancien Kmax? ", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva5 = Label(self.frameSilva2, text = "Quel est le Kmax?", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva6 = Label(self.frameSilva3, text = "Quelle est l'ancienne taille du cylindre subjectif  :", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva7 = Label(self.frameSilva3, text = "Quelle est la taille du cylindre subjectif  :", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva8 = Label(self.frameSilva4, text = "Quelle est l'ancienne taille sphérique :", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva9 = Label(self.frameSilva4, text = "Quelle est la taille sphérique :  :", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva10 = Label(self.frameSilva5, text = "Quelle est l'ancien rayon de la lentille :", font=("Courrier", 30), fg='#2f61ad')
			self.labSilva2 = Label(self.frameSilva5, text = "Quelle est le rayon de la lentille :", font=("Courrier", 30), fg='#2f61ad')

			# Input de la méthode Silva
			self.entrySilva4 = Entry(self.frameSilva2, width=75)
			self.entrySilva5 = Entry(self.frameSilva2, width=75)
			self.entrySilva6 = Entry(self.frameSilva3, width=75)
			self.entrySilva7 = Entry(self.frameSilva3, width=75)
			self.entrySilva8 = Entry(self.frameSilva4, width=75)
			self.entrySilva9 = Entry(self.frameSilva4, width=75)
			self.entrySilva10 = Entry(self.frameSilva5, width=75)
			self.entrySilva2 = Entry(self.frameSilva5, width=75)

			# Bouton suivant de la méthode Silva
			self.btnAVC_sphere = Button(self.frameSilva2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fs2to3)
			self.btnsphere_SAI = Button(self.frameSilva3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fs3to4)
			self.btnSAI_pachy = Button(self.frameSilva4, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fs4to5)
			self.btnpachy_kmean = Button(self.frameSilva5, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fs5tosilva)
			
			# Bouton retour de la méthode Silva
			self.btnsphere_AVC = Button(self.frameSilva3, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fsshe_avc)
			self.btnSAI_shere = Button(self.frameSilva4, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fssai_she)
			self.btnpachy_SAI = Button(self.frameSilva5, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fspachy_sai)
			

			# Composant KC Non Evolutif
			self.labNonEvo1 = Label(self.frameNonEvo1, text = "Le patient à t'il déjà subi une opération pour le keratocone : ", font=("Courrier", 15),fg='#2f61ad')
			self.labNonEvo2 = Label(self.frameNonEvo2, text = "Quelle est l'AV du patient : ", font=("Courrier", 30),fg='#2f61ad')

			self.btnNonEvo1to2 = Button(self.frameNonEvo1, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.nonEvo1to2)
			self.btnNonEvo2to3 = Button(self.frameNonEvo2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.nonEvo2to3)
			self.btnNonEvo2to1 = Button(self.frameNonEvo2, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.nonEvo2to1)

			self.entryNonEvo1 = Entry(self.frameNonEvo1, width=75)
			self.entryNonEvo2 = Entry(self.frameNonEvo2, width=75)


			# Composant KC Evolutif
			self.labEvo1 = Label(self.frameEvo1, text = "Quelle est l'AV du patient : ", font=("Courrier", 18), fg='#2f61ad')
			self.labEvo2 = Label(self.frameEvo2, text = "Est ce que le patient possède une cicatrice cornéenne profonde  : ", font=("Courrier", 18), fg='#2f61ad')
			self.labEvo3 = Label(self.frameEvo3, text = "Quelle est la taille de la cornée  :  ", font=("Courrier", 18), fg='#2f61ad')
			self.labEvo4 = Label(self.frameEvo4, text = "Avez-vous deja subi une opération (CXL, LR, PTK, etc...) : ", font=("Courrier", 18), fg='#2f61ad')
			self.labEvo5 = Label(self.frameEvo5, text = "Le patient présente-t-il un des symptomes suivants Grossesse/Allaitement", font=("Courrier", 18), fg='#2f61ad')



			self.btnEvo1to2 = Button(self.frameEvo1, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo1to2)
			self.btnEvo2to3 = Button(self.frameEvo2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo2to3)
			self.btnEvo3to4 = Button(self.frameEvo3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo3to4)
			self.btnEvo4to5 = Button(self.frameEvo4, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo4to5)
			self.btnEvo5to6 = Button(self.frameEvo5, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo5to6)

			self.btnEvo2to1 = Button(self.frameEvo2, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo2to1)
			self.btnEvo3to2 = Button(self.frameEvo3, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo3to2)
			self.btnEvo4to3 = Button(self.frameEvo4, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo4to3)
			self.btnEvo5to4 = Button(self.frameEvo5, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo5to4)
	
			self.entryEvo1 = Entry(self.frameEvo1, width=75)
			self.entryEvo2 = Entry(self.frameEvo2, width=75)
			self.entryEvo3 = Entry(self.frameEvo3, width=75)
			self.entryEvo4 = Entry(self.frameEvo4, width=75)
			self.entryEvo5 = Entry(self.frameEvo5, width=75)
			

			# Composant présent sur la scène frameEvo1
			self.labEvo1.pack(pady=100)
			self.entryEvo1.pack()
			self.entryEvo1.focus()
			self.btnEvo1to2.pack(pady=10)

			# Composant présent sur la scène frameEvo2
			self.labEvo2.pack(pady=100)
			self.entryEvo2.pack()
			self.entryEvo2.focus()
			self.btnEvo2to3.pack(pady=10)
			self.btnEvo2to1.pack()

			# Composant présent sur la scène frameEvo3
			self.labEvo3.pack(pady=100)
			self.entryEvo3.pack()
			self.entryEvo3.focus()
			self.btnEvo3to4.pack(pady=10)
			self.btnEvo3to2.pack()

			# Composant présent sur la scène frameEvo4
			self.labEvo4.pack(pady=100)
			self.entryEvo4.pack()
			self.entryEvo4.focus()
			self.btnEvo4to5.pack(pady=10)
			self.btnEvo4to3.pack()

			# Composant présent sur la scène frameEvo5
			self.labEvo5.pack(pady=100)
			self.entryEvo5.pack()
			self.entryEvo5.focus()
			self.btnEvo5to6.pack(pady=10)
			self.btnEvo5to4.pack()

			# Composant présent sur la scène frameNonEvo1
			self.labNonEvo1.pack(pady=100)
			self.entryNonEvo1.pack()
			self.entryNonEvo1.focus()
			self.btnNonEvo1to2.pack(pady=10)

			# Composant présent sur la scène frameNonEvo2
			self.labNonEvo2.pack(pady=100)
			self.entryNonEvo2.pack()
			self.entryNonEvo2.focus()
			self.btnNonEvo2to3.pack(pady=10)
			self.btnNonEvo2to1.pack()

			# Composant présent sur la scène FrameSilva2
			self.labSilva4.pack(pady=50)
			self.entrySilva4.pack()
			self.entrySilva4.focus()
			self.labSilva5.pack(pady=50)
			self.entrySilva5.pack()
			self.btnAVC_sphere.pack(pady=10)

			# Composant présent sur la scène FrameSilva3
			self.labSilva6.pack(pady=50)
			self.entrySilva6.pack()
			self.entrySilva6.focus()
			self.labSilva7.pack(pady=50)
			self.entrySilva7.pack()
			self.btnsphere_SAI.pack(pady=10)
			self.btnsphere_AVC.pack(pady=10)

			# Composant présent sur la scène FrameSilva4
			self.labSilva8.pack(pady=50)
			self.entrySilva8.pack()
			self.entrySilva8.focus()
			self.labSilva9.pack(pady=50)
			self.entrySilva9.pack()
			self.btnSAI_pachy.pack(pady=10)
			self.btnSAI_shere.pack(pady=10)

			# Composant présent sur la scène FrameSilva5
			self.labSilva10.pack(pady=50)
			self.entrySilva10.pack()
			self.entrySilva10.focus()
			self.labSilva2.pack(pady=50)
			self.entrySilva2.pack()
			self.btnpachy_kmean.pack(pady=10)
			self.btnpachy_SAI.pack(pady=10)

			#Composant présent sur la scène frame 
			self.lab1f.grid(row=0,columnspan=3,pady=85)
			self.btn0to1.grid(row=1, column=0)
			self.btn0.grid(row=2, column=0,columnspan=2,padx=140,pady=10)
			self.boutonsilva.grid(row=2, column=1,columnspan=2,)
			self.boutonquit.grid(row=3,column=2, pady=110)
			self.btnkcNon.grid(row=1,column=1)
			self.btnkc.grid(row=1,column=2)

			#Composant présent sur la scène frame 1
			self.lab1f1.pack(padx=5,pady=100)
			self.entry1.pack(padx=5,pady=5)
			self.entry1.focus()
			self.btn1to2.pack(pady=10)
			

			# Composant présent sur la scène frame 2
			self.lab1f2.pack(pady=100)
			self.entry2.pack()
			self.entry2.focus()
			self.btn2to3.pack(pady=10)
			self.btn2to1.pack(pady=10)
			

			# Composant présent sur la scène frame 3
			self.lab1f3.pack(pady=100)
			self.entry3.pack()
			self.entry3.focus()
			self.btn3to4.pack(pady=10)
			self.btn3to2.pack(pady=10)
			self.frame3.pack_propagate(False)

			# Composant présent sur la scène frame 4
			self.lab1f4.pack(pady=100)
			self.entry4.pack()
			self.entry4.focus()
			self.btn4to5.pack(pady=10)
			self.btn4to3.pack(pady=10)
			self.frame4.pack_propagate(False)

			# Composant présent sur la scène frame 5
			self.lab1f5.pack(pady=100)
			self.entry5.pack()
			self.entry5.focus()
			self.btn5to6.pack(pady=10)
			self.btn5to4.pack(pady=10)
			self.frame5.pack_propagate(False)

			# Composant présent sur la scène frame 6
			self.lab1f6.pack(pady=100)
			self.entry6.pack()
			self.entry6.focus()
			self.btn6toresult.pack(pady=10)
			self.btn6to5.pack(pady=10)
			self.frame6.pack_propagate(False)

			# Composant présent sur la scène frameMazzo1 
			self.labMazzo1.pack(pady=100)
			self.entryMazzo1.pack()
			self.entryMazzo1.focus()
			self.btn1_2.pack(pady=10)


			# Chosir la première scene que l'on affiche
			self.frame.pack()
			self.root.mainloop()


	#Behaviours - Methods
# Mathode de suivi de la maladie
	def fnc1to2(self):
		self.frame1.pack_forget()
		self.frame2.pack(expand=1)
	def fnc2to3(self):
		self.frame2.pack_forget()
		self.frame3.pack(expand=1)
	def fnc2to1(self):
		self.frame2.pack_forget()
		self.frame1.pack(expand=1)
	def fnc3to2(self):
		self.frame3.pack_forget()
		self.frame2.pack(expand=1)
	def fnc0to1(self):
		self.frame.pack_forget()
		self.frame1.pack(expand=1)
	def fnc3to4(self):
		self.frame3.pack_forget()
		self.frame4.pack(expand=1)
	def fnc4to5(self):
		self.frame4.pack_forget()
		self.frame5.pack(expand=1)
	def fnc5to6(self):
		self.frame5.pack_forget()
		self.frame6.pack(expand=1)	
	def fnc6to5(self):
		self.frame6.pack_forget()
		self.frame5.pack(expand=1)
	def fnc5to4(self):
		self.frame5.pack_forget()
		self.frame4.pack(expand=1)
	def fnc4to3(self):
		self.frame4.pack_forget()
		self.frame3.pack(expand=1)

# Calcul le diagnostique
	def result(self,KC,niveau):
		if(self.entry1.get()==''):
			self.entry1.insert(0,0)
		age=int(self.entry1.get())
		if(self.entry2.get()==''):
			self.entry2.insert(0,0)
		consultation=int(self.entry2.get())
		self.entry1.delete(0, 'end')
		self.entry2.delete(0, 'end')
		self.frame6.pack_forget()
		self.frame.pack(expand=1)
		
		if (age<15):
			if (consultation == 1):
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 1 à 3 mois ou CXL d’emblée"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 1 à 3 mois ou CXL d’emblée"
				elif (KC == "sévère"):
					msg="CXL d’emblée si non contre-indiqué ou surveillance à 1 mois"
			else:
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois"
	                
		if (age>15 and age<20):
			if (consultation == 1):
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois ou CXL d’emblée"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois ou CXL d’emblée"
				elif (KC == "sévère"):
					msg="CXL d’emblée si non contre-indiqué ou surveillance à 1 mois"
			else:
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois"

		if (age>20 and age<=30):
			if (consultation == 1):
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 3 mois"
			else:
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
	        
		if (age>30 and age<40):
			if (consultation == 1):
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 3 à 6 mois"
			else:
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
	                
		if (age>40):
			if (consultation == 1):
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois"
			else:
				if (KC == "léger"):
					msg="Le prochain rendez-vous est à prendre dans 1 an"
				elif (KC == "modéré"):
					msg="Le prochain rendez-vous est à prendre dans 1 an"
				elif (KC == "sévère"):
					msg="Le prochain rendez-vous est à prendre dans 6 mois à 1 an" 
		self.popupmsg(msg,niveau)

# Fenetre popup affichant les résultats
	def popupmsg(self,msg,niveau):
	    popup = Tk()
	    popup.title("Les Résultats")
	    popup.geometry("480x360")
	    label = Label(popup, text=msg)
	    label.pack(side="top", fill="x", pady=10)
	    if (niveau!=None):
	    	label = Label(popup, text=niveau)
	    	label.pack(side="top", fill="x", pady=10)
	    B1 = Button(popup, text="Okay", command = popup.destroy)
	    B1.pack()
	    popup.mainloop()

# Evalue le niveau de la maladie (KC)
	def niveaux(self):
		if(self.entry3.get()==''):
			self.entry3.insert(0,0)
		Myopie=int(self.entry3.get())
		if(self.entry4.get()==''):
			self.entry4.insert(0,0)
		Kmean=int(self.entry4.get())
		if(self.entry5.get()==''):
			self.entry5.insert(0,0)
		Opacite=int(self.entry5.get())
		if(self.entry6.get()==''):
			self.entry6.insert(0,0)
		Pachy=int(self.entry6.get())
		if (Myopie<5 and Kmean<=48 ): 
			stade=1
			KC="léger"
			niveau="Le stade de la maladie est un KC légé de stade 1"
		elif (Myopie>=5 and Myopie<8 and Kmean<=53 and Opacite==0 and Pachy>=400):
			stade=2
			KC="modéré"
			niveau="Le stade de la maladie est un KC modéré de stade 2"
		elif (Myopie>8 and Myopie<10 and Kmean>53 and Opacite==0 and Pachy<400 and Pachy>=300):
			stade =3
			KC="modéré"
			niveau="Le stade de la maladie est un KC modéré de stade 3"
		elif (Kmean>=55 and Opacite==1 and Pachy<300):
			stade=4
			KC="sévère"
			niveau="Le stade de la maladie est un KC sévère de stade 4"
		else :
			stade=4
			KC="sévère"
			niveau="Les données discordantes de la maladie sont considérées comme de stade 4"

		self.result(KC,niveau)

# Méthode de Mazzo changement de scène
	def fm0to1(self):
		self.frame.pack_forget()
		self.frameMazzo1.pack(expand=1)
	def fm1to2(self):
		if(self.entryMazzo1.get()==''):
			self.entryMazzo1.insert(0,0)
		age=int(self.entryMazzo1.get())
		self.calcul_age(age)
		self.frameMazzo1.pack_forget()
		self.frameMazzo2.pack(expand=1)	
	def fm2to3(self):
		self.frameMazzo2.pack_forget()
		self.frameMazzo3.pack(expand=1)
	def fm3to4(self):
		self.frameMazzo3.pack_forget()
		self.frameMazzo4.pack(expand=1)
	def fm4to5(self):
		self.frameMazzo4.pack_forget()
		self.frameMazzo5.pack(expand=1)
	def fm5to6(self):
		self.frameMazzo5.pack_forget()
		self.frameMazzo6.pack(expand=1)
	def fm2to3(self):
		self.frameMazzo2.pack_forget()
		self.frameMazzo3.pack(expand=1)
	def fm2to1(self):
		self.frameMazzo2.pack_forget()
		self.frameMazzo1.pack(expand=1)
	def fm3to2(self):
		self.frameMazzo3.pack_forget()
		self.frameMazzo2.pack(expand=1)
	def methode(self):
		self.frameMazzo6.pack_forget()
		if(self.entryMazzo2.get()==''):
			self.entryMazzo2.insert(0,0)
		Pachy=float(self.entryMazzo2.get())
		if(self.entryMazzo3.get()==''):
			self.entryMazzo3.insert(0,0)
		Kmean=float(self.entryMazzo3.get())
		if(self.entryMazzo4.get()==''):
			self.entryMazzo4.insert(0,0)
		ancien_AVC=float(self.entryMazzo4.get())
		if(self.entryMazzo5.get()==''):
			self.entryMazzo5.insert(0,0)
		nouveau_AVC=float(self.entryMazzo5.get())
		if(self.entryMazzo6.get()==''):
			self.entryMazzo6.insert(0,0)
		Sphere_4=float(self.entryMazzo6.get())
		if(self.entryMazzo7.get()==''):
			self.entryMazzo7.insert(0,0)
		Sphere=float(self.entryMazzo7.get())
		if(self.entryMazzo8.get()==''):
			self.entryMazzo8.insert(0,0)
		SAI_4=float(self.entryMazzo8.get())
		if(self.entryMazzo9.get()==''):
			self.entryMazzo9.insert(0,0)
		SAI=float(self.entryMazzo9.get())
		if(self.entryMazzo10.get()==''):
			self.entryMazzo10.insert(0,0)
		Pachy_4=float(self.entryMazzo10.get())
		if(self.entryMazzo11.get()==''):
			self.entryMazzo11.insert(0,0)
		Kmean_4=float(self.entryMazzo11.get())
		self.entryMazzo1.delete(0, 'end')
		self.entryMazzo2.delete(0, 'end')
		self.entryMazzo3.delete(0, 'end')
		self.entryMazzo4.delete(0, 'end')
		self.entryMazzo5.delete(0, 'end')
		self.entryMazzo6.delete(0, 'end')
		self.entryMazzo7.delete(0, 'end')
		self.entryMazzo8.delete(0, 'end')
		self.entryMazzo9.delete(0, 'end')
		self.entryMazzo10.delete(0, 'end')
		self.entryMazzo11.delete(0, 'end')
		i=0
		niveau=None
		if(nouveau_AVC-ancien_AVC>0.5):
			i=i+1
		if(Sphere-Sphere_4>0.5):
			i=i+1
		if(SAI-SAI_4>1):
			i=i+1
		if(Kmean-Kmean_4>1):
			i=i+1
		if(Pachy-Pachy_4>10):
			i=i+1
		if(i>=3):
			msg="La maladie est évolutive"
		else:
			msg="La maladie n'est pas concidérée comme évolutive"
		self.frame.pack(expand=1)
		self.popupmsg(msg,niveau)

# Bouton retour sur chaque scène
	def fmshe_avc(self):
		self.frameMazzo3.pack_forget()
		self.frameMazzo2.pack(expand=1)
	def fmsai_she(self):
		self.frameMazzo4.pack_forget()
		self.frameMazzo3.pack(expand=1)
	def fmpachy_sai(self):
		self.frameMazzo5.pack_forget()
		self.frameMazzo4.pack(expand=1)
	def fmkmea_pach(self):
		self.frameMazzo6.pack_forget()
		self.frameMazzo5.pack(expand=1)
# En fonction de l'age affiche différents textes
	def calcul_age(self,age):
		if (age<18):
			self.labMazzo4 = Label(self.frameMazzo2, text = "Quelle est l'AVC d'il y a 4 mois : ", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo5 = Label(self.frameMazzo2, text = "Quelle est le nouveau AVC  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo6 = Label(self.frameMazzo3, text = "Quelle est la sphere d'il y a 4 mois : ", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo7 = Label(self.frameMazzo3, text = "Quelle est la nouvelle sphere  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo8 = Label(self.frameMazzo4, text = "Quelle est l'SAI d'il y a 4 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo9 = Label(self.frameMazzo4, text = "Quelle est le nouveau SAI  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo10 = Label(self.frameMazzo5, text = "Quelle est la pachymetrie d'il y a 4 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo2 = Label(self.frameMazzo5, text = "Quelle est la pachymétrie?", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo11 = Label(self.frameMazzo6, text = "Quelle est le Kmean d'il y a 4 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo3 = Label(self.frameMazzo6, text = "Quel est le Kmean?", font=("Courrier", 30), fg='#2f61ad')

			# global entryMazzo2,entryMazzo3,entryMazzo4,entryMazzo5,entryMazzo6,entryMazzo7,entryMazzo8,entryMazzo9,entryMazzo10,entryMazzo11
			self.entryMazzo4 = Entry(self.frameMazzo2, width=75)
			self.entryMazzo5 = Entry(self.frameMazzo2, width=75)
			self.entryMazzo6 = Entry(self.frameMazzo3, width=75)
			self.entryMazzo7 = Entry(self.frameMazzo3, width=75)
			self.entryMazzo8 = Entry(self.frameMazzo4, width=75)
			self.entryMazzo9 = Entry(self.frameMazzo4, width=75)
			self.entryMazzo10 = Entry(self.frameMazzo5, width=75)
			self.entryMazzo2 = Entry(self.frameMazzo5, width=75)
			self.entryMazzo11 = Entry(self.frameMazzo6, width=75)
			self.entryMazzo3 = Entry(self.frameMazzo6, width=75)

			self.btnAVC_sphere = Button(self.frameMazzo2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm2to3)
			self.btnsphere_SAI = Button(self.frameMazzo3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm3to4)
			self.btnSAI_pachy = Button(self.frameMazzo4, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm4to5)
			self.btnpachy_kmean = Button(self.frameMazzo5, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm5to6)
			self.btnkmean_result = Button(self.frameMazzo6, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.methode)

			self.btnsphere_AVC = Button(self.frameMazzo3, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmshe_avc)
			self.btnSAI_shere = Button(self.frameMazzo4, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmsai_she)
			self.btnpachy_SAI = Button(self.frameMazzo5, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmpachy_sai)
			self.btnkmean_pachy = Button(self.frameMazzo6, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmkmea_pach)

			self.labMazzo4.pack(pady=50)
			self.entryMazzo4.pack()
			self.entryMazzo4.focus()
			self.labMazzo5.pack(pady=50)
			self.entryMazzo5.pack()
			self.btnAVC_sphere.pack(pady=10)

			self.labMazzo6.pack(pady=50)
			self.entryMazzo6.pack()
			self.entryMazzo6.focus()
			self.labMazzo7.pack(pady=50)
			self.entryMazzo7.pack()
			self.btnsphere_SAI.pack(pady=10)
			self.btnsphere_AVC.pack(pady=10)

			self.labMazzo8.pack(pady=50)
			self.entryMazzo8.pack()
			self.entryMazzo8.focus()
			self.labMazzo9.pack(pady=50)
			self.entryMazzo9.pack()
			self.btnSAI_pachy.pack(pady=10)
			self.btnSAI_shere.pack(pady=10)

			self.labMazzo10.pack(pady=50)
			self.entryMazzo10.pack()
			self.entryMazzo10.focus()
			self.labMazzo2.pack(pady=50)
			self.entryMazzo2.pack()
			self.btnpachy_kmean.pack(pady=10)
			self.btnpachy_SAI.pack(pady=10)

			self.labMazzo11.pack(pady=50)
			self.entryMazzo11.pack()
			self.entryMazzo11.focus()
			self.labMazzo3.pack(pady=50)
			self.entryMazzo3.pack()
			self.btnkmean_result.pack(pady=10)
			self.btnkmean_pachy.pack(pady=10)
		else:
			self.labMazzo4 = Label(self.frameMazzo2, text = "Quelle est l'AVC d'il y a 6 mois : ", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo5 = Label(self.frameMazzo2, text = "Quelle est le nouveau AVC  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo6 = Label(self.frameMazzo3, text = "Quelle est la sphere d'il y a 6 mois : ", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo7 = Label(self.frameMazzo3, text = "Quelle est la nouvelle sphere  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo8 = Label(self.frameMazzo4, text = "Quelle est l'SAI d'il y a 6 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo9 = Label(self.frameMazzo4, text = "Quelle est le nouveau SAI  :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo10 = Label(self.frameMazzo5, text = "Quelle est la pachymetrie d'il y a 6 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo2 = Label(self.frameMazzo5, text = "Quelle est la pachymétrie?", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo11 = Label(self.frameMazzo6, text = "Quelle est le Kmean d'il y a 6 mois :", font=("Courrier", 30), fg='#2f61ad')
			self.labMazzo3 = Label(self.frameMazzo6, text = "Quel est le Kmean?", font=("Courrier", 30), fg='#2f61ad')

			# global entryMazzo2,entryMazzo3,entryMazzo4,entryMazzo5,entryMazzo6,entryMazzo7,entryMazzo8,entryMazzo9,entryMazzo10,entryMazzo11
			self.entryMazzo4 = Entry(self.frameMazzo2, width=75)
			self.entryMazzo5 = Entry(self.frameMazzo2, width=75)
			self.entryMazzo6 = Entry(self.frameMazzo3, width=75)
			self.entryMazzo7 = Entry(self.frameMazzo3, width=75)
			self.entryMazzo8 = Entry(self.frameMazzo4, width=75)
			self.entryMazzo9 = Entry(self.frameMazzo4, width=75)
			self.entryMazzo10 = Entry(self.frameMazzo5, width=75)
			self.entryMazzo2 = Entry(self.frameMazzo5, width=75)
			self.entryMazzo11 = Entry(self.frameMazzo6, width=75)
			self.entryMazzo3 = Entry(self.frameMazzo6, width=75)

			self.btnAVC_sphere = Button(self.frameMazzo2, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm2to3)
			self.btnsphere_SAI = Button(self.frameMazzo3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm3to4)
			self.btnSAI_pachy = Button(self.frameMazzo4, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm4to5)
			self.btnpachy_kmean = Button(self.frameMazzo5, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fm5to6)
			self.btnkmean_result = Button(self.frameMazzo6, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.methode)

			self.btnsphere_AVC = Button(self.frameMazzo3, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmshe_avc)
			self.btnSAI_shere = Button(self.frameMazzo4, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmsai_she)
			self.btnpachy_SAI = Button(self.frameMazzo5, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmpachy_sai)
			self.btnkmean_pachy = Button(self.frameMazzo6, text = "Retour",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.fmkmea_pach)

			self.labMazzo4.pack(pady=50)
			self.entryMazzo4.pack()
			self.entryMazzo4.focus()
			self.labMazzo5.pack(pady=50)
			self.entryMazzo5.pack()
			self.btnAVC_sphere.pack(pady=10)

			self.labMazzo6.pack(pady=50)
			self.entryMazzo6.pack()
			self.entryMazzo6.focus()
			self.labMazzo7.pack(pady=50)
			self.entryMazzo7.pack()
			self.btnsphere_SAI.pack(pady=10)
			self.btnsphere_AVC.pack(pady=10)

			self.labMazzo8.pack(pady=50)
			self.entryMazzo8.pack()
			self.entryMazzo8.focus()
			self.labMazzo9.pack(pady=50)
			self.entryMazzo9.pack()
			self.btnSAI_pachy.pack(pady=10)
			self.btnSAI_shere.pack(pady=10)

			self.labMazzo10.pack(pady=50)
			self.entryMazzo10.pack()
			self.entryMazzo10.focus()
			self.labMazzo2.pack(pady=50)
			self.entryMazzo2.pack()
			self.btnpachy_kmean.pack(pady=10)
			self.btnpachy_SAI.pack(pady=10)

			self.labMazzo11.pack(pady=50)
			self.entryMazzo11.pack()
			self.entryMazzo11.focus()
			self.labMazzo3.pack(pady=50)
			self.entryMazzo3.pack()
			self.btnkmean_result.pack(pady=10)
			self.btnkmean_pachy.pack(pady=10)


# Méthode de Silva changement de scène
	def fs0to1(self):
		self.frame.pack_forget()
		self.frameSilva2.pack(expand=1)
	def fs1to2(self):
		self.frameSilva1.pack_forget()
		self.frameSilva2.pack(expand=1)
	def fs2to3(self):
		self.frameSilva2.pack_forget()
		self.frameSilva3.pack(expand=1)
	def fs3to4(self):
		self.frameSilva3.pack_forget()
		self.frameSilva4.pack(expand=1)
	def fs4to5(self):
		self.frameSilva4.pack_forget()
		self.frameSilva5.pack(expand=1)

# Bouton retour
	def fsshe_avc(self):
		self.frameSilva3.pack_forget()
		self.frameSilva2.pack(expand=1)
	def fssai_she(self):
		self.frameSilva4.pack_forget()
		self.frameSilva3.pack(expand=1)
	def fspachy_sai(self):
		self.frameSilva5.pack_forget()
		self.frameSilva4.pack(expand=1)

# Retour page d'accueil+ calcul maladie
	def fs5tosilva(self):
		self.frameSilva5.pack_forget()
		if(self.entrySilva2.get()==''):
			self.entrySilva2.insert(0,0)
		nouveau_lentille=float(self.entrySilva2.get())
		if(self.entrySilva4.get()==''):
			self.entrySilva4.insert(0,0)
		ancien_kmean=float(self.entrySilva4.get())
		if(self.entrySilva5.get()==''):
			self.entrySilva5.insert(0,0)
		nouveau_kmean=float(self.entrySilva5.get())
		if(self.entrySilva6.get()==''):
			self.entrySilva6.insert(0,0)
		ancien_cylindre=float(self.entrySilva6.get())
		if(self.entrySilva7.get()==''):
			self.entrySilva7.insert(0,0)
		nouveau_cylindre=float(self.entrySilva7.get())
		if(self.entrySilva8.get()==''):
			self.entrySilva8.insert(0,0)
		ancien_sphere=float(self.entrySilva8.get())
		if(self.entrySilva9.get()==''):
			self.entrySilva9.insert(0,0)
		nouveau_sphere=float(self.entrySilva9.get())
		if(self.entrySilva10.get()==''):
			self.entrySilva10.insert(0,0)
		ancien_lentille=float(self.entrySilva10.get())
		self.entrySilva2.delete(0, 'end')
		self.entrySilva4.delete(0, 'end')
		self.entrySilva5.delete(0, 'end')
		self.entrySilva6.delete(0, 'end')
		self.entrySilva7.delete(0, 'end')
		self.entrySilva8.delete(0, 'end')
		self.entrySilva9.delete(0, 'end')
		self.entrySilva10.delete(0, 'end')
		i=0
		niveau=None
		if(nouveau_kmean-ancien_kmean>1):
			i=i+1
		if(nouveau_cylindre-ancien_cylindre>1):
			i=i+1
		if(nouveau_sphere-ancien_sphere>1):
			i=i+1
		if(nouveau_lentille-ancien_lentille>0.1):
			i=i+1
		if(i>=1):
			msg="La maladie est évolutive"
		else:
			msg="La maladie n'est pas concidérée comme évolutive"
		self.frame.pack(expand=1)
		self.popupmsg(msg,niveau)

	def nonEvo1to2(self):
		self.frameNonEvo1.pack_forget()
		self.frameNonEvo2.pack(expand=1)

	def nonEvo2to1(self):
		self.frameNonEvo2.pack_forget()
		self.frameNonEvo1.pack(expand=1)
	def nonEvo2to3(self):
		operation=self.entryNonEvo1.get()
		if(self.entryNonEvo2.get()==''):
			self.entryNonEvo2.insert(0,0)
		AV=float(self.entryNonEvo2.get())
		self.frameNonEvo2.pack_forget()
		self.calcul_operation(operation,AV)
		

	def calcul_operation(self,operation,AV):
		if (operation=="oui"):	
			self.frameNonEvo3.pack(expand=1)
			self.labNonEvo3 = Label(self.frameNonEvo3, text = "Quelle type d'opération a t'il subi (LR, AIC, PTK) : ", font=("Courrier", 15),fg='#2f61ad')
			self.entryNonEvo3 = Entry(self.frameNonEvo3, width=75)
			self.labNonEvo4 = Label(self.frameNonEvo3, text = "Le KC est de quelle type ?  ", font=("Courrier", 15),fg='#2f61ad')
			self.entryNonEvo4 = Entry(self.frameNonEvo3, width=75)
			self.btnNonResult = Button(self.frameNonEvo3, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.nonEvo3toresult)
			self.labNonEvo3.pack(pady=50)
			self.entryNonEvo3.pack()
			self.entryNonEvo3.focus()
			self.labNonEvo4.pack(pady=50)
			self.entryNonEvo4.pack()
			self.btnNonResult.pack(pady=10)
		else :
			niveau=None
			self.frame.pack(expand=1)
			self.entryNonEvo1.delete(0, 'end')
			self.entryNonEvo2.delete(0, 'end')
			
			if (AV >=0.8):
				msg="Surveillance du patient sans opération"
			else :
				msg="Nous vous conseillons de faire l'opération LR"
			self.popupmsg(msg,niveau)
	def nonEvo3toresult(self):
		self.frameNonEvo3.pack_forget()
		type_operation=self.entryNonEvo3.get()
		KC=self.entryNonEvo4.get()
		if(self.entryNonEvo2.get()==''):
			self.entryNonEvo2.insert(0,0)
		AV=float(self.entryNonEvo2.get())
		self.entryNonEvo1.delete(0, 'end')
		self.entryNonEvo2.delete(0, 'end')
		self.entryNonEvo3.delete(0, 'end')
		niveau=None
		if (type_operation =="LR"):
			if (AV >=0.8):
					msg="Surveillance du patient sans opération pendant 3 mois"
			else :
				if (KC == "central"):
					msg="Nous vous conseillons de faire l'opération PTK"
				else :
					msg="Nous vous conseillons de faire l'opération AIC"
		elif (type_operation =="AIC"):
			if (AV >=0.8):
				msg="Surveillance du patient sans opération pendant 3 mois"
			else :
				msg="Nous vous conseillons de faire l'opération Keratoplastie"
		elif (type_operation =="PTK"):
			if (AV >=0.8):
				msg="Surveillance du patient sans opération pendant 3 mois"
			else :
				msg="Nous vous conseillons de faire l'opération Keratoplastie"
		self.frame.pack(expand=1)
		self.popupmsg(msg,niveau)
	def fg0to1(self):
		self.frame.pack_forget()
		self.frameNonEvo1.pack(expand=1)




	def fa0to1(self):
		self.frame.pack_forget()
		self.frameEvo1.pack(expand=1)	
	def Evo1to2(self):
		self.frameEvo1.pack_forget()
		self.frameEvo2.pack(expand=1)
	def Evo2to3(self):
		self.frameEvo2.pack_forget()
		self.frameEvo3.pack(expand=1)
	def Evo3to4(self):
		self.frameEvo3.pack_forget()
		self.frameEvo4.pack(expand=1)
	def Evo4to5(self):
		self.frameEvo4.pack_forget()
		self.frameEvo5.pack(expand=1)

	def Evo5to6(self):
		self.frameEvo5.pack_forget()
		symptome=self.entryEvo5.get()
		operation=self.entryEvo4.get()
		if(self.entryEvo1.get()==''):
			self.entryEvo1.insert(0,0)
		AV=float(self.entryEvo1.get())
		if(self.entryEvo3.get()==''):
			self.entryEvo3.insert(0,0)
		Cornée=float(self.entryEvo3.get())
		Cicatrice=self.entryEvo2.get()
		niveau= None
		if(symptome=="oui"):
			niveau="Si à la suite du diagnostique le patient doit subir CXL, le patient ne pourra pas en bénéficier."
		if (operation=="oui"):
			if(AV>=0.8):
				self.entryEvo1.delete(0, 'end')
				self.entryEvo2.delete(0, 'end')
				self.entryEvo3.delete(0, 'end')
				self.entryEvo4.delete(0, 'end')
				self.entryEvo5.delete(0, 'end')
				msg="Surveillance du patient pendant 3 mois."
				self.frame.pack(expand=1)
				self.popupmsg(msg,niveau)
			else:
				self.frameEvo6.pack(expand=1)
				self.labEvo6 = Label(self.frameEvo6, text = "Quelle type d'opération a t'il subi (CXL ou CXL+LR, CXL+PTK, CXL+AIC) : ", font=("Courrier", 15),fg='#2f61ad')
				self.entryEvo6 = Entry(self.frameEvo6, width=75)
				self.btnEvo6 = Button(self.frameEvo6, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo6to7)
				self.labEvo6.pack(pady=100)
				self.entryEvo6.pack()
				self.entryEvo6.focus()
				self.btnEvo6.pack()
		else:
  			if (AV<=0.1 or Cicatrice == "True" or Cornée <350):
  				self.frameEvo6.pack(expand=1)
  				self.labEvo8 = Label(self.frameEvo6, text = "Le patient a-t-il une cicatrice stromale ou des antécédents hydrops ?", font=("Courrier", 15),fg='#2f61ad')
  				self.entryEvo8 = Entry(self.frameEvo6, width=75)
  				self.btnEvo8 = Button(self.frameEvo6, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo7to9)
  				self.labEvo8.pack(pady=100)
  				self.entryEvo8.pack()
  				self.entryEvo8.focus()
  				self.btnEvo8.pack(pady=10)
  			elif(AV>=0.8):
  				self.entryEvo1.delete(0, 'end')
  				self.entryEvo2.delete(0, 'end')
  				self.entryEvo3.delete(0, 'end')
  				self.entryEvo4.delete(0, 'end')
  				self.entryEvo5.delete(0, 'end')
  				msg="CXL recommandé puis surveillance du patient."
  				self.frame.pack(expand=1)
  				self.popupmsg(msg,niveau)
  			elif(AV>0.1 and AV<0.8):
  				self.entryEvo1.delete(0, 'end')
  				self.entryEvo2.delete(0, 'end')
  				self.entryEvo3.delete(0, 'end')
  				self.entryEvo4.delete(0, 'end')
  				self.entryEvo5.delete(0, 'end')
  				msg="CXL recommandé puis LR, PTK, AIC selon le type de KC du patient."
  				self.frame.pack(expand=1)
  				self.popupmsg(msg,niveau)

	def Evo6to7(self):
		self.frameEvo6.pack_forget()
		self.frameEvo7.pack(expand=1)
		type_operation=self.entryEvo6.get()
		if(type_operation=="CXL"):
			self.labEvo7 = Label(self.frameEvo7, text = "Quelle est le type du KC (central,périphérique, autre) ? :", font=("Courrier", 15),fg='#2f61ad')
			self.entryEvo7 = Entry(self.frameEvo7, width=75)
			self.btnEvo7 = Button(self.frameEvo7, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo7to8)
			self.labEvo7.pack(pady=100)
			self.entryEvo7.pack()
			self.entryEvo7.focus()
			self.btnEvo7.pack(pady=10)
		if(type_operation=="CXL+LR" or type_operation=="CXL+PTK" or type_operation=="CXL+AIC" ):
			self.labEvo8 = Label(self.frameEvo7, text = "Le patient a-t-il une cicatrice stromale ou des antécédents hydrops ?", font=("Courrier", 15),fg='#2f61ad')
			self.entryEvo8 = Entry(self.frameEvo7, width=75)
			self.btnEvo8 = Button(self.frameEvo7, text = "Valider",font=("Courrier", 15), bg='white', fg='#2f61ad', command = self.Evo7to9)
			self.labEvo8.pack(pady=100)
			self.entryEvo8.pack()
			self.entryEvo8.focus()
			self.btnEvo8.pack(pady=10)
			
			
	def Evo7to8(self):
		self.frameEvo7.pack_forget()
		self.frame.pack(expand=1)
		type_KC=self.entryEvo7.get()
		symptome=self.entryEvo5.get()
		self.entryEvo1.delete(0, 'end')
		self.entryEvo2.delete(0, 'end')
		self.entryEvo3.delete(0, 'end')
		self.entryEvo4.delete(0, 'end')
		self.entryEvo5.delete(0, 'end')
		self.entryEvo6.delete(0, 'end')
		self.entryEvo7.delete(0, 'end')
		niveau=None
		if(symptome=="oui"):
			niveau="Si à la suite du diagnostique le patient doit subir CXL, le patient ne pourra pas en bénéficier."
		if(type_KC=="central"):
			msg="Réaliser une PTK puis surveiller AV pendant 3mois"
		if(type_KC=="périphérique"):
			msg="Réaliser une AIC puis surveiller AV pendant 3mois"
		else:
			msg="Réaliser une LR puis surveiller AV pendant 3mois"
		self.popupmsg(msg,niveau)
	def Evo7to9(self):
		self.frameEvo6.pack_forget()
		self.frameEvo7.pack_forget()
		self.frame.pack(expand=1)
		keratoplastie=self.entryEvo8.get()
		operation=self.entryEvo4.get()
		symptome=self.entryEvo5.get()
		self.entryEvo1.delete(0, 'end')
		self.entryEvo2.delete(0, 'end')
		self.entryEvo3.delete(0, 'end')
		self.entryEvo4.delete(0, 'end')
		self.entryEvo5.delete(0, 'end')
		niveau=None
		if(symptome=="oui"):
			niveau="Si à la suite du diagnostique le patient doit subir CXL, le patient ne pourra pas en bénéficier."
		if (operation=="oui"):
			self.entryEvo6.delete(0, 'end')
		self.entryEvo8.delete(0, 'end')	
		if(keratoplastie=="oui"):
			msg="KT fortement recomandée."
		else:
			msg="KLAP fortement recomandée."
		self.popupmsg(msg,niveau)
	def Evo2to1(self):
		self.frameEvo2.pack_forget()
		self.frameEvo1.pack(expand=1)
	def Evo3to2(self):
		self.frameEvo3.pack_forget()
		self.frameEvo2.pack(expand=1)
	def Evo4to3(self):
		self.frameEvo4.pack_forget()
		self.frameEvo3.pack(expand=1)
	def Evo5to4(self):
		self.frameEvo5.pack_forget()
		self.frameEvo4.pack(expand=1)

a=App()

