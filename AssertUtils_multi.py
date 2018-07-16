import xlrd
import time, codecs
import include.excel
#import include.ncc_excel_na
import include.survey
import Field_complete_multi

#This code reads the requirements spreadsheet and compares it against the site to check for perfect match.

#for future, change to a class determine sheet name using "sh.name" or "sh.number".
#Then make the class load the include.excel needed for either SA.com or NCC


def rm_dbl_space(x_text):
##    j = 0
##    while (j < len(x_text))and (j<50):
##        print j
##        print ord(x_text[j])
##        print str(x_text[j])
##        j = j + 1
    x_text = str(x_text)
    x_text = x_text.replace("  ", " ")
    x_text = x_text.replace("   ", " ")
    x_text = x_text.replace("    ", " ")
    x_text = x_text.rstrip(" ")
    x_text = x_text.lstrip(" ")
    return(x_text)

def Assert_Compare_GQuest(self, sel, sheet, row, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')
    field_name = field_name + "_groupquestion"

    column = x.GROUP_QUESTION
    survey_str = s.GROUP_QUESTION

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))
    field_name = prefix+field_name+switch

    x_text = rm_dbl_space(sheet.cell_value(rowx=row, colx=column))

    try: self.assertEqual(x_text, sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)))
    except AssertionError, e: self.verificationErrors.append("GQ:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))


def Assert_Compare_Quest(self, sel, sheet, row, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    column = x.QUESTION
    survey_str = s.QUESTION

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        for i in range(20):
            try:
                if (sel.is_element_present("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))):
                    prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))
                    break
            except:
                pass
            time.sleep(0.2)

    field_name = prefix+field_name+switch

    text = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
    text = convertToAscii(text)

    x_text = convertToAscii(sheet.cell_value(rowx=row, colx=column))
    if ((x_text.find ('<') >=0) and (x_text.find('>')>=0)):
        x_text = removeEscape(x_text)
        x_text = x_text.replace ("<ul><li>", "")
        x_text = x_text.replace ("<li><li>", "")
        x_text = x_text.replace ("<li><ul>", "")
        x_text = x_text.replace ("<br>", "")
        x_text = x_text.replace ("<br><br>", "")

    x_text = rm_dbl_space(x_text)
    try: self.assertEqual(x_text, text)
    except AssertionError, e: self.verificationErrors.append("Q:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Cap(self, sel, sheet, row, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name+switch

    column = x.CAPTION
    survey_str = s.CAPTION

#    print "Cap: //div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)
    web_str = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
    caption = sheet.cell_value(rowx=row, colx=column)
    caption = caption.replace ('<a href="#privacyPolicy" name="modal">', '')
    caption = caption.replace ('</a>', '')
    caption = caption.replace ("\'s", "'s")
    caption = caption.replace ("</li></ul>", "")
    caption = caption.replace ("</li><li>", "")
    caption = caption.replace ("<ul><li>", "")
    caption = caption.replace ("<li><li>", "")
    caption = caption.replace ("<li><ul>", "")
    caption = caption.replace ("<br>", "")
    caption = caption.replace ("<br><br>", "")

    caption = rm_dbl_space(caption)
    try: self.assertEqual(caption, web_str)
    except AssertionError, e: self.verificationErrors.append("C:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))



def Assert_Compare_Hhdr(self, sel, sheet, row, click=""):
    x = include.excel
    s = include.survey

    field_name = "SurveyHelp"

    column = x.HELP_HEADER
    survey_str = s.HELP_HEADER

    text = ""
    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                text = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    x_text = rm_dbl_space(sheet.cell_value(rowx=row, colx=column))
    try: self.assertEqual(x_text, text)
    except AssertionError, e: self.verificationErrors.append("HH:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))



def Assert_Compare_Help(self, sel, sheet, row, click = ""):
    x = include.excel
    s = include.survey

    if ((sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='ACT_COMPOSITE_SCORE')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_2')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='PSAT_COMPOSITE_SCORE_2')):
        return


    field_name = "SurveyHelp"

    column = x.HELP_TXT
    survey_str = s.HELP_TXT
    x_text = convertToAscii(sheet.cell_value(rowx=row, colx=column))
    if ((x_text.find ('<') >=0) and (x_text.find('>')>=0)):
        x_text = removeEscape(x_text)
        x_text = x_text.replace ("<ul><li>", "")
        x_text = x_text.replace ("<li><li>", "")
        x_text = x_text.replace ("<li><ul>", "")
        x_text = x_text.replace ("<br>", "")
        x_text = x_text.replace ("<br><br>", "")
        x_text = x_text.replace ("<\t>", "")

    web_str = ""

    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                web_str = (sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)))
                if (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1'):
                    sel.click("//div[@id='ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_SAT_COMPOSITE_SCORE_1']/div[2]/div[1]")
                    web_str = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    web_str = convertToAscii(web_str)
    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)

    try: self.assertEqual(x_text, web_str)
    except AssertionError, e: self.verificationErrors.append("HT: %s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_GQuest_String(self, sel, sheet, row, x_text, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')
    field_name = field_name + "_groupquestion"

    column = x.GROUP_QUESTION
    survey_str = s.GROUP_QUESTION


    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name+switch

    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)
    try: self.assertEqual(x_text, sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)))
    except AssertionError, e: self.verificationErrors.append("GQ:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Quest_String(self, sel, sheet, row, x_text, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    column = x.QUESTION
    survey_str = s.QUESTION

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name+switch

    text = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
    text = convertToAscii(text)

    if ((x_text.find ('<') >=0) and (x_text.find('>')>=0)):
        x_text = removeEscape(x_text)
        x_text = x_text.replace ("<ul><li>", "")
        x_text = x_text.replace ("<li><li>", "")
        x_text = x_text.replace ("<li><ul>", "")
        x_text = x_text.replace ("<br>", "")
        x_text = x_text.replace ("<br><br>", "")

    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)
    try: self.assertEqual(x_text, text)
    except AssertionError, e: self.verificationErrors.append("Q:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_HelpHeader_String(self, sel, sheet, row, x_text, click = ""):
    x = include.excel
    s = include.survey

    if ((sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='ACT_COMPOSITE_SCORE')):
        return


    field_name = "SurveyHelp"

    column = x.HELP_HEADER
    survey_str = s.HELP_HEADER


##    if (x_text.find ("<")>=0 and x_text.find(">")>=0):
##        x_text = removeEscape(x_text)
##        x_text = x_text.replace ("<ul><li>", "")
##        x_text = x_text.replace ("<li><li>", "")
##        x_text = x_text.replace ("<li><ul>", "")
##        x_text = x_text.replace ("<br>", "")
##        x_text = x_text.replace ("<br><br>", "")

    web_str = ""

    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                web_str = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    web_str = convertToAscii(web_str)
    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)
    try: self.assertEqual(x_text, web_str)
    except AssertionError, e: self.verificationErrors.append("HH:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Help_String(self, sel, sheet, row, x_text, click = ""):

    x = include.excel
    s = include.survey

    if ((sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='ACT_COMPOSITE_SCORE')):
        return

    field_name = "SurveyHelp"


    column = x.HELP_TXT
    survey_str = s.HELP_TXT
    if (x_text.find ("<")>=0 and x_text.find(">")>=0):
        x_text = removeEscape(x_text)
        x_text = x_text.replace ("<ul><li>", "")
        x_text = x_text.replace ("<li><li>", "")
        x_text = x_text.replace ("</li><li>", "")
        x_text = x_text.replace ("</li></ul>", "")
        x_text = x_text.replace ("<li><ul>", "")
        x_text = x_text.replace ("<br>", "")
        x_text = x_text.replace ("<br><br>", "")
        x_text = x_text.replace ("<\t>", "")

    web_str = ""

    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                web_str = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    web_str = convertToAscii(web_str)
    web_str = str(web_str)
    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)
    try: self.assertEqual(x_text, web_str)
    except AssertionError, e: self.verificationErrors.append("HT  341:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))


def Assert_Compare_Cap_String(self, sel, sheet, row, x_text, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name+switch

    column = x.CAPTION
    survey_str = s.CAPTION

    web_str = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
    caption = x_text
    caption = caption.replace ('<a href="#privacyPolicy" name="modal">', '')
    caption = caption.replace ('</a>', '')
    caption = caption.replace ("\'s", "'s")
    caption = rm_dbl_space(caption)
    caption = convertToAscii(caption)
    try: self.assertEqual(caption, web_str)
    except AssertionError, e: self.verificationErrors.append("C:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))


def Assert_Compare_Quest_Name(self, sel, sheet, row, group, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    if (field_name.find("prefix") != -1):
        survey_str = s.PREFIX
    if (field_name.find("first") != -1):
        survey_str = s.FIRST
    if (field_name.find("middle") != -1):
        survey_str = s.MIDDLE
    if (field_name.find("last") != -1):
        survey_str = s.LAST
    if (field_name.find("suffix") != -1):
        survey_str = s.SUFFIX
    group = prefix+group+switch

    column = x.QUESTION

    try: self.assertEqual((sheet.cell_value(rowx=row, colx=column)), sel.get_text("//span[@id=\'%s_%s_%s_%s_groupquestion_ext\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,group,survey_str)))
    except AssertionError, e: self.verificationErrors.append("Q:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Quest_Name_String(self, sel, sheet, row, group, text, switch = ""):

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    if (field_name.find("prefix") != -1):
        survey_str = s.PREFIX
    if (field_name.find("first") != -1):
        survey_str = s.FIRST
    if (field_name.find("middle") != -1):
        survey_str = s.MIDDLE
    if (field_name.find("last") != -1):
        survey_str = s.LAST
    if (field_name.find("suffix") != -1):
        survey_str = s.SUFFIX
    group = prefix+group+switch

    column = x.QUESTION


    try: self.assertEqual(text, sel.get_text("//span[@id=\'%s_%s_%s_%s_groupquestion_ext\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,group,survey_str)))
    except AssertionError, e: self.verificationErrors.append("Q:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))



def Assert_Quest_Ready(self, sel, sheet, row,switch):

    for i in range(6):
        try:
            if "Checking for errors..." == sel.get_text("modalTitle"): return(False)
        except: pass
        time.sleep(1)

    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name

    column = x.QUESTION
    survey_str = s.QUESTION
    if (switch != ''):
        test_quest = "//div[@id=\'%s_%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,switch,s.QUESTION)
    else:
        test_quest = "//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)

    for p in range(6):
        try:
            if ("" != sel.get_text(test_quest)):
                return (True)#Ready to move on...
        except: pass
        time.sleep(1)

    else: return(False)

        #self.fail("time out") #Next page not showing up



def convertToAscii(nameString):
#    translations = {8217:"'", 10:"", 8211:"-", 8220:'"', 8221:'"'}
    translations = {8217:"'", 39:"'", 10:"", 8211:"-", 8220:'"',
                    8221:'"',47:"", 8212:"-", 8226:" ", 8364:" ",
                    8729:" ", 226:" ", 710:" ", 8482:" ", 183:" ",
                    194:" ", 162:" ", 247:"//", 195:"//" }
    revisedNameString = ''
    original = ''
    ordlist=[]

    for character in nameString:
        ordCharacter=ord(character)
        ordlist.append(ordCharacter)


        if ordCharacter in translations:
##            print "translations", translations[ordCharacter]
##            print ordCharacter
            revisedNameString = revisedNameString + translations[ordCharacter]
        else:
            revisedNameString = revisedNameString + character
##            print ordCharacter
##            print character

    newlist=[]
    j=0
    for i in revisedNameString:
        newlist.append(revisedNameString[j])
        newlist.append(ordlist[j])
        j = j +1
##    print "newlist"
##    print newlist

    return revisedNameString

def removeEscape(nameString):
    translations = {47:""}
    revisedNameString = ''

    for character in nameString:
        ordCharacter=ord(character)

        if ordCharacter in translations:
            revisedNameString = revisedNameString + translations[ordCharacter]
        else:
            revisedNameString = revisedNameString + character


    return revisedNameString


def Is_Hidden_Quest(self, sel, sheet, row):
    x = include.excel
    s = include.survey

    field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
    field_name = field_name.replace(' ','')

    column = x.QUESTION
    survey_str = s.QUESTION

    if (s.TYPE == "FAFSA"):
        prefix = ""
    else:
        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

    field_name = prefix+field_name

    test = sel.is_visible("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,s.QUESTION))


def Assert_Compare_Output(self, sel, data_table):

    output_table = Field_complete_multi.Field_complete_output_table(data_table)

    if sel.is_text_present("Concordia University offers additional gift"):
        sel.click("//a[@id='%s_%s_btnNext']/img"%(include.ncc_survey.ROOT_CONTROL,include.ncc_survey.MASTER_PAGE))

    for i in range(60):
        try:
            if (sel.is_text_present("Please confirm your mailing information below:") or
                sel.is_text_present("Please verify and confirm your registration information below:")):
                sel.click("id=ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_address_carryover_yn_chk")
                sel.click("css=#ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext > img")
                sel.wait_for_page_to_load("30000")
            if (sel.is_text_present("Congratulations on completing the Berea College Quick Estimator")):
                return (Compare_BereaEstimator_Text(self,sel,data_table))
            if (sel.is_text_present("Thank you for completing the Berea College FRQ.")):
                return (Compare_BereaFRQ_Text(self,sel,data_table))
            if (sel.is_text_present("Based on the information provided the student is not eligible for a Merit Scholarship. Please consider using the Pace Net Price Calculator. It has a more detailed questionnaire and provides estimates of potential eligibility for need- and merit-based aid from Pace, as well as New York and federal sources.")):
                break
            if ((sel.is_text_present("Your Net Price Calculator Results"))
              or (sel.is_element_present(output_table[0]))
              or (sel.is_text_present("Your Estimated Results"))
              or (sel.is_text_present("Estimates for the 2011-2012 Academic Year"))
              or (sel.is_text_present("Estimates for the 2012-2013 Academic Year"))
              or (sel.is_text_present("Your estimated cost of attendance"))
              or (sel.is_text_present("Congratulations! You qualify for the ISU Honors Program."))
              or (sel.is_text_present("Register to get your FREE DePaul Estimated Award Packet."))
              or (sel.is_text_present("Register to get your FREE Ave Maria Estimated Award Packet."))
              or (sel.is_text_present("Pace University Merit Scholarship Estimator"))):
              #or (sel.is_text_present("Thank you for completing the Net Price Calculator for John Carroll University."))):

                if ((sel.is_text_present("Register to get your FREE DePaul Estimated Award Packet.")
                   or(sel.is_text_present("Register to get your FREE Ave Maria Estimated Award Packet.")
                   or(sel.is_text_present("Congratulations! You qualify for the ISU Honors Program."))))):
                    sel.click("ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_address_carryover_yn_chk")
                    sel.click("css=#ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext > img")
                    sel.wait_for_page_to_load("30000")

                break

        except: pass
        time.sleep(1)
    else:
        self.verificationErrors.append ("\nTimeout at Check Errors\n")
        return (0)

    for i in output_table:
        print i

        table_val = Field_complete_multi.Field_complete_excel(data_table,i)
        if (table_val == "not found"):
            continue
        else:
            data_name = str(i)

            table_val = table_val.replace("$", "")
            table_val = table_val.replace(",", "")
            table_val = table_val.replace("+", "")
            table_val = table_val.replace(" ", "")

            k = 0
            t_data = ""
            while (k < len(table_val)):
                if (ord(table_val[k]) == int(8211)):
                    t_data = t_data + '-'
                else:
                    t_data = t_data + table_val[k]
                k +=1

            if sel.is_element_present(data_name):
                site_data =  sel.get_text(data_name)
                site_data = site_data.replace("$", "")
                site_data = site_data.replace(",", "")
                site_data = site_data.replace("+", "")
                site_data = site_data.replace(" ", "")

                #because it doesn't look like negative 0 is going away
                if site_data == "-0":
                    site_data = site_data.replace("-","")

            else: site_data = ""

            k = 0
            x_data = ""
            while (k < len(site_data)):
                if (ord(site_data[k]) == int(8211)):
                    x_data = x_data + '-'
                else:
                    x_data = x_data + site_data[k]
                k +=1

            try: self.assertEqual(t_data, x_data)
            except AssertionError, e: self.verificationErrors.append("NCP Output:%s:\n"%data_name + str(e))

    #get the Report ID
    if (sel.is_element_present("//div[@id='tab1']/font[2]/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/font[2]/table/tbody/tr/td"))
    elif (sel.is_element_present("//div[@id='tab1']/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/table/tbody/tr/td"))
    else:
        return(0)

def Compare_BereaEstimator_Text(self, sel, data_table):
    if (Field_complete_multi.Field_complete_excel(data_table, "parent_total_income_shortform") == '46125'):
        if(sel.is_text_present("If you were to apply today, it is likely that you will meet the financial requirements for admission to Berea College. We recommend you submit an application.")==False) :
            self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if (Field_complete_multi.Field_complete_excel(data_table, "parent_total_income_shortform") == '92104'):
        if(sel.is_text_present("If you were to apply today, it is unlikely that you will meet the financial requirements for admission to Berea College, based on the information you have submitted. If your financial situation changes significantly prior to submitting an application, we encourage you to complete an updated financial eligibility estimate.")==False):
            self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if (Field_complete_multi.Field_complete_excel(data_table, "parent_total_income_shortform") == '20000'):
        if(sel.is_text_present("This is great news! If you were to apply today, it is highly likely that you will meet the financial requirements for admission to Berea College. If you are a high school senior or above, we recommend you submit an application and submit your financial information. By completing the application process and being selected for admission, you will receive Berea's four year tuition scholarship.")==False):
            self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if (sel.is_element_present("//div[@id='tab1']/font[2]/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/font[2]/table/tbody/tr/td"))
    elif (sel.is_element_present("//div[@id='tab1']/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/table/tbody/tr/td"))
    else:
        return(0)

def Compare_BereaFRQ_Text(self, sel, data_table):
    if(sel.is_text_present("Your results have been securely transmitted to the Office of Admissions and will be included in your application file.")==False):
        print ("Your results have been securely transmitted to the Office of Admissions and will be included in your application file. - mismatch")
        self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if(sel.is_text_present("We strongly recommend you click on the data summary tab and review your results for accuracy before exiting this tool. If you find an error, click on the return to survey button, correct the information, and resubmit. If you do not find errors or after corrections have been made, we recommend you print your results and keep a copy in your personal records.")==False):
        print ("1st Paragraph mismatch")
        self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if(sel.is_text_present("The most recent FRQ report will be used in assessing your financial eligibility to attend Berea. Please note that once you exit this questionnaire, you will not be able to correct your submission and will need to resubmit your FRQ in its entirety.")==False):
        print ("2nd Paragraph mismatch")
        self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if(sel.is_text_present("If you have questions regarding your status or any terminology contained in the FRQ, please contact us at 1-800-326-5948")==False):
        print ("3rd Paragraph mismatch")
        self.verificationErrors.append ("\nOutput Text Mismatch\n")
    if (sel.is_element_present("//div[@id='tab1']/font[2]/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/font[2]/table/tbody/tr/td"))
    elif (sel.is_element_present("//div[@id='tab1']/table/tbody/tr/td")):
        return(sel.get_text("//div[@id='tab1']/table/tbody/tr/td"))
    else:
        return(0)

def Assert_Compare_GQuest_Index(self, sel, sheet, row, x_text, index, switch = ""):

    if (sheet.cell_value(rowx=row, colx=self.x.GROUP_QUESTION)!= ""):
        x = include.excel
        s = include.survey

        field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
        field_name = field_name.replace(' ','')
        field_name = field_name + "_groupquestion"

        column = x.GROUP_QUESTION
        survey_str = s.GROUP_QUESTION

        if (s.TYPE == "FAFSA"):
            prefix = ""
        else:
            prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

        field_name = prefix+field_name+switch

        x_text = rm_dbl_space(sheet.cell_value(rowx=row, colx=column))

        if (x_text.find('|')!= -1):
            x_text = x_text.split('|')
            x_text = x_text[index]

        x_text = rm_dbl_space(x_text)
        x_text = convertToAscii(x_text)
        try: self.assertEqual(x_text, sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str)))
        except AssertionError, e: self.verificationErrors.append("GQ:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Quest_Index(self, sel, sheet, row, index, switch = ""):

    if (sheet.cell_value(rowx=row, colx=self.x.QUESTION)!= ""):

        x = include.excel
        s = include.survey

        field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
        field_name = field_name.replace(' ','')
        prefix =''
        column = x.QUESTION
        survey_str = s.QUESTION
        time.sleep(0.5)

        print
        print s.TYPE
        print
        if (s.TYPE == "FAFSA"):
            prefix = ""
        else:
            for i in range(20):
                try:
                    if (sel.is_element_present("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))):
                        prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))
                        break
                except:
                    pass
                time.sleep(0.2)

        field_name = prefix+field_name+switch

        text = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
        text = convertToAscii(text)
        text = text.replace ("\n", "")

        x_text = rm_dbl_space(sheet.cell_value(rowx=row, colx=column))

        if (x_text.find('|')!= -1):
            x_text = x_text.split('|')
            x_text = x_text[index]

        x_text = rm_dbl_space(x_text)
        x_text = convertToAscii(x_text)
        try: self.assertEqual(x_text, text)
        except AssertionError, e: self.verificationErrors.append("Q:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_HelpHeader_Index(self, sel, sheet, row, index, click = ""):

    x = include.excel
    s = include.survey

    if (sheet.cell_value(rowx=row, colx=x.HELP_HEADER)== ''):
        return

    if ((sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='ACT_COMPOSITE_SCORE')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_2')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='PSAT_COMPOSITE_SCORE_2')):
        return

    field_name = "SurveyHelp"

    column = x.HELP_HEADER
    survey_str = s.HELP_HEADER


    web_str = ""

    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                web_str = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    web_str = convertToAscii(web_str)
    x_text = (sheet.cell_value(rowx=row, colx=column))

    if (x_text.find('|')!= -1):
        x_text = x_text.split('|')
        x_text = x_text[index]

    x_text = rm_dbl_space(x_text)
    x_text = convertToAscii(x_text)
    try: self.assertEqual(x_text, web_str)
    except AssertionError, e: self.verificationErrors.append("HH:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))

def Assert_Compare_Help_Index(self, sel, sheet, row, index, click = ""):
    x = include.excel
    s = include.survey

    if (sheet.cell_value(rowx=row, colx=x.HELP_TXT)== ''):
        return

    if ((sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_1')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='ACT_COMPOSITE_SCORE')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='SAT_COMPOSITE_SCORE_2')
        or (sheet.cell_value(rowx=row, colx=self.x.FIELD_NAME)=='PSAT_COMPOSITE_SCORE_2')):
        return

    field_name = "SurveyHelp"

    column = x.HELP_TXT
    survey_str = s.HELP_TXT

    web_str = ""

    for i in range(20):
        try:
            #sel.fire_event(click, "blur")
            #sel.click(click)
            if (sel.is_element_present("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))):
                web_str = sel.get_text("//td[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
                break
        except:
            pass
        time.sleep(0.2)

    web_str = convertToAscii(web_str)

## code to debug non-ASCII characters in help text
##    j = 0
##    print "start now \n"
##    while (j < len(web_str)):
##        print j
##        print ord(web_str[j])
##        print str(web_str[j])
##        j = j + 1


    web_str = str(web_str)
    web_str = web_str.replace("  ","")
    web_str = web_str.replace(". ",".")
    x_text = sheet.cell_value(rowx=row, colx=column)


    if (x_text.find('|')!= -1):
        x_text = x_text.split('|')
        x_text = x_text[index]

    x_text = convertToAscii(x_text)
    x_text = x_text.replace ("<\t>", "")
    x_text = x_text.replace ("    ", "")
    x_text = x_text.replace ("\t", "")


## code to debug non-ASCII characters in help text
##    j = 0
##    print "start now \n"
##    while (j < len(x_text)):
##        print j
##        print ord(x_text[j])
##        print str(x_text[j])
##        j = j + 1

    x_text = rm_dbl_space(x_text)
    x_text = x_text.replace("  ","")
    x_text = x_text.replace(". ",".")

    try: self.assertEqual(x_text, web_str)
    except AssertionError, e: self.verificationErrors.append("HT:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))


def Assert_Compare_Cap_Index(self, sel, sheet, row, index, switch = ""):

    if (sheet.cell_value(rowx=row, colx=self.x.CAPTION)!= ""):
        x = include.excel
        s = include.survey

        field_name = sheet.cell_value(rowx = row, colx = x.FIELD_NAME)
        field_name = field_name.replace(' ','')

        if (s.TYPE == "FAFSA"):
            prefix = ""
        else:
            prefix = sel.get_value("%s_%s_%s_prefix"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL))

        field_name = prefix+field_name+switch

        column = x.CAPTION
        survey_str = s.CAPTION

        web_str = sel.get_text("//div[@id=\'%s_%s_%s_%s\']%s"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL,field_name,survey_str))
        web_str = web_str.replace ("\'s", "'s")
        web_str = web_str.replace ("\n", "")
        web_str = web_str.replace ("&nbsp", "")
        web_str = web_str.replace ("  ", " ")
        web_str = web_str.replace ("  ", " ")
        web_str = web_str.replace ("  ", " ")
        web_str = convertToAscii(web_str)
        x_text = rm_dbl_space(sheet.cell_value(rowx=row, colx=column))

        if (x_text.find('|')!= -1):
            x_text = x_text.split('|')
            x_text = x_text[index]

        x_text = x_text.replace ("\'s", "'s")
        x_text = x_text.replace ("\n", "")
        x_text = x_text.replace ("&nbsp", "")
        x_text = x_text.replace ("  ", " ")
        x_text = x_text.replace ("  ", " ")
        x_text = rm_dbl_space(x_text)
        x_text = convertToAscii(x_text)

        try: self.assertEqual(x_text, web_str)
        except AssertionError, e: self.verificationErrors.append("C:%s:\n"%sheet.cell_value(rowx=row, colx=x.FIELD_NAME)+str(e))
