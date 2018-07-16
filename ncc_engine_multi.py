# -*- coding: cp1252 -*-
import unittest
import utils.AssertUtils_multi
import include.survey
import include.field_id
import time
from selenium import selenium
from utils.Field_complete_multi import Field_complete_excel


class ncc_engine(unittest.TestCase):

    def __init__(self, vErr, sel, sheet, data_table, Field_list, school):
        self.verificationErrors = vErr
        self.school= school
        self.Field_list = Field_list
        self.au_qr = utils.AssertUtils_multi.Assert_Quest_Ready
        self.au_q_ind = utils.AssertUtils_multi.Assert_Compare_Quest_Index
        self.au_hh_ind = utils.AssertUtils_multi.Assert_Compare_HelpHeader_Index
        self.au_ht_ind = utils.AssertUtils_multi.Assert_Compare_Help_Index
        self.au_c_ind = utils.AssertUtils_multi.Assert_Compare_Cap_Index

        self.au_output = utils.AssertUtils_multi.Assert_Compare_Output
        s = include.survey
        self.sv = "%s_%s_%s_"%(s.ROOT_CONTROL,s.MASTER_PAGE,s.SURVEY_CONTROL)

        self.x = include.excel

    def Process(self, sel, e, d, sheet, data_table):
        i = 0
        quest_on_page = 0
        transID_reported = 0
        transID = 0

        section = self.Field_list[i][2]
        s = include.survey
        while section == "Intro":
            i += 1
            section = self.Field_list[i][2]



        #cycle through Field_list which has the questions listed in the order they should appear
        while i < (len(self.Field_list)):

            switch = ""
            index = 0

            print "\nstart %d"%i
            print " field: %s"%sheet.cell_value(rowx=self.Field_list[i][0],colx=1)

            #print " self.Field_list[i][0]: %s"%self.Field_list[i][0]
            #print " self.Field_list[i][3]: %s"%self.Field_list[i][3]
            #Is the question dynamic or fieldID is dynamic?  If the question should not be there, then skip it.
            #If the fieldId is dynamic, ask in the exception code.
            #If the question dynamic status is a complicated test then it will use the ncc_exception class
            (switch, index) = e.ex_test(sel, self.Field_list[i][0], self.Field_list[i][3], sheet, data_table)

            if switch == "Done":
                #This question is done, move to the next one.
                print "Question handled by exception class: %s."%sheet.cell_value(rowx=self.Field_list[i][0],colx=1)
                i +=1

            elif (switch == "") and (self.Field_list[i][1] != "") and (d.ex_test(sel, self.Field_list[i][3])==False):

                print "skipping field: %s. Question should not be there."%sheet.cell_value(rowx=self.Field_list[i][0],colx=1)
                i+=1
            else:
                if (sel.is_text_present("The student may be eligible to receive additional funding not reflected here if you meet all criteria for the TEACH grant.")):
                    sel.click("//img[@alt='Click to continue']")
                if sel.is_text_present("Note about Yeshiva Academic Scholarships"):
                        sel.click("css=#ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext > img")
                        time.sleep(1)
                if sel.is_text_present("Get Your FREE North South University Personal Student Prospectus!"):
                        sel.click("css=#ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext > img")
                        time.sleep(1)
                if (switch == "Not Done"): switch = ""

                #Compare the text in the requirements spread sheet with the actual text on the site
                #Question:
                self.au_q_ind(self, sel, sheet, (self.Field_list[i][0]), index, switch)
