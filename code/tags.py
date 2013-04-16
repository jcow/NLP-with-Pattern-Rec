# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:41:30 2013

@author: jason
"""
class Tags(object):
    tags = ['ABL','ABN','ABX','AP','AP$','AP+AP','AT','BE','BED','BED*','BEDZ','BEDZ*','BEG','BEM','BEM*','BEN','BER','BER*','BEZ','BEZ*','CC','CD','CD$','CS','DO','DO*','DO+PPSS','DOD','DOD*','DOZ','DOZ*','DT','DT$','DT+BEZ','DT+MD','DTI','DTS','DTS+BEZ','DTX','EX','EX+BEZ','EX+HVD','EX+HVZ','EX+MD','FW-*','FW-AT','FW-AT+NN','FW-AT+NP','FW-BE','FW-BER','FW-BEZ','FW-CC','FW-CD','FW-CS','FW-DT','FW-DT+BEZ','FW-DTS','FW-HV','FW-IN','FW-IN+AT','FW-IN+NN','FW-IN+NP','FW-JJ','FW-JJR','FW-JJT','FW-NN','FW-NN$','FW-NNS','FW-NP','FW-NPS','FW-NR','FW-OD','FW-PN','FW-PP$','FW-PPL','FW-PPL+VBZ','FW-PPO','FW-PPO+IN','FW-PPS','FW-PPSS','FW-PPSS+HV','FW-QL','FW-RB','FW-RB+CC','FW-TO+VB','FW-UH','FW-VB','FW-VBD','FW-VBG','FW-VBN','FW-VBZ','FW-WDT','FW-WPO','FW-WPS','HV','HV*','HV+TO','HVD','HVD*','HVG','HVN','HVZ','HVZ*','IN','IN+IN','IN+PPO','JJ','JJ$','JJ+JJ','JJR','JJR+CS','JJS','JJT','MD','MD*','MD+HV','MD+PPSS','MD+TO','NN','NN$','NN+BEZ','NN+HVD','NN+HVZ','NN+IN','NN+MD','NN+NN','NNS','NNS$','NNS+MD','NP','NP$','NP+BEZ','NP+HVZ','NP+MD','NPS','NPS$','NR','NR$','NR+MD','NRS','OD','PN','PN$','PN+BEZ','PN+HVD','PN+HVZ','PN+MD','PP$','PP$$','PPL','PPLS','PPO','PPS','PPS+BEZ','PPS+HVD','PPS+HVZ','PPS+MD','PPSS','PPSS+BEM','PPSS+BER','PPSS+BEZ','PPSS+BEZ*','PPSS+HV','PPSS+HVD','PPSS+MD','PPSS+VB','QL','QLP','RB','RB$','RB+BEZ','RB+CS','RBR','RBR+CS','RBT','RN','RP','RP+IN','TO','TO+VB','UH','VB','VB+AT','VB+IN','VB+JJ','VB+PPO','VB+RP','VB+TO','VB+VB','VBD','VBG','VBG+TO','VBN','VBN+TO','VBZ','WDT','WDT+BER','WDT+BER+PP','WDT+BEZ','WDT+DO+PPS','WDT+DOD','WDT+HVZ','WP$','WPO','WPS','WPS+BEZ','WPS+HVD','WPS+HVZ','WPS+MD','WQL','WRB','WRB+BER','WRB+BEZ','WRB+DO','WRB+DOD','WRB+DOD*','WRB+DOZ','WRB+IN','WRB+MD']
    tag_count = []
    
    def __init__(self):
        self.tag_count = []
        for i in self.tags:
            self.tag_count.append((i, 0))

    def get_tags(self):
        return self.tags            
            
    def get_tag_counts(self, tagged_word_list):
        for tagged_word_item in tagged_word_list:
            counter = 0
            for tag in self.tag_count:
                if tagged_word_item[1] == tag[0]:
                    self.tag_count[counter] = (self.tag_count[counter][0], self.tag_count[counter][1]+1)
                    break
                counter += 1
        return self.tag_count