import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

bioTu = []
bioBo = []

chemTu = []
chemBo = []

physTu = []
physBo = []

matTu = []
matBo = []

earsTu = []
earsBo = []

gensciTu = []
gensciBo = []

astrTu = []
astrBo = []



for s in range(12):
	for r in range(15):
		fd = open('Set '+str(s+1)+'/round'+str(r+1)+'.pdf', "rb")
		doc = PDFDocument(fd)
		viewer = SimplePDFViewer(fd)

		all_pages = [p for p in doc.pages()]

		for x in range(len(all_pages)):
			viewer.navigate(x+1)
			viewer.render()

			i = 0;

			pageTxt = "".join(viewer.canvas.strings)
			##print(pageTxt)

			
			bioloc = pageTxt.find("BIOLOGY")
			while bioloc>0:
				i+=1
				if i%2 != 0:
					bioTu.append([pageTxt[bioloc-14 : pageTxt.find("ANSWER", bioloc+8)-1], pageTxt[pageTxt.find("ANSWER", bioloc+8) : pageTxt.find("BONUS", bioloc+8)-1]])
				else:
					bioBo.append([pageTxt[bioloc-12 : pageTxt.find("ANSWER", bioloc+8)-1], pageTxt[pageTxt.find("ANSWER", bioloc+8) : pageTxt.find("TOSS-UP", bioloc+8)-1]])
		

				bioloc = pageTxt.find("BIOLOGY", bioloc+8)

			chemloc = pageTxt.find("CHEMISTRY")
			while chemloc>0:
				i+=1
				if i%2 != 0:
					chemTu.append([pageTxt[chemloc-14 : pageTxt.find("ANSWER", chemloc+8)-1], pageTxt[pageTxt.find("ANSWER", chemloc+8) : pageTxt.find("BONUS", chemloc+8)-1]])
				else:
					chemBo.append([pageTxt[chemloc-12 : pageTxt.find("ANSWER", chemloc+8)-1], pageTxt[pageTxt.find("ANSWER", chemloc+8) : pageTxt.find("TOSS-UP", chemloc+8)-1]])
		
				chemloc = pageTxt.find("CHEMISTRY", chemloc+8)

				physloc = pageTxt.find("PHYSICS")
			while physloc>0:
				i+=1
				if i%2 != 0:
					physTu.append([pageTxt[physloc-14 : pageTxt.find("ANSWER", physloc+8)-1], pageTxt[pageTxt.find("ANSWER", physloc+8) : pageTxt.find("BONUS", physloc+8)-1]])
				else:
					physBo.append([pageTxt[physloc-12 : pageTxt.find("ANSWER", physloc+8)-1], pageTxt[pageTxt.find("ANSWER", physloc+8) : pageTxt.find("TOSS-UP", physloc+8)-1]])

				physloc = pageTxt.find("PHYSICS", physloc+8)

			matloc = pageTxt.find("MATH")
			while matloc>0:
				i+=1
				if i%2 != 0:
					matTu.append([pageTxt[matloc-14 : pageTxt.find("ANSWER", matloc+8)-1], pageTxt[pageTxt.find("ANSWER", matloc+8) : pageTxt.find("BONUS", matloc+8)-1]])
				else:
					matBo.append([pageTxt[matloc-12 : pageTxt.find("ANSWER", matloc+8)-1], pageTxt[pageTxt.find("ANSWER", matloc+8) : pageTxt.find("TOSS-UP", matloc+8)-1]])	

				matloc = pageTxt.find("MATH", matloc+8)

			earsloc = pageTxt.find("EARTH SCIENCE")
			while earsloc>0:
				i+=1
				if i%2 != 0:
					earsTu.append([pageTxt[earsloc-14 : pageTxt.find("ANSWER", earsloc+8)-1], pageTxt[pageTxt.find("ANSWER", earsloc+8) : pageTxt.find("BONUS", earsloc+8)-1]])
				else:
					earsBo.append([pageTxt[earsloc-12 : pageTxt.find("ANSWER", earsloc+8)-1], pageTxt[pageTxt.find("ANSWER", earsloc+8) : pageTxt.find("TOSS-UP", earsloc+8)-1]])
				

				earsloc = pageTxt.find("EARTH SCIENCE", earsloc+8)
		
			gensciloc = pageTxt.find("GENERAL SCIENCE")
			while gensciloc>0:
				i+=1
				if i%2 != 0:
					gensciTu.append([pageTxt[gensciloc-14 : pageTxt.find("ANSWER", gensciloc+8)-1], pageTxt[pageTxt.find("ANSWER", gensciloc+8) : pageTxt.find("BONUS", gensciloc+8)-1]])
				else:
					gensciBo.append([pageTxt[gensciloc-12 : pageTxt.find("ANSWER", gensciloc+8)-1], pageTxt[pageTxt.find("ANSWER", gensciloc+8) : pageTxt.find("TOSS-UP", gensciloc+8)-1]])
				

				gensciloc = pageTxt.find("GENERAL SCIENCE", gensciloc+8)
		
			astrloc = pageTxt.find("ASTRONOMY")
			while astrloc>0:
				i+=1
				if i%2 != 0:
					astrTu.append([pageTxt[astrloc-14 : pageTxt.find("ANSWER", astrloc+8)-1], pageTxt[pageTxt.find("ANSWER", astrloc+8) : pageTxt.find("BONUS", astrloc+8)-1]])
				else:
					astrBo.append([pageTxt[astrloc-12 : pageTxt.find("ANSWER", astrloc+8)-1], pageTxt[pageTxt.find("ANSWER", astrloc+8) : pageTxt.find("TOSS-UP", astrloc+8)-1]])
				

				astrloc = pageTxt.find("ASTRONOMY", astrloc+8)
			
		## 1)BIOLOGY(bio), 2)CHEMISTRY(chem), 3)PHYSICS(phys), 4)MATH(mat), 5)EARTH SCIENCE(ears), 6)GENERAL SCIENCE(gensci), 7)ASTRONOMY(astr)
txtfile = open("questionTxt.txt", "a")
txtfile.writelines(str(bioTu)+str(bioBo)+str(chemTu)+str(chemBo)+str(physTu)+str(physBo)+str(matTu)+str(matBo)+str(earsTu)+str(earsBo)+str(gensciTu)+str(gensciBo)+str(astrTu)+str(astrBo))