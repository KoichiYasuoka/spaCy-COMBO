[![Current PyPI packages](https://badge.fury.io/py/spacy-combo.svg)](https://pypi.org/project/spacy-combo/)

# spaCy-COMBO

[COMBO](https://github.com/360er0/COMBO) wrapper for [spaCy](https://spacy.io)

## Basic Usage

```py
>>> import spacy_combo
>>> nlp=spacy_combo.load("en_ewt")
>>> doc=nlp("I saw a horse yesterday which had no name.")
>>> for t in doc:
...   print("\t".join([str(t.i+1),t.orth_,t.lemma_,t.pos_,t.tag_,"_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))
...
1	I	I	PRON	PRON_Case=Nom|Number=Sing|Person=1|PronType=Prs	_	2	nsubj	_	_
2	saw	see	VERB	VERB_Mood=Ind|Tense=Past|VerbForm=Fin	_	0	ROOT	_	_
3	a	a	DET	DET_Definite=Ind|PronType=Art	_	4	det	_	_
4	horse	horse	NOUN	NOUN_Number=Sing	_	2	obj	_	_
5	yesterday	yesterday	NOUN	NOUN_Number=Sing	_	2	obl:tmod	_	_
6	which	which	PRON	PRON_PronType=Rel	_	7	nsubj	_	_
7	had	have	VERB	VERB_Mood=Ind|Tense=Past|VerbForm=Fin	_	4	acl:relcl	_	_
8	no	no	DET	DET	_	9	det	_	_
9	name	name	NOUN	NOUN_Number=Sing	_	7	obj	_	SpaceAfter=No
10	.	.	PUNCT	PUNCT	_	2	punct	_	SpaceAfter=No
>>> import deplacy
>>> deplacy.render(doc)
I         PRON  <══════════════╗   nsubj
saw       VERB  ═══════════╗═╗═╝═╗ ROOT
a         DET   <════════╗ ║ ║   ║ det
horse     NOUN  ═══════╗═╝<╝ ║   ║ obj
yesterday NOUN  <══════║═════╝   ║ obl:tmod
which     PRON  <════╗ ║         ║ nsubj
had       VERB  ═══╗═╝<╝         ║ acl:relcl
no        DET   <╗ ║             ║ det
name      NOUN  ═╝<╝             ║ obj
.         PUNCT <════════════════╝ punct
```

`spacy_combo.load(treebank)` loads spaCy Language pipeline for COMBO. Available treebanks are shown in [COMBO page](https://github.com/360er0/COMBO#trained-models).

## Installation

pip version 20.0 (or higher) required:

```sh
pip install spacy_combo
```