##
##              self.au_gq_ind(self, sel, sheet, self.Field_list[i][0], index, switch)

                self.au_c_ind(self, sel, sheet, self.Field_list[i][0], index, switch)


                #Answer the question with data from the data_table
                #Answer:
                field_type = sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)
                field_name_data = sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_NAME)
                field_name_data = field_name_data.replace(" ", "")


                prefix = sel.get_value("%sprefix"%self.sv)
                field_name = prefix+field_name_data+switch
                print "field_name: %s"%field_name

                #Text
                if (field_type == "Text") or (field_type.find("Digits")!= -1)and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):
                    sel.click("%s%s_txt"%(self.sv,field_name))
                    sel.type("%s%s_txt"%(self.sv,field_name), "%s"%Field_complete_excel(data_table,"%s"%field_name_data))
                    ## sel.click present below just to get code to move off the field get verification to fire.

                    click = "%s%s_txt"%(self.sv,field_name)


                #Pull Down
                elif ((sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE))== "Pull-Down")and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):

                    string_test = Field_complete_excel(data_table,"%s"%field_name_data)

                    print "string test: %s"%string_test

                    if (((field_name =="GPA")or (field_name == "HS_GPA_by_thirds")or(field_name == "HS_GPA_by_tenths_withoutDK")or(field_name == "college_GPA_by_quarters") or
                         (field_name == "college_gpa_by_quarters"))and ((string_test.find("Don")!= -1)or (string_test.find("4") != -1))):
                        if string_test.find("Don")!= -1:
                            sel.select("%s%s_lst"%(self.sv,field_name), u"label=Don�t Know")
                        elif string_test == ("4"):
                            sel.select("%s%s_lst"%(self.sv,field_name), "label=4.0")
                        else:
                            sel.select("%s%s_lst"%(self.sv,field_name), "label=%s"%Field_complete_excel(data_table,"%s"%field_name_data))
                    elif ((field_name == "SAT_ACT_SCORES")and (string_test.find("Don")!= -1)):
                        sel.select("%s%s_lst"%(self.sv,field_name), "label=Don't Know")
                    elif ((field_name == "transfer_credits_33")and (string_test.find("31")!= -1)):
                        sel.select("ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_transfer_credits_33_lst", u"label=31 � 56")
                    elif (string_test.find("Don")!= -1)and (field_name =="enrollment_status"):
                        sel.select("%s%s_lst"%(self.sv,field_name), "label=Don't know")
                    elif (string_test.find("Neither/Don't Know GPA")!= -1):
                        sel.select("%s%s_lst"%(self.sv,field_name), "label=Neither/Don't Know GPA")
                    elif ((string_test.find("Don")!= -1) and ((field_name =="college_gpa_by_quarters") or
                          (field_name =="GPA"))):
                        sel.select("%s%s_lst"%(self.sv,field_name), u"label=Don�t Know")
                    elif ((string_test.find("Know")!= -1) and (field_name !="gpa_option")):
                        if (field_name.find("minisurveyreference6#GPA")!= -1):
                            sel.select("id=ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_minisurveyreference6#GPA_lst", u"label=Don�t Know")
                        elif (field_name.find("Merit#GPA")!= -1):
                            sel.select("id=ctl00_ctl00_WrapperPlaceHolder_MainBody_SurveyControl1_Merit#GPA_lst", u"label=Don�t Know")
                        else:
                            sel.select("%s%s_lst"%(self.sv,field_name), "label=Don't Know")
                    # elif (string_test.find("Spring (Jan")!= -1):
                        # sel.select("id=%s%s_lst"%(self.sv,field_name), u"label=Winter/Spring (Jan � June)")
                    elif (string_test.find("Greystone")!= -1):
                        sel.select("id=%s%s_lst"%(self.sv,field_name), u"label=Greystone � Saint Helena, CA")
                    elif (string_test.find("Cruces")!= -1):
                        sel.select("id=%s%s_lst"%(self.sv,field_name), u"Las Cruces � Main Campus")

                    else:
                        print 'field_name_data is %s'%field_name_data
                        sel.select("%s%s_lst"%(self.sv,field_name), "label=%s"%Field_complete_excel(data_table,"%s"%field_name_data))

                    ## sel.click present below just to get code to move off the field get verification to fire.
                    click = "%s%s_lst"%(self.sv,field_name)


                #Check box
                elif (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Check")and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):
                    chk = Field_complete_excel(data_table,"%s"%field_name_data)
                    chk = chk.capitalize()
                    if (chk == "True")or (chk == "TRUE")or (chk == "1"):
                        print "checking the check"
                        sel.click("%s%s_chk"%(self.sv,field_name))
                        click = "%s%s_chk"%(self.sv,field_name)

                #Radio
                elif ((sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Radio")and(Field_complete_excel(data_table,"%s"%field_name_data)!= '')):
                    print "Radio"
                    print "field_name_data is %s"%field_name_data
                    radio_val = Field_complete_excel(data_table,"%s"%field_name_data)
                    print "radio_val is %s"%radio_val
                    if (self.Field_list[i][3] == include.field_id.BW_Division_ID):
                        if radio_val == "Liberal Arts":
                            field_val = 0
                        else:
                            field_val = 1
                    elif radio_val == "No":
                        field_val = 1
                    elif radio_val == "Yes":
                        field_val = 0
                    elif radio_val == "Don't Know":
                        field_val = 2
                    elif radio_val == "School of Liberal Arts":
                        field_val = 1
                    elif radio_val == "Male":
                        field_val = 0
                    elif radio_val == "Female":
                        field_val = 1
                    elif radio_val == "Culinary Arts":
                        field_val = 0
                    elif radio_val == "Baking and Pastry Arts":
                        field_val = 1
                    elif radio_val == "Please contact me for more information about Berkeley College":
                        field_val = 0
                    elif radio_val == "I do not wish to be contacted.":
                        field_val = 1
                    else:
                        print "Undefined input Radio value in data file for %s with value %s"%(field_name, radio_val)

                    if (radio_val != "not found"):
                        click = "%s%s_lst_%s"%(self.sv,field_name,field_val)
                        sel.click(click)

                #Radio 1/2
                elif (((sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Radio 1/2")
                      or (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)=="Radio Y/N"))
                      and(Field_complete_excel(data_table,"%s"%field_name_data)!= '')):
                    radio_val = Field_complete_excel(data_table,"%s"%field_name_data)
                    if radio_val == "No":
                        field_val = 1
                    elif radio_val == "Yes":
                        field_val = 0
                    else:
                        print "Undefined input Radio value in data file for %s"%field_name
                        return

                    click = "%s%s_lst_%s"%(self.sv,field_name, field_val)
                    sel.click(click)


                #Radio 1/2/3
                elif (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Radio 1/2/3")and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):
                    radio_val = Field_complete_excel(data_table,"%s"%field_name_data)
                    if radio_val == "Yes":
                        field_val = 0
                    elif radio_val == "No":
                        field_val = 1
                    else:
                        field_val = 2

                    click = "%s%s_lst_%s"%(self.sv,field_name, field_val)
                    sel.click(click)

                #Radio Mother/Father
                elif (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Radio Mother/Father")and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):
                    radio_val = Field_complete_excel(data_table,"%s"%field_name_data)
                    if radio_val == "Select":
                        field_val = 0
                    elif radio_val == "Mother":
                        field_val = 1
                    elif radio_val == "Father":
                        field_val = 2
                    else:
                        print "Undefined input Radio value in data file for %s"%field_name
                        return

                    click = "%s%s_lst_%s"%(self.sv,field_name, field_val)
                    sel.click(click)

                #Radio Mother/Father BW_Division
                elif (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)== "Radio 1/2 BW_Division")and(Field_complete_excel(data_table,"%s"%field_name_data)!= ''):
                    radio_val = Field_complete_excel(data_table,"%s"%field_name_data)
                    if radio_val == "Liberal Arts":
                        field_val = 0
                    else:
                        field_val = 1

                    click = "%s%s_lst_%s"%(self.sv,field_name, field_val)
                    sel.click(click)

                #Helptxt:
                quest_on_page += 1
                if ((Field_complete_excel(data_table,"%s"%field_name_data)!= '')and
                    (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.FIELD_TYPE)!= "Check")):

                    if (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.HELP_HEADER)!= ""):
                        self.au_hh_ind(self, sel, sheet, self.Field_list[i][0], index, click)

                    if (sheet.cell_value(rowx=self.Field_list[i][0], colx=self.x.HELP_TXT)!= ""):
                        self.au_ht_ind(self, sel, sheet, self.Field_list[i][0], index, click)



                i += 1


            # Time to hit <next>
            if i < (len(self.Field_list)):
                if (section != self.Field_list[i][2]):
                    #print "%s vs %s"%(section,self.Field_list[i][2])
                    time.sleep(1)
                    if (quest_on_page >0):
                        #sel.click("css=#ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext > img")
                        #time.sleep(6)
                        sel.click("//a[@id='%s_%s_btnNext']/img"%(include.ncc_survey.ROOT_CONTROL,include.ncc_survey.MASTER_PAGE))
                        time.sleep(1)
                        quest_on_page = 0

                    if ((transID_reported == 0) and (sel.is_text_present("Report ID:"))and sel.is_element_present("test_transaction_id")):
                        transID_reported = 1
                        time.sleep(1)
                        if (sel.is_element_present("test_transaction_id")):
                            transID = sel.get_text("test_transaction_id")
                        trans = "\nTrans ID: %s\n"%transID
                        print transID



                    for j in range(4):
                        try:
                            if ((i < (len(self.Field_list)))
                                and(sel.is_text_present("Your Net Price Calculator Results")
                                    or (sel.is_text_present("Checking for errors"))
                                    or (sel.is_text_present("Calculating Net Price Results....")))):
                                i = len(self.Field_list)
                                print "checking for: Your Net Price Calculator Results"
                                transID_out = self.au_output(self, sel, data_table)
                                if (transID_out != 0):
                                    transID = transID_out

                        except:
                            pass
                        time.sleep(0.5)


                    #switch = "Done"
                    while (i <(len(self.Field_list)))and ((switch == "Done")or(switch == "Not Found")):
                        print "ready...%s"%sheet.cell_value(rowx=self.Field_list[i][0],colx=1)
                        switch = e.ex_test_ready(sel, self.Field_list[i][0], self.Field_list[i][3], sheet, data_table)
                        if switch == "Done":
                            i = i+1
                        #means this question is not there, go to next question
                        elif (switch != "Not Found"):
                            switch == ""
                        elif (d.ex_test(sel, self.Field_list[i][3])==False):
                            i = i+1
                        else:
                            switch = ""

                    if i >= (len(self.Field_list)):
                        transID_out = self.au_output(self, sel, data_table)
                        if (transID_out != 0):
                            transID = transID_out

                        for k in range (10):
                            try:
                                if (sel.get_text("//div[@id='results']/div[%i]/table/tbody/tr/td"%k)):
                                    transID = sel.get_text("//div[@id='results']/div[%i]/table/tbody/tr/td"%k)
                                    print k
                                    print transID
                                    transID = transID.replace("Report ID:", "")
                            except: pass
                        return (transID)

                    section = self.Field_list[i][2]
            else:
                print "Last one..."
                #Last one, hit next

                if (sel.is_element_present("//a[@id='ctl00_ctl00_WrapperPlaceHolder_MainBody_btnNext']/img")):
                    sel.click("//a[@id='%s_%s_btnNext']/img"%(include.ncc_survey.ROOT_CONTROL,include.survey.MASTER_PAGE))
                    sel.wait_for_page_to_load("30000")

                transID_out = self.au_output(self, sel, data_table)
                if (transID_out != 0):
                    transID = transID_out

                for k in range (10):
                    try:
                        if (sel.get_text("//div[@id='results']/div[%i]/table/tbody/tr/td"%k)):
                            transID = sel.get_text("//div[@id='results']/div[%i]/table/tbody/tr/td"%k)
                            print k
                            print transID
                            transID = transID.replace("Report ID:", "")
                    except: pass

                return (transID)
