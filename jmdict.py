#!/usr/bin/python
"""Import dictionary and provide a simple interface"""

import xml.etree.cElementTree as ElementTree

class KanjiElement(object):
    """
    Provides a simple interface to a dictionary entry kanji element
    """
    def __init__(self, ke_node):
        """Simply pass the kanji element node"""
        self.kanji_element_node = ke_node

    def __get_text(self):
        """return text, this is Word that gets looked up"""
        return self.kanji_element_node.find('keb').text

    def __get_priorities(self):
        """return list of priority strings"""
        return [pri_node.text for pri_node in self.kanji_element_node.findall('ke_pri')]

    def __get_infos(self):
        """return list of information strings"""
        return [info_node.text for info_node in self.kanji_element_node.findall('ke_inf')]

    text = property(__get_text)
    priorities = property(__get_priorities)
    infos = property(__get_infos)

class ReadingElement(object):
    """
    Provides a simple interface to a dictionary entry reading element
    """
    def __init__(self, re_node):
        """Simply pass the reading element node"""
        self.reading_element_node = re_node

    def __get_text(self):
        """return reading text"""
        return self.reading_element_node.find('reb').text

    def __get_priorities(self):
        """return list of priority strings"""
        return [pri_node.text for pri_node in self.reading_element_node.findall('re_pri')]

    def __get_infos(self):
        """return list of information strings"""
        return [info_node.text for info_node in self.reading_element_node.findall('re_inf')]

    def __get_no_kanji(self):
        """return no kanji flag, if element exists return True"""
        return self.reading_element_node.find('re_nokanji') != None

    def __get_kanji_texts(self):
        """return [] if reading applies to all kanji text otherwise a list of kanji texts for this reading """
        return [info_node.text for info_node in self.reading_element_node.findall('re_restr')]

    text = property(__get_text)
    priorities = property(__get_priorities)
    infos = property(__get_infos)
    no_kanji = property(__get_no_kanji)
    kanji_texts = property(__get_kanji_texts)

class LoanSource(object):
    """
    Provides a simple interface to a dictionary entry sense loan source
    """
    def __init__(self, ls_node):
        """Simply pass the source node"""
        self.lsource_node = ls_node

    def __get_language(self):
        """return the language of the text (if not present then English)"""
        return self.lsource_node.get("xml:lang")

    def __get_type(self):
        """return whether loansource describe all or part of the text"""
        return self.lsource_node.get("ls_type")

    def __get_wasei(self):
        """return whether the Japanese word is directly from a loan word or constructed(waseieigo)"""
        return self.lsource_node.get("ls_wasei")

    def __get_text(self):
        """return the loan word text"""
        return self.lsource_node.text

    language = property(__get_language)
    type = property(__get_type)
    wasei = property(__get_wasei)
    text = property(__get_text)

class Glossary(object):
    """
    Provides a simple interface to a dictionary entry sense glossary
    """
    def __init__(self, g_node):
        """Simply pass the glossary node"""
        self.gloss_node = g_node

    def __get_reverse_lookups(self):
        """return list of reverse lookups in the target language for this sense"""
        return [rl_node.text for rl_node in self.gloss_node.findall('pri')]

    def __get_language(self):
        """return the language of the text (if not present then English)"""
        return self.gloss_node.get("xml:lang")

    def __get_gender(self):
        """return the gender of the text"""
        return self.gloss_node.get("g_gen")

    def __get_text(self):
        """return glossary text"""
        return self.gloss_node.text

    reverse_lookups = property(__get_reverse_lookups)
    language = property(__get_language)
    gender = property(__get_gender)
    text = property(__get_text)

