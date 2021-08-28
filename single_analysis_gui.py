#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import analyze_gui
from main_imports import *


def gc_content():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("750x500")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def cgContent():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = cg_content(dna_seq)
		user_response = messagebox.showinfo(title='GC Content',message=f'Your GC Content is: {feature_output}%')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	gcContentBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="GC Content",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=cgContent)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	gcContentBtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()


def complement():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("750x500")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def complement():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = complement_DNA(dna_seq)
		user_response = messagebox.showinfo(title='Complementary Strad',message=f'Your complementary strand is: {feature_output}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	complementbtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Complementary Strand",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=complement)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	complementbtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()

def count_nuc():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("750x500")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def count():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output_1 = number_of_each_nucleotide(dna_seq)
		feature_output_2 = percentage_of_each_nucleotide(dna_seq)
		user_response = messagebox.showinfo(title='Nucleotides Count & Percentages',message=f'[G,C,T,A] Count: {feature_output_1}\n[G,C,T,A] Percentages: {feature_output_2}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	count = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	count.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()


def main():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("750x750")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	# dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	# dnaInputLabel.place(x=20,y=160)

	#defining functions
	def homepage():
		window.destroy()
		analyze_gui.main()

	def count_nuc_local():
		window.destroy()
		count_nuc()

	def complement_local():
		window.destroy()
		complement()

	def gc_content_local():
		window.destroy()
		gc_content()

	#defining buttons
	count = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count_nuc_local)
	complementbtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Complementary Strand",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=complement_local)
	gcContent = Button(window, relief="solid",borderwidth=4, padx=40, text="G-C Content",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=gc_content_local)
	palindrome = Button(window, relief="solid",borderwidth=4, padx=40, text="Palindrome?",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	ligate = Button(window, relief="solid",borderwidth=4, padx=40, text="Ligate a Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	segmentSearch = Button(window, relief="solid",borderwidth=4, padx=40, text="Search for Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	segmentCount = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	reverseComplement = Button(window, relief="solid",borderwidth=4, padx=40, text="Reverse Complementary",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	reverseTranscriptase = Button(window, relief="solid", borderwidth=4, padx=40, text="Reverse Transcriptase",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)
	#openFileLabel = Button(window, relief="solid", borderwidth=4, padx=30, text="Open File",width=12,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=openFile)

	#defining input fields and file navigation
	# dnaInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=30)
	# dnaInput.place(x=20,y=220)

	#displaying buttons
	count.place(x=360,y=100)
	complementbtn.place(x=360,y=160)
	gcContent.place(x=360,y=220)
	palindrome.place(x=360,y=280)
	ligate.place(x=360,y=340)
	segmentSearch.place(x=360,y=400)
	segmentCount.place(x=360,y=460)
	reverseComplement.place(x=360,y=520)
	reverseTranscriptase.place(x=360,y=580)
	back.place(x=360,y=640)
	#openFileLabel.place(x=20,y=300)

	#running the program
	window.mainloop()
