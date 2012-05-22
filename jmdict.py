"""Import dictionary and provide a simple interface"""

import xml.etree.cElementTree as ElementTree

       
class JMDictionaryEntrySense(object):
    """
    Provides a simple interface to a dictionary entry sense
    """
    def __init__(self, s_node):
        """Simply pass the sense node"""
        self.sense_node = s_node
   
    def __get_parts_of_speech(self):
        """return list of part of speech strings"""
        return [pos_node.text for pos_node in self.sense_node.findall('pos')]    

    def __get_glossaries(self):
        """return list of glossary strings"""
        return [gloss_node.text for gloss_node in self.sense_node.findall('gloss')]    
    
    parts_of_speech = property(__get_parts_of_speech)
    glossaries = property(__get_glossaries)
    
    
class JMDictionaryEntry(object):
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
        """return list of DictionaryEntrySense"""
        return [JMDictionaryEntrySense(sense_node) for sense_node in self.entry_node.findall('sense')]
    
    entry_number = property(__get_entry_number)
    senses = property(__get_senses)


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
                self.word_to_entries[word].add(JMDictionaryEntry(entry))

    def lookup(self, word):
        return self.word_to_entries.get(word, [])


if __name__ == "__main__":
    # This is placeholder until unit tests are in place
    JMDICT = "./JMdict"
    dictionary = JMDictionary(JMDICT)
    # Simple Demonstrative Method
    for item in dictionary.lookup(u'\u79c1'):  #  u'\u79c1'  watashi kanji
        # print item.senses, item.entry_number
        print item.entry_node.find('k_ele/keb').text,\
              item.entry_node.find('r_ele/reb').text,\
              item.entry_node.find('sense/gloss').text