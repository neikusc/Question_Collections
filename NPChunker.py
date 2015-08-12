import nltk

class NTENT():
  def __init__(self):
  ''' define tag patterns using Regrex '''
    self.patterns = '''
                    NP: {<DT|PP\$>?<JJ>*<NN.*>+}
                    {<NN.*>+}
                    '''
    
  def leaves(self, tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()
      
  def NPChunker(self,sentence):
    '''Parsing sentence and get all the NP'''
    chunk = nltk.RegexpParser(self.patterns)
    nouns = []

    tree = chunk.parse(sentence)
    for leaf in self.leaves(tree):
      leaf = [l[0] for l in leaf]
      nouns.append( ' '.join(leaf) )
    return nouns


collections = ['''Darren Gold had a stomach virus the first time he used an app called Heal to summon a doctor to his Beverly Hills home.''',
               '''Mr. Vinken is chairman of Elsevier N.V., the Dutch publishing group.''']
ntent = NTENT()

for text in collections:
  tokens = nltk.word_tokenize(text)
  tokens = nltk.pos_tag(tokens)
  print text
  print ntent.NPChunker(tokens)
  print '\n'