class Sense(object):
    """
    Provides a simple interface to a dictionary entry sense
    """
    def __init__(self, s_node):
        """Simply pass the sense node"""
        self.sense_node = s_node

    def __get_kanji_restrictions(self):
        """return list of kanji this sense is restricted to"""
        return [kr_node.text for kr_node in self.sense_node.findall('stagk')]

    def __get_reading_restrictions(self):
        """return list of readings this sense is restricted to"""
        return [rr_node.text for rr_node in self.sense_node.findall('stagr')]

    def __get_cross_references(self):
        """return list of cross-references for this sense"""
        return [cr_node.text for cr_node in self.sense_node.findall('xref')]

    def __get_antonyms(self):
        """return list of antonyms for this sense"""
        return [ant_node.text for ant_node in self.sense_node.findall('ant')]

    def __get_fields(self):
        """return list of fields(e.g. medical, technology) for this sense"""
        return [fld_node.text for fld_node in self.sense_node.findall('field')]

    def __get_miscs(self):
        """return list of miscellaneous notes for this sense"""
        return [misc_node.text for misc_node in self.sense_node.findall('misc')]

    def __get_infos(self):
        """return list of information(currency of use, etc) for this sense"""
        return [info_node.text for info_node in self.sense_node.findall('s_inf')]

    def __get_dialects(self):
        """return list of dialects for this sense"""
        return [dia_node.text for dia_node in self.sense_node.findall('dia')]

    def __get_loan_sources(self):
        """return list of loan sources"""
        return [LoanSource(ls_node) for ls_node in self.sense_node.findall('lsource')]

    def __get_examples(self):
        """return list of examples for this sense"""
        return [example_node.text for example_node in self.sense_node.findall('example')]

    def __get_parts_of_speech(self):
        """return list of part of speech strings"""
        return [pos_node.text for pos_node in self.sense_node.findall('pos')]    

    def __get_glossaries(self):
        """return list of glossary entries"""
        return [Glossary(gloss_node) for gloss_node in self.sense_node.findall('gloss')]

    kanji_restrictions = property(__get_kanji_restrictions)
    reading_restrictions = property(__get_reading_restrictions)
    cross_references = property(__get_cross_references)
    antonyms = property(__get_antonyms)
    fields = property(__get_fields)
    miscs = property(__get_miscs)
    infos = property(__get_infos)
    dialects = property(__get_dialects)
    loan_sources = property(__get_loan_sources)
    examples = property(__get_examples)
    parts_of_speech = property(__get_parts_of_speech)
    glossaries = property(__get_glossaries)
    
    
class Entry(object):
    """
    Provides a simple interface to a dictionary entry
    """
    def __init__(self, e_node):
        """Simply pass the entry node"""
        self.entry_node = e_node
   
    def __get_entry_number(self):
        """return entry number"""
        return self.entry_node.find('ent_seq').text
   
    def __get_senses(self):
        """return list of Entry"""
        return [Sense(sense_node) for sense_node in self.entry_node.findall('sense')]

    def __get_kanji_element(self):
        """return the kanji_element"""
        return KanjiElement(self.entry_node.find('k_ele'))

    def __get_reading_element(self):
        """return the reading_element"""
        return ReadingElement(self.entry_node.find('r_ele'))

    entry_number = property(__get_entry_number)
    senses = property(__get_senses)
    kanji_element = property(__get_kanji_element)
    reading_element = property(__get_reading_element)

class JMDictionary(object):
    """
    A Japanese-Multilingual Dictionary
    """
    def __init__(self, path=None, init=True):
        """Dictionary initializes by default"""
        self.xml_tree = None
        self.word_to_entries = {}
        if (path != None):
            self.load_from_file(path)
            if (init == True):
                self.generate_indexes()

    def load_from_file(self, path):
        """Path must include the name of the jmdict file"""
        file = open(path, "rb")
        self.xml_tree = ElementTree.ElementTree(file=file)

    def generate_indexes(self):
        """Generate the data structures needed to perform searches"""
        # This index is for exact_search
        self.word_to_entries = {}
        for entry in self.xml_tree.getroot().getchildren():
            word_node = entry.find('k_ele/keb')
            if word_node != None: # Has Kanji Entry
                #is word in list, if not, add it
                word = word_node.text
                if self.word_to_entries.has_key(word) != True:
                    self.word_to_entries[word] = set()
                self.word_to_entries[word].add(Entry(entry))

    def lookup(self, word):
        return self.word_to_entries.get(word, [])


if __name__ == "__main__":
    # This is placeholder until unit tests are in place
    JMDICT = "./JMdict"
    dictionary = JMDictionary(JMDICT)
    # Simple Demonstrative Method
    for item in dictionary.lookup(u'\u79c1'):  #  u'\u79c1'  watashi kanji
        # print item.senses, item.entry_number
        print item.kanji_element.text,\
              item.reading_element.text,\
              item.senses[0].glossaries[0].text