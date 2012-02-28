# coding: utf-8

ENGLISH_KEYS_SMALL = u'qwertyuiopasdfghjklzxcvbnm'
ENGLISH_KEYS_CAPS = u'QWERTYUIOPASDFGHJKLZXCVBNM'
GREEK_KEYS_SMALL = u';ςερτυθιοπασδφγηξκλζχψωβνμ'
GREEK_KEYS_CAPS = u';ςΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ'
GREEK_KEYS_WITH_ACCENT = u'άέήίόύώΆΈΉΊΌΎΏ'
ENGLISH_KEYS_WITH_ACCENT = u'aehioyvAEHIOYV'
GREEK_ACCENT = u';'

def _ell2en():
  el_dir = {}
  en_dir = {}
  for (el, en) in zip(GREEK_KEYS_SMALL, ENGLISH_KEYS_SMALL):
    el_dir[el] = en
    en_dir[en] = el
  for (el, en) in zip(GREEK_KEYS_CAPS, ENGLISH_KEYS_CAPS):
    el_dir[el] = en
    en_dir[en] = el
  for (el, en) in zip(GREEK_KEYS_WITH_ACCENT, ENGLISH_KEYS_WITH_ACCENT):
    el_dir[el] = GREEK_ACCENT + en
    en_dir[GREEK_ACCENT + en] = el
    
  return (el_dir, en_dir)
  
(EL_TO_EN, EN_TO_EL) = _ell2en()

class Converter:
  
  def __init__(self):
    self.layout1to2 = EL_TO_EN
    self.layout2to1 = EN_TO_EL
    self._debug = False
    
  def toggle_layout(self, text):
    text = text.decode('utf-8')
    #text = unicode(text)
    new_text = ''
    skip_next = False
    for i in range(len(text)):
      if skip_next:
        skip_next = False
        continue
      skip_next = False
      ch = text[i]
      if self._debug: print ch
      # check if is a case of accent greek (e.g. ά, ί) -> ;a ;i
      if ch == GREEK_ACCENT:
        next = ch + text[i+1]
        if next in self.layout2to1.keys():
          skip_next = True
          new_text += self.layout2to1[next]
        elif next in self.layout1to2.keys():
          skip_next = True
          new_text += self.layout1to2[next]
        else:
          new_text += ch       
      else:
        if ch in self.layout2to1.keys():
          new_text += self.layout2to1[ch]
        elif ch in self.layout1to2.keys():
          new_text += self.layout1to2[ch]
        else:
          new_text += ch
    #print 'import: ', text
    #print 'export: ', new_text
    return new_text
    
    
  
